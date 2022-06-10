# Alamiyan: THis file has been created instead of robot_dict file.

import numpy as np
from canal import canal
# ______________________________________________________________________________________________________________________
canal_dict = {
    'TheCanal' : {'class': canal,
                       'set_point': np.array([0, 0, 0, 0, 0, 0, 0, 0]),
                       'initial_state': np.array([[0, 0, 0, 0, 0, 0, 0, 0]]),
                       # gate controller actions :  1  8 ,  2  3 , 4  7 , 5  6 -- four controller
                       # 'action_centroid': np.array([1.3, 0.03,\
                       #                              2.3, 0.06,\
                       #                              5.6, 0.16,\
                       #                              7.7, 0.21]),
                       'action_centroid': np.array([1.5, 1.5,\
                                                    1.5, 1.5,\
                                                    1.5, 1.5,\
                                                    1.5, 1.5]),
                       # 'action_centroid': np.array([0.5, 0.5, \
                       #                         0.5, 0.5, \
                       #                         0.5, 0.5, \
                       #                         0.5, 0.5]),
                       'K_step': 0.3,
                       'comments': ''}
    }


