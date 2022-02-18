# spine rig

import maya.cmds as mc
import itertools
import character_rigger

class fk_spine_rig_class():

    def fk_spine_rig_meth(self):
        character_rigger.ar_functions.sel_near_jnt.sel_near_jnt('spine_ROOT_selection_box')
        spine_root = mc.ls(sl=True)

        character_rigger.ar_functions.sel_near_jnt.sel_near_jnt('spine_END_selection_box')
        spine_end = mc.ls(sl=True)

        x = character_rigger.ar_functions.sel_joints.sel_joints(spine_root, spine_end)
        sel_spine = x.rev_sel_jnt_chain()

        fk_ctrl_grp_list = []
        fk_ctrl_list = []

        for i in sel_spine:
            z = character_rigger.ar_functions.nurbs_ctrl.nurbs_ctrl( i + '_ctrl', 4.5, 1, 0, 0)
            alpha = z.circle_ctrl()
            curveGroup = alpha[0]
            nurbsCurve = alpha[1]
            
            # grp location and rotation to joint
            mc.parent( curveGroup, i, relative=True )
            mc.Unparent( curveGroup )

            fk_ctrl_grp_list.append(curveGroup)
            fk_ctrl_list.append(nurbsCurve)

            # constrain joints to nurbs controls
            mc.parentConstraint(nurbsCurve, i)
            mc.scaleConstraint(nurbsCurve, i)

            # turn off "segmentScaleCompensate" to avoid double scale while joints parented under global contrl
            mc.setAttr( i + '.segmentScaleCompensate', 0 )

        top_grp = fk_ctrl_grp_list[0]

        fk_ctrl_grp_list.pop(0)
        fk_ctrl_list.pop(-1)

        for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list, fk_ctrl_list):
            mc.parent(i_grp, i_ctrl)

        return top_grp




