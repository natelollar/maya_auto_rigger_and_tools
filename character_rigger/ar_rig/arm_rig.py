import maya.cmds as mc

import maya.api.OpenMaya as om

import itertools

from ..ar_functions import find_jnts
from ..ar_functions import sel_joints

# arm rig
class arm_rig():

    def arm_rig(self, 
                direction, 
                offset_parent_jnt, 
                fk_ctrl_size, 
                ik_ctrl_size, 
                pv_ctrl_size, 
                knee_dist_mult, 
                global_ctrl):
        #___________________Find Arm Joints____________________________#
        # create arm joint list
        if direction == 'left':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts = arm_jnts_temp.find_arm_jnts('left')
        elif direction == 'right':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts = arm_jnts_temp.find_arm_jnts('right')
        
        # create arm joint variables
        clav_jnt = arm_jnts[0] 
        shlder_jnt = arm_jnts[1] 
        elbow_jnt = arm_jnts[2] 
        twist_jnts = arm_jnts[3:-1]
        wrist_jnt = arm_jnts[-1]

        # arm joints without twist jnts
        main_arm_jnts = [clav_jnt, shlder_jnt, elbow_jnt, wrist_jnt]

        #_____________________________________________________________________#
        #___________________End of Find Arm Joints____________________________#
        #_____________________________________________________________________#

        #______________________________#
        #_____Blended Joint Chain______#
        #______________________________#

        fkJoint_list = []
        ikJoint_list = []
        for i in main_arm_jnts:
            #______________________#
            #____create FK chain___#
            fkJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 6)
            #joint color
            mc.setAttr('.overrideEnabled', 1)
            mc.setAttr('.overrideRGBColors', 1)
            mc.setAttr('.overrideColorRGB', 1, 0, 0.1)
            
            fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
            mc.Unparent(fkJoint)

            # scale constraint instead of blend joint (for proper ctrl and global scale)
            mc.scaleConstraint(fkJoint, i)
            
            # create list of fk joints
            fkJoint_list.append(fkJoint)
            
            #_______________________#
            #____create _IK chain___#
            ikJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 4)
            #joint color
            mc.setAttr('.overrideEnabled', 1)
            mc.setAttr('.overrideRGBColors', 1)
            mc.setAttr('.overrideColorRGB', .1, .9, 0.1)
            
            ikJoint = mc.rename(ikJoint_orig, ('IK_' + i))
            mc.Unparent(ikJoint)

            # scale constraint instead of blend joint (for proper ctrl and global scale)
            mc.scaleConstraint(ikJoint, i)

            # create list of ik joints
            ikJoint_list.append(ikJoint)

            # set arm jnt scale comp off to avoid double scale (when global scale)
            mc.setAttr( i + '.segmentScaleCompensate', 0 )
            mc.setAttr( ('FK_' + i) + '.segmentScaleCompensate', 0 )
            mc.setAttr( ('IK_' + i) + '.segmentScaleCompensate', 0 )

            
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
        for i_FK, i_IK, i in itertools.izip(fkJoint_list, ikJoint_list, main_arm_jnts):
            #create blend color nodes
            blendColorsTran = mc.createNode('blendColors', n= i + '_blendColorsTran')
            blendColorsRot = mc.createNode('blendColors', n= i + '_blendColorsRot')
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
        
        mc.parent(fkJoint_list[0], offset_parent_jnt)

        mc.parent(ikJoint_list[0], offset_parent_jnt)
        
        #__________________________________________________________________#
        # wrist length offset, since twist not included in blend joints (b/c using blend color nodes and not constraints)
        #__________________________________________________________________#

        # twist joint lengths for offset
        twist_jnt_tx_list = []
        for i in twist_jnts:
            twist_len = mc.getAttr(i + '.tx')
            twist_jnt_tx_list.append(twist_len)
        # add together twist jnt length to get wrist offset
        wrist_offset_sum = sum(twist_jnt_tx_list)

        # create plus minus average for wrist offset
        wrist_offset_plusMinus = mc.shadingNode('plusMinusAverage', asUtility=True, n=direction + '_wrist_offset' )
        # twist jnt translate x length sum to offset for not having twist jnts
        mc.setAttr(wrist_offset_plusMinus + '.input3D[1].input3Dx', wrist_offset_sum)
        # set plusMinus to subtract
        mc.setAttr(wrist_offset_plusMinus + '.operation', 2)
        # connect wrist offset length between wrist translate blend node and plusMinusAverage node
        blendNode_offset = mc.listConnections(main_arm_jnts[-1], s=1, d=0, type='blendColors')
        mc.connectAttr(blendNode_offset[0] + '.output', wrist_offset_plusMinus + '.input3D[0]')
        mc.connectAttr(wrist_offset_plusMinus + '.output3D', main_arm_jnts[-1] + '.translate', f=1)


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
            mc.setAttr('.scale', fk_ctrl_size, fk_ctrl_size, fk_ctrl_size)
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
            mc.scaleConstraint(myCurve_name, i)
        
        #remove first and last of lists to correctly parent ctrls and grps together in for loop
        fk_ctrl_grp_list_temp = fk_ctrl_grp_list[1:]

        fk_ctrl_list_temp = fk_ctrl_list[:-1]


        #parent ctrls and grps together
        for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
            mc.parent(i_grp, i_ctrl)

        
        #_____________________________________#
        #______________IK Ctrls_______________#
        #_____________________________________#
        #group for organization
        myIKGrp = mc.group(em=True, n = direction + '_arm_ik_grp')
        
        #___________create IK HANDLE____________#

        ikHandle_var = mc.ikHandle(n=ikJoint_list[1] + '_ikHandkle', sj=ikJoint_list[1], ee=ikJoint_list[3])

        mc.setAttr((ikHandle_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorZ'), 0)

        ikHandle_effector_var = mc.listConnections(ikHandle_var, s=True, type='ikEffector')

        mc.rename(ikHandle_effector_var, ikHandle_var[0] + '_effector')

        #hide ik handle
        mc.setAttr(ikHandle_var[0] + '.visibility', 0)

        #parent ik handle global grp to organize
        mc.parent(ikHandle_var[0], myIKGrp)


        #___________ik wrist CTRL____________#
        ik_group_list = []
        ik_ctrl_list = []
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
            mc.setAttr((myCurve + '.scale'), ik_ctrl_size, ik_ctrl_size, ik_ctrl_size)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.1, 1, 0)

            #rename curve
            myCurve = mc.rename(ikJoint_list[-1] + '_ik_ctrl')
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

            #parent grp to global grp to organize
            mc.parent(myGroup, global_ctrl)

            #append grp for outside use
            ik_group_list.append(myGroup)
            ik_ctrl_list.append(myCurve)
        

            # parent constrain ik handle to ik wrist ctrl
            #translate contrain ik ctrl to ik handle
            mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
            #rotate and scale constrain ik ctrl to ik wrist joint
            mc.parentConstraint(myCurve, ikJoint_list[-1], st=('x','y','z'))
            mc.scaleConstraint(myCurve, ikJoint_list[-1])

        
        #___________ik shldr CTRL____________#
        ik_shldr_group_list = []
        ik_shldr_ctrl_list = []
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
            mc.setAttr((myCurve + '.scale'), ik_ctrl_size, ik_ctrl_size, ik_ctrl_size)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.1, 1, 0)

            #rename curve
            myCurve = mc.rename(ikJoint_list[1] + '_ik_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            #parent and zero curveGrp to joints
            mc.parent(myGroup, ikJoint_list[1], relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(myGroup)

            #parent grp to global grp to organize
            mc.parent(myGroup, myIKGrp)

            #append grp for outside use
            ik_shldr_group_list.append(myGroup)
            ik_shldr_ctrl_list.append(myCurve)

        # parent and scale constrain shldr joint translation to control
        mc.parentConstraint(ik_shldr_ctrl_list[0], ikJoint_list[1])
        #scale constrain ctrl to jnt
        mc.scaleConstraint(ik_shldr_ctrl_list[0], ikJoint_list[1])
        # lock and hide rotation values for shldr control
        #mc.setAttr((ik_shldr_ctrl_list[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        #mc.setAttr((ik_shldr_ctrl_list[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        #mc.setAttr((ik_shldr_ctrl_list[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        
        
        #_________________POLE VECTOR Start___________________#
        #_____________________________________________________#
        pv_group_list = []
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
            mc.setAttr((myCurve + '.scale'), pv_ctrl_size, pv_ctrl_size, pv_ctrl_size)

            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorRGB'), 1, 1, 0)
            #rename curve
            myCurve = mc.rename(ikJoint_list[2] + '_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            

            #___more accurate mid point (for 'hip_to_ankle_scaled')___
            #length of whole limb (tran X of elbow and wrist)
            limb_lenA = (   mc.getAttr(ikJoint_list[2] + '.tx') + 
                            mc.getAttr(ikJoint_list[3] + '.tx') )

            #length of upper half of limb (tran X of elbow)
            upperLimb_lenA = mc.getAttr(ikJoint_list[2] + '.tx')

            #divide sum of arm lengths by upper arm length (for more accurate mid point)
            better_midPoint_var = ( limb_lenA / upperLimb_lenA )  

            #__vector math____#
            #vector positions of hip, knee, ankle
            shldr_pos = om.MVector(mc.xform(ikJoint_list[1], q=True, rp=True, ws=True))
            elbow_pos = om.MVector(mc.xform(ikJoint_list[2], q=True, rp=True, ws=True))
            wrist_pos = om.MVector(mc.xform(ikJoint_list[3], q=True, rp=True, ws=True))

            #finding vector point of pv knee (on plane of hip, knee, ankle)
            hip_to_ankle = wrist_pos - shldr_pos
            hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
            mid_point = shldr_pos + hip_to_ankle_scaled
            mid_point_to_knee_vec = elbow_pos - mid_point
            mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * knee_dist_mult  #pv ctrl distance from knee multiplier
            mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

            #final polve vector point (to avoid knee changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

            myAimConst = mc.aimConstraint(  ikJoint_list[2], 
                                            myGroup, 
                                            offset=(0, 0, 0), 
                                            weight=1, 
                                            aimVector=(0, 0, 1), 
                                            upVector=(0, 1, 0), 
                                            worldUpType=('vector'), 
                                            worldUpVector=(0, 1, 0) )
            mc.delete(myAimConst)

            #___connect pole vector
            mc.poleVectorConstraint(myCurve, ikHandle_var[0])

            # connect scale of knee and pole vector control (scale constraint creates cyclical error)
            mc.connectAttr( (myCurve + '.scale'), ( ikJoint_list[2] ) + '.scale', f=True)

            #parent grp to global grp to organize
            mc.parent(myGroup, global_ctrl)

            pv_group_list.append(myGroup)

        
        #______________________________________________________________________________#
        #____________________________IK/ FK Switch Ctrl _______________________________#
        #______________________________________________________________________________#

        switch_ctrl_list = []
        switch_ctrl_grp_list = []
        for i in range(0,1):
            #name circle curves
            if direction == 'left':
                switchCurveA_name = 'l_switch_ctrl'
                switchCurveB_name = 'l_switch_ctrlA'
                switchCurveC_name = 'l_switch_ctrlB'
            if direction == 'right':
                switchCurveA_name = 'r_switch_ctrl'
                switchCurveB_name = 'r_switch_ctrlA'
                switchCurveC_name = 'r_switch_ctrlB'

            #create nurbs circle
            switchCurveA = mc.circle(n=switchCurveA_name, ch=False, r=3, nr=(0,1,0))
            #create variable for nurbs circle shape
            switchCurveA_shape = mc.listRelatives(switchCurveA, s=True)
            #color nurbs circle shape
            mc.setAttr((switchCurveA_shape[0] + '.overrideEnabled'), 1)
            mc.setAttr((switchCurveA_shape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((switchCurveA_shape[0] + '.overrideColorRGB'), 0, .5, 1)

            #create 2nd nurbs circle
            switchCurveB = mc.circle(n=switchCurveB_name, ch=False, r=3, nr=(0,0,0))
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
            switchCurveC = mc.circle(n=switchCurveC_name, ch=False, r=3, nr=(1,0,0))
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
            if direction == 'left':
                mc.setAttr((switchCurveA[0] + '.tz'), -35)
            elif direction == 'right':
                mc.setAttr((switchCurveA[0] + '.tz'), 35)
            mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
            mc.makeIdentity(switchCurveA, apply=True)

            #_______move joint to ankle and parent_______#
            #parent and zero joints to last joint in selection
            mc.parent(switchCurveA_grp, main_arm_jnts[-1], relative=True)
            #parent joints to world space
            mc.Unparent(switchCurveA_grp)

            # parent and scale constrain switch ctrl to ankle
            mc.parentConstraint(main_arm_jnts[-1], switchCurveA_grp, mo=True)
            mc.scaleConstraint(main_arm_jnts[-1], switchCurveA_grp, mo=True)

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
        for items_trans, items_rot in itertools.izip(   blendColorsTran_list, 
                                                        blendColorsRot_list ):
            mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
            mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)


        #_______connect switch control to visibility______#
        for i in range(0,1): 
            # 1 is fk, 0 is ik, (for loop to avoid clashing variables)
            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
            mc.setAttr((ik_group_list[0] + '.visibility'), 1)
            mc.setAttr((pv_group_list[0] + '.visibility'), 1)
            mc.setAttr((ik_shldr_group_list[0] + '.visibility'), 1)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)


            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_shldr_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
            mc.setAttr((ik_group_list[0] + '.visibility'), 0)
            mc.setAttr((pv_group_list[0] + '.visibility'), 0)
            mc.setAttr((ik_shldr_group_list[0] + '.visibility'), 0)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)

            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_shldr_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

        # scale constraint switch
        for jnt in main_arm_jnts:
            # 1 is fk, 0 is ik
            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
            # alternative is to disconnect/ unlock and use '.target[0].targetWeight'
            mc.setAttr( (jnt + '_scaleConstraint1.FK_' + jnt + 'W0'),  0)
            mc.setAttr( (jnt + '_scaleConstraint1.IK_' + jnt + 'W1'),  1)

            mc.setDrivenKeyframe((jnt + '_scaleConstraint1.FK_' + jnt + 'W0'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((jnt + '_scaleConstraint1.IK_' + jnt + 'W1'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
            mc.setAttr( (jnt + '_scaleConstraint1.FK_' + jnt + 'W0'),  1)
            mc.setAttr( (jnt + '_scaleConstraint1.IK_' + jnt + 'W1'),  0)

            mc.setDrivenKeyframe((jnt + '_scaleConstraint1.FK_' + jnt + 'W0'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((jnt + '_scaleConstraint1.IK_' + jnt + 'W1'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

    
    #________________________________________________________________________________#
    #________________________END of FK/IK BLEND______________________________________#

        # ______________________________________________________#
        # __________________ IK stretchy arm ___________________#
        # ______________________________________________________#

        # get joint x lengths
        to_knee_len = mc.getAttr(ikJoint_list[2] + '.tx')
        to_ankle_len = mc.getAttr(ikJoint_list[-1] + '.tx')
        # create ruler tool
        ik_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
        ik_jnt_ruler = mc.rename(ik_jnt_ruler_temp, ( direction + '_ik_jnt_rulerShape' ) )
        # rename transform parent of distanceDimesion tool
        ruler_loc_list_rel = mc.listRelatives( ik_jnt_ruler, ap=1, type='transform' )
        ruler_loc_list_parent = mc.rename(ruler_loc_list_rel, direction + '_ik_jnt_ruler')

        # get locators controling length
        ruler_loc_list = mc.listConnections( ik_jnt_ruler, type='locator' )
        # rename and hide distance locators
        arm_loc_0 = mc.rename(ruler_loc_list[0], direction + '_hip_dist_loc')
        arm_loc_1 = mc.rename(ruler_loc_list[1], direction + '_ankle_dist_loc')
        # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
        mc.parentConstraint(ik_shldr_ctrl_list[0], arm_loc_0 )
        mc.parentConstraint(ik_ctrl_list[0], arm_loc_1 )
        
        # make nodes for stretchy limb
        arm_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_arm_dist_ratio' )
        # set mulDiv node to Divide
        mc.setAttr(arm_dist_ratio + '.operation', 2)
        # global scale offset multDiv node
        globalScale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_arm_globalScale_off' )
        # operation to divide
        mc.setAttr(globalScale_off + '.operation', 2)
        # create mult/div nodes for ratio * length
        ratio_knee_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_knee_mult' )
        ratio_ankle_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_ankle_mult' )
        #create condition nodes for if greater than length, to prevent negative stretching
        #set operation to 'greater than'
        knee_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_knee_len_con' )
        ankle_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_ankle_len_con' )
        #set operation to 'greater than'
        if direction == 'left':
            mc.setAttr(knee_len_con + '.operation', 2)
            mc.setAttr(ankle_len_con + '.operation', 2)
        #set operation to 'less than'
        elif direction == 'right':
            mc.setAttr(knee_len_con + '.operation', 4)
            mc.setAttr(ankle_len_con + '.operation', 4)
        
        # connect arm distance to global scale offset
        mc.connectAttr( (ik_jnt_ruler + '.distance'), (globalScale_off + '.input1X'), f=True )
        # connect global ctrl scale X to global scale offset
        mc.connectAttr( (global_ctrl + '.scaleX'), (globalScale_off + '.input2X'), f=True )

        # connect ruler distance over total distance of joints
        if direction == 'left':
            mc.connectAttr( (globalScale_off + '.outputX'), (arm_dist_ratio + '.input1X'), f=True )
        elif direction == 'right':
            # (right) invert to negative translate X (since x is up the chain instead of down the chain)
            invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_arm_invert_value' )
            mc.setAttr( (invert_value + '.input2X'), -1 )
            mc.connectAttr( (globalScale_off + '.outputX'), (invert_value + '.input1X'), f=True )
            mc.connectAttr( (invert_value + '.outputX'), (arm_dist_ratio + '.input1X'), f=True )

        # soft ik, a little less than total length to keep some bend in knee joint
        mc.setAttr( (arm_dist_ratio + '.input2X'), (to_knee_len + to_ankle_len) * 0.994 )

        # connect length ratio to apply to x length of knee and ankle (fraction * distance)
        mc.connectAttr( (arm_dist_ratio + '.outputX'), (ratio_knee_mult + '.input2X'), f=True )
        mc.connectAttr( (arm_dist_ratio + '.outputX'), (ratio_ankle_mult + '.input2X'), f=True )
        # joint length to input 1X
        mc.setAttr( (ratio_knee_mult + '.input1X'), to_knee_len )
        mc.setAttr( (ratio_ankle_mult + '.input1X'), to_ankle_len )

        # connect mult ratio nodes to condition node (if length greater, then stretch)
        mc.connectAttr( (ratio_knee_mult + '.outputX'), (knee_len_con + '.colorIfTrueR'), f=True )
        mc.connectAttr( (ratio_knee_mult + '.outputX'), (knee_len_con + '.firstTerm'), f=True )

        mc.connectAttr( (ratio_ankle_mult + '.outputX'), (ankle_len_con + '.colorIfTrueR'), f=True )
        mc.connectAttr( (ratio_ankle_mult + '.outputX'), (ankle_len_con + '.firstTerm'), f=True )

        # add joint lengths to base value, if false
        mc.setAttr( (knee_len_con + '.colorIfFalseR'), to_knee_len )
        mc.setAttr( (knee_len_con + '.secondTerm'), to_knee_len )

        mc.setAttr( (ankle_len_con + '.colorIfFalseR'), to_ankle_len )
        mc.setAttr( (ankle_len_con + '.secondTerm'), to_ankle_len )

        #connect stretch lengths to joint translate x
        mc.connectAttr( (knee_len_con + '.outColorR'), (ikJoint_list[2] + '.tx'), f=True )
        mc.connectAttr( (ankle_len_con + '.outColorR'), (ikJoint_list[-1] + '.tx'), f=True )


        #___________________________________________#
        #___________________________________________#
        #___________________________________________#
        # hide dist loc and tool
        mc.setAttr(ruler_loc_list_parent + '.visibility', 0)
        mc.setAttr(arm_loc_0 + '.visibility', 0)
        mc.setAttr(arm_loc_1 + '.visibility', 0)
        #parent grp to global grp to organize
        mc.parent(ruler_loc_list_parent, myIKGrp)
        mc.parent(arm_loc_0, myIKGrp)
        mc.parent(arm_loc_1, myIKGrp)

        # return top ik and fk controls to parent to hip
        return ik_shldr_group_list[0], fk_ctrl_grp_list[0]

        