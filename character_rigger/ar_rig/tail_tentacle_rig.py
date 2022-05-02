import maya.cmds as mc

import string

from ..ar_functions import sel_near_jnt
from ..ar_functions import sel_joints


def tail_tentacle_rig(  defaultJnt_prefix = 'sknJnt_', 
                        fkJnt_prefix = 'fkJnt_', 
                        ikJnt_prefix = 'ikJnt_',
                        offs_prntJnt = 'offs_prntJnt_hips', 
                        fk_ctrl_size = 10):
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

    # organization group
    organizeGrp = mc.group(em=True, n=name + '_grp')

    
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

    #parent ik Hndl global grp to organize
    mc.parent(ikHndl_var[0], organizeGrp)



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
                    n = ikHndl_crv + '_skinCluster')



    '''
    #___________ik handle CTRL____________#
    ik_group_list = []
    #create curve box
    for items in range(0,1):
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
        mc.setAttr((myCurve + ".scaleX"), 5)
        mc.setAttr((myCurve + ".scaleY"), 5)
        mc.setAttr((myCurve + ".scaleZ"), 5)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 0.1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename(ikJoint_list[0] + '_ik_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(myGroup, ikJoint_list[-1], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        #translate contrain ik ctrl to ik handle
        mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
        #rotate constrain ik ctrl to ankle joint
        mc.parentConstraint(myCurve, ikJoint_list[-1], st=('x','y','z'))

        #parent grp to global grp to organize
        mc.parent(myGroup, myIKGrp)

        #append grp for outside use
        ik_group_list.append(myGroup)
    
    '''


    #______________________________________________________________________________#
    #____________________________IK/ FK Switch Ctrl ________________________________#
    #______________________________________________________________________________#
    switch_ctrl_list = []
    switch_ctrl_grp_list = []
    for items in range(0,1):
        #name circle curves
        switchCurveA_name = 'switch_ctrlA#'
        switchCurveB_name = 'switch_ctrlB#'
        switchCurveC_name = 'switch_ctrlC#'

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
        mc.setAttr((switchCurveA[0] + ".translateY"), 20)
        mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(switchCurveA, apply=True)

        #_______move joint to ankle and parent_______#
        #parent and zero joints to last joint in selection
        mc.parent(switchCurveA_grp, mySel[-1], relative=True)
        #parent joints to world space
        mc.Unparent(switchCurveA_grp)

        # parent constrain switch ctrl to ankle
        mc.parentConstraint(mySel[-1], switchCurveA_grp, mo=True)

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
    for items_trans, items_rot, items_scale in zip(  blendColorsTran_list, 
                                                                blendColorsRot_list, 
                                                                blendColorsScale_list):
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_scale + '.blender'), f=True)


    #_______connect switch control to visibility______#
    for i in range(0,1): 
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
        mc.setAttr((ik_group_list[0] + '.visibility'), 1)
        mc.setAttr((pv_group_list[0] + '.visibility'), 1)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)
        mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
        mc.setAttr((ik_group_list[0] + '.visibility'), 0)
        mc.setAttr((pv_group_list[0] + '.visibility'), 0)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)
        mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


    #_____________ organize _____________#
    #organize into final group
    ik_fk_blend_grp = mc.group(em=True, n='ik_fk_blend_grp')
    mc.parent(fk_ctrl_grp_list[0], ik_fk_blend_grp)
    mc.parent(switch_ctrl_grp_list[0], ik_fk_blend_grp)
    mc.parent(myIKGrp, ik_fk_blend_grp)
    #parent joints to final group too
    mc.parent(fkJoint_list[0], ik_fk_blend_grp)
    mc.parent(ikJoint_list[0], ik_fk_blend_grp)

    #_____________ visibility _____________#
    #hide ik handle
    #mc.setAttr(ikHandle_var[0] + '.visibility', 0)
    
