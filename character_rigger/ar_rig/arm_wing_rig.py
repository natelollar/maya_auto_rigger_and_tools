import maya.cmds as mc

import maya.mel as mel

try:
    from itertools import izip as zip
except: # will be python 3.x series
    pass

from ..ar_functions import sel_near_jnt



# create arm rig ('global_ctrl' for scale offset)
def arm_wing_rig(   direction = 'r',
                    offset_parent_jnt = 'chest_offset_parent_jnt_TEST',
                    swch_ctrl_size = 3,
                    swch_ctrl_dist = 35,
                    fk_ctrl_size = 10,
                    ik_ctrl_size = 10,
                    pv_ctrl_size = 20,
                    chest_ctrl = 'chest_ctrl_TEST',
                    global_ctrl = 'global_ctrl_TEST',
                    global_misc_grp = 'character_misc_grp_TEST' ):


    #_______ initial joints ________#
    defaultJnt_prefix = 'sknJnt_'
    
    chestRoot_jnt = sel_near_jnt.sel_near_jnt('standin_obj_chest_root')
    clavicle_jnt = sel_near_jnt.sel_near_jnt('standin_obj_' + direction + ' _clavicle')
    shoulder_jnt = sel_near_jnt.sel_near_jnt('standin_obj_' + direction + '_arm_start')
    elbow_jnt = sel_near_jnt.sel_near_jnt('standin_obj_' + direction + '_elbow')
    elbow_poleVector_pos = 'standin_obj_' + direction + '_elbow_pv'
    #autoClav_poleVector_pos = 'standin_obj_l_autoClav_pv'
    wrist_jnt = sel_near_jnt.sel_near_jnt('standin_obj_' + direction + '_arm_end')

    chestRoot_ctrl_nm0 = chestRoot_jnt[0].replace(defaultJnt_prefix, '')
    chestRoot_ctrl_nm1 = chestRoot_ctrl_nm0 + '_ctrl'

    # select joint chain
    arm_chain = [clavicle_jnt[0], shoulder_jnt[0], elbow_jnt[0], wrist_jnt[0] ]

    #_________________________________#
    name = 'arm'
    
    #group for organization
    myArmGrp = mc.group(em=True, n= direction + '_arm_grp')

    
    #______________________________#
    #_____Blended Joint Chains______#
    #______________________________#

    fkJoint_list = []
    ikJoint_list = []
    for i in arm_chain:
        #______________________#
        #____create FK chain___#
        fkJoint_orig = mc.joint(i)

        #joint visual size
        mc.setAttr('.radius', 4)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', 1, 0, 0.1)

        fkJoint_rename = i.replace(defaultJnt_prefix, 'fkJnt_')
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

        ikJoint_rename = i.replace(defaultJnt_prefix, 'ikJnt_')
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
    for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, arm_chain):
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
    # parent ik fk clavicle joints to chest offset jnt  # otherwise blend color node position is off
    #__________________________________________________________________#
    mc.parent(fkJoint_list[0], offset_parent_jnt)

    mc.parent(ikJoint_list[0], offset_parent_jnt)


    
    #_______________Stretch Length Joints___________________#
    #_______________________________________________________#
    arm_chain_strchJnts = [ arm_chain[1], arm_chain[3] ]
    strchJnt_lst = []
    for i in arm_chain_strchJnts:
        #______________________#
        #____create FK chain___#
        strchJoint_orig = mc.joint(i)

        #joint visual size
        mc.setAttr('.radius', 11)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', 1, .8, 0)
        #show attr
        mc.setAttr('.rotateOrder', cb=True)
        mc.setAttr('.rotateAxisX', cb=True)
        mc.setAttr('.rotateAxisY', cb=True)
        mc.setAttr('.rotateAxisZ', cb=True)
        mc.setAttr('.jointOrientX', cb=True)
        mc.setAttr('.jointOrientY', cb=True)
        mc.setAttr('.jointOrientZ', cb=True)

        #rename jnt
        strchJoint_rename = i.replace(defaultJnt_prefix, 'strchJnt_')
        strchJoint = mc.rename(strchJoint_orig, strchJoint_rename)
        mc.Unparent(strchJoint)

        # create list of fk joints
        strchJnt_lst.append(strchJoint)


    # parent stretch joint together
    mc.parent(strchJnt_lst[1], strchJnt_lst[0])
    #orient joints
    mc.joint(strchJnt_lst[0], e=True, oj='xyz', secondaryAxisOrient='yup')
    mc.setAttr(strchJnt_lst[1] +  '.jointOrient', 0, 0, 0)


    # parent stretch jnt to spine1 offset jnt
    mc.parent(strchJnt_lst[0], offset_parent_jnt)

    #point constrain strch joint to ik joint
    mc.pointConstraint(ikJoint_list[1], strchJnt_lst[0], mo=True)

    #_______________Auto Clav Joints___________________#
    #_______________________________________________________#
    autoClav_jnt_pos = [ arm_chain[0], arm_chain[3] ]
    autoClav_jnt_lst = []
    for i in autoClav_jnt_pos:
        #______________________#
        #____create FK chain___#
        autoClav_orig = mc.joint(i)

        #joint visual size
        mc.setAttr('.radius', 12)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', 1, 0, .8)
        #show attr
        mc.setAttr('.rotateOrder', cb=True)
        mc.setAttr('.rotateAxisX', cb=True)
        mc.setAttr('.rotateAxisY', cb=True)
        mc.setAttr('.rotateAxisZ', cb=True)
        mc.setAttr('.jointOrientX', cb=True)
        mc.setAttr('.jointOrientY', cb=True)
        mc.setAttr('.jointOrientZ', cb=True)

        #rename jnt
        autoClav_jnt_rename = i.replace(defaultJnt_prefix, 'autoClav_jnt_')
        autoClav_jnt = mc.rename(autoClav_orig, autoClav_jnt_rename)
        mc.Unparent(autoClav_jnt)

        # create list of fk joints
        autoClav_jnt_lst.append(autoClav_jnt)


    # parent stretch joint together
    mc.parent(autoClav_jnt_lst[1], autoClav_jnt_lst[0])
    #orient joints
    mc.joint(autoClav_jnt_lst[0], e=True, oj='xyz', secondaryAxisOrient='yup')
    mc.setAttr(autoClav_jnt_lst[1] +  '.jointOrient', 0, 0, 0)


    # parent stretch jnt to spine1 offset jnt
    mc.parent(autoClav_jnt_lst[0], offset_parent_jnt)


    #_______________reg Clav Joints___________________#
    #_______________________________________________________#
    regClav_jnt_pos = [ arm_chain[0], arm_chain[1] ]
    regClav_jnt_lst = []
    for i in regClav_jnt_pos:
        #______________________#
        #____create FK chain___#
        regClav_orig = mc.joint(i)

        #joint visual size
        mc.setAttr('.radius', 17)
        #joint color
        mc.setAttr('.useObjectColor', 2)
        mc.setAttr('.wireColorRGB', 0, 1, 1)
        #show attr
        mc.setAttr('.rotateOrder', cb=True)
        mc.setAttr('.rotateAxisX', cb=True)
        mc.setAttr('.rotateAxisY', cb=True)
        mc.setAttr('.rotateAxisZ', cb=True)
        mc.setAttr('.jointOrientX', cb=True)
        mc.setAttr('.jointOrientY', cb=True)
        mc.setAttr('.jointOrientZ', cb=True)

        #rename jnt
        regClav_jnt_rename = i.replace(defaultJnt_prefix, 'regClav_jnt_')
        regClav_jnt = mc.rename(regClav_orig, regClav_jnt_rename)
        mc.Unparent(regClav_jnt)

        # create list of fk joints
        regClav_jnt_lst.append(regClav_jnt)

    # parent stretch joint together
    mc.parent(regClav_jnt_lst[1], regClav_jnt_lst[0])
    #mc.setAttr(regClav_jnt_lst[1] +  '.jointOrient', 0, 0, 0)

    # parent stretch jnt to spine1 offset jnt
    mc.parent(regClav_jnt_lst[0], offset_parent_jnt)
    


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

    
    #_____________________________________#
    #______________IK Ctrls_______________#
    #_____________________________________#

    #___________create IK HANDLE, for softIK, stretch joint top to bottom, Single Chain Solver____________#

    #main ik handle, SCS ___________
    ikHndl_strch = mc.ikHandle( n=direction + '_' + name + '_strchJnt_ikHndl', 
                                sj=strchJnt_lst[0], 
                                ee=strchJnt_lst[1], 
                                sol='ikSCsolver')
    # rename effector
    ikHndl_strch_eff = mc.listConnections(ikHndl_strch, s=True, type='ikEffector')
    mc.rename(ikHndl_strch_eff, ikHndl_strch[0] + '_effector')


    #___________create IK HANDLE, for autoClav joint top to bottom, Rotate Plane Solver____________#

    #main ik handle, RPS ___________
    ikHndl_autoClav = mc.ikHandle( n=direction + '_' + name + '_autoClav_jnt_ikHndl', 
                                sj=autoClav_jnt_lst[0], 
                                ee=autoClav_jnt_lst[1],
                                sol='ikSCsolver' )  # CHANGED TO SINGLE CHAIN SOLVER, WHY RPS NEEDED?
    # rename effector
    ikHndl_autoClav_eff = mc.listConnections(ikHndl_strch, s=True, type='ikEffector')
    mc.rename(ikHndl_autoClav_eff, ikHndl_autoClav[0] + '_effector')

    

    #___________create IK HANDLE, shoulder to wrist, Rotate Plane Solver____________#

    ikHndlWrist = mc.ikHandle(  n=direction + '_' + name + '_ikHndl', 
                                sj=ikJoint_list[1], 
                                ee=ikJoint_list[3])

    ikHandle_effector_var = mc.listConnections(ikHndlWrist, s=True, type='ikEffector')

    mc.rename(ikHandle_effector_var, ikHndlWrist[0] + '_effector')


    #___________create IK HANDLE, Clavicle to Shoulder, Single Chain Solver______________#

    #create single chain ikHandle for shoudler________
    shoulder_ikHandle = mc.ikHandle(n=direction + '_' + name + '_ikHndl_shldr',
                                    sj=regClav_jnt_lst[0], 
                                    ee=regClav_jnt_lst[1], 
                                    sol='ikSCsolver')
    
    #rename ik effector
    shoulder_ikHandle_effector = mc.listConnections(shoulder_ikHandle, s=True, type='ikEffector')
    mc.rename(shoulder_ikHandle_effector, shoulder_ikHandle[0] + '_effector')
    #group ik handle
    shldrGrp = mc.group(em=True)
    shldrGrp = mc.rename(shldrGrp, shoulder_ikHandle[0] + '_grp')
    shldrGrp_const = mc.parentConstraint(shoulder_ikHandle[0], shldrGrp)
    mc.delete(shldrGrp_const)
    mc.parent(shoulder_ikHandle[0], shldrGrp)
    

    #___________ikHandle wrist CTRL____________#
    ik_wristGrp_lst = []
    ik_wristCtrl_lst = []
    #create curve box
    for i in range(0,1):
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
        #curve size # *.9 to make smaller than FK ctrls
        mc.setAttr((myCurve + '.scale'), ik_ctrl_size * .9, ik_ctrl_size * .9, ik_ctrl_size * .9)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.1, 1, 0)

        #rename curve
        myCurve = mc.rename(direction + '_ikWrist_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))

        #parent and zero curveGrp to joints
        mc.parent(myGroup, ikJoint_list[3], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        #parent grp to global grp to organize
        mc.parent(myGroup, global_ctrl)

        #append grp for outside use
        ik_wristGrp_lst.append(myGroup)
        ik_wristCtrl_lst.append(myCurve)

        # add Soft Ik/ No Ik stretch ctrl
        mc.addAttr(myCurve, ln='Stretch_Blend', nn='Stretch_Blend', min=0, max=1, at='double', dv=1, k=1)

    mc.orientConstraint(ik_wristCtrl_lst[0], ikJoint_list[3])
    #so that l is oriented same as right
    #mc.setAttr((ik_wristGrp_lst[0] + '.rotate'), 0, -90, 0)


    #___________ik shoulder CTRL____________#
    ik_shldrGrp_lst = []
    ik_shldrCtrl_lst = []
    #create curve box
    for i in range(0,1):
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
        mc.setAttr((myCurve + '.scale'), ik_ctrl_size * .9, ik_ctrl_size * .9, ik_ctrl_size * .9)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.1, 1, 0)

        #rename curve
        myCurve = mc.rename(direction + '_ikShldr_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp') )
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(myGroup, ikJoint_list[1], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)


        #append grp for outside use
        ik_shldrGrp_lst.append(myGroup)
        ik_shldrCtrl_lst.append(myCurve)

    
    #set ctrl grp rotate to be world space flat
    mc.setAttr( (ik_shldrGrp_lst[0] + '.rotate'), 0, 0, 0)

    # constrain shoulder ctrl to shoulder jnt (translation only)
    #mc.pointConstraint(ik_shldrCtrl_lst[0], ikJoint_list[0])
    #mc.pointConstraint(ik_shldrCtrl_lst[0], autoShldr_jnt_lst[0])

    # lock and hide rotation values for hip control
    mc.setAttr( (ik_shldrCtrl_lst[0] + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr( (ik_shldrCtrl_lst[0] + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr( (ik_shldrCtrl_lst[0] + '.rz'), lock=True, keyable=False, channelBox=False)



    #___________ik clav CTRL____________#
    ik_clavGrp_lst = []
    ik_clavCtrl_lst = []
    #create curve box
    for i in range(0,1):
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
        mc.setAttr((myCurve + '.scale'), ik_ctrl_size * .9, ik_ctrl_size * .9, ik_ctrl_size * .9)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.1, 1, 0)

        #rename curve
        myCurve = mc.rename(direction + '_ikClav_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp') )
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(myGroup, ikJoint_list[0], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)


        #append grp for outside use
        ik_clavGrp_lst.append(myGroup)
        ik_clavCtrl_lst.append(myCurve)

    
    #set ctrl grp rotate to be world space flat
    mc.setAttr( (ik_clavGrp_lst[0] + '.rotate'), 0, 0, 0)

    # constrain clav ctrl to clav jnt (translation only)
    mc.pointConstraint(ik_clavCtrl_lst[0], ikJoint_list[0])
    mc.pointConstraint(ik_clavCtrl_lst[0], autoClav_jnt_lst[0])
    mc.pointConstraint(ik_clavCtrl_lst[0], regClav_jnt_lst[0]) # for clav blend

    # lock and hide rotation values for hip control
    mc.setAttr( (ik_clavCtrl_lst[0] + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr( (ik_clavCtrl_lst[0] + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr( (ik_clavCtrl_lst[0] + '.rz'), lock=True, keyable=False, channelBox=False)


    
    #_________________POLE VECTOR ELBOW___________________#
    #_____________________________________________________#
    pvGrp_lst = []
    pvCtrl_lst = []
    for i in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0, 5, -5),
                                    (-5, 0, -5),
                                    (0, -5, -5),
                                    (5, 0, -5),
                                    (0, 5, -5),
                                    (0, 0, 5),
                                    (5, 0, -5),
                                    (0, -5, -5),
                                    (0, 0, 5),
                                    (-5, 0, -5),
                                    ])
        #curve size
        mc.setAttr((myCurve + '.scale'), 0.1 * pv_ctrl_size, 0.1 * pv_ctrl_size, 0.1 * pv_ctrl_size)

        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((curveShape[0] + '.overrideColorRGB'), 1, 1, 0)
        #rename curve
        myCurve = mc.rename(direction + '_elbow_PV_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))


        #final polve vector point (to avoid elbow changing position on creation)
        mc.parent( myGroup, elbow_poleVector_pos, r=1 )
        mc.Unparent( myGroup )


        
        #___connect pole vector
        mc.poleVectorConstraint(myCurve, ikHndlWrist[0])

        #parent grp to global grp to organize
        mc.parent(myGroup, global_ctrl)

        pvGrp_lst .append(myGroup)
        pvCtrl_lst .append(myCurve)



    #_________________POLE VECTOR autoClav___________________#
    #________________________________________________________#
    autoClav_pvGrp_lst = []
    autoClav_pvCtrl_lst = []
    for i in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0.0, 0.0, 5.0),
                                    (0.0, 0.0, -5.0),
                                    (0.0, 0.0, 0.0),
                                    (-5.0, 0.0, 0.0),
                                    (5.0, 0.0, 0.0),
                                    (0.0, 0.0, 0.0),
                                    (0.0, 5.0, 0.0),
                                    (0.0, 0.0, 0.0),
                                    (0.0, -5.0, 0.0) 
                                    ] )
        #curve size
        mc.setAttr((myCurve + '.scale'), 0.1 * pv_ctrl_size, 0.1 * pv_ctrl_size, 0.1 * pv_ctrl_size)

        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((curveShape[0] + '.overrideColorRGB'), 1, 0, 1)
        #rename curve
        myCurve = mc.rename(direction + '_autoClav_PV_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))


        #parent pv to autoClav end joint, then unparent for just position
        mc.parent( myGroup, ikHndl_autoClav[1], r=1 )
        mc.Unparent( myGroup )

        mc.setAttr(myGroup_offset + '.ty', -100)

        # freeze offset grp transform ?
        #mc.makeIdentity(myGroup_offset, apply=True)

        #___connect pole vector
        #mc.poleVectorConstraint(myCurve, ikHndl_autoClav[0]) #changed to single chain solver

        
        #parent grp to global grp to organize
        mc.parent(myGroup, global_ctrl)

        autoClav_pvGrp_lst.append(myGroup)
        autoClav_pvCtrl_lst.append(myCurve)
        

    # point constrain ik wrist control to autoClav pole vector ctrl
    mc.pointConstraint(ik_wristCtrl_lst[0], autoClav_pvGrp_lst[0], mo=True)
    
    # point constrain wrist control to autoClav ik handle
    mc.pointConstraint(ik_wristCtrl_lst[0], ikHndl_autoClav[0], mo=True)

    

    

    
    #______________________________________________________________________________#
    #____________________________IK/ FK Switch Ctrl _______________________________#
    #______________________________________________________________________________#

    switch_ctrl_list = []
    switch_ctrl_grp_list = []
    for i in range(0,1):
        #name circle curves
        if direction == 'l':
            switchCurveA_name = 'l_armSwtch_ctrl'
            switchCurveB_name = 'l_armSwtch_ctrlA'
            switchCurveC_name = 'l_armSwtch_ctrlB'
        if direction == 'r':
            switchCurveA_name = 'r_armSwtch_ctrl'
            switchCurveB_name = 'r_armSwtch_ctrlA'
            switchCurveC_name = 'r_armSwtch_ctrlB'

        #create nurbs circle
        switchCurveA = mc.circle(n=switchCurveA_name, ch=False, r=swch_ctrl_size, nr=(0,1,0))
        #create variable for nurbs circle shape
        switchCurveA_shape = mc.listRelatives(switchCurveA, s=True)
        #color nurbs circle shape
        mc.setAttr((switchCurveA_shape[0] + '.overrideEnabled'), 1)
        mc.setAttr((switchCurveA_shape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((switchCurveA_shape[0] + '.overrideColorRGB'), 0, .5, 1)

        #create 2nd nurbs circle
        switchCurveB = mc.circle(n=switchCurveB_name, ch=False, r=swch_ctrl_size, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        switchCurveB_shape = mc.listRelatives(switchCurveB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((switchCurveB_shape[0] + '.overrideEnabled'), 1)
        mc.setAttr((switchCurveB_shape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((switchCurveB_shape[0] + '.overrideColorRGB'), 0, .5, 1)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveB_shape, switchCurveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(switchCurveB)

        #create 3rd nurbs circle
        switchCurveC = mc.circle(n=switchCurveC_name, ch=False, r=swch_ctrl_size, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        switchCurveC_shape = mc.listRelatives(switchCurveC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((switchCurveC_shape[0] + '.overrideEnabled'), 1)
        mc.setAttr((switchCurveC_shape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((switchCurveC_shape[0] + '.overrideColorRGB'), 0, .5, 1)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveC_shape, switchCurveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(switchCurveC)

        #_______group switch ctrl_______#
        switchCurveA_grp = mc.group(switchCurveA, n = (switchCurveA_name + '_grp'))
        switchCurveA_l_grp_offset = mc.group(switchCurveA, n = (switchCurveA_name + '_grp_offset'))

        #_______move ctrl shapes in -z_______#
        if direction == 'l':
            mc.setAttr((switchCurveA[0] + '.ty'), (2 * swch_ctrl_dist))
        elif direction == 'r':
            mc.setAttr((switchCurveA[0] + '.ty'), -(2 * swch_ctrl_dist))

        #mc.setAttr((switchCurveA[0] + '.ty'), (2 * swch_ctrl_dist))

        mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(switchCurveA, apply=True)


        
        #_______move joint to wrist and parent_______#
        #parent and zero joints to last joint in selection
        mc.parent(switchCurveA_grp, arm_chain[3], relative=True)
        #parent joints to world space
        mc.Unparent(switchCurveA_grp)

        # parent and scale constrain switch ctrl to wrist
        mc.parentConstraint(arm_chain[3], switchCurveA_grp, mo=True)
        mc.scaleConstraint(arm_chain[3], switchCurveA_grp)

        #_______add IK FK Blend attr to switch ctrl_______#
        mc.addAttr(switchCurveA, ln = 'fk_ik_blend', min=0, max=1, k=True)

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
    for items_trans, items_rot in zip( blendColorsTran_list, blendColorsRot_list ):
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)


    #_______connect switch control to visibility______#
    for i in range(0,1):
        # 1 is fk, 0 is ik, (for loop to avoid clashing variables)
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)  #--
        mc.setAttr((ik_wristGrp_lst[0] + '.visibility'), 1)
        mc.setAttr((pvGrp_lst[0] + '.visibility'), 1)
        mc.setAttr((ik_clavGrp_lst[0] + '.visibility'), 1)
        mc.setAttr((ik_shldrGrp_lst[0] + '.visibility'), 1)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)


        mc.setDrivenKeyframe((ik_wristGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pvGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((ik_clavGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((ik_shldrGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)  #--
        mc.setAttr((ik_wristGrp_lst[0] + '.visibility'), 0)
        mc.setAttr((pvGrp_lst[0] + '.visibility'), 0)
        mc.setAttr((ik_clavGrp_lst[0] + '.visibility'), 0)
        mc.setAttr((ik_shldrGrp_lst[0] + '.visibility'), 0)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)


        mc.setDrivenKeyframe((ik_wristGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pvGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((ik_clavGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((ik_shldrGrp_lst[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


        
#________________________________________________________________________________#
#________________________END of FK/IK BLEND______________________________________#

    #________________________________#
    # stretch jnt ik handle parenting

    ikHndl_strch_grp0 = mc.group(em=1)
    ikHndl_strch_grp_offs0 = mc.group(em=1)
    #rename group
    ikHndl_strch_grp1 = mc.rename(ikHndl_strch_grp0, (ikHndl_strch[0] + '_grp'))
    ikHndl_strch_grp_offs1 = mc.rename(ikHndl_strch_grp_offs0, (ikHndl_strch[0] + '_grp_offset'))

    #pos parent grp
    mc.parent(ikHndl_strch_grp_offs1, ikHndl_strch_grp1)
    mc.parent(ikHndl_strch_grp1, ik_wristCtrl_lst[0], r=1) # to position
    mc.parent(ikHndl_strch_grp1, myArmGrp) # final spot
    mc.parent(ikHndl_strch[0], ikHndl_strch_grp_offs1)
    # parent constrain translation only
    mc.parentConstraint( ik_wristCtrl_lst[0], ikHndl_strch_grp1, mo=True , sr=('x','y','z') )

    

    #_______ create stretch offset grp _______#   
    ikHndl_wrist_grp0 = mc.group(em=1)
    ikHndl_wrist_grp_offs0 = mc.group(em=1)
    #rename group
    ikHndl_wrist_grp1 = mc.rename(ikHndl_wrist_grp0, (ikHndlWrist[0] + '_grp'))
    ikHndl_wrist_grp_offs1 = mc.rename(ikHndl_wrist_grp_offs0, (ikHndlWrist[0] + '_grp_offset'))

    #pos parent grp
    mc.parent(ikHndl_wrist_grp_offs1, ikHndl_wrist_grp1)
    mc.parent(ikHndl_wrist_grp1, strchJnt_lst[1], r=1) # to position
    #mc.parent(ikHndl_wrist_grp1, myArmGrp) # final spot
    mc.parent(ikHndlWrist[0], ikHndl_wrist_grp_offs1)



    
    
    # ______________________________________________________#
    # __________________ IK stretchy Arm ___________________#
    # ______________________________________________________#

    # get joint x lengths
    to_elbow_len = mc.getAttr(ikJoint_list[2] + '.tx')
    to_wrist_len = mc.getAttr(ikJoint_list[3] + '.tx')
    # create ruler tool
    ik_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
    ik_jnt_ruler = mc.rename(ik_jnt_ruler_temp, ( direction + '_' + name + '_ik_jnt_rulerShape' ) )
    # rename transform parent of distanceDimesion tool
    ruler_loc_list_rel = mc.listRelatives( ik_jnt_ruler, ap=1, type='transform' )
    ruler_loc_list_parent = mc.rename(ruler_loc_list_rel, direction + '_' + name + '_ik_jnt_ruler')

    # get locators controling length
    ruler_loc_list = mc.listConnections( ik_jnt_ruler, type='locator' )
    # rename and hide distance locators
    arm_loc_0 = mc.rename(ruler_loc_list[0], direction + '_' + name + '_hip_dist_loc')
    arm_loc_1 = mc.rename(ruler_loc_list[1], direction + '_' + name + '_wrist_dist_loc')
    # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
    mc.pointConstraint(strchJnt_lst[0], arm_loc_0 )
    mc.pointConstraint(ik_wristCtrl_lst[0], arm_loc_1 )

    
    #_______________________________#


    #______Function Variables_______#
    #variable ... ruler distance output
    ruler_dist = ik_jnt_ruler + '.distance'
    ruler_dist_result = mc.getAttr(ik_jnt_ruler + '.distance')

    #variable ... global_ctrl scale X
    global_ctrl_sclX = global_ctrl + '.scaleX'

    #variable
    stretch_blend = ik_wristCtrl_lst[0] + '.Stretch_Blend'



    # _______________create nodes____________________#

    # part1 ... ikHandle grp nodes
    stretch_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + name + '_stretch_dist_ratio' ) # create multDiv node
    mc.setAttr(stretch_dist_ratio + '.operation', 2) # set to Divide

    global_scale_offs = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + name + '_global_scale_offs' ) # default is multiply

    ikHndl_fllw_pma = mc.shadingNode('plusMinusAverage', asUtility=1, n = direction + '_' + name + '_ikHandle_follow_pma' ) # for ik handle to follow hip ctrl
    mc.setAttr(ikHndl_fllw_pma + '.operation', 2) # set to Subtract

    glbl_offs_ikHndl_fllw = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + name + '_global_scale_offs_ikHndl_follow' ) # global scale offset for ikHandle follow grp
    mc.setAttr(glbl_offs_ikHndl_fllw + '.operation', 2) # set to Divide

    clamp_end_stop = mc.shadingNode('clamp', asUtility=1, n = direction + '_' + name + '_clamp_end_stop' ) # limit ikHndl follow grp from going past wrist

    invert_node = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + name + '_invert_node' ) # invert value to negative, or positive, if already neg

    softIk_fllw_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_softIk_fllw_grp_blend' ) # blend between 0 or follow

    softIk_fllw_offs_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_softIk_fllw_offs_grp_blend' ) # smooth ikHndl grp follow

    
    # part2 ... joint nodes

    jnt_strch_ratio = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + name + '_jnt_strch_ratio' )

    ikHdl_grp_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = direction + '_' + name + '_ikHdl_grp_smooth_setDrvKey' )


    # elbow joints nodes

    elbow_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + name + '_elbow_strch' )

    mainJnts_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = direction + '_' + name + '_mainJnts_smooth_setDrvKey' )
    mc.setAttr(mainJnts_smooth_setDrvKey + '.preInfinity', 1)

    elbow_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + name + '_elbow_smooth_offs' )

    elbow_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_elbow_stretch_blend' )


    # wrist jnt nodes

    wrist_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + name + '_wrist_strch' )

    wrist_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + name + '_wrist_smooth_offs' )

    wrist_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_wrist_stretch_blend' )


    
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
    mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=50, value=5)
    mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=150, value=7.1)

    mc.connectAttr( clamp_end_stop + '.outputR', softIk_fllw_grp_blend + '.color2R', f=1 )  # sets follow grp to follow constant distance from hip ctrl
    mc.setAttr(softIk_fllw_grp_blend + '.color1R', 0) # set ikHndl grp follow to 0, to stay at wrist
    mc.connectAttr( stretch_blend, softIk_fllw_grp_blend + '.blender', f=1 )

    mc.connectAttr( ikHdl_grp_smooth_setDrvKey + '.output', softIk_fllw_offs_grp_blend + '.color2R', f=1 )  # sets follow offset grp to smoothly adjust follow distance for softIK
    mc.setAttr(softIk_fllw_offs_grp_blend + '.color1R', 0) # set ikHndl offset grp follow to 0, to have no effect
    mc.connectAttr( stretch_blend, softIk_fllw_offs_grp_blend + '.blender', f=1 )

    mc.connectAttr( softIk_fllw_offs_grp_blend + '.outputR', ikHndl_wrist_grp_offs1 + '.tx', f=1 ) # connect to ikHandle Grp
    mc.connectAttr( softIk_fllw_grp_blend + '.outputR', ikHndl_wrist_grp1 + '.tx', f=1 ) # connect to ikHandle Grp offset


    
    # part2 ... joint connections

    mc.connectAttr( ruler_dist, stretch_dist_ratio + '.input1X', f=1 ) # create stretch ratio
    mc.connectAttr( global_scale_offs + '.outputX', stretch_dist_ratio + '.input2X', f=1 ) # create stretch ratio

    mc.connectAttr( stretch_dist_ratio + '.outputX', jnt_strch_ratio + '.input1X', f=1 ) # create drv jnt stretch ratio
    mc.setAttr(jnt_strch_ratio + '.input2X', ruler_dist_result) #set drv jnt stretch ratio 2X to static ruler distance default
    mc.connectAttr( jnt_strch_ratio + '.outputX', strchJnt_lst[1] + '.translateX', f=1 ) # create drv jnt stretch ratio



    # elbow / elbow jnt connections _______________________________
    mc.connectAttr( stretch_dist_ratio + '.outputX', elbow_strch + '.input1X', f=1 ) # elbow stretch amount, base length multiplied by stretch ratio
    mc.setAttr(elbow_strch + '.input2X', to_elbow_len)

    mc.connectAttr( stretch_dist_ratio + '.outputX', mainJnts_smooth_setDrvKey + '.input', f=1 ) # smooth offset keys

    mc.setKeyframe(mainJnts_smooth_setDrvKey, float=0.3, value=3.35, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change # also ajust spline afterwards
    mc.setKeyframe(mainJnts_smooth_setDrvKey, float=0.5, value=2)
    mc.setKeyframe(mainJnts_smooth_setDrvKey, float=1, value=1)
    mc.setKeyframe(mainJnts_smooth_setDrvKey, float=2, value=0.957)


    mc.connectAttr( elbow_strch + '.outputX', elbow_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
    mc.connectAttr( mainJnts_smooth_setDrvKey + '.output', elbow_smooth_offs + '.input2X', f=1 )


    mc.connectAttr( elbow_smooth_offs + '.outputX', elbow_stretch_blend + '.color1R', f=1 )
    mc.setAttr(elbow_stretch_blend + '.color2R', to_elbow_len )  # set to default jnt length, static value

    mc.connectAttr( elbow_stretch_blend + '.outputR', ikJoint_list[2] + '.translateX', f=1 ) # connect blend to jnt translate X length
    #mc.connectAttr( elbow_stretch_blend + '.outputR', ikDriverJoint_list[1] + '.translateX', f=1 ) # connect blend to drvJnt translate X length

    mc.connectAttr( stretch_blend, elbow_stretch_blend + '.blender', f=1 )  # arm ctrl stretch blend attr


    # wrist jnt _______________________________
    mc.connectAttr( stretch_dist_ratio + '.outputX', wrist_strch + '.input1X', f=1 )
    mc.setAttr(wrist_strch + '.input2X', to_wrist_len)


    mc.connectAttr( wrist_strch + '.outputX', wrist_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
    mc.connectAttr( mainJnts_smooth_setDrvKey + '.output', wrist_smooth_offs + '.input2X', f=1 )


    mc.connectAttr( wrist_smooth_offs + '.outputX', wrist_stretch_blend + '.color1R', f=1 )
    mc.setAttr(wrist_stretch_blend + '.color2R', to_wrist_len )  # set to default jnt length, static value

    mc.connectAttr( wrist_stretch_blend + '.outputR', ikJoint_list[3] + '.translateX', f=1 ) # connect blend to jnt translate X length
    #mc.connectAttr( wrist_stretch_blend + '.outputR', ikDriverJoint_list[2] + '.translateX', f=1 ) # connect blend to drvJnt translate X length

    mc.connectAttr( stretch_blend, wrist_stretch_blend + '.blender', f=1 )  # arm ctrl stretch blend attr


    #________________#
    #________________#


    
    #_________________________________________________________________________________________#
    #____________________ Regular Clavicle to Shoulder Stretch IK Setup_______________________#
    #_______________________________(single chain solver)_____________________________________#
    to_shoulder_len = mc.getAttr(ikJoint_list[1] + '.tx')

    shoulder_var_loc = mc.spaceLocator(n=regClav_jnt_lst[0] + '_locator')
    upperArm1_var_loc = mc.spaceLocator(n=regClav_jnt_lst[1] + '_locator')
    #***was getting "cycle" glitch for parentConstraining shoulder locator instead of pointConstraining
    mc.pointConstraint(regClav_jnt_lst[0], shoulder_var_loc)
    mc.pointConstraint(shoulder_ikHandle[0], upperArm1_var_loc)
    shldr_measerTool = mc.distanceDimension(shoulder_var_loc, upperArm1_var_loc)
    shldr_measerTool_parent = mc.listRelatives(shldr_measerTool, p=True)
    shldr_measerTool_parent = mc.rename(shldr_measerTool_parent, ('distanceDimension_' + shoulder_ikHandle[0]))
    
    # global scale offset
    shldr_globalScale_offs = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + name + '_shldr_globalScale_offs' ) # default is multiply
    mc.connectAttr( global_ctrl_sclX, shldr_globalScale_offs + '.input1X' )
    shldr_measure_dist = mc.getAttr( shldr_measerTool_parent + '.distance' )
    mc.setAttr( shldr_globalScale_offs + '.input2X' , shldr_measure_dist )
    
    # get shoulder length ratio
    shldr_len_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_' + name + '_shldr_len_ratio' )
    mc.setAttr( shldr_len_ratio + '.operation', 2) # set operation to divide
    mc.connectAttr( shldr_measerTool_parent + '.distance', shldr_len_ratio + '.input1X')
    mc.connectAttr( shldr_globalScale_offs + '.outputX', shldr_len_ratio + '.input2X')

    # multiply length ratio with joint default length
    shldr_len_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_' + name + '_shldr_len_mult' )
    mc.connectAttr( shldr_len_ratio + '.outputX' , shldr_len_mult + '.input1X') # mult value
    mc.setAttr( shldr_len_mult + '.input2X' , to_shoulder_len)

    # set joint length to calculated value
    mc.connectAttr( shldr_len_mult + '.outputX', regClav_jnt_lst[1] + '.translateX')

    
    # if direction == 'l':
    #     mc.connectAttr(shldr_measerTool_parent + '.distance', shldr_scale_off + '.input1X')
    # elif direction == 'r':
    #     # (right) invert to negative translate X (since x is up the chain instead of down the chain)
    #     shldr_invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_shldr_invert_value' )
    #     mc.setAttr( (shldr_invert_value + '.input2X'), -1 )
    #     mc.connectAttr( (shldr_measerTool_parent + '.distance'), (shldr_invert_value + '.input1X'), f=True)
    #     mc.connectAttr( (shldr_invert_value + '.outputX') , shldr_scale_off + '.input1X')
    

    # create grp for ctrls and measure tool for organization
    shldr_measerTool_grp = mc.group(em = True, n= direction + '_shldr_measure_grp')
    mc.parent(shldr_measerTool_parent, shoulder_var_loc, upperArm1_var_loc, shldr_measerTool_grp)
    

    
    #____________parenting ik shoulder ctrl__________________#
    # parent constrain shldr joint translation and rotation to single solver ik handle grp
    mc.parentConstraint(ik_shldrCtrl_lst[0], shldrGrp, mo=True) # skipping rotation constrain caused shoulder flipping when rig upside down  #problem here shoulder not in perfect x direction from shldr, therefore scaling with X is off
    # lock and hide rotation values for shldr control
    mc.setAttr((ik_shldrCtrl_lst[0] + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ik_shldrCtrl_lst[0] + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ik_shldrCtrl_lst[0] + '.rz'), lock=True, keyable=False, channelBox=False)
    
    
    #_____________________#
    #____blend shldr______#
    #_____________________#

    # add blend between auto and regular clavical attribute to shoulder control 
    mc.addAttr( ik_shldrCtrl_lst[0], ln='__________', nn='__________', at='enum', enumName = '__________') # add divider organizer attr
    mc.setAttr( ik_shldrCtrl_lst[0] + '.__________', channelBox=1 ) # does not appear in channel box otherwise
    mc.addAttr( ik_shldrCtrl_lst[0], ln='Auto_or_Regular_Clav', nn='Auto_or_Regular_Clav', min=0, max=1, at='double', dv=1, k=1)
    mc.addAttr( ik_shldrCtrl_lst[0], ln='Stretch_Blend', nn='Stretch_Blend', min=0, max=1, at='double', dv=1, k=1)

    # parent rotate constrain both autoClav and regClav to clavicle, to switch between
    shldr_rot_const = mc.parentConstraint(autoClav_jnt_lst[0], regClav_jnt_lst[0], ikJoint_list[0], st=('x','y','z'), mo=True ) #
    # change interp type to prevent flipping
    if direction == 'r':
        mc.setAttr(shldr_rot_const[0] + '.interpType', 2) # shortest (def is average)

    #blend between shoulder lengths____#
    shldr_len_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_shldr_len' )
    mc.connectAttr(shldr_len_mult + '.outputX', shldr_len_blend + '.color1R') # set to stretch length
    mc.setAttr(shldr_len_blend + '.color2R', to_shoulder_len)  # set to default shldr length

    #stretch blend____# same as above, but needed twice (one for auto clav blend, one for stretch blend)
    shldr_strch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + name + '_shldr_strch' )
    mc.connectAttr(shldr_len_blend + '.outputR', shldr_strch_blend + '.color1R')
    mc.setAttr(shldr_strch_blend + '.color2R', to_shoulder_len)  # set to default shldr length

    # connect blend attr
    mc.connectAttr(ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav', shldr_len_blend + '.blender')
    mc.connectAttr(shldr_strch_blend + '.outputR', ikJoint_list[1] + '.translateX')
   
    # connect blend attr
    mc.connectAttr(ik_shldrCtrl_lst[0] + '.Stretch_Blend', shldr_strch_blend + '.blender')


    # shldr orient constraint blend
    #_______0_________#
    mc.setAttr((ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav'), 0)

    mc.setAttr( (ikJoint_list[0] + '_parentConstraint1.' + autoClav_jnt_lst[0] + 'W0'),  1)
    mc.setAttr( (ikJoint_list[0] + '_parentConstraint1.' + regClav_jnt_lst[0] + 'W1'),  0)

    mc.setDrivenKeyframe( (ikJoint_list[0] + '_parentConstraint1.' + autoClav_jnt_lst[0] + 'W0'), currentDriver = (ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav') )
    mc.setDrivenKeyframe( (ikJoint_list[0] + '_parentConstraint1.' + regClav_jnt_lst[0] + 'W1'), currentDriver = (ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav') )
    
    #_______1_________#
    mc.setAttr((ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav'), 1)

    mc.setAttr( (ikJoint_list[0] + '_parentConstraint1.' + autoClav_jnt_lst[0] + 'W0'),  0)
    mc.setAttr( (ikJoint_list[0] + '_parentConstraint1.' + regClav_jnt_lst[0] + 'W1'),  1)

    mc.setDrivenKeyframe( (ikJoint_list[0] + '_parentConstraint1.' + autoClav_jnt_lst[0] + 'W0'), currentDriver = (ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav') )
    mc.setDrivenKeyframe( (ikJoint_list[0] + '_parentConstraint1.' + regClav_jnt_lst[0] + 'W1'), currentDriver = (ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav') )
    



    
    #___________________________________________________________________#
    #___________________Visibility and Parenting________________________#
    #___________________________________________________________________#

    # hide unused auto clav pole vector
    mc.setAttr(autoClav_pvCtrl_lst[0] + '.visibility', 0)
    # stretch joint ik handle grp to invisible
    mc.setAttr(ikHndl_strch_grp1 + '.visibility', 0)
    #hide ikHandle
    mc.setAttr(ikHndlWrist[0] + '.visibility', 0)
    # hide dist loc and tool
    mc.setAttr(ruler_loc_list_parent + '.visibility', 0)
    mc.setAttr(arm_loc_0 + '.visibility', 0)
    mc.setAttr(arm_loc_1 + '.visibility', 0)
    #parent grp to global grp to organize
    mc.parent(ruler_loc_list_parent, myArmGrp)
    mc.parent(arm_loc_0, myArmGrp)
    mc.parent(arm_loc_1, myArmGrp)
    #_____clav______#
    mc.setAttr(shldrGrp + '.visibility', 0)
    mc.setAttr(ikHndl_autoClav[0] + '.visibility', 0)
    # hide dist loc and tool
    mc.setAttr(shldr_measerTool_grp + '.visibility', 0)
    #parent grp to arm grp to organize
    mc.parent(shldr_measerTool_grp, myArmGrp)
    mc.parent(shldrGrp, myArmGrp)
    mc.parent(ikHndl_autoClav[0], myArmGrp)
    
    
    
    # parent switch grp to main arm grp
    mc.parent(switch_ctrl_grp_list, myArmGrp)

    #parent arm group to global misc grp
    mc.parent(myArmGrp, global_misc_grp)

    #parent top fk ctrl grp to chest ctrl
    mc.parent(fk_ctrl_grp_list[0], chest_ctrl)
    mc.parent(ik_clavGrp_lst[0], chest_ctrl)
    mc.parent(ik_shldrGrp_lst[0], ik_clavCtrl_lst[0]) # parent to clav


    # set default to ik arm
    mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
    mc.setAttr((stretch_blend), 0.5)
    mc.setAttr((ik_shldrCtrl_lst[0] + '.Auto_or_Regular_Clav'), 0.5)
    mc.setAttr((ik_shldrCtrl_lst[0] + '.Stretch_Blend'), 0)
    

    
    # return top ik and fk controls to parent to hip
    return ik_clavGrp_lst[0], fk_ctrl_grp_list[0], myArmGrp, pvCtrl_lst[0], switch_ctrl_list[0]

    
