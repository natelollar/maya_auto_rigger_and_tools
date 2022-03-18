# fk chain

import maya.cmds as mc

try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass

from ..ar_functions import nurbs_ctrl


class fk_chain():
    #fk spine rig
    def fk_chain(self, 
                jnt_chain, 
                parent_to = '', 
                parent_type = 'parent', 
                ctrl_type='circle',
                size=5, 
                color_r=1, 
                color_g=0, 
                color_b=0,
                circle_normal=[1,0,0],
                mat_name='blinn_ctrl_mat'):

        fk_ctrl_grp_list = []
        fk_ctrl_list = []
        for jnt in jnt_chain:
            if ctrl_type == 'circle':
                make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, color_r, color_g, color_b)
                make_curve_info = make_curve.circle_ctrl(normal=circle_normal)
                curveGroup = make_curve_info[0]
                nurbsCurve = make_curve_info[1]
            if ctrl_type == 'box':
                make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, color_r, color_g, color_b)
                make_curve_info = make_curve.box_ctrl()
                curveGroup = make_curve_info[0]
                nurbsCurve = make_curve_info[1]
            if ctrl_type == 'sphere':
                make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, color_r, color_g, color_b)
                make_curve_info = make_curve.sphere_ctrl()
                curveGroup = make_curve_info[0]
                nurbsCurve = make_curve_info[1]
            if ctrl_type == 'locator':
                make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, color_r, color_g, color_b)
                make_curve_info = make_curve.locator_ctrl()
                curveGroup = make_curve_info[0]
                nurbsCurve = make_curve_info[1]
            if ctrl_type == 'nurbs_sphere':
                make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, color_r, color_g, color_b)
                make_curve_info = make_curve.nurbs_sphere_ctrl(mat_name=mat_name)
                curveGroup = make_curve_info[0]
                nurbsCurve = make_curve_info[1]
            
            # grp location and rotation to joint
            mc.parent( curveGroup, jnt, relative=True )
            mc.Unparent( curveGroup )

            fk_ctrl_grp_list.append(curveGroup)
            fk_ctrl_list.append(nurbsCurve)

            # constrain joints to nurbs controls
            mc.parentConstraint(nurbsCurve, jnt)
            mc.scaleConstraint(nurbsCurve, jnt)

            # turn off "segmentScaleCompensate" to avoid double scale while joints parented under global contrl
            mc.setAttr( jnt + '.segmentScaleCompensate', 0 )

        first_grp = fk_ctrl_grp_list[0]
        first_ctrl = fk_ctrl_list[0]

        last_grp = fk_ctrl_grp_list[-1]
        last_ctrl = fk_ctrl_list[-1]

        if parent_type == 'parent':
            mc.parent(first_grp, parent_to)
        elif parent_type == 'constrain':
            mc.parentConstraint(parent_to, first_grp)
            mc.scaleConstraint(parent_to, first_grp)
        else:
            pass


        # pop off first and last of list, to parent ctrl and grp correctly
        fk_ctrl_grp_list.pop(0)
        fk_ctrl_list.pop(-1)
        # parent ctrl and grp
        for i_grp, i_ctrl in zip(fk_ctrl_grp_list, fk_ctrl_list):
            mc.parent(i_grp, i_ctrl)

        return first_grp, first_ctrl, last_grp, last_ctrl