import maya.cmds as mc

from ..ar_functions import sel_near_jnt


def fk_chains_rig(  standin_name = 'fkObj',
                    fk_ctrl_size = 10):


    #______________find correct standin_obj's _______________#
    scene_nrbsCrv_shp_lst = mc.ls(type='nurbsCurve') # gets curve shapes
    #print(scene_nrbsCrv_shp_lst)
    nrbsCrv_transform_lst = []
    for i in scene_nrbsCrv_shp_lst:
        nrbsCrv_transform = mc.listRelatives(i, parent=True)
        if standin_name in nrbsCrv_transform[0]: # get fk ctrl standin objects
            if nrbsCrv_transform[0] not in nrbsCrv_transform_lst: #is unique
                nrbsCrv_transform_lst.append(nrbsCrv_transform[0])

    #print(nrbsCrv_transform_lst)


    #____________find jnt chains_____________#
    jntChain_lst_lst = []
    for i in nrbsCrv_transform_lst:
        strt_jnt = sel_near_jnt.sel_near_jnt(i)
        #_____find jnt chain______#
        jntChain_lst = []
        jntChain_lst0 = mc.listRelatives(strt_jnt, type='joint', ad=True)
        jntChain_lst0.append(strt_jnt[0]) # add jnt back in 
        jntChain_lst0.reverse()
        # remove joint with 'end'
        for jnt in jntChain_lst0:
            if 'end' not in jnt.lower():
                jntChain_lst.append(jnt)
        # list of jnt chain lists
        jntChain_lst_lst.append(jntChain_lst)

    #print(jntChain_lst_lst)

    
    for standin_obj in nrbsCrv_transform_lst:
        #____________________________________________#
        #____ get standin_obj parent jnt_____________#
        #get connecting curve
        standin_curve = mc.listConnections(standin_obj, 
                                        source=False, 
                                        destination=True,
                                        type = 'nurbsCurve')

        # get curve shape
        standin_curve_shape = mc.listRelatives(standin_curve, type='shape')
        #get other standin_obj connected to curve
        parent_standin = mc.listConnections(standin_curve_shape[0] + '.controlPoints[0]', 
                                            source=True, 
                                            destination=False)
        # get joint under connected standin_obj
        parent_jnt = sel_near_jnt.sel_near_jnt(parent_standin)

        #print(standin_curve)
        #print(standin_obj + '_____________')
        #print(parent_standin_jnt)

        #____________________________________________#
        #____ get jnt chain of standin obj___________#
        strt_jnt = sel_near_jnt.sel_near_jnt(standin_obj)
        #_____find jnt chain______#
        jntChain_lst = []
        jntChain_lst0 = mc.listRelatives(strt_jnt, type='joint', ad=True)
        jntChain_lst0.append(strt_jnt[0]) # add jnt back in 
        jntChain_lst0.reverse()
        # remove joint with 'end'
        for jnt in jntChain_lst0:
            if 'end' not in jnt.lower():
                jntChain_lst.append(jnt)

        #print(jntChain_lst)
        
        #______________________________#
        #_________FK Controls__________#
        #create list for ctrl grp parenting to one another
        fk_ctrl_grp_list = []
        #create list for ctrl parenting to one another
        fk_ctrl_list = []
        #create nurbs curve ctrls
        for i in jntChain_lst:
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

        print(parent_jnt)
        print(fk_ctrl_grp_list[0])
        mc.parentConstraint(parent_jnt, fk_ctrl_grp_list[0], mo=True )

        #remove first and last of lists to correctly parent ctrls and grps together in for loop
        fk_ctrl_grp_list_temp = fk_ctrl_grp_list[1:]

        fk_ctrl_list_temp = fk_ctrl_list[:-1]

        #parent ctrls and grps together
        for i_grp, i_ctrl in zip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
            mc.parent(i_grp, i_ctrl)
        
