import maya.cmds as mc

import string

from ..ar_functions import sel_near_jnt
from ..ar_functions import sel_joints


def tentacle_rig(  defaultJnt_prefix = 'sknJnt_', 
                        fkJnt_prefix = 'fkJnt_', 
                        ikJnt_prefix = 'ikJnt_',
                        offs_prntJnt = 'offs_prntJnt_hips', 
                        spine_root_ctrl = 'hip_ctrl',
                        global_ctrl = 'global_ctrl',
                        global_misc_grp = 'global_misc_grp',
                        fk_ctrl_size = 10,
                        name = 'test_'):

    print('________________Gadzooooks!__________________')
    #_______ initial joints ________#
    
    spineRoot_jnt = sel_near_jnt.sel_near_jnt('standin_obj_spine_root')
    tailStart_jnt = sel_near_jnt.sel_near_jnt('standin_obj_tail_start')
    tailEnd_jnt = sel_near_jnt.sel_near_jnt('standin_obj_tail_end')
    ikSpline_jntA_pos = sel_near_jnt.sel_near_jnt('standin_obj_ikSpline_A')
    ikSpline_jntB_pos = sel_near_jnt.sel_near_jnt('standin_obj_ikSpline_B')

    spineRoot_ctrl_nm0 = spineRoot_jnt[0].replace(defaultJnt_prefix, '')
    spineRoot_ctrl_nm1 = spineRoot_ctrl_nm0 + '_ctrl'

    # select joint chain
    jnt_chain = sel_joints.sel_joints(tailStart_jnt[0], tailEnd_jnt[0]).rev_sel_jnt_chainA()

    #_________________________________#
    # extract basic name of joint chain
    name0 = jnt_chain[0].replace(defaultJnt_prefix, '')
    name = ''.join([i for i in name0 if not i.isdigit()]) 


    
    #______________________________#
    #_____Blended Joint Chain______#
    #______________________________#

    fkJoint_list = []
    ikJoint_list = []
    for i in jnt_chain:
        #______________________#
        #____create FK chain___#
        fkJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr('.radius', 4)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', 1, 0, 0.1)
        #show attr
        mc.setAttr('.rotateOrder', cb=True)
        mc.setAttr('.rotateAxisX', cb=True)
        mc.setAttr('.rotateAxisY', cb=True)
        mc.setAttr('.rotateAxisZ', cb=True)
        mc.setAttr('.jointOrientX', cb=True)
        mc.setAttr('.jointOrientY', cb=True)
        mc.setAttr('.jointOrientZ', cb=True)

        
        fkJoint_rename = i.replace(defaultJnt_prefix, fkJnt_prefix)
        fkJoint = mc.rename(fkJoint_orig, fkJoint_rename)
        mc.Unparent(fkJoint)

        # create list of fk joints
        fkJoint_list.append(fkJoint)
        
        #_______________________#
        #____create _IK chain___#
        ikJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr('.radius', 5)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', .1, .9, 0.1)
        #show attr
        mc.setAttr('.rotateOrder', cb=True)
        mc.setAttr('.rotateAxisX', cb=True)
        mc.setAttr('.rotateAxisY', cb=True)
        mc.setAttr('.rotateAxisZ', cb=True)
        mc.setAttr('.jointOrientX', cb=True)
        mc.setAttr('.jointOrientY', cb=True)
        mc.setAttr('.jointOrientZ', cb=True)
        
        ikJoint_rename = i.replace(defaultJnt_prefix, ikJnt_prefix)
        ikJoint = mc.rename(ikJoint_orig, ikJoint_rename)
        mc.Unparent(ikJoint)

        # create list of ik joints
        ikJoint_list.append(ikJoint)


    #parent FK joints together based on current index
    currentIndex = -1
    for i in fkJoint_list:
        currentIndex += 1
        if i != fkJoint_list[0]:
            mc.parent(fkJoint_list[currentIndex], fkJoint_list[currentIndex-1])
    #parent IK joints together based on current index
    currentIndex = -1
    for i in ikJoint_list:
        currentIndex += 1
        if i != ikJoint_list[0]:
            mc.parent(ikJoint_list[currentIndex], ikJoint_list[currentIndex-1])

    
    #blend color node lists
    blendColorsTran_list = []
    blendColorsRot_list = []
    #blend joints together
    for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, jnt_chain):
        #create blend color nodes
        blendColorsTran = mc.createNode('blendColors', n= i + '_blendColorsTran')
        blendColorsRot = mc.createNode('blendColors', n= i + 'blendColorsRot')
        #translate
        mc.connectAttr((i_FK + '.translate'), (blendColorsTran + '.color1'), f=True)
        mc.connectAttr((i_IK + '.translate'), (blendColorsTran + '.color2'), f=True)
        mc.connectAttr((blendColorsTran + '.output'), (i + '.translate'), f=True)
        #rotate
        mc.connectAttr((i_FK + '.rotate'), (blendColorsRot + '.color1'), f=True)
        mc.connectAttr((i_IK + '.rotate'), (blendColorsRot + '.color2'), f=True)
        mc.connectAttr((blendColorsRot + '.output'), (i + '.rotate'), f=True)
        #append lists for outside loop use
        blendColorsTran_list.append(blendColorsTran)
        blendColorsRot_list.append(blendColorsRot)
    
    
    #__________________________________________________________________#
    # parent top joints to original root spine0 to offset blend Color nodes
    #__________________________________________________________________#
    mc.parent(fkJoint_list[0], offs_prntJnt)

    mc.parent(ikJoint_list[0], offs_prntJnt)

    



    #______________________________#
    #_________FK Controls__________#
    #______________________________#
    #create list for ctrl grp parenting to one another
    fk_ctrl_grp_list = []
    #create list for ctrl parenting to one another
    fk_ctrl_list = []
    #create nurbs curve ctrls
    for i in fkJoint_list[:-1]:
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

        # rename curve
        myCurve_name0 = mc.rename(myCurve, i)
        myCurve_name1 = myCurve_name0.replace(fkJnt_prefix, '') # get rid of jnt prefix
        myCurve_name2 = myCurve_name1.replace('|', '') # to avoid python error
        myCurve_name = mc.rename(myCurve_name2 + '_fkCtrl')

        
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

    
    #_____________________________________#
    #______________IK Ctrls_______________#
    #_____________________________________#
    
    
    #___________create IK HANDLE____________#

    ikHndl_var = mc.ikHandle( n=name + '_ikHndl', 
                                sj=ikJoint_list[0], 
                                ee=ikJoint_list[-1], 
                                sol='ikSplineSolver',
                                scv=False, # simplify curve
                                pcv=False) # parent curve

    # rename effector
    ikHndl_effector_var = mc.listConnections(ikHndl_var, s=True, type='ikEffector')
    mc.rename(ikHndl_effector_var, ikHndl_var[0] + '_effector')
    
    # rename curve
    ikHndl_crv0 = mc.listConnections(ikHndl_var[0], s=True, type='nurbsCurve')
    ikHndl_crv = mc.rename(ikHndl_crv0, ikHndl_var[0] + '_curve')

    


    #_______________________________________#
    #___________ik Spline Joints____________#
    #_______________________________________#
    
    ikSpline_jntPos_lst = [tailStart_jnt, ikSpline_jntA_pos, ikSpline_jntB_pos]

    ikSpline_jnt_lst = []
    for i in ikSpline_jntPos_lst:
        current_index = ikSpline_jntPos_lst.index(i)
        #create joint at correct position
        ikSpline_jnt = mc.joint(i, n=name + '_ikSpline_jnt' + string.ascii_uppercase[current_index], rad=25)
        mc.Unparent(ikSpline_jnt)
        
        #color joint
        mc.setAttr(ikSpline_jnt + '.useObjectColor', 2)
        mc.setAttr(ikSpline_jnt + '.wireColorRGB', 0, .5, 1)

        #show attr
        mc.setAttr(ikSpline_jnt + '.rotateOrder', cb=True)
        mc.setAttr(ikSpline_jnt + '.rotateAxisX', cb=True)
        mc.setAttr(ikSpline_jnt + '.rotateAxisY', cb=True)
        mc.setAttr(ikSpline_jnt + '.rotateAxisZ', cb=True)
        mc.setAttr(ikSpline_jnt + '.jointOrientX', cb=True)
        mc.setAttr(ikSpline_jnt + '.jointOrientY', cb=True)
        mc.setAttr(ikSpline_jnt + '.jointOrientZ', cb=True)
        

        ikSpline_jnt_lst.append(ikSpline_jnt)

    #_____skin start and end joints to ik spline curve_____#
    mc.skinCluster( ikSpline_jnt_lst[0], 
                    ikSpline_jnt_lst[1], 
                    ikSpline_jnt_lst[2],
                    ikHndl_crv, 
                    n = ikHndl_crv + '_skinCluster',
                    dropoffRate = 2)

    # to organize and global scale
    mc.parent(ikSpline_jnt_lst, offs_prntJnt)
    
    # ______ arrow twist curve _______   #
    # for last spline ctrl, to represent twist
    arrowTwist_list = []
    for i in range(0,1):
        myCurve0 = mc.curve(p=[ 
                            (-6.97, -0.0, -50.0),
                            (-6.97, -0.0, -50.0),
                            (-8.499, -25.022, -47.673),
                            (-10.39, -41.372, -29.961),
                            (-12.015, -52.16, -9.608),
                            (-12.5, -47.005, 21.995),
                            (-12.5, -38.326, 32.149),
                            (-12.5, -38.326, 32.149),
                            (-12.5, -38.326, 32.149),
                            (-20.974, -36.448, 34.227),
                            (-20.974, -36.448, 34.227),
                            (-20.974, -36.448, 34.227),
                            (-13.57, -27.743, 42.15),
                            (-5.718, -14.063, 48.981),
                            (0.0, 0.0, 50.0),
                            (0.0, 0.0, 50.0),
                            (0.0, 0.0, 50.0),
                            (5.545, -14.063, 48.981),
                            (13.506, -27.743, 42.15),
                            (20.974, -36.448, 34.227),
                            (20.974, -36.448, 34.227),
                            (20.974, -36.448, 34.227),
                            (12.5, -38.326, 32.149),
                            (12.5, -38.326, 32.149),
                            (12.5, -38.326, 32.149),
                            (12.5, -47.005, 21.995),
                            (12.015, -52.16, -9.608),
                            (10.39, -41.372, -29.961),
                            (8.499, -25.022, -47.673),
                            (6.97, -0.0, -50.0),
                            (6.97, -0.0, -50.0),
                            (6.97, -0.0, -50.0),
                            (-6.97, -0.0, -50.0),
                            ] )
                            
                            
        myCurve1 = mc.duplicate(myCurve0)
        mc.setAttr(myCurve1[0] + '.scaleY', -1)
        mc.setAttr(myCurve1[0] + '.rotateY', -180)
        mc.makeIdentity(myCurve1, apply=True)

        crv_lst = [myCurve0, myCurve1[0]]

        crvShp_lst = []
        for i in crv_lst:
            #change transform scale
            mc.setAttr(i + '.scale', .35, .85, .85)
            mc.makeIdentity(i, apply=True)
            #change shape color, line width
            crv_shp = mc.listRelatives(i, s=True)
            mc.setAttr((crv_shp[0] + '.overrideEnabled'), 1)
            mc.setAttr((crv_shp[0] + '.overrideRGBColors'), 1)
            mc.setAttr((crv_shp[0] + '.overrideColorRGB'), .6, .8, 0)
            mc.setAttr((crv_shp[0] + '.lineWidth'), 1.5)

            crvShp_lst.append(crv_shp)

        
        mc.parent(crvShp_lst[1], myCurve0, r=1, s=1)
        
        mc.delete(myCurve1) # delete empty transform
            
        myCurve = mc.rename(myCurve0, name + 'arrowTwist_ctrl#')

        arrowTwist_list.append(myCurve)


    
    #___________ik Spline CTRLs____________#
    ik_splineCtrl_list = []
    ik_splineGrp_list = []
    for i in ikSpline_jnt_lst:
        current_index = ikSpline_jnt_lst.index(i) # above other for loops in loop, b/c share i 
        myJnt = i # to know what i referreing too
        #______ create curve shape ______#
        myCurve0 = mc.curve(p=[ 
                            (-71.438, 0.0, -71.438),
                            (-57.509, 0.0, -84.796),
                            (-41.145, 0.0, -92.642),
                            (-26.517, 0.0, -97.227),
                            (-26.517, 0.0, -97.227),
                            (-26.517, 0.0, -97.227),
                            (-24.436, 0.0, -118.027),
                            (-24.436, 0.0, -118.027),
                            (-24.436, 0.0, -118.027),
                            (-48.922, 0.0, -117.978),
                            (-48.922, 0.0, -117.978),
                            (-48.922, 0.0, -117.978),
                            (0.0, 0.0, -205.925),
                            (0.0, 0.0, -205.925),
                            (0.0, 0.0, -205.925),
                            (49.02, 0.0, -118.175),
                            (49.02, 0.0, -118.175),
                            (49.02, 0.0, -118.175),
                            (24.535, 0.0, -118.126),
                            (24.535, 0.0, -118.126),
                            (24.535, 0.0, -118.126),
                            (26.517, 0.0, -97.227),
                            (26.517, 0.0, -97.227),
                            (26.517, 0.0, -97.227),
                            (42.538, 0.0, -91.659),
                            (58.975, 0.0, -83.918),
                            (71.438, 0.0, -71.438)
                            ] )

        myCurve1 = mc.duplicate(myCurve0)
        mc.setAttr(myCurve1[0] + '.scaleZ', -1)
        mc.makeIdentity(myCurve1, apply=True)

        myCurve2 = mc.duplicate(myCurve0)
        mc.setAttr(myCurve2[0] + '.rotateY', -90)
        mc.makeIdentity(myCurve2, apply=True)

        myCurve3 = mc.duplicate(myCurve0)
        mc.setAttr(myCurve3[0] + '.rotateY', 90)
        mc.makeIdentity(myCurve3, apply=True)

        myCurveCircle = mc.circle(r=93, nr=(0,1,0), ch=0)

        crv_lst = [myCurve0, myCurve1, myCurve2, myCurve3, myCurveCircle]

        crvShp_lst = []
        for i in crv_lst:
            crv_shp = mc.listRelatives(i, s=True)
            mc.setAttr((crv_shp[0] + '.overrideEnabled'), 1)
            mc.setAttr((crv_shp[0] + '.overrideRGBColors'), 1)
            mc.setAttr((crv_shp[0] + '.overrideColorRGB'), .1, .8, 0)
            mc.setAttr((crv_shp[0] + '.lineWidth'), 1.5)

            crvShp_lst.append(crv_shp)

        for i in crvShp_lst[1:]:
            mc.parent(i, myCurve0, r=1, s=1)

        for i in crv_lst[1:]:
            mc.delete(i) # delete empty transforms
            
        for i in crvShp_lst:
            mc.rename(i, name + 'fourArrow_ctrlShape#') # to make sure all shapes get renamed # glitch with circle shape
            

        myCurve = mc.rename(myCurve0, name + '_ik_ctrl' + string.ascii_uppercase[current_index])

        #_____________create curve shape END______________#

        #curve orient
        mc.setAttr(myCurve + '.rotate', 0, 0, 90)
        #curve size
        mc.setAttr(myCurve + '.scale', .2, .2, .2)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        
        #group curve
        curveGrouped_offset = mc.group(myCurve)

        curveGrouped = mc.group(curveGrouped_offset)
        
        
        #rename group
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        
        
        #parent and zero curveGrp to joints
        mc.parent(myGroup, myJnt, relative=True)

        
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        
        #constrain ctrl to jnt
        mc.parentConstraint(myCurve, myJnt)

        
        #append grp for outside use
        ik_splineCtrl_list.append(myCurve)
        ik_splineGrp_list.append(myGroup)

    #________________#
    # parent twist shape to last ik ctrl
    arrowTwist_pos = mc.parentConstraint(ikSpline_jnt_lst[-1], arrowTwist_list[0] ) # position arrow twist curve
    mc.delete(arrowTwist_pos) # delete positional parent constraint
    arrowTwist_shp = mc.listRelatives(arrowTwist_list[0], s=True)
    mc.parent(arrowTwist_shp, ik_splineCtrl_list[-1], r=1, s=1) # parent arrow twist shape to last spline ctrl
    mc.delete(arrowTwist_list) # delete empty transform
    #________________#


    # to organize and for visibility
    myIKGrp = mc.group(em=True, n=name + '_ik_grp')
    mc.parent(ik_splineGrp_list, myIKGrp)


    # add stretch attribute to last ik spline ctrl
    mc.addAttr(ik_splineCtrl_list[-1], ln='__________', nn='__________', at='enum', enumName = '__________') # add divider organizer attr
    mc.setAttr(ik_splineCtrl_list[-1] + '.__________', channelBox=1 ) # does not appear in channel box otherwise
    mc.addAttr(ik_splineCtrl_list[-1], ln='Stretch_Blend', nn='Stretch_Blend', min=0, max=1, at='double', dv=1, k=1) # actual stretch attr
    

    #_______________________IK Twist _______________________#
    #_______________________________________________________#

    mc.connectAttr(ik_splineCtrl_list[-1] + '.rotateX', ikHndl_var[0] + '.twist')

    #______________________________________________________________________________#
    #____________________________IK Stretch _______________________________________#
    #______________________________________________________________________________#

    # _____ nodes ______ #

    curveInfo = mc.shadingNode('curveInfo', asUtility=1, n = name + '_ikSpline_curveInfo' ) # for arc length

    global_scale_offs = mc.shadingNode('multiplyDivide', asUtility=1, n = name + '_global_scale_offs' )

    crv_len_ratio = mc.shadingNode('multiplyDivide', asUtility=1, n = name + '_crv_len_ratio' ) # create multDiv node
    mc.setAttr(crv_len_ratio + '.operation', 2) # set to Divide


    # _____ attributes ______ #

    global_ctrl_sclX = global_ctrl + '.scaleX'

    stretch_blend = ik_splineCtrl_list[-1] + '.Stretch_Blend'

    #_____ node connections ________#

    mc.connectAttr(ikHndl_crv + '.worldSpace[0]', curveInfo + '.inputCurve')  # needs to be first connection to input arc length
    curveInfo_length = mc.getAttr(curveInfo + '.arcLength') # get length from recent input

    mc.connectAttr( global_ctrl_sclX, global_scale_offs + '.input1X', f=1 ) # create global scale offset node
    mc.setAttr(global_scale_offs + '.input2X', curveInfo_length) #set to spline curve length

    mc.connectAttr( curveInfo + '.arcLength', crv_len_ratio + '.input1X', f=1 )
    mc.connectAttr( global_scale_offs + '.outputX', crv_len_ratio + '.input2X', f=1 )


    # jnt attr, nodes, connections

    for i in ikJoint_list:
        jnt_tx = mc.getAttr(i + '.tx' )

        jnt_len_mult = mc.shadingNode('multiplyDivide', asUtility=1, n = i + '_len_mult' )
        jnt_strch_blend = mc.shadingNode('blendColors', asUtility=1, n = i + '_strch_blend' )

        mc.connectAttr( crv_len_ratio + '.outputX', jnt_len_mult + '.input1X', f=1 )
        mc.setAttr(jnt_len_mult + '.input2X', jnt_tx )

        mc.connectAttr( jnt_len_mult + '.outputX', jnt_strch_blend + '.color1R', f=1 )
        mc.setAttr(jnt_strch_blend + '.color2R', jnt_tx )

        mc.connectAttr( stretch_blend, jnt_strch_blend + '.blender', f=1 )
        mc.connectAttr( jnt_strch_blend + '.outputR', i + '.tx', f=1 )


    


    #______________________________________________________________________________#
    #____________________________IK/ FK Switch Ctrl _______________________________#
    #______________________________________________________________________________#
    switch_ctrl_list = []
    switch_ctrl_grp_list = []
    for items in range(0,1):
        #name circle curves
        switchCurveA_name = name + '_swch_ctrl'
        switchCurveB_name = name + '_swch_ctrlA'
        switchCurveC_name = name + '_swch_ctrlB'

        #create nurbs circle
        switchCurveA = mc.circle(n=switchCurveA_name, ch=False, r=3, nr=(0,1,0))
        #create variable for nurbs circle shape
        switchCurveA_shape = mc.listRelatives(switchCurveA, s=True)
        #color nurbs circle shape
        mc.setAttr((switchCurveA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveA_shape[0] + ".overrideColorRGB"), 0, .5, 1)

        #create 2nd nurbs circle
        switchCurveB = mc.circle(n=switchCurveB_name, ch=False, r=3, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        switchCurveB_shape = mc.listRelatives(switchCurveB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((switchCurveB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveB_shape[0] + ".overrideColorRGB"), 0, .5, 1)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveB_shape, switchCurveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(switchCurveB)

        #create 3rd nurbs circle
        switchCurveC = mc.circle(n=switchCurveC_name, ch=False, r=3, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        switchCurveC_shape = mc.listRelatives(switchCurveC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((switchCurveC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveC_shape[0] + ".overrideColorRGB"), 0, .5, 1)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveC_shape, switchCurveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(switchCurveC)


        #_______group switch ctrl_______#
        switchCurveA_grp = mc.group(switchCurveA, n = (switchCurveA_name + '_grp'))
        switchCurveA_l_grp_offset = mc.group(switchCurveA, n = (switchCurveA_name + '_grp_offset'))

        

        #_______move ctrl shapes in -z_______#
        mc.setAttr((switchCurveA[0] + ".translateY"), -60)
        mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(switchCurveA, apply=True)

        #_______move joint to ankle and parent_______#
        #parent and zero joints to last joint in selection
        mc.parent(switchCurveA_grp, jnt_chain[-1], relative=True)
        #parent joints to world space
        mc.Unparent(switchCurveA_grp)

        # parent and scale constrain switch ctrl to ankle
        mc.parentConstraint(jnt_chain[-1], switchCurveA_grp, mo=True)
        mc.scaleConstraint(jnt_chain[-1], switchCurveA_grp)

        #_______add IK FK Blend attr to switch ctrl_______#
        mc.addAttr(switchCurveA, ln = "fk_ik_blend", min=0, max=1, k=True)

        #lock and hide unneeded attributes for switch ctrl
        mc.setAttr((switchCurveA[0] + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.tz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sy'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sz'), lock=True, keyable=False, channelBox=False)

        

        switch_ctrl_list.append(switchCurveA[0])
        switch_ctrl_grp_list.append(switchCurveA_grp)

        

    
    #_______connect switch control to blendNodes_______#
    for items_trans, items_rot in zip(  blendColorsTran_list, 
                                        blendColorsRot_list):
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)

    
    #_______connect switch control to visibility______#
    for i in range(0,1): 
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
        mc.setAttr((myIKGrp + '.visibility'), 1)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)
        mc.setDrivenKeyframe((myIKGrp + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
        mc.setAttr((myIKGrp + '.visibility'), 0)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)
        mc.setDrivenKeyframe((myIKGrp + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
    


    #_____________ organize _____________#
    # organization group
    organizeGrp = mc.group(em=True, n=name + '_grp')

    mc.parent(fk_ctrl_grp_list[0], organizeGrp)
    mc.parent(switch_ctrl_grp_list[0], organizeGrp)
    mc.parent(ikHndl_crv, organizeGrp)
    mc.parent(ikHndl_var[0], organizeGrp)
    # parent to hip
    mc.parent(myIKGrp, spine_root_ctrl)
    mc.parent(fk_ctrl_grp_list[0], spine_root_ctrl)
    # parent organize grp to global grp
    mc.parent(organizeGrp, global_misc_grp)


    #_____________ visibility _____________#
    #hide ik handle
    mc.setAttr(ikHndl_var[0] + '.visibility', 0)
    mc.setAttr(ikHndl_crv + '.visibility', 0)

    #clear final selection
    mc.select(cl=True)

    # ________ other ________ #
    mc.setAttr(switch_ctrl_list[0] + '.fk_ik_blend', 0) # so ik appears first

    return ikHndl_crv
