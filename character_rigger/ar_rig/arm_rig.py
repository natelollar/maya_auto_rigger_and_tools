import maya.cmds as mc

import maya.api.OpenMaya as om

import itertools

from ..ar_functions import find_jnts
from ..ar_functions import sel_joints

# arm rig
class arm_rig():

    def arm_rig(self, direction):
        #___________________Find Arm Joints____________________________#
        # create arm joint list
        if direction == 'left':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts = arm_jnts_temp.find_arm_jnts('left')
        elif direction == 'right':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts = arm_jnts_temp.find_arm_jnts('right')
        
        # create arm joint variables
        clav_jnt = arm_jnts[0] 
        shlder_jnt = arm_jnts[1] 
        elbow_jnt = arm_jnts[2] 
        twist_jnts = arm_jnts[3:-1]
        wrist_jnt = arm_jnts[-1]

        # arm joints without twist jnts
        base_arm_jnts = [clav_jnt, shlder_jnt, elbow_jnt, wrist_jnt]

        #___________________End of Find Arm Joints____________________________#



