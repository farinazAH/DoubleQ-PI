# Alamiyan: THis file has been modified.

# general libraries
import numpy as np
from collections import deque
import signal
import time
import pickle
# custom files
from action_chooser import action_chooser
from double_Q import DQPID 
from memory import memory_comparator
from functions import sigint_handler
from algorithm_4 import algorithm_4
from algorithm_3 import algorithm_3
from algorithm_2 import algorithm_2
from long_term_memory import update_long_term_memory
# custom canal files
from canal_dict import canal_dict as canal_dict
# ______________________________________________________________________________________________________________________
# Canals
# the blocks have different parameters, with this you can select the correct one.
# select the platform from the canal dictionary
platform = 'TheCanal'       # select the simulation platform from canal_dict file, see the parameters there.
simulation = True           # reserved to change the controller
mode = 'long_term_memory'   # this sets the mode for the memory used in this file

# Constants
E_GREED = 1.                # used in action_chooser file
# ---
E_GREED_BASE = 0.05         # used in action_chooser file- should be checked and adjusted
# ------
EXECUTION_TIME = 50     # The number of all steps in each execution
Ts = 100.                   # The time used to compute dt in PID controller in canal file
Teval = 1  #24          # The interval used to compute execution loop in PID controller in canal file

N_mariano = 8               # The threshold used to switch between algorithms in this file
memory_repetition = 8       # The size of visiting same states to switch between algorithm 3 and 4 in this file
np.random.seed(1234)

# canal gate control
def main_DQPID(load):
    global platform
    signal.signal(signal.SIGINT, sigint_handler)  # to execute the signal interrupt

    # QPID parameters
    Q_index = 0
    Q_arrange = deque()
    action_discretization_n = 3   # The number of produced actions in each discretization
    maximum_depth = 8             # The maximum depth level used in this algorithm to discretize state space

    # the parameters of the simulated platform (canal)
    current_canal_block = canal_dict[platform]
    state = current_canal_block['initial_state']
    set_point = current_canal_block['set_point']
    initial_action_centroid = current_canal_block['action_centroid']
    # simulation parameter can use as controller selector (MPC or PID)
    environment = current_canal_block['class'](set_point, dt=1./Ts, Teval=Teval, simulation=simulation)
    K_step = current_canal_block['K_step']
    print('k step', K_step)
    time.sleep(1)

    # Classes instantiations
    action_selector = action_chooser(E_GREED, E_GREED_BASE, EXECUTION_TIME)
    memory = memory_comparator(memory_repetition)

    Q_arrange.append(DQPID(state, None, 1., initial_action_centroid, action_discretization_n, maximum_depth, 0., 0., K_step=K_step  ))
    ltm = deque(maxlen=10000)    # long term memory max
    minibatch_size = 32          # The size of the batch used to update Q_table by long_term memory
    # others
    time.sleep(1)

    # using the first state-------------------------------------------
    state = state[0]

    if load:
        n_to_load = np.load('len_Q.npy')[0]
        for _ in range(n_to_load):
            file = open('Q_arrange' + str(_) + '.txt','rb')
            Q_arrange.append(pickle.load(file))
        print(len(Q_arrange))
    # ---------------------------------------------------------------------------------------------------------
    for x in range(EXECUTION_TIME):

        start = time.time()
        
        flag_ab, action, action_index, e_greed, state_index = action_selector.get(Q_arrange[Q_index], state)
        memory.update(state_index, action_index, Q_index, action)

        # apply the action and visit next state
        next_state = environment.update(action, Q_arrange[Q_index].depth)
        # compute the reward
        reward = environment.get_gaussian_reward(next_state, set_point)
       
        if x < N_mariano:
             Q_arrange[Q_index] = algorithm_2(Q_arrange[Q_index], state_index, next_state, reward, action_index, flag_ab)
             next_Q_index = Q_index
             memory.counter = 0

        else:
            memory.compare()
            if memory.flag_no_variation == True:
                #print('algorithm 4')
                Q_arrangement, Q_index, next_Q_index, action_selector.e_greed_counter = algorithm_4(Q_arrange, memory.Mt, next_state, reward, maximum_depth, action_discretization_n, action_selector.e_greed_counter, set_point, flag_ab, K_step)
                memory.flag_no_variation = False
            else:
                #print('algorithm 3')
                Q_arrange, Q_index, next_Q_index = algorithm_3(Q_arrange, memory.Mt, next_state, reward, flag_ab)
            
        end = time.time()
        
        ltm.append([state, next_state, action, Q_index, next_Q_index, reward, flag_ab, action_index])
        if mode=='long_term_memory':
            Q_arrange = update_long_term_memory(ltm, Q_arrange, minibatch_size)

        Q_index = next_Q_index
        state = next_state

        print(x, 'R',  round(reward,3),'s', next_state, 'depth', Q_arrange[Q_index].depth, 't', round(end-start,2) )


    # ---------------------------------------------------------------------------------------------------------
    #saving Q tables
    for _ in range(len(Q_arrange)):
        file = open('Q_arrange' + str(_) + '.txt','wb')
        print(Q_arrange[_])
        pickle.dump(Q_arrange[_], file, protocol=4)

    np.save('len_Q.npy', np.array([len(Q_arrange)]))
    
    # ploting and printing performance
    print('actions', action)
    environment.plotter.plot(savefig=True)
    environment.plotter.save_values()
    print('finish')
    # mse = environment.plotter.mean_squared_error(set_point)
    # print('mse', mse, 'mean mse', np.mean(mse))
    # euclidean_distance = environment.plotter.euclidean_distance(set_point)
    # print('euclidean_distance', euclidean_distance)
    # mahalanobis = environment.plotter.mahalanobis(set_point)
    # print('mahalanobis', mahalanobis)

    environment.stop()


if __name__ == '__main__':
    main_DQPID(load = False)
