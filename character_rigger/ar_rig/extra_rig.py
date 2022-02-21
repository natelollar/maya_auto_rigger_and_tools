
import maya.cmds as mc
import itertools
from character_rigger.ar_functions import create_jnts
from character_rigger.ar_functions import sel_near_jnt


class extra_rig():

    # create offset joints for blend color limbs
    def blend_jnt_offset(self, parent, parentTo, size, colorR, colorG, colorB):

        sel_near_jnt.sel_near_jnt('spine_ROOT_select_object')
        spine_root = mc.ls(sl=True)

        if parent == 'spine_root_pos':
            single_jnt_var = create_jnts.create_jnts(spine_root[0] + '_blendOffset', size, colorR, colorG, colorB)
            myJoint = single_jnt_var.single_jnt()
            mc.Unparent(myJoint)

            pos_const = mc.parentConstraint(spine_root, myJoint)
            mc.delete(pos_const)

            mc.parentConstraint(parentTo, myJoint)
            mc.scaleConstraint(parentTo, myJoint)

        else:
            pass

        return myJoint

    def single_fk_ctrl(self):
        pass

