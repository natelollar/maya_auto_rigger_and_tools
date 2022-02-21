import maya.cmds as mc
from character_rigger.ar_functions import sel_near_jnt

# find joints with boudning box object as starting point
class find_jnts():

    def __init__(self, standin_obj):
        self.standin_obj = standin_obj
        
    # get left or right most child joint (immediate child)
    def l_r_child_jnt(self, direction):
        # select bounding box object joint
        myJoint = sel_near_jnt.sel_near_jnt(self.standin_obj)
        # spine root children
        jointSel = mc.listConnections(myJoint, d=True, type='joint')
        # get world positions
        x_pos_list = []
        for i in jointSel:
            pos = mc.xform(i, q=True , ws=True, t=True)
            x_pos = pos[0]
            x_pos_list.append(x_pos)

        # get index of joint with highest x value position (more Left)
        high_x_val_ind = x_pos_list.index(max(x_pos_list))
        # get joint name with highest x value
        high_x_val_jnt = [jointSel[high_x_val_ind]]
        
        # get index of joint with lowest x value position (more Left)
        low_x_val_ind = x_pos_list.index(min(x_pos_list))
        # get joint name with lowest x value
        low_x_val_jnt = [jointSel[low_x_val_ind]]

        if direction == 'left':
            mc.select(high_x_val_jnt)
            return high_x_val_jnt
        elif direction == 'right':
            mc.select(low_x_val_jnt)
            return low_x_val_jnt

    def l_r_clavicle_jnt(self, direction):
        # select bounding box object joint
        myJoint = sel_near_jnt.sel_near_jnt(self.standin_obj)
        mc.select(cl=True)
        # list immediate joint children
        jointSel = mc.listConnections(myJoint, d=True, type='joint')

        y_pos_list = []
        for i in jointSel:
            pos = mc.xform(i, q=True , ws=True, t=True)
            y_pos = pos[1]
            y_pos_list.append(y_pos)

        # get index of joint with highest x value position (more Left)
        high_y_val_ind = y_pos_list.index(max(y_pos_list))
        # get joint name with highest x value
        high_y_val_jnt = [jointSel[high_y_val_ind]]

        jointSelA = mc.listConnections(high_y_val_jnt, s=False, type='joint')

        for i in range(1,25):
            if len(jointSelA) == 1:
                jointSelA = mc.listConnections( jointSelA, s=False, type = 'joint' )
            else:
                jointSelB = mc.listConnections( jointSelA, d=False, type = 'joint')
                mc.select(cl=True)
                mc.select(jointSelB)
        
        # with chest found, now select right or left clavicle
        jointSelC_temp = mc.listConnections(jointSelB, type='joint', s=False )
        mc.select(jointSelC_temp)
        jointSelC = mc.ls(sl=True)

        # get world positions of joints
        x_pos_list = []
        for i in jointSelC:
            pos = mc.xform(i, q=True , ws=True, t=True)
            x_pos = pos[0]
            x_pos_list.append(x_pos)

        # get index of joint with highest x value position (more Left)
        high_x_val_ind = x_pos_list.index(max(x_pos_list))
        # get joint name with highest x value
        high_x_val_jnt = [jointSelC[high_x_val_ind]]

        # get index of joint with lowest x value position (more Left)
        low_x_val_ind = x_pos_list.index(min(x_pos_list))
        # get joint name with lowest x value
        low_x_val_jnt = [jointSelC[low_x_val_ind]]
    
        if direction == 'left':
            mc.select(high_x_val_jnt)
            return high_x_val_jnt
        elif direction == 'right':
            mc.select(low_x_val_jnt)
            return low_x_val_jnt





