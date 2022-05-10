import maya.cmds as mc

from ..ar_functions import sel_near_jnt



def fk_chains_rig(fk_ctrl_size = 10):


    scene_nurbs = mc.ls(type='nurbsCurve')
    print(scene_nurbs)

    scene_transforms = mc.ls(type='transform')
    print(scene_transforms)


    standin_curve = mc.listConnections('standin_obj_l_wingA', 
                                        source=False, 
                                        destination=True,
                                        type = 'shape')

    standin_curve_shape = mc.listRelatives(standin_curve, type='shape')

    parent_standin = mc.listConnections(standin_curve_shape[0] + '.controlPoints[0]', 
                                        source=True, 
                                        destination=False)

    print(standin_curve)

    print(standin_curve_shape)

    print(parent_standin)

    parent_standin_jnt = sel_near_jnt.sel_near_jnt(parent_standin)

    print(parent_standin_jnt)




    fkJoint_list = []

    '''

    #______________________________#
    #_________FK Controls__________#
    #______________________________#
    #create list for ctrl grp parenting to one another
    fk_ctrl_grp_list = []
    #create list for ctrl parenting to one another
    fk_ctrl_list = []
    #create nurbs curve ctrls
    for i in fkJoint_list:
        #create curve box
        myCurve = mc.curve(d=1, p=[ (-1, 1, 1),
                                    (-1, 1, -1),
                                    (1, 1, -1),
                                    (1, 1, 1),
                                    (-1, 1, 1),
                                    (-1, -1, 1),
                                    (-1, -1, -1),
                                    (1, -1, -1),
                                    (1, -1, 1),
                                    (-1, -1, 1),
                                    (-1, 1, 1),
                                    (1, 1, 1),
                                    (1, -1, 1),
                                    (1, -1, -1),
                                    (1, 1, -1),
                                    (-1, 1, -1),
                                    (-1, -1, -1)
                                    ])
        #curve size
        mc.setAttr(myCurve + '.scale', fk_ctrl_size, fk_ctrl_size, fk_ctrl_size)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((itemsShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((itemsShape[0] + '.overrideColorRGB'), 1, 0, 0)

        #rename curve, with joint name, and then new prefix
        myCurve_name = mc.rename(i + '_ctrl')

        #group curve
        curveGroup = mc.group(myCurve_name)
        curveGroup_offset = mc.group(myCurve_name)
        #rename group
        curveGroup_name = mc.rename(curveGroup, (myCurve_name + '_grp'))
        curveGroup_offset_name = mc.rename(curveGroup_offset, (myCurve_name + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(curveGroup_name, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(curveGroup_name)
        #create a list for the groups (for parenting to one another)
        fk_ctrl_grp_list.append(curveGroup_name)
        #create a list of the ctrl curves (to parent constrain the joints to)
        fk_ctrl_list.append(myCurve_name)

        #parent and scale constrain ctrls to fk jnts
        mc.parentConstraint(myCurve_name, i)


    #remove first and last of lists to correctly parent ctrls and grps together in for loop
    fk_ctrl_grp_list_temp = fk_ctrl_grp_list[1:]

    fk_ctrl_list_temp = fk_ctrl_list[:-1]

    #parent ctrls and grps together
    for i_grp, i_ctrl in zip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
        mc.parent(i_grp, i_ctrl)
    '''
