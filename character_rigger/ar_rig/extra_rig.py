
import maya.cmds as mc

from ..ar_functions import create_jnts
from ..ar_functions import find_jnts


class extra_rig():

    # create offset joints for blend color limbs
    def blend_jnt_offset(self, parent, parentTo, size, colorR, colorG, colorB):

        spine_root_temp = find_jnts.find_jnts()
        spine_root = spine_root_temp.find_spine_root()

        chest_temp = find_jnts.find_jnts()
        chest = chest_temp.find_chest_jnt()

        if parent == 'spine_root_pos':
            single_jnt_var = create_jnts.create_jnts(   spine_root + '_blendOffset', 
                                                        size, 
                                                        colorR, 
                                                        colorG, 
                                                        colorB)
            myJoint = single_jnt_var.single_jnt()
            mc.Unparent(myJoint)

            pos_const = mc.parentConstraint(spine_root, myJoint)
            mc.delete(pos_const)
            
            # freeze join attr (to 0 rid of rotation) 
            mc.makeIdentity(myJoint, apply=True)

            #turn off scale compensate to prevent double scaling (when global scaling)
            #mc.setAttr(myJoint + '.segmentScaleCompensate', 0 )
            
            mc.parentConstraint(parentTo, myJoint)
            mc.scaleConstraint(parentTo, myJoint)  
            

        if parent == 'chest_pos':
            # create single joint
            single_jnt_var = create_jnts.create_jnts(   chest[0] + '_blendOffset', 
                                                        size, 
                                                        colorR, 
                                                        colorG, 
                                                        colorB)
            # myJoint = single joint
            myJoint = single_jnt_var.single_jnt()
            # unparent if auto parented to anything
            mc.Unparent(myJoint)

            # parent single jnt to chest
            pos_const = mc.parentConstraint(chest, myJoint)
            # delete parent constraint
            mc.delete(pos_const)

            # freeze join attr (to 0 rid of rotation) 
            mc.makeIdentity(myJoint, apply=True)

            #turn off scale compensate to prevent double scaling (when global scaling)
            mc.setAttr(myJoint + '.segmentScaleCompensate', 0 )

            # constrain jnt to chest control
            mc.parentConstraint(parentTo, myJoint)
            mc.scaleConstraint(parentTo, myJoint)

        else:
            pass

        return myJoint


    # find spine ctrls up to and including chest ctrl
    def to_chest_ctrl(self, fk_ctrl_list):
        chest_jnt_index = find_jnts.find_jnts().find_chest_jnt_index()

        to_chest_ctrl = fk_ctrl_list[:(chest_jnt_index + 1)]

        return to_chest_ctrl