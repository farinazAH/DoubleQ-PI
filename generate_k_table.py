# Alamiyan: THis file has been modified. Add generate_k_table_8 and generate_k_table_16

import numpy as np

def generate_k_table_16(number_of_actions, k_step, k_min, k_max, k_size):
    k1_step = k_step[0]
    k1_min = k_min[0]
    k1_max = k_max[0]
    k1_size = k_size

    k2_step = k_step[1]
    k2_min = k_min[1]
    k2_max = k_max[1]
    k2_size = k_size

    k3_step = k_step[2]
    k3_min = k_min[2]
    k3_max = k_max[2]
    k3_size = k_size

    k4_step = k_step[3]
    k4_min = k_min[3]
    k4_max = k_max[3]
    k4_size = k_size

    k5_step = k_step[4]
    k5_min = k_min[4]
    k5_max = k_max[4]
    k5_size = k_size

    k6_step = k_step[5]
    k6_min = k_min[5]
    k6_max = k_max[5]
    k6_size = k_size

    k7_step = k_step[6]
    k7_min = k_min[6]
    k7_max = k_max[6]
    k7_size = k_size

    k8_step = k_step[7]
    k8_min = k_min[7]
    k8_max = k_max[7]
    k8_size = k_size

    k9_step = k_step[8]
    k9_min = k_min[8]
    k9_max = k_max[8]
    k9_size = k_size

    k10_step = k_step[9]
    k10_min = k_min[9]
    k10_max = k_max[9]
    k10_size = k_size

    k11_step = k_step[10]
    k11_min = k_min[10]
    k11_max = k_max[10]
    k11_size = k_size

    k12_step = k_step[11]
    k12_min = k_min[11]
    k12_max = k_max[11]
    k12_size = k_size

    k13_step = k_step[12]
    k13_min = k_min[12]
    k13_max = k_max[12]
    k13_size = k_size

    k14_step = k_step[13]
    k14_min = k_min[13]
    k14_max = k_max[13]
    k14_size = k_size

    k15_step = k_step[14]
    k15_min = k_min[14]
    k15_max = k_max[14]
    k15_size = k_size

    k16_step = k_step[15]
    k16_min = k_min[15]
    k16_max = k_max[15]
    k16_size = k_size

    k_table = np.zeros((number_of_actions, 16))
    count = 0

    for a1 in [k16_min, k16_min + k16_step, k16_max]:
        for b1 in [k15_min, k15_min + k15_step, k15_max]:
            for p1 in [k14_min, k14_min + k14_step, k14_max]:
                for n1 in [k13_min, k13_min + k13_step, k13_max]:
                    for m1 in [k12_min, k12_min + k12_step, k12_max]:
                        for k1 in [k11_min, k11_min + k11_step, k11_max]:
                            for j1 in [k10_min, k10_min + k10_step, k10_max]:
                                for i1 in [k9_min, k9_min + k9_step, k9_max]:
                                    for a in [k8_min, k8_min + k8_step, k8_max]:
                                        for b in [k7_min, k7_min + k7_step, k7_max]:
                                            for p in [k6_min, k6_min + k6_step, k6_max]:
                                                for n in [k5_min, k5_min + k5_step, k5_max]:
                                                    for m in [k4_min, k4_min + k4_step, k4_max]:
                                                        for k in [k3_min, k3_min + k3_step, k3_max]:
                                                            for j in [k2_min, k2_min + k2_step, k2_max]:
                                                                for i in [k1_min, k1_min + k1_step, k1_max]:

                                                                    k1 = i
                                                                    k2 = j
                                                                    k3 = k
                                                                    k4 = m
                                                                    k5 = n
                                                                    k6 = p
                                                                    k7 = b
                                                                    k8 = a

                                                                    k9 = i1
                                                                    k10 = j1
                                                                    k11 = k1
                                                                    k12 = m1
                                                                    k13 = n1
                                                                    k14 = p1
                                                                    k15 = b1
                                                                    k16 = a1


                                                                    if k1 < 0.:
                                                                        k1 = 0.001

                                                                    if k2 <= 0.:
                                                                        k2 = 0.001

                                                                    if k3 < 0.:
                                                                        k3 = 0.001

                                                                    if k4 < 0.:
                                                                        k4 = 0.001

                                                                    if k5 < 0.:
                                                                        k5 = 0.001

                                                                    if k6 < 0.:
                                                                        k6 = 0.001

                                                                    if k7 < 0.:
                                                                        k7 = 0.001

                                                                    if k8 < 0.:
                                                                        k8 = 0.001

                                                                    if k9 < 0.:
                                                                        k9 = 0.001

                                                                    if k10 <= 0.:
                                                                        k10 = 0.001

                                                                    if k11 < 0.:
                                                                        k11 = 0.001

                                                                    if k12 < 0.:
                                                                        k12 = 0.001

                                                                    if k13 < 0.:
                                                                        k13 = 0.001

                                                                    if k14 < 0.:
                                                                        k14 = 0.001

                                                                    if k15 < 0.:
                                                                        k15 = 0.001

                                                                    if k16 < 0.:
                                                                        k16 = 0.001


                                                                    k_table[count] = np.array([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16])
                                                                    count = count + 1
    return k_table


