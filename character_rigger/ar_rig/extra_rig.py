
import maya.cmds as mc

from ..ar_functions import create_jnts
from ..ar_functions import find_jnts


class extra_rig():

    # create offset joints for blend color limbs
    def blend_jnt_offset(self, parent, parentTo, size, colorR, colorG, colorB):

        spine_root_temp = find_jnts.find_jnts()
        spine_root = spine_root_temp.find_spine_root()

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

            mc.parentConstraint(parentTo, myJoint)
            mc.scaleConstraint(parentTo, myJoint)

        else:
            pass

        # set offset joint to invisible
        #mc.setAttr(myJoint + '.visibility', 0)

        return myJoint

    def single_fk_ctrl(self):
        pass

