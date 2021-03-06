import maya.cmds as mc
from ..ar_functions import nurbs_ctrl

class fk_ctrl():

    def single_fk_ctrl(self, jnt, parent_to, normal, size=4.5, colorR=1, colorG=0, colorB=0):
        make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, colorR, colorG, colorB )
        make_curve_info = make_curve.circle_ctrl(normal)
        curveGroup = make_curve_info[0]
        nurbsCurve = make_curve_info[1]
        
        # grp location and rotation to joint
        mc.parent( curveGroup, jnt, relative=True )
        mc.Unparent( curveGroup )

        # constrain joints to nurbs controls
        mc.parentConstraint(nurbsCurve, jnt)
        mc.scaleConstraint(nurbsCurve, jnt)

        # turn off "segmentScaleCompensate" to avoid double scale while joints parented under global contrl
        mc.setAttr( jnt + '.segmentScaleCompensate', 0 )

        mc.parent(curveGroup, parent_to)

        return curveGroup, nurbsCurve

    def single_fk_sphere_ctrl(self, jnt, parent_to, mat_name='nurbsSphere_mat#', size=1, colorR=1, colorG=0, colorB=0):
        make_sphere = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, colorR, colorG, colorB )
        make_sphere_info = make_sphere.nurbs_sphere_ctrl(mat_name)
        sphereGroup = make_sphere_info[0]
        nurbsSphere = make_sphere_info[1]
        
        # grp location and rotation to joint
        mc.parent( sphereGroup, jnt, relative=True )
        mc.Unparent( sphereGroup )

        # constrain joints to nurbs controls
        mc.parentConstraint(nurbsSphere, jnt)
        mc.scaleConstraint(nurbsSphere, jnt)

        # turn off "segmentScaleCompensate" to avoid double scale while joints parented under global contrl
        mc.setAttr( jnt + '.segmentScaleCompensate', 0 )
        
        if parent_to != '':
            mc.parent(sphereGroup, parent_to)

        return sphereGroup, nurbsSphere

    def single_fk_curve_ctrl(self, jnt, parent_to, version, size=1, colorR=1, colorG=0, colorB=0):
        if version == 'box':
            make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, colorR, colorG, colorB )
            make_curve_info = make_curve.box_ctrl()
            curveGroup = make_curve_info[0]
            nurbsCurve = make_curve_info[1]
        elif version == 'pyramid':
            make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, colorR, colorG, colorB )
            make_curve_info = make_curve.pyramid_ctrl()
            curveGroup = make_curve_info[0]
            nurbsCurve = make_curve_info[1]
        elif version == 'locator':
            make_curve = nurbs_ctrl.nurbs_ctrl( jnt + '_ctrl', size, colorR, colorG, colorB )
            make_curve_info = make_curve.locator_ctrl()
            curveGroup = make_curve_info[0]
            nurbsCurve = make_curve_info[1]
        
        # grp location and rotation to joint
        mc.parent( curveGroup, jnt, relative=True )
        mc.Unparent( curveGroup )

        # constrain joints to nurbs controls
        mc.parentConstraint(nurbsCurve, jnt)
        mc.scaleConstraint(nurbsCurve, jnt)

        # turn off "segmentScaleCompensate" to avoid double scale while joints parented under global contrl
        mc.setAttr( jnt + '.segmentScaleCompensate', 0 )

        if parent_to != '':
            mc.parent(curveGroup, parent_to)

        return curveGroup, nurbsCurve