def generate_k_table_8(number_of_actions, k_step, k_min, k_max, k_size):
    k1_step = k_step[0]
    k1_min = k_min[0]
    k1_max = k_max[0]
    k1_size = k_size

    k2_step = k_step[1]
    k2_min = k_min[1]
    k2_max = k_max[1]
    k2_size = k_size

    k3_step = k_step[2]
    k3_min = k_min[2]
    k3_max = k_max[2]
    k3_size = k_size

    k4_step = k_step[3]
    k4_min = k_min[3]
    k4_max = k_max[3]
    k4_size = k_size

    k5_step = k_step[4]
    k5_min = k_min[4]
    k5_max = k_max[4]
    k5_size = k_size

    k6_step = k_step[5]
    k6_min = k_min[5]
    k6_max = k_max[5]
    k6_size = k_size

    k7_step = k_step[6]
    k7_min = k_min[6]
    k7_max = k_max[6]
    k7_size = k_size

    k8_step = k_step[7]
    k8_min = k_min[7]
    k8_max = k_max[7]
    k8_size = k_size

    k_table = np.zeros((number_of_actions, 8))
    count = 0

    for a in [k8_min, k8_min + k8_step, k8_max]:
        for b in [k7_min, k7_min + k7_step, k7_max]:
            for p in [k6_min, k6_min + k6_step, k6_max]:
                for n in [k5_min, k5_min + k5_step, k5_max]:
                    for m in [k4_min, k4_min + k4_step, k4_max]:
                        for k in [k3_min, k3_min + k3_step, k3_max]:
                            for j in [k2_min, k2_min + k2_step, k2_max]:
                                for i in [k1_min, k1_min + k1_step, k1_max]:

                                    k1 = i
                                    k2 = j
                                    k3 = k
                                    k4 = m
                                    k5 = n
                                    k6 = p
                                    k7 = b
                                    k8 = a

                                    if k1 < 0.:
                                        k1 = 0.001

                                    if k2 <= 0.:
                                        k2 = 0.001

                                    if k3 < 0.:
                                        k3 = 0.001

                                    if k4 < 0.:
                                        k4 = 0.001

                                    if k5 < 0.:
                                        k5 = 0.001

                                    if k6 < 0.:
                                        k6 = 0.001

                                    if k7 < 0.:
                                        k7 = 0.001

                                    if k8 < 0.:
                                        k8 = 0.001


                                    k_table[count] = np.array([k1, k2, k3, k4, k5, k6, k7, k8])
                                    count = count + 1
    return k_table


