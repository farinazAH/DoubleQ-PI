# Alamiyan: THis file has been created instead of robot file.
# Alamiyan: It is the main file to define canal specifications.
from copy import deepcopy

import matlab.engine
import numpy as np
from plotter import plotter
# ______________________________________________________________________________________________________________________

class canal():
# ______________________________________________________________________________________________________________________
    def __init__(self, set_point, dt = 0.0001, Teval = 1., simulation = True):

        self.eng = matlab.engine.start_matlab()

        self.uMin = -1
        self.uMax = 1

        self.y_target = np.array([2.1, 2.1, 2.1, 1.9, 1.9, 1.7, 1.7, 1.7])
        self.real_depth = np.zeros(len(set_point))
        self.depth_error = np.zeros(len(set_point))

        self.dt = dt
        self.Teval = Teval

        self.error = np.zeros((3, len(set_point)))
        self.u0 = np.zeros(len(set_point))

        self.u = np.zeros(len(set_point))
        self.set_point = set_point

        # action_pid
        self.actions = np.zeros(8)

        self.reward = -1.
        self.execution = np.divide(self.Teval,self.dt).astype(int)

        # to plot
        self.plotter = plotter('Depth error', 'PI outputs', 'actions')

        self.time = 0.
# ______________________________________________________________________________________________________________________
    def update(self, action, depth):   #depth is the RL algorithm depth
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # action = np.array([2.5, 1.5,\
        #                    1.5, 1.5,\
        #                    1.5, 1.5,\
        #                    2.5, 1.5])
        for _ in range(self.execution):
            self.actions = action

            # update errors        
            self.error[2] = self.error[1]
            self.error[1] = self.error[0] 
            self.error[0] = self.depth_error
            # print(self.error,'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            # get controller commands

            for ind in range(0,len(self.u),2):
                self.u[ind:ind+2] = self.controller_pi(self.error[0][ind:ind+2], self.error[1][ind:ind+2], self.error[2][ind:ind+2], self.actions[ind:ind+2], self.u0[ind:ind+2])
                self.u[ind:ind+2] = np.clip(self.u[ind:ind+2], self.uMin, self.uMax)
                self.u0[ind:ind+2] = self.u[ind:ind+2]

            # call environment simulator in matlab
            # create matlab.u and matlab.et
            # self.u[0:0] = 0
            # self.u[1:len(self.u)] = 0   #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            # self.u[len(self.u)-1] = 0

            u_temp = deepcopy(self.u)

            print(u_temp)
            depth_error_temp = deepcopy(self.depth_error)
            self.depth_error = self.eng.canal_simulator_step(matlab.double(u_temp.tolist()), matlab.double(depth_error_temp.tolist()), self.time, nargout=1)
            self.depth_error = np.array(self.depth_error)[:,0]

            # print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
            # print('K_pid = ', self.actions, '\nerror = ', self.error, '\depth_error = ', self.depth_error)
            # print('u = ', self.u)
            # print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

            # to plot
            self.real_depth = self.y_target + self.depth_error
            us = np.array([self.u[0], self.u[1], self.u[2], self.u[3], self.u[4], self.u[5], self.u[6], self.u[7]])
            self.time = self.time + self.dt
            self.plotter.update( self.real_depth, self.depth_error, us, self.time, depth, self.actions)

        return self.depth_error
# ______________________________________________________________________________________________________________________
    def controller_pid(self, et, et1, et2, action, u0):

        Kp = action[0]
        Ti = action[1]
        Td = 0.

        k1 = Kp*(1+Td/self.dt)
        k2 = -Kp*(1+2*Td/self.dt-self.dt/Ti)
        k3 = Kp*(Td/Ti)

        # u = u0 + k1 * et + k2 * et1 + k3 * et2
        u = k1*et + k2*et1 + k3*et2

        return u
# ______________________________________________________________________________________________________________________
    def controller_pid2(self, et, et1, et2, action, u0):

        Kp = action[0]
        Ti = action[1]
        Td = action[2]

        k1 = Kp*(1+Td/self.dt)
        k2 =-Kp*(1+2*Td/self.dt-self.dt/Ti)
        k3 = Kp*(Td)

        u = u0 + k1*et + k2*et1 + k3*et2

        return u
# ______________________________________________________________________________________________________________________
    def controller_pi(self, et, et1, et2, action, u0):

        Kp = action[0]
        Ti = action[1]

        k1 = Kp
        k2 =-Kp*(1 -self.dt/Ti)
        k3 = 0.

        # u = u0 + k1*et + k2*et1 + k3*et2
        # u = k1 * et + k2 * et1 + k3 * et2
        u = u0 + k1 * et #+ k2 * et1 + k3 * et2
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        return u
# ______________________________________________________________________________________________________________________
    def controller_pd(self, et, et1, et2, action, u0):

        Kp = action[0]
        Td = action[1]

        k1 = Kp*(1+Td/self.dt)
        k2 = 0.
        k3 = Kp*(Td)

        u = u0 + k1*et + k2*et1 + k3*et2

        return u
# ______________________________________________________________________________________________________________________
    def get_gaussian_reward(self, state, set_point):
        a_gauss = np.power(0.5, 2.)  # 0.017
        # a_gauss = np.power(0.017,2.) #0.017
        exponent = np.zeros(len(set_point))
        for _ in range(len(set_point)):
            exponent[_] = np.power((state[_] - set_point[_]), 2.)

        exponent_total = np.sum(exponent)
        self.reward = -1. + 2 * np.exp(-0.5 * (exponent_total / a_gauss))

        # self.reward = 100/(exponent_total+1.01)

        # save reward to plot it
        self.plotter.update_reward(self.reward)

        return self.reward
# ______________________________________________________________________________________________________________________
    def stop(self):
        self.eng.quit()