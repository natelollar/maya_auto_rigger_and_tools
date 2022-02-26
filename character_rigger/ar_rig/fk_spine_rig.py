# spine rig

import maya.cmds as mc
import itertools
from ..ar_functions import find_jnts
from ..ar_functions import sel_joints
from ..ar_functions import nurbs_ctrl


class fk_spine_rig_class():
    #fk spine rig
    def fk_spine_rig_meth(self):
        #get spine root and head joitns
        spine_root_temp = find_jnts.find_jnts()
        spine_root = spine_root_temp.find_spine_root()

        head_end_temp = find_jnts.find_jnts()
        head_end = head_end_temp.find_head_jnt()
        
        # select joints in chain
        sel_joints_temp = sel_joints.sel_joints(spine_root, head_end)
        sel_spine = sel_joints_temp.rev_sel_jnt_chain()

        fk_ctrl_grp_list = []
        fk_ctrl_list = []
        for i in sel_spine:
            make_curve = nurbs_ctrl.nurbs_ctrl( i + '_ctrl', 4.5, 1, 0, 0)
            make_curve_info = make_curve.circle_ctrl()
            curveGroup = make_curve_info[0]
            nurbsCurve = make_curve_info[1]
            
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

        first_grp = fk_ctrl_grp_list[0]
        first_ctrl = fk_ctrl_list[0]

        last_grp = fk_ctrl_grp_list[-1]
        last_ctrl = fk_ctrl_list[-1]

        fk_ctrl_grp_list.pop(0)
        fk_ctrl_list.pop(-1)

        for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list, fk_ctrl_list):
            mc.parent(i_grp, i_ctrl)

        return first_grp, first_ctrl, last_grp, last_ctrl, fk_ctrl_list
        