def generate_k_table_6(number_of_actions, k_step,k_min,k_max,k_size):

    k1_step =k_step[0] 
    k1_min  =k_min[0] 
    k1_max  =k_max[0] 
    k1_size =k_size 

    k2_step =k_step[1] 
    k2_min = k_min[1] 
    k2_max = k_max[1] 
    k2_size =k_size 

    k3_step =k_step[2] 
    k3_min  =k_min[2] 
    k3_max  =k_max[2] 
    k3_size =k_size 

    k4_step =k_step[3] 
    k4_min = k_min[3] 
    k4_max = k_max[3] 
    k4_size =k_size 

    k5_step =k_step[4] 
    k5_min  =k_min[4] 
    k5_max  =k_max[4] 
    k5_size =k_size 

    k6_step =k_step[5] 
    k6_min = k_min[5] 
    k6_max = k_max[5] 
    k6_size =k_size 

    k_table = np.zeros((number_of_actions,6))
    count = 0

    for p in [k6_min,  k6_min + k6_step, k6_max]: 
        for n in [k5_min,  k5_min + k5_step, k5_max]:
            for m in [k4_min,  k4_min + k4_step, k4_max]:
                 for k in [k3_min,  k3_min + k3_step, k3_max]:
                    for j in [k2_min,  k2_min + k2_step, k2_max]:
                        for i in [k1_min,  k1_min + k1_step, k1_max]:

                            k1=i
                            k2=j
                            k3=k
                            k4=m
                            k5=n
                            k6=p
                            
                            if k1<0.:
                                k1 = 0.
                            
                            if k2<=0.:
                                k2 = 0. + k2_step
                            
                            if k3<0.:
                                k3 = 0.

                            if k4<0.:
                                k4 = 0.
                            
                            if k5<0.:
                                k5 = 0. + k5_step
                            
                            if k6<0.:
                                k6 = 0.
                            

                            k_table[count]=np.array([k1, k2, k3, k4, k5, k6])
                            count = count + 1


    return k_table




def generate_k_table_4(number_of_actions, k_step,k_min,k_max,k_size):

    k1_step =k_step[0] 
    k1_min  =k_min[0] 
    k1_max  =k_max[0] 

    k2_step =k_step[1] 
    k2_min = k_min[1] 
    k2_max = k_max[1] 

    k3_step =k_step[2] 
    k3_min  =k_min[2] 
    k3_max  =k_max[2] 

    k4_step =k_step[3] 
    k4_min = k_min[3] 
    k4_max = k_max[3] 

    k_table = np.zeros((number_of_actions,4))
    count = 0

    
    for m in [k4_min,  k4_min + k4_step, k4_max]:
         for k in [k3_min,  k3_min + k3_step, k3_max]:
            for j in [k2_min,  k2_min + k2_step, k2_max]:
                for i in [k1_min,  k1_min + k1_step, k1_max]:

                    k1=i
                    k2=j
                    k3=k
                    k4=m
                    
                    if k1<0.:
                        k1 = 0.
                    
                    if k2<=0.:
                        k2 = 0. + k2_step
                    
                    if k3<0.:
                        k3 = 0.

                    if k4<0.:
                        k4 = 0.
                    
                    k_table[count]=np.array([k1, k2, k3, k4])
                    count = count + 1


    return k_table


def generate_k_table_3(number_of_actions, k_step,k_min,k_max,k_size):

    k1_step = k_step[0] 
    k1_min  = k_min[0] 
    k1_max  = k_max[0] 

    k2_step = k_step[1] 
    k2_min  = k_min[1] 
    k2_max  = k_max[1] 

    k3_step = k_step[2] 
    k3_min  = k_min[2] 
    k3_max  = k_max[2] 


    k_table = np.zeros((number_of_actions,3))
    count = 0

    
    
    for k in [k3_min,  k3_min + k3_step, k3_max]:
        for j in [k2_min,  k2_min + k2_step, k2_max]:
            for i in [k1_min,  k1_min + k1_step, k1_max]:

                k1=i
                k2=j
                k3=k
                
                if k1<0.:
                    k1 = 0.
                
                if k2<=0.:
                    k2 = 0. + k2_step
                
                if k3<0.:
                    k3 = 0.

                
                k_table[count]=np.array([k1, k2, k3])
                count = count + 1


    return k_table


def generate_k_table_2(number_of_actions, k_step,k_min,k_max,k_size):

    k1_step = k_step[0] 
    k1_min  = k_min[0] 
    k1_max  = k_max[0] 

    k2_step = k_step[1] 
    k2_min  = k_min[1] 
    k2_max  = k_max[1] 

    
    k_table = np.zeros((number_of_actions,2))
    count = 0

    
    
    
    for j in [k2_min,  k2_min + k2_step, k2_max]:
        for i in [k1_min,  k1_min + k1_step, k1_max]:

            k1=i
            k2=j
            
            if k1<0.:
                k1 = 0.
            
            if k2<=0.:
                k2 = 0. + k2_step
            
            
            k_table[count]=np.array([k1, k2])
            count = count + 1


    return k_table



