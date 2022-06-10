import numpy as np
#import pylab as py
import matplotlib.pyplot as py
from collections import deque
# ______________________________________________________________________________________________________________________
class plotter(object):
# ______________________________________________________________________________________________________________________
    def __init__(self, gate_states, u, action_1, mode='normal'):

        self.us = deque()
        self.real_depths = deque()
        self.gate_states = deque()
        self.reward = deque()
        self.depth = deque()
        self.time = deque()
        self.action_pid = deque()

        # names
        self.n_gate_states = gate_states
        self.n_u = u
        self.n_action_1 = action_1


        # mode
        self.mode = mode
# ______________________________________________________________________________________________________________________
    def update(self, real_depth, gate_states, u, time, depth, action_pid):
        self.real_depths.append(real_depth)
        self.us.append(u)
        self.gate_states.append(gate_states)
        self.time.append(time)
        self.depth.append(depth)
        self.action_pid.append(action_pid)
# ______________________________________________________________________________________________________________________
    # the reward and the rest of the variables have different updating cicles    
    def update_reward(self, reward):
        self.reward.append(reward)
# ______________________________________________________________________________________________________________________
    def plot(self, savefig=False):

        py.plot(self.time, self.real_depths)
        py.xlabel('Time (hour)')
        py.ylabel('Real depths')
        py.title('Double QPI')
        py.legend(('d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'))
        if savefig == True: py.savefig('real_depths.png')
        py.show()

        py.plot(self.time, self.gate_states)
        py.xlabel('Time (hour)')
        py.ylabel(self.n_gate_states)
        py.title('Double QPI')
        py.legend(('Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8'))

        # py.legend(('Y1', 'Y8', 'Y2', 'Y3', 'Y4', 'Y7', 'Y5', 'Y6'), bbox_to_anchor=(1.1, 0.5), loc="center right")
        #py.axis([0, simulation_lenght, -1., 1.])
        if savefig == True: py.savefig('gate_states.png')
        py.show()

        # print(self.us)
        py.plot(self.time, self.us)
        py.xlabel('Time (hour)')
        py.ylabel(self.n_u)
        py.title('Double QPI')
        py.legend(('u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'u7', 'u8'))

        # py.legend(('u1', 'u8', 'u2', 'u3', 'u4', 'u7', 'u5', 'u6'), bbox_to_anchor=(1.1, 0.5), loc="center right")
        #py.axis([0, simulation_lenght, -1., 1.])
        if savefig == True: py.savefig('U.png')
        py.show()

        py.plot(self.time, self.depth)
        py.xlabel('Time (hour)')
        py.ylabel('Double QPI depth')
        py.title('Double QPI')
        # py.legend(('1', '2', '3', '4' , '5', '6'  ))
        #py.axis([0, simulation_lenght, -1., 1.])
        if savefig == True: py.savefig('depth.png')
        py.show()

        kp_18 = np.array([_[0] for _ in self.action_pid])
        ki_18 = np.array([_[1] for _ in self.action_pid])
        kp_23 = np.array([_[2] for _ in self.action_pid])
        ki_23 = np.array([_[3] for _ in self.action_pid])
        kp_47 = np.array([_[4] for _ in self.action_pid])
        ki_47 = np.array([_[5] for _ in self.action_pid])
        kp_56 = np.array([_[6] for _ in self.action_pid])
        ki_56 = np.array([_[7] for _ in self.action_pid])
        fig, axs = py.subplots(2, 2, sharex=True)
        k1, k2 = axs[0, 0].plot(self.time, kp_18, 'b.', self.time, ki_18, 'r.')
        axs[0, 0].set_title('Gates 1 and 2 Contoller')
        axs[0, 1].plot(self.time, kp_23, 'b.', self.time, ki_23, 'r.')
        axs[0, 1].set_title('Gates 3 and 4 Contoller')
        axs[1, 0].plot(self.time, kp_47, 'b.', self.time, ki_47, 'r.')
        axs[1, 0].set_title('Gates 5 and 6 Contoller')
        axs[1, 1].plot(self.time, kp_56, 'b.', self.time, ki_56, 'r.')
        axs[1, 1].set_title('Gates 7 and 8 Contoller')
        for ax in axs.flat:
            ax.set_ylim([1, 2])
            ax.legend([k1, k2], ['Kp', 'Ki'])
        fig.text(0.5, 0.04, 'Time (hour)', ha='center')
        fig.text(0.04, 0.5, 'PI Parameters', va='center', rotation='vertical')
        #py.axis([0, simulation_lenght, -1., 1.])
        if savefig == True: py.savefig('actions.png')
        py.show()
# ______________________________________________________________________________________________________________________
    def mean_squared_error(self, set_point):
        
        try:
            vx = np.array([_[0] for _ in self.gate_states])
            wz = np.array([_[1] for _ in self.gate_states])
            
            mse_vx = np.sqrt(np.mean((vx - set_point[0])**2))
            mse_wz = np.sqrt(np.mean((wz - set_point[1])**2))
            mse = np.array([mse_vx, mse_wz])
        except IndexError: 
            print('index error calculating for only one variable')
            mse = np.sqrt(np.mean(( np.subtract(self.velocity,set_point[0]))**2))
        
        return mse
# ______________________________________________________________________________________________________________________
    def mahalanobis(self, set_point):

        try: 
            vx = np.array([_[0] for _ in self.gate_states])
            wz = np.array([_[1] for _ in self.gate_states])

            # x centered        
            vxm = vx - set_point[0]
            wzm = wz - set_point[1]
            # Generate matrix Xc
            xc = np.transpose(np.matrix([vxm,wzm]))
            # covariance matrix
            cx = np.matmul( np.transpose(xc), xc)
            #print('cx', cx)
            cx = cx/(len(vx)-1)
            #print('cx2', cx)
            # inverse of the covariate
            cx_inv = np.linalg.inv(cx)

            # initialize MD matrix
            MD = np.zeros(len(vx))
            # calculate each coefficient
            for i in range(len(vx)):
                #diff = np.array([x1[i] - np.mean(x1),x2[i] - np.mean(x2)])
                diff = np.array([vx[i] - set_point[0] ,wz[i] - set_point[1]])
                diff_t = np.transpose(diff)
                temp = np.matmul(diff,np.array(cx_inv))
                MD[i] = np.sqrt( np.matmul(temp,diff_t))
        except IndexError: 
            print('could not calculate mahalanobis only one dimension')
            MD = 0.

        return np.mean(MD) 
# ______________________________________________________________________________________________________________________
    def euclidean_distance(self, set_point):

        try:
            vx = np.array([_[0] for _ in self.gate_states])
            wz = np.array([_[1] for _ in self.gate_states])

            # x centered
            vxm = vx - set_point[0]
            wzm = wz - set_point[1]

            ED = np.zeros(len(vx))
            for i in range(len(vx)):
                ED[i]= np.sqrt(vxm[i]**2 + wzm[i]**2)
        except IndexError:
            print('index error calculating euclidean_distance for only one distance variable')
            ED = np.zeros(len(self.gate_states))
            for i in range(len(self.gate_states)):
                ED[i] = np.sqrt(np.mean(( np.subtract(self.gate_states[i],set_point[0]))**2))

        return np.mean(ED)
# ______________________________________________________________________________________________________________________
    def save_values(self):
        np.save('Us', self.us)
        np.save('real_depths', self.real_depths)
        np.save('gate_states', self.gate_states)
        np.save('reward', self.reward)
        np.save('time', self.time)
        np.save('depth', self.depth)
        np.save('action_pid', self.action_pid)
# ______________________________________________________________________________________________________________________
    def reset(self):
        self.us = deque()
        self.gate_states = deque()
        self.reward = deque()
# ______________________________________________________________________________________________________________________
    def load(self):
        self.us = np.load('Us.npy')
        self.real_depths = np.load('real_depths.npy')
        self.gate_states = np.load('gate_states.npy')
        self.reward = np.load('reward.npy')
        self.time = np.load('time.npy')
        self.depth = np.load('depth.npy')
        self.action_pid = np.load('action_pid.npy')
# ______________________________________________________________________________________________________________________
if __name__ == '__main__':
    plotter = plotter('gate_states', 'u', 'action_pid')
    plotter.load()
    print(plotter.euclidean_distance(np.array([0.21,-0.1])))
    print(plotter.mahalanobis(np.array([0.21,-0.1])))
    print(plotter.mean_squared_error(np.array([0.21,-0.1])))
    print(plotter.gate_states)