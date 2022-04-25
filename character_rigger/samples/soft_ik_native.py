import maya.cmds as mc

def soft_ik_native():
    print ('HWEEO!')

    # create skeleton (test leg) __________

    jointA_nm = mc.joint( p=(0, 85, 0), o=(90, -23, -90), rad=2 )
    jointA = mc.rename(jointA_nm, 'jntA')
    mc.select(cl=True) 
    
    jointB_nm = mc.joint( p=(0, 43.577, 17.583), o=(90, 23, -90), rad=2 )
    jointB = mc.rename(jointB_nm, 'jntB')
    mc.select(cl=True)

    jointC_nm = mc.joint( p=(0, 2.155, 0), o=(90, 23, -90), rad=2 )
    jointC = mc.rename(jointC_nm, 'jntC')
    mc.select(cl=True)

    mc.parent(jointB, jointA)
    mc.parent(jointC, jointB)

    jnt_lst = [jointA, jointB, jointC]
    for i in jnt_lst:
        #show channels
        mc.setAttr(i +  '.rotateOrder', cb=True)

        mc.setAttr(i +  '.rotateAxisX', cb=True)
        mc.setAttr(i +  '.rotateAxisY', cb=True)
        mc.setAttr(i +  '.rotateAxisZ', cb=True)

        mc.setAttr(i +  '.jointOrientX', cb=True)
        mc.setAttr(i +  '.jointOrientY', cb=True)
        mc.setAttr(i +  '.jointOrientZ', cb=True)

        mc.setAttr(i +  '.wireColorR', cb=True)
        mc.setAttr(i +  '.wireColorG', cb=True)
        mc.setAttr(i +  '.wireColorB', cb=True)

        # change color
        mc.setAttr(i + '.useObjectColor', 2)
        mc.setAttr(i + '.wireColorRGB', 1, .5, 0)


    #create drv jnt and ik handle______

    #clear selection
    mc.select(cl=True)

    jointA1_nm = mc.joint( p=(0, 85, 0), o=(90, 0, -90), rad=4 )
    jointA1 = mc.rename(jointA1_nm, 'jntA_drv')
    mc.select(cl=True) 

    jointB1_nm = mc.joint( p=(0, 2.155, 0), o=(90, 0, -90), rad=4 )
    jointB1 = mc.rename(jointB1_nm, 'jntB_drv')
    mc.select(cl=True) 

    mc.parent(jointB1, jointA1)

    jnt_lst1 = [jointA1, jointB1]
    for i in jnt_lst1:
        #show channels
        mc.setAttr(i +  '.rotateOrder', cb=True)

        mc.setAttr(i +  '.rotateAxisX', cb=True)
        mc.setAttr(i +  '.rotateAxisY', cb=True)
        mc.setAttr(i +  '.rotateAxisZ', cb=True)

        mc.setAttr(i +  '.jointOrientX', cb=True)
        mc.setAttr(i +  '.jointOrientY', cb=True)
        mc.setAttr(i +  '.jointOrientZ', cb=True)

        mc.setAttr(i +  '.wireColorR', cb=True)
        mc.setAttr(i +  '.wireColorG', cb=True)
        mc.setAttr(i +  '.wireColorB', cb=True)

        # change color
        mc.setAttr(i + '.useObjectColor', 2)
        mc.setAttr(i + '.wireColorRGB', 0, 0, 1)

    #_________main ik handle, RPS ___________#
    ikHandle_RPS = mc.ikHandle(n='hip_ikHandkle', sj=jointA, ee=jointC)
    # rename effector
    ikHandle_RPS_eff = mc.listConnections(ikHandle_RPS, s=True, type='ikEffector')
    mc.rename(ikHandle_RPS_eff, ikHandle_RPS[0] + '_effector')

    # create grp and offset grp for ik RPS
    #group curve
    ikHan_RPS_grp0 = mc.group(em=1)
    ikHan_RPS_grp_offs0 = mc.group(em=1)
    #rename group
    ikHan_RPS_grp1 = mc.rename(ikHan_RPS_grp0, (ikHandle_RPS[0] + '_grp'))
    ikHan_RPS_grp_offs1 = mc.rename(ikHan_RPS_grp_offs0, (ikHandle_RPS[0] + '_grp_offset'))
    #pos parent grp
    mc.parent(ikHan_RPS_grp_offs1, ikHan_RPS_grp1, r=1)
    mc.parent(ikHan_RPS_grp1, jointB1, r=1)


    #main ik handle, RPS ___________
    ikHandle_SCS = mc.ikHandle(n='drv_ikHandkle', sj=jointA1, ee=jointB1)
    # rename effector
    ikHandle_SCS_eff = mc.listConnections(ikHandle_SCS, s=True, type='ikEffector')
    mc.rename(ikHandle_SCS_eff, ikHandle_SCS[0] + '_effector')

    


    #foot_ctrl _____________
    foot_ctrl = mc.circle(n='foot_ctrl', r=10, nr=(0, 1, 0), ch=0 )
    # shape curve cv
    mc.setAttr((foot_ctrl[0] + '.controlPoints[2]'), -10, 0, -10 )
    mc.setAttr((foot_ctrl[0] + '.controlPoints[4]'), -10, 0, 10 )
    mc.setAttr((foot_ctrl[0] + '.controlPoints[6]'), 10, 0, 10 )
    mc.setAttr((foot_ctrl[0] + '.controlPoints[0]'), 10, 0, -10 )

    # foot ctrl shape
    foot_ctrl_shp = mc.listRelatives(foot_ctrl, s=True)
    #color
    mc.setAttr((foot_ctrl_shp[0] + '.overrideEnabled'), 1)
    mc.setAttr((foot_ctrl_shp[0] + '.overrideRGBColors'), 1)
    mc.setAttr((foot_ctrl_shp[0] + '.overrideColorRGB'), 1, 1, 0)
    # curve thickness
    mc.setAttr((foot_ctrl_shp[0] + '.lineWidth'), 2)
    #group curve
    foot_ctrl_grp0 = mc.group(foot_ctrl)
    foot_ctrl_grp_offs0 = mc.group(foot_ctrl)
    #rename group
    foot_ctrl_grp1 = mc.rename(foot_ctrl_grp0, (foot_ctrl[0] + '_grp'))
    foot_ctrl_grp_offs1 = mc.rename(foot_ctrl_grp_offs0, (foot_ctrl[0] + '_grp_offset'))
    # position foot ctrl
    mc.parent(foot_ctrl_grp1, jointB1, r=True)
    mc.Unparent(foot_ctrl_grp1)
    mc.setAttr(foot_ctrl_grp1 + '.rotate', 0,0,0)

    # _add Stretch_Blend attr_ #
    mc.addAttr(foot_ctrl, ln='Stretch_Blend', nn='Stretch_Blend', min=0, max=1, at='double', dv=0, k=1)
    

    #hip_ctrl
    hip_ctrl = mc.circle(n='hip_ctrl', r=10, nr=(0, 1, 0), ch=0 )
    # hip ctrl shape
    #select curve box's shape
    hip_ctrl_shp = mc.listRelatives(hip_ctrl, s=True)
    #color
    mc.setAttr((hip_ctrl_shp[0] + '.overrideEnabled'), 1)
    mc.setAttr((hip_ctrl_shp[0] + '.overrideRGBColors'), 1)
    mc.setAttr((hip_ctrl_shp[0] + '.overrideColorRGB'), .3, 0, .6)
    # curve thickness
    mc.setAttr((hip_ctrl_shp[0] + '.lineWidth'), 2)
    #group curve
    hip_ctrl_grp0 = mc.group(hip_ctrl)
    hip_ctrl_grp_offs0 = mc.group(hip_ctrl)
    #rename group
    hip_ctrl_grp1 = mc.rename(hip_ctrl_grp0, (hip_ctrl[0] + '_grp'))
    hip_ctrl_grp_offs1 = mc.rename(hip_ctrl_grp_offs0, (hip_ctrl[0] + '_grp_offset'))
    # position hip ctrl
    mc.parent(hip_ctrl_grp1, jointA1, r=True)
    mc.Unparent(hip_ctrl_grp1)
    mc.setAttr(hip_ctrl_grp1 + '.rotate', 0,0,0)

    # global_ctrl
    global_ctrl = mc.circle(n='global_ctrl', r=30, nr=(0, 1, 0), ch=0 )
    # adjust verts
    mc.setAttr((global_ctrl[0] + '.controlPoints[2]'), -10, 0, -10 )
    mc.setAttr((global_ctrl[0] + '.controlPoints[4]'), -10, 0, 10 )
    mc.setAttr((global_ctrl[0] + '.controlPoints[6]'), 10, 0, 10 )
    mc.setAttr((global_ctrl[0] + '.controlPoints[0]'), 10, 0, -10 )
    #select curve box's shape
    global_ctrl_shp = mc.listRelatives(global_ctrl, s=True)
    #color
    mc.setAttr((global_ctrl_shp[0] + '.overrideEnabled'), 1)
    mc.setAttr((global_ctrl_shp[0] + '.overrideRGBColors'), 1)
    mc.setAttr((global_ctrl_shp[0] + '.overrideColorRGB'), .6, 0, .3)
    # curve thickness
    mc.setAttr((global_ctrl_shp[0] + '.lineWidth'), 2)
    #group curve
    global_ctrl_grp0 = mc.group(global_ctrl)
    global_ctrl_grp_offs0 = mc.group(global_ctrl)
    #rename group
    global_ctrl_grp1 = mc.rename(global_ctrl_grp0, (global_ctrl[0] + '_grp'))
    global_ctrl_grp_offs1 = mc.rename(global_ctrl_grp_offs0, (global_ctrl[0] + '_grp_offset'))


    #_________________#

    # create ruler tool
    jnt_ruler0 = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
    jnt_ruler1 = mc.rename(jnt_ruler0, ( 'jnt_rulerShape' ) )
    # rename transform parent of distanceDimesion tool
    ruler_loc_list_rel = mc.listRelatives( jnt_ruler1, ap=1, type='transform' )
    ruler_loc_list_parent = mc.rename(ruler_loc_list_rel, 'jnt_ruler')
    # get locators
    ruler_loc_list = mc.listConnections( jnt_ruler1, type='locator' )
    # rename distance locators
    leg_loc_0 = mc.rename(ruler_loc_list[0], 'hip_dist_loc')
    leg_loc_1 = mc.rename(ruler_loc_list[1], 'ankle_dist_loc')

    # parent and constrain objects_____________
    # parent measure locators under ctrls (ruler loc is ends of distanceMeasure tool)
    mc.parent(leg_loc_0, hip_ctrl, r=1 )
    tmp_cons = mc.parentConstraint(foot_ctrl, leg_loc_1) #to position
    mc.delete(tmp_cons)
    mc.parent(leg_loc_1, foot_ctrl)

    # parent ik handles 
    mc.parent(ikHandle_SCS[0], foot_ctrl)
    #position before parent
    mc.parent(ikHandle_RPS[0], ikHan_RPS_grp_offs1)

    # parent top joints to hip ctrls
    mc.parentConstraint(hip_ctrl, jointA, mo=1)
    mc.parentConstraint(hip_ctrl, jointA1, mo=1)

    #______________ parent everything under global ctrl ____________#
    mc.parent(jointA, global_ctrl)
    mc.parent(jointA1, global_ctrl)
    mc.parent(foot_ctrl_grp1, global_ctrl)
    mc.parent(hip_ctrl_grp1, global_ctrl)



    #_______________________________#
    #_________node graph____________#
    #_______________________________#
    prefix = 'leg'

    #______Function Variables_______#
    #variable ... ruler distance output
    ruler_dist = jnt_ruler1 + '.distance'
    ruler_dist_result = mc.getAttr(jnt_ruler1 + '.distance')

    #variable ... global_ctrl scale X
    global_ctrl_sclX = global_ctrl[0] + '.scaleX'

    #variable
    stretch_blend = foot_ctrl[0] + '.Stretch_Blend'

    #joints
    shoulderHip_jnt = ''
    kneeElbow_jnt = ''
    kneeElbow_jnt_len = mc.getAttr(jointB + '.tx')
    ankleWrist_jnt = ''
    ankleWrist_jnt_len = mc.getAttr(jointC + '.tx')

    

    drvJnt_start = ''
    drvJnt_end = ''

    # _______________create nodes____________________#
    # part1 ... ikHandle grp nodes
    stretch_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=1, n = prefix + '_stretch_dist_ratio' ) # create multDiv node
    mc.setAttr(stretch_dist_ratio + '.operation', 2) # set to Divide

    global_scale_offs = mc.shadingNode('multiplyDivide', asUtility=1, n = prefix + '_global_scale_offs' ) # default is multiply

    ikHndl_fllw_pma = mc.shadingNode('plusMinusAverage', asUtility=1, n = prefix + '_ikHandle_follow_pma' ) # for ik handle to follow hip ctrl
    mc.setAttr(ikHndl_fllw_pma + '.operation', 2) # set to Subtract

    glbl_offs_ikHndl_fllw = mc.shadingNode('multiplyDivide', asUtility=1, n = prefix + '_global_scale_offs_ikHndl_follow' ) # global scale offset for ikHandle follow grp
    mc.setAttr(glbl_offs_ikHndl_fllw + '.operation', 2) # set to Divide

    clamp_end_stop = mc.shadingNode('clamp', asUtility=1, n = prefix + '_clamp_end_stop' ) # limit ikHndl follow grp from going past ankle/ wrist

    invert_node = mc.shadingNode('multiplyDivide', asUtility=1, n = prefix + '_invert_node' ) # invert value to negative, or positive, if already neg

    softIk_fllw_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = prefix + '_softIk_fllw_grp_blend' ) # blend between 0 or follow

    softIk_fllw_offs_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = prefix + '_softIk_fllw_offs_grp_blend' ) # smooth ikHndl grp follow


    # part2 ... joint nodes

    drvJnt_strch_ratio = mc.shadingNode( 'multiplyDivide', asUtility=1, n = prefix + '_drvJnt_strch_ratio' )

    ikHdl_grp_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = prefix + '_ikHdl_grp_smooth_setDrvKey' )


    # knee/ elbow joints nodes

    kneeElbow_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = prefix + '_kneeElbow_strch' )

    kneeElbow_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = prefix + '_kneeElbow_smooth_setDrvKey' )
    mc.setAttr(kneeElbow_smooth_setDrvKey + '.preInfinity', 1)

    kneeElbow_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = prefix + '_kneeElbow_smooth_offs' )

    kneeElbow_stretch_clamp = mc.shadingNode('clamp', asUtility=1, n = prefix + '_kneeElbow_stretch_clamp' )

    kneeElbow_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = prefix + '_kneeElbow_stretch_blend' )


    # ankle / wrist jnt nodes

    ankleWrist_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = prefix + '_ankleWrist_strch' )

    ankleWrist_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = prefix + '_ankleWrist_smooth_setDrvKey' )
    mc.setAttr(ankleWrist_smooth_setDrvKey + '.preInfinity', 1)

    ankleWrist_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = prefix + '_ankleWrist_smooth_offs' )

    ankleWrist_stretch_clamp = mc.shadingNode('clamp', asUtility=1, n = prefix + '_ankleWrist_stretch_clamp' )

    ankleWrist_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = prefix + '_ankleWrist_stretch_blend' )


    # _______________connect nodes/ set attributes____________________#
    # part1 ... ikHandle grp connections

    mc.connectAttr( global_ctrl_sclX, global_scale_offs + '.input2X', f=1 ) # create global scale offset node
    mc.setAttr(global_scale_offs + '.input1X', ruler_dist_result) #set to ruler distance

    mc.connectAttr( global_scale_offs + '.outputX', ikHndl_fllw_pma + '.input1D[0]', f=1 ) # global scale offset to 1D[0]
    mc.connectAttr( ruler_dist, ikHndl_fllw_pma + '.input1D[1]', f=1 ) # ruler distance to ikHndl follow 1D[1]

    mc.connectAttr( ikHndl_fllw_pma + '.output1D', glbl_offs_ikHndl_fllw + '.input1X', f=1 ) # ikHandle follow to input 1x  # scale offset for ikHandle grp follow distance
    mc.connectAttr( global_ctrl_sclX, glbl_offs_ikHndl_fllw + '.input2X', f=1 ) # global scale x to input 2x

    mc.connectAttr( glbl_offs_ikHndl_fllw + '.outputX', clamp_end_stop + '.inputR', f=1 ) # follow distance w/ scl offset, to 0 clamp
    mc.setAttr(clamp_end_stop + '.minR', -1000) #set to ruler distance

    mc.connectAttr( clamp_end_stop + '.outputR', invert_node + '.input1X', f=1 ) # make value positive, to go correct X direction
    mc.setAttr(invert_node + '.input2X', -1) # -1 to multiply and get posative value, since already negative

    mc.connectAttr( invert_node + '.outputX', ikHdl_grp_smooth_setDrvKey + '.input', f=1 )

    mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=0, value=0, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change
    mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=12, value=4.3)
    mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=63, value=7.1)

    mc.connectAttr( clamp_end_stop + '.outputR', softIk_fllw_grp_blend + '.color2R', f=1 )  # sets follow grp to follow constant distance from hip ctrl
    mc.setAttr(softIk_fllw_grp_blend + '.color1R', 0) # set ikHndl grp follow to 0, to stay at ankle/ wrist
    mc.connectAttr( stretch_blend, softIk_fllw_grp_blend + '.blender', f=1 )

    mc.connectAttr( ikHdl_grp_smooth_setDrvKey + '.output', softIk_fllw_offs_grp_blend + '.color2R', f=1 )  # sets follow offset grp to smoothly adjust follow distance for softIK
    mc.setAttr(softIk_fllw_offs_grp_blend + '.color1R', 0) # set ikHndl offset grp follow to 0, to have no effect
    mc.connectAttr( stretch_blend, softIk_fllw_offs_grp_blend + '.blender', f=1 )

    mc.connectAttr( softIk_fllw_offs_grp_blend + '.outputR', ikHan_RPS_grp_offs1 + '.tx', f=1 ) # connect to ikHandle Grp
    mc.connectAttr( softIk_fllw_grp_blend + '.outputR', ikHan_RPS_grp1 + '.tx', f=1 ) # connect to ikHandle Grp offset

    

    # part2 ... joint connections

    mc.connectAttr( ruler_dist, stretch_dist_ratio + '.input1X', f=1 ) # create stretch ratio
    mc.connectAttr( global_scale_offs + '.outputX', stretch_dist_ratio + '.input2X', f=1 ) # create stretch ratio

    mc.connectAttr( stretch_dist_ratio + '.outputX', drvJnt_strch_ratio + '.input1X', f=1 ) # create drv jnt stretch ratio
    mc.setAttr(drvJnt_strch_ratio + '.input2X', ruler_dist_result) #set drv jnt stretch ratio 2X to static ruler distance default
    mc.connectAttr( drvJnt_strch_ratio + '.outputX', jointB1 + '.translateX', f=1 ) # create drv jnt stretch ratio



    # knee / elbow jnt connections _______________________________
    mc.connectAttr( stretch_dist_ratio + '.outputX', kneeElbow_strch + '.input1X', f=1 ) # kneeElbow stretch amount, base length multiplied by stretch ratio
    mc.setAttr(kneeElbow_strch + '.input2X', kneeElbow_jnt_len)
    
    mc.connectAttr( stretch_dist_ratio + '.outputX', kneeElbow_smooth_setDrvKey + '.input', f=1 ) # smooth offset keys
    
    mc.setKeyframe(kneeElbow_smooth_setDrvKey, float=0.4, value=2.4956, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change
    mc.setKeyframe(kneeElbow_smooth_setDrvKey, float=1, value=1)
    mc.setKeyframe(kneeElbow_smooth_setDrvKey, float=1.761, value=0.921)
    # mc.cutKey('animCurveUU_test', float=(6, 6) ) # how to delete key
    

    mc.connectAttr( kneeElbow_strch + '.outputX', kneeElbow_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
    mc.connectAttr( kneeElbow_smooth_setDrvKey + '.output', kneeElbow_smooth_offs + '.input2X', f=1 )

    mc.connectAttr( kneeElbow_smooth_offs + '.outputX', kneeElbow_stretch_clamp + '.inputR', f=1 ) # connect jnt length to have bottom value clamped during stretch
    mc.setAttr(kneeElbow_stretch_clamp + '.minR', ( kneeElbow_jnt_len * 0.80) ) #clamp smallest length value  #0.83, exact from test  
    mc.setAttr(kneeElbow_stretch_clamp + '.maxR', 1000) # just to have a high that will not be reached

    mc.connectAttr( kneeElbow_stretch_clamp + '.outputR', kneeElbow_stretch_blend + '.color1R', f=1 ) # blend between stretch and no stretch default static length
    mc.setAttr(kneeElbow_stretch_blend + '.color2R', kneeElbow_jnt_len )  # set to default jnt length, static value

    mc.connectAttr( kneeElbow_stretch_blend + '.outputR', jointB + '.translateX', f=1 ) # connect blend to jnt translate X length

    mc.connectAttr( stretch_blend, kneeElbow_stretch_blend + '.blender', f=1 )  # foot ctrl stretch blend attr


    # ankle / wrist jnt _______________________________
    mc.connectAttr( stretch_dist_ratio + '.outputX', ankleWrist_strch + '.input1X', f=1 )
    mc.setAttr(ankleWrist_strch + '.input2X', ankleWrist_jnt_len)
    
    mc.connectAttr( stretch_dist_ratio + '.outputX', ankleWrist_smooth_setDrvKey + '.input', f=1 ) # smooth offset keys
    
    mc.setKeyframe(ankleWrist_smooth_setDrvKey, float=0.4, value=2.4956, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change
    mc.setKeyframe(ankleWrist_smooth_setDrvKey, float=1, value=1)
    mc.setKeyframe(ankleWrist_smooth_setDrvKey, float=1.761, value=0.921)
    # mc.cutKey('animCurveUU_test', float=(6, 6) ) # how to delete key
    

    mc.connectAttr( ankleWrist_strch + '.outputX', ankleWrist_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
    mc.connectAttr( ankleWrist_smooth_setDrvKey + '.output', ankleWrist_smooth_offs + '.input2X', f=1 )

    mc.connectAttr( ankleWrist_smooth_offs + '.outputX', ankleWrist_stretch_clamp + '.inputR', f=1 ) # connect jnt length to have bottom value clamped during stretch
    mc.setAttr(ankleWrist_stretch_clamp + '.minR', ( ankleWrist_jnt_len * 0.80) ) #clamp smallest length value  #0.83, exact from test  
    mc.setAttr(ankleWrist_stretch_clamp + '.maxR', 1000) # just to have a high that will not be reached

    mc.connectAttr( ankleWrist_stretch_clamp + '.outputR', ankleWrist_stretch_blend + '.color1R', f=1 ) # blend between stretch and no stretch default static length
    mc.setAttr(ankleWrist_stretch_blend + '.color2R', ankleWrist_jnt_len )  # set to default jnt length, static value

    mc.connectAttr( ankleWrist_stretch_blend + '.outputR', jointC + '.translateX', f=1 ) # connect blend to jnt translate X length

    mc.connectAttr( stretch_blend, ankleWrist_stretch_blend + '.blender', f=1 )  # foot ctrl stretch blend attr


    













'''
## import _____ ## use in maya script editor to execute script

import maya.cmds as mc

import imp

import character_rigger.samples.soft_ik_native

imp.reload( character_rigger.samples.soft_ik_native)

character_rigger.samples.soft_ik_native.soft_ik_native()

'''