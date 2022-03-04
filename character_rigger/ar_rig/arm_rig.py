import maya.cmds as mc

import maya.api.OpenMaya as om

import itertools

import random

from ..ar_functions import find_jnts
from ..ar_functions import sel_joints
from ..ar_tools import fk_chain

# arm rig
class arm_rig():

    def arm_rig(self, 
                direction, 
                offset_parent_jnt, 
                fk_ctrl_size, 
                ik_ctrl_size, 
                pv_ctrl_size, 
                elbow_dist_mult,
                to_chest_ctrl, 
                global_ctrl,
                global_misc_grp):

        #___________________Find Arm Joints____________________________#
        # create arm joint list
        if direction == 'left':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts_info = arm_jnts_temp.find_arm_jnts('left')
        elif direction == 'right':
            arm_jnts_temp = find_jnts.find_jnts()
            arm_jnts_info = arm_jnts_temp.find_arm_jnts('right')
        
        # arm joints without twist jnts (clavicle, shoulder, elbow, wrist)
        main_arm_jnts = arm_jnts_info[0]

        # create arm joint variables
        clav_jnt = main_arm_jnts[0] 
        shlder_jnt = main_arm_jnts[1] 
        elbow_jnt = main_arm_jnts[2] 

        twist_jnts = arm_jnts_info[1]

        wrist_jnt = main_arm_jnts[-1]

        # forearm list, elbow start, wrist end, twist in middle
        foreArm_jnts = [elbow_jnt] + twist_jnts + [wrist_jnt]

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
        # overall group for organization
        myArmGrp = mc.group(em=True, n = direction + '_arm_grp')
        
        #___________create IK HANDLE____________#

        ikHandle_var = mc.ikHandle(n=ikJoint_list[1] + '_ikHandkle', sj=ikJoint_list[1], ee=ikJoint_list[3])

        mc.setAttr((ikHandle_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorZ'), 0)

        ikHandle_effector_var = mc.listConnections(ikHandle_var, s=True, type='ikEffector')

        mc.rename(ikHandle_effector_var, ikHandle_var[0] + '_effector')

        #parent ik handle global grp to organize
        mc.parent(ikHandle_var[0], myArmGrp)


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

            # 0 out rotation, to level out ctrl, and represent that it does not control rotation
            mc.setAttr((myGroup + '.rotate'), 0, 0, 0)

            #parent grp to global grp to organize
            #mc.parent(myGroup, myArmGrp)

            #append grp for outside use
            ik_shldr_group_list.append(myGroup)
            ik_shldr_ctrl_list.append(myCurve)

        
        #___________ik clav CTRL____________#
        ik_clav_group_list = []
        ik_clav_ctrl_list = []
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
            myCurve = mc.rename(ikJoint_list[0] + '_ik_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            #parent and zero curveGrp to joints
            mc.parent(myGroup, ikJoint_list[0], relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(myGroup)

            # 0 out rotation, to level out ctrl, and represent that it does not control rotation
            mc.setAttr((myGroup + '.rotate'), 0, 0, 0)

            #parent grp to global grp to organize
            #mc.parent(myGroup, myArmGrp)

            #append grp for outside use
            ik_clav_group_list.append(myGroup)
            ik_clav_ctrl_list.append(myCurve)

        # parent and scale constrain clav joint translation to control
        mc.parentConstraint(ik_clav_ctrl_list[0], ikJoint_list[0], sr=('x','y','z'))
        #scale constrain ctrl to jnt
        mc.scaleConstraint(ik_clav_ctrl_list[0], ikJoint_list[0])
        # lock and hide rotation values for clav control
        mc.setAttr((ik_clav_ctrl_list[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_clav_ctrl_list[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_clav_ctrl_list[0] + '.rz'), lock=True, keyable=False, channelBox=False)

        # ____________________ grp ik shldr under ik clav___________________#
        mc.parent(ik_shldr_group_list[0], ik_clav_ctrl_list[0])

        
        #__________________________________________________________#
        #___________ik Clavicle (single chain solver)______________#
        #__________________________________________________________#

        #create single chain ikHandle for clavicle________
        clavicle_ikHandle = mc.ikHandle(n=direction + '_ikHndl_clv',sj=ikJoint_list[0], ee=ikJoint_list[1], sol='ikSCsolver')
        
        mc.setAttr((clavicle_ikHandle[0] + '.poleVectorX'), 0)
        mc.setAttr((clavicle_ikHandle[0] + '.poleVectorY'), 0)
        mc.setAttr((clavicle_ikHandle[0] + '.poleVectorZ'), 0)
        #rename ik effector
        clavicle_ikHandle_effector = mc.listConnections(clavicle_ikHandle, s=True, type='ikEffector')
        mc.rename(clavicle_ikHandle_effector, 'effector_' + direction + '_arm')
        #group ik handle
        clvGrp = mc.group(em=True)
        clvGrp = mc.rename(clvGrp, clavicle_ikHandle[0] + '_grp')
        clvGrp_const = mc.parentConstraint(clavicle_ikHandle[0], clvGrp)
        mc.delete(clvGrp_const)
        mc.parent(clavicle_ikHandle[0], clvGrp)
        
        #_____________________ik Clavicle Stretch (single chain solver)___________________________#
        clavicle_var_loc = mc.spaceLocator(n=ikJoint_list[0] + '_locator')
        upperArm1_var_loc = mc.spaceLocator(n=ikJoint_list[1] + '_locator')
        #***was getting "cycle" glitch for parentConstraining clavicle locator instead of pointConstraining
        mc.pointConstraint(ikJoint_list[0], clavicle_var_loc)
        mc.pointConstraint(clavicle_ikHandle[0], upperArm1_var_loc)
        clv_measerTool = mc.distanceDimension(clavicle_var_loc, upperArm1_var_loc)
        clv_measerTool_parent = mc.listRelatives(clv_measerTool, p=True)
        clv_measerTool_parent = mc.rename(clv_measerTool_parent, ('distanceDimension_' + ikJoint_list[0]))

        # scale offset multDiv node
        clav_scale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_clav_scale_off' )
        # set operation to divide
        mc.setAttr( clav_scale_off + '.operation', 2)

        # connect global ctrl scale X to scale offset
        # _____create expression to multiply all scaling offset ctrls together____#
        # spine ctrls for scale offset
        clav_exp_str = ''
        for ctrl in to_chest_ctrl:
            clav_exp_str = clav_exp_str + (ctrl + '.scaleX * ')

        #mc.connectAttr( (global_ctrl + '.scaleX'), (fk_globalScale_off + '.input2X'), f=True )
        mc.expression( s = clav_scale_off + '.input2X = ' + clav_exp_str + global_ctrl + '.scaleX' )
        
        if direction == 'left':
            mc.connectAttr(clv_measerTool_parent + '.distance', clav_scale_off + '.input1X')
        elif direction == 'right':
            # (right) invert to negative translate X (since x is up the chain instead of down the chain)
            clav_invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_clav_invert_value' )
            mc.setAttr( (clav_invert_value + '.input2X'), -1 )
            mc.connectAttr( (clv_measerTool_parent + '.distance'), (clav_invert_value + '.input1X'), f=True)
            mc.connectAttr( (clav_invert_value + '.outputX') , clav_scale_off + '.input1X')

        #connect scale offset to tranlate x of shldr jnt
        mc.connectAttr( (clav_scale_off + '.outputX') , ikJoint_list[1] + '.translateX')

        # create grp for ctrls and measure tool for organization
        clv_measerTool_grp = mc.group(em = True, n= direction + '_clav_measure_grp')
        mc.parent(clv_measerTool_parent, clavicle_var_loc, upperArm1_var_loc, clv_measerTool_grp)

        
        #____________parenting ik shoulder ctrl__________________#
        # parent constrain shldr joint translation to single solver ik handle grp
        mc.parentConstraint(ik_shldr_ctrl_list[0], clvGrp, sr=('x','y','z'))
        #scale constrain ctrl to shldr jnt
        mc.scaleConstraint(ik_shldr_ctrl_list[0], ikJoint_list[1])
        # lock and hide rotation values for shldr control
        mc.setAttr((ik_shldr_ctrl_list[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_shldr_ctrl_list[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_shldr_ctrl_list[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        

        #_________________POLE VECTOR Start___________________#
        #_____________________________________________________#
        pv_group_list = []
        pv_ctrl_list = []
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
            

            #___more accurate mid point (for 'hip_to_wrist_scaled')___
            #length of whole limb (tran X of elbow and wrist)
            limb_lenA = (   mc.getAttr(ikJoint_list[2] + '.tx') + 
                            mc.getAttr(ikJoint_list[3] + '.tx') )

            #length of upper half of limb (tran X of elbow)
            upperLimb_lenA = mc.getAttr(ikJoint_list[2] + '.tx')

            #divide sum of arm lengths by upper arm length (for more accurate mid point)
            better_midPoint_var = ( limb_lenA / upperLimb_lenA )  

            #__vector math____#
            #vector positions of hip, elbow, wrist
            shldr_pos = om.MVector(mc.xform(ikJoint_list[1], q=True, rp=True, ws=True))
            elbow_pos = om.MVector(mc.xform(ikJoint_list[2], q=True, rp=True, ws=True))
            wrist_pos = om.MVector(mc.xform(ikJoint_list[3], q=True, rp=True, ws=True))

            #finding vector point of pv elbow (on plane of hip, elbow, wrist)
            hip_to_wrist = wrist_pos - shldr_pos
            hip_to_wrist_scaled = hip_to_wrist / better_midPoint_var #/two-ish
            mid_point = shldr_pos + hip_to_wrist_scaled
            mid_point_to_elbow_vec = elbow_pos - mid_point
            mid_point_to_elbow_vec_scaled = mid_point_to_elbow_vec * elbow_dist_mult  #pv ctrl distance from elbow multiplier
            mid_point_to_elbow_point = mid_point + mid_point_to_elbow_vec_scaled

            #final polve vector point (to avoid elbow changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_elbow_point)

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

            # connect scale of elbow and pole vector control (scale constraint creates cyclical error)
            mc.connectAttr( (myCurve + '.scale'), ( ikJoint_list[2] ) + '.scale', f=True)

            pv_group_list.append(myGroup)
            pv_ctrl_list.append(myCurve)

        
        #______________________________________________________________________________#
        #____________________________IK/ FK Switch Ctrl _______________________________#
        #______________________________________________________________________________#

        switch_ctrl_list = []
        switch_ctrl_grp_list = []
        for i in range(0,1):
            #name circle curves
            if direction == 'left':
                switchCurveA_name = 'l_armSwch_ctrl'
                switchCurveB_name = 'l_armSwch_ctrlA'
                switchCurveC_name = 'l_armSwch_ctrlB'
            if direction == 'right':
                switchCurveA_name = 'r_armSwch_ctrl'
                switchCurveB_name = 'r_armSwch_ctrlA'
                switchCurveC_name = 'r_armSwch_ctrlB'

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

            #_______move joint to wrist and parent_______#
            #parent and zero joints to last joint in selection
            mc.parent(switchCurveA_grp, main_arm_jnts[-1], relative=True)
            #parent joints to world space
            mc.Unparent(switchCurveA_grp)

            # parent and scale constrain switch ctrl to wrist
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
            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0) ###
            mc.setAttr((ik_group_list[0] + '.visibility'), 1)
            mc.setAttr((pv_group_list[0] + '.visibility'), 1)
            mc.setAttr((ik_shldr_group_list[0] + '.visibility'), 1)
            mc.setAttr((ik_clav_group_list[0] + '.visibility'), 1)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)

            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_shldr_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_clav_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1) ###
            mc.setAttr((ik_group_list[0] + '.visibility'), 0)
            mc.setAttr((pv_group_list[0] + '.visibility'), 0)
            mc.setAttr((ik_shldr_group_list[0] + '.visibility'), 0)
            mc.setAttr((ik_clav_group_list[0] + '.visibility'), 0)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)

            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_shldr_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_clav_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
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


        #_____________________________________________________________________________#
        #____________________________ Twist Jnts______________________________________#
        #_____________________________________________________________________________#

        #_____ start twist joint_____#
        
        #create joint at elbow
        arm_startTwist_jnt = mc.joint(main_arm_jnts[2], n=direction + '_startTwistJnt_arm', rad=7)
        mc.Unparent(arm_startTwist_jnt)
        #color joint
        mc.setAttr(arm_startTwist_jnt + '.overrideEnabled', 1)
        mc.setAttr(arm_startTwist_jnt + '.overrideRGBColors', 1)
        mc.setAttr(arm_startTwist_jnt + '.overrideColorRGB', 0, 0, 0)
        #mc.parent(arm_startTwist_jnt, main_arm_jnts[2])
        mc.parentConstraint(main_arm_jnts[2], arm_startTwist_jnt)
        #mc.scaleConstraint(main_arm_jnts[2], arm_startTwist_jnt)
        mc.setAttr( arm_startTwist_jnt + '.segmentScaleCompensate', 0 )


        #_____end twist joint_____
        #create joint at elbow
        arm_endTwist_jnt = mc.joint(main_arm_jnts[3], n=direction + '_endTwistJnt_arm', rad=7)
        mc.Unparent(arm_endTwist_jnt)
        #color joint
        mc.setAttr(arm_endTwist_jnt + '.overrideEnabled', 1)
        mc.setAttr(arm_endTwist_jnt + '.overrideRGBColors', 1)
        mc.setAttr(arm_endTwist_jnt + '.overrideColorRGB', 0, 0, 0)
        #parent constrain to ik wrist ctrl
        mc.parentConstraint(main_arm_jnts[3], arm_endTwist_jnt)
        #mc.scaleConstraint(main_arm_jnts[3], arm_endTwist_jnt)
        #parent constrain to fk wrist ctrl
        mc.setAttr( arm_endTwist_jnt + '.segmentScaleCompensate', 0 )

        
        #_______create arm mid twist joints_______

        arm_twist_list = []

        for i in foreArm_jnts:
            #i_betterName = str(i[0])
            #prefix_betterName = str(skel_pre_var_list[0])
            #create twist joint
            mc.joint()
            #joint visual size
            mc.setAttr('.radius', 3)
            #joint color
            mc.setAttr('.overrideEnabled', 1)
            mc.setAttr('.overrideRGBColors', 1)
            mc.setAttr('.overrideColorRGB', 1, 1, 1)
            #rename joint
            #newName = i_betterName.replace(i, twistSkelPrefix)
            myJnt = mc.rename('twist_' + i)
            #parent and zero joints to arm_list
            mc.parent(myJnt, i, relative=True)
            #parent joints to world space
            mc.Unparent(myJnt)
            arm_twist_list.append(myJnt)
            # avoid double global scale
            mc.setAttr( i + '.segmentScaleCompensate', 0 )
            mc.setAttr( myJnt + '.segmentScaleCompensate', 0 )

        # scale constrain elbow fk to first twist joint (for proper twist scaling)
        # for fk
        mc.scaleConstraint(fk_ctrl_list[2], arm_twist_list[0])
        # for ik
        mc.scaleConstraint(pv_ctrl_list[0], arm_twist_list[0])

        #parent FK joints together based on current index
        currentIndex = -1
        for i in arm_twist_list:
            currentIndex += 1
            if i != arm_twist_list[0]:
                mc.parent(arm_twist_list[currentIndex], arm_twist_list[currentIndex-1])
        
        #parent twist spline joints to twist main joints
        for i_twist, i_foreArm in itertools.izip(arm_twist_list, foreArm_jnts):
            # first and last forearm are already constrained/ parented
            if i_twist != arm_twist_list[0] and i_twist != arm_twist_list[-1]:
                if i_foreArm != foreArm_jnts[0] and i_foreArm != foreArm_jnts[-1]:
                    #mc.connectAttr(i_twist + '.rotate', i_foreArm + '.rotate')
                    #mc.connectAttr(i_twist + '.translate', i_foreArm + '.translate')
                    mc.parentConstraint(i_twist, i_foreArm)
                    mc.scaleConstraint(i_twist, i_foreArm)
        
        
        # scale constraint switch
        # twist elbow, fk elbow ctrl and ik pole vector ctrl
        # 1 is fk, 0 is ik
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
        # alternative is to disconnect/ unlock and use '.target[0].targetWeight'
        mc.setAttr( (arm_twist_list[0] + '_scaleConstraint1.' + fk_ctrl_list[2] + 'W0'),  0)
        mc.setAttr( (arm_twist_list[0] + '_scaleConstraint1.' + pv_ctrl_list[0] + 'W1'),  1)

        mc.setDrivenKeyframe((arm_twist_list[0] + '_scaleConstraint1.' + fk_ctrl_list[2] + 'W0'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((arm_twist_list[0] + '_scaleConstraint1.' + pv_ctrl_list[0] + 'W1'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))

        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
        mc.setAttr( (arm_twist_list[0] + '_scaleConstraint1.' + fk_ctrl_list[2] + 'W0'),  1)
        mc.setAttr( (arm_twist_list[0] + '_scaleConstraint1.' + pv_ctrl_list[0] + 'W1'),  0)

        mc.setDrivenKeyframe((arm_twist_list[0] + '_scaleConstraint1.' + fk_ctrl_list[2] + 'W0'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((arm_twist_list[0]+ '_scaleConstraint1.' + pv_ctrl_list[0] + 'W1'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
    
        
        
        #__________________create IK SPLINE for arm TWIST__________________
        #create simple curve
        twistStart_pos = mc.xform(arm_startTwist_jnt,q=1,ws=1,rp=1)
        twistEnd_pos = mc.xform(arm_endTwist_jnt,q=1,ws=1,rp=1)
        twistCurve = mc.curve(d=1, p=[twistStart_pos, twistEnd_pos])
        #create ik spline
        arm_twist_ikHandle = mc.ikHandle(   n=direction + '_ikHandle_arm_twist',
                                            sj=arm_twist_list[0],
                                            ee=arm_twist_list[-1],
                                            sol='ikSplineSolver', 
                                            ccv=False, 
                                            c=twistCurve )
        #set pole vectors to 0 to be clean (probably unesaccary)
        mc.setAttr((arm_twist_ikHandle[0] + '.poleVectorX'), 0)
        mc.setAttr((arm_twist_ikHandle[0] + '.poleVectorY'), 0)
        mc.setAttr((arm_twist_ikHandle[0] + '.poleVectorZ'), 0)
        #rename ik spline effector and curve
        arm_ikHandle_effector = mc.listConnections(arm_twist_ikHandle, s=True, type='ikEffector')
        arm_ikHandle_curve = mc.listConnections(arm_twist_ikHandle, s=True, type='nurbsCurve')
        arm_ikHandle_effector_newName = mc.rename(arm_ikHandle_effector, direction + '_effector_arm_twist')
        arm_ikHandle_curve_newName = mc.rename(arm_ikHandle_curve, direction + '_curve_arm_twist')
        #set up advanced twist controls for ik spline 
        mc.setAttr(arm_twist_ikHandle[0] + '.dTwistControlEnable', 1)
        mc.setAttr(arm_twist_ikHandle[0] + '.dWorldUpType', 4)
        mc.setAttr(arm_twist_ikHandle[0] + '.dWorldUpAxis', 4)
        # switch forward axis X to negative for right side (default is posative X)
        if direction == 'right':
            mc.setAttr(arm_twist_ikHandle[0] + '.dForwardAxis', 1)

        mc.setAttr(arm_twist_ikHandle[0] + '.dWorldUpVector', 0, 0, -1)
        mc.setAttr(arm_twist_ikHandle[0] + '.dWorldUpVectorEnd', 0, 0, -1)
        mc.connectAttr(arm_startTwist_jnt + '.worldMatrix[0]', arm_twist_ikHandle[0] + '.dWorldUpMatrix')
        mc.connectAttr(arm_endTwist_jnt + '.worldMatrix[0]', arm_twist_ikHandle[0] + '.dWorldUpMatrixEnd')
        #_____skin start and end joints to ik spline curve_____# (parenting twist jnts to start/end jnts)
        mc.skinCluster(arm_startTwist_jnt, arm_endTwist_jnt, arm_ikHandle_curve_newName, n= direction + '_skinCluster_arm_twist')
        #RENAME twist curve TWEAK node
        arm_ikHandle_curve_newName_shape = mc.listRelatives(arm_ikHandle_curve_newName, s=True)
        arm_twist_curve_tweak = mc.listConnections(arm_ikHandle_curve_newName_shape, s=True, type='tweak')
        mc.rename(arm_twist_curve_tweak, direction + '_tweak_arm_twist')
        
        
        # ______________________________________________________#
        # __________________ IK stretchy arm ___________________#
        # ______________________________________________________#

        # get joint x lengths
        to_elbow_len = mc.getAttr(ikJoint_list[2] + '.tx')
        to_wrist_len = mc.getAttr(ikJoint_list[-1] + '.tx')
        # create ruler tool
        ik_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
        ik_jnt_ruler = mc.rename(ik_jnt_ruler_temp, ( direction + '_ikArm_jnt_rulerShape' ) )
        # rename transform parent of distanceDimesion tool
        ruler_loc_list_rel = mc.listRelatives( ik_jnt_ruler, ap=1, type='transform' )
        ruler_loc_list_parent = mc.rename(ruler_loc_list_rel, direction + '_ikArm_jnt_ruler')

        # get locators controling length
        ruler_loc_list = mc.listConnections( ik_jnt_ruler, type='locator' )
        # rename and hide distance locators
        arm_loc_0 = mc.rename(ruler_loc_list[0], direction + '_shlder_dist_loc')
        arm_loc_1 = mc.rename(ruler_loc_list[1], direction + '_wrist_dist_loc')
        # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
        mc.pointConstraint(ikJoint_list[1], arm_loc_0 )  #ik_shldr_ctrl_list[0]
        mc.pointConstraint(ik_ctrl_list[0], arm_loc_1 )   #ik_ctrl_list[0]
        
        # make nodes for stretchy limb
        arm_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikArm_dist_ratio' )
        # set mulDiv node to Divide
        mc.setAttr(arm_dist_ratio + '.operation', 2)

        # global scale offset multDiv node
        globalScale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikArm_globalScale_off' )
        # operation to divide
        mc.setAttr(globalScale_off + '.operation', 2)
        # create mult/div nodes for ratio * length
        ratio_elbow_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_elbow_mult' )
        ratio_wrist_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_wrist_mult' )
        #create condition nodes for if greater than length, to prevent negative stretching
        #set operation to 'greater than'
        elbow_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_elbow_len_con' )
        wrist_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_wrist_len_con' )
        #set operation to 'greater than'
        if direction == 'left':
            mc.setAttr(elbow_len_con + '.operation', 2)
            mc.setAttr(wrist_len_con + '.operation', 2)
        #set operation to 'less than'
        elif direction == 'right':
            mc.setAttr(elbow_len_con + '.operation', 4)
            mc.setAttr(wrist_len_con + '.operation', 4)
        
        # connect arm distance to global scale offset
        mc.connectAttr( (ik_jnt_ruler + '.distance'), (globalScale_off + '.input1X'), f=True )
        # connect global ctrl scale X to global scale offset
        mc.connectAttr( (global_ctrl + '.scaleX'), (globalScale_off + '.input2X'), f=True )

        # connect ruler distance over total distance of joints
        if direction == 'left':
            mc.connectAttr( (globalScale_off + '.outputX'), (arm_dist_ratio + '.input1X'), f=True )
        elif direction == 'right':
            # (right) invert to negative translate X (since x is up the chain instead of down the chain)
            invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikArm_invert_value' )
            mc.setAttr( (invert_value + '.input2X'), -1 )
            mc.connectAttr( (globalScale_off + '.outputX'), (invert_value + '.input1X'), f=True )
            mc.connectAttr( (invert_value + '.outputX'), (arm_dist_ratio + '.input1X'), f=True )

        # ARM stretch only, twist stretch below
        #___________ik arm stretch scale normalize____________#
        forearm_len_prc = ( (to_wrist_len) / (to_elbow_len + to_wrist_len) )
        # ik arm ctrl scale offset (b/c of fk spine ctrls)
        ik_exp_str = ''
        for ctrl in to_chest_ctrl:
            ik_exp_str = ik_exp_str + (ctrl + '.scaleX * ')
        # must create expression to account for offset of elbow and wrist length when scaling
        # soft ik, a little less than total length to keep some bend in elbow joint
        mc.expression ( s = arm_dist_ratio + '.input2X =' + str( (to_elbow_len + to_wrist_len) * 0.994 ) + ' *' + 
                        ik_exp_str + 
                        '(1 +' '( ( (' + pv_ctrl_list[0] + '.scaleX) - 1) *' + str(forearm_len_prc) + ') ) * ' +
                        # pv_ctrl_list[0] + '.scaleX *' +
                        ik_shldr_ctrl_list[0] + '.scaleX *' +
                        ik_clav_ctrl_list[0] + '.scaleX' )

        #__________________________#


        # connect length ratio to apply to x length of elbow and wrist (fraction * distance)
        mc.connectAttr( (arm_dist_ratio + '.outputX'), (ratio_elbow_mult + '.input2X'), f=True )
        mc.connectAttr( (arm_dist_ratio + '.outputX'), (ratio_wrist_mult + '.input2X'), f=True )
        # joint length to input 1X
        mc.setAttr( (ratio_elbow_mult + '.input1X'), to_elbow_len )
        mc.setAttr( (ratio_wrist_mult + '.input1X'), to_wrist_len )

        # connect mult ratio nodes to condition node (if length greater, then stretch)
        mc.connectAttr( (ratio_elbow_mult + '.outputX'), (elbow_len_con + '.colorIfTrueR'), f=True )
        mc.connectAttr( (ratio_elbow_mult + '.outputX'), (elbow_len_con + '.firstTerm'), f=True )

        mc.connectAttr( (ratio_wrist_mult + '.outputX'), (wrist_len_con + '.colorIfTrueR'), f=True )
        mc.connectAttr( (ratio_wrist_mult + '.outputX'), (wrist_len_con + '.firstTerm'), f=True )

        # add joint lengths to base value, if false
        mc.setAttr( (elbow_len_con + '.colorIfFalseR'), to_elbow_len )
        mc.setAttr( (elbow_len_con + '.secondTerm'), to_elbow_len )

        mc.setAttr( (wrist_len_con + '.colorIfFalseR'), to_wrist_len )
        mc.setAttr( (wrist_len_con + '.secondTerm'), to_wrist_len )

        #connect stretch lengths to joint translate x
        mc.connectAttr( (elbow_len_con + '.outColorR'), (ikJoint_list[2] + '.tx'), f=True )
        mc.connectAttr( (wrist_len_con + '.outColorR'), (ikJoint_list[-1] + '.tx'), f=True )
        


        # ______________________________________________________#
        # __________________ ik twist stretch ___________________#
        # ______________________________________________________#
        
        # create ruler tool
        ikTwst_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
        ikTwst_jnt_ruler = mc.rename(ikTwst_jnt_ruler_temp, ( direction + '_ikTwst_jnt_rulerShape' ) )
        # rename transform parent of distanceDimesion tool
        ikTwst_ruler_loc_list_rel = mc.listRelatives( ikTwst_jnt_ruler, ap=1, type='transform' )
        ikTwst_ruler_loc_list_parent = mc.rename(ikTwst_ruler_loc_list_rel, direction + '_ikTwst_jnt_ruler')

        # get locators controling length
        ikTwst_ruler_loc_list = mc.listConnections( ikTwst_jnt_ruler, type='locator' )
        # rename and hide distance locators
        ikTwst_arm_loc_0 = mc.rename(ikTwst_ruler_loc_list[0], direction + '_ikTwst_elbow_dist_loc')
        ikTwst_arm_loc_1 = mc.rename(ikTwst_ruler_loc_list[1], direction + '_ikTwst_wrist_dist_loc')
        # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
        mc.pointConstraint(ikJoint_list[2], ikTwst_arm_loc_0 )
        mc.pointConstraint(ik_ctrl_list[0], ikTwst_arm_loc_1 )
        
        # make node for stretchy limb
        ikTwst_arm_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikTwst_arm_dist_ratio' )
        # set mulDiv node to Divide
        mc.setAttr(ikTwst_arm_dist_ratio + '.operation', 2)
        # global scale offset multDiv node
        ikTwst_globalScale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikTwst_arm_globalScale_off' )
        # operation to divide
        mc.setAttr(ikTwst_globalScale_off + '.operation', 2)
        
        # connect arm distance to global scale offset
        mc.connectAttr( (ikTwst_jnt_ruler + '.distance'), (ikTwst_globalScale_off + '.input1X'), f=True )

        
        # connect global ctrl scale X to global scale offset
        # _____create expression to multiply all scaling offset ctrls together____#
        # ikTwst arm scale offset spine ctrls
        ikTwst_exp_str = ''
        for ctrl in to_chest_ctrl:
            ikTwst_exp_str = ikTwst_exp_str + (ctrl + '.scaleX * ')
        mc.expression(  s = ikTwst_globalScale_off + '.input2X = ' + global_ctrl + '.scaleX * ' + 
                        pv_ctrl_list[0] + '.scaleX' )


        # connect ruler distance over total distance of joints
        if direction == 'left':
            mc.connectAttr( (ikTwst_globalScale_off + '.outputX'), (ikTwst_arm_dist_ratio + '.input1X'), f=True )
        elif direction == 'right':
            # (right) invert to negative translate X (since x is up the chain instead of down the chain)
            ikTwst_invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ikTwst_arm_invert_value' )
            mc.setAttr( (ikTwst_invert_value + '.input2X'), -1 )
            mc.connectAttr( (ikTwst_globalScale_off + '.outputX'), (ikTwst_invert_value + '.input1X'), f=True )
            mc.connectAttr( (ikTwst_invert_value + '.outputX'), (ikTwst_arm_dist_ratio + '.input1X'), f=True )

        # soft ik, a little less than total length to keep some bend in elbow joint
        mc.setAttr( (ikTwst_arm_dist_ratio + '.input2X'), to_wrist_len )
        
        #_____________ikTwst_ twist stretch___________#
        ikTwst_ratio_mult_ls = []
        for i in arm_twist_list:
            if i != arm_twist_list[0]:
                # length of joint
                ikTwst_to_len = mc.getAttr(i + '.tx')
                # create mult/div nodes for ratio * length
                ikTwst_ratio_mult = mc.shadingNode('multiplyDivide', asUtility=True, n= direction + '_' + i + '_ikTwst_ratio_mult' )
                #create condition nodes for if greater than length, to prevent negative stretching

                # connect length ratio to apply to x length of elbow and wrist (fraction * distance)
                mc.connectAttr( (ikTwst_arm_dist_ratio + '.outputX'), (ikTwst_ratio_mult + '.input2X'), f=True )
                # joint length to input 1X
                mc.setAttr( (ikTwst_ratio_mult + '.input1X'), ikTwst_to_len )

                # append twist condition to join with blendshape
                ikTwst_ratio_mult_ls.append(ikTwst_ratio_mult)


        
        # ______________________________________________________#
        # __________________ fk stretchy arm ___________________#
        # ______________________________________________________#
        
        # create ruler tool
        fk_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
        fk_jnt_ruler = mc.rename(fk_jnt_ruler_temp, ( direction + '_fk_jnt_rulerShape' ) )
        # rename transform parent of distanceDimesion tool
        fk_ruler_loc_list_rel = mc.listRelatives( fk_jnt_ruler, ap=1, type='transform' )
        fk_ruler_loc_list_parent = mc.rename(fk_ruler_loc_list_rel, direction + '_fk_jnt_ruler')

        # get locators controling length
        fk_ruler_loc_list = mc.listConnections( fk_jnt_ruler, type='locator' )
        # rename and hide distance locators
        fk_arm_loc_0 = mc.rename(fk_ruler_loc_list[0], direction + '_fk_elbow_dist_loc')
        fk_arm_loc_1 = mc.rename(fk_ruler_loc_list[1], direction + '_fk_wrist_dist_loc')
        # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
        mc.parentConstraint(fk_ctrl_list[2], fk_arm_loc_0 )
        mc.parentConstraint(fk_ctrl_list[-1], fk_arm_loc_1 )
        
        # make node for stretchy limb
        fk_arm_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_fk_arm_dist_ratio' )
        # set mulDiv node to Divide
        mc.setAttr(fk_arm_dist_ratio + '.operation', 2)
        # global scale offset multDiv node
        fk_globalScale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_fk_arm_globalScale_off' )
        # operation to divide
        mc.setAttr(fk_globalScale_off + '.operation', 2)
        
        # connect arm distance to global scale offset
        mc.connectAttr( (fk_jnt_ruler + '.distance'), (fk_globalScale_off + '.input1X'), f=True )

        # connect global ctrl scale X to global scale offset
        # _____create expression to multiply all scaling offset ctrls together____#
        # fk arm scale offset spine ctrls
        fk_exp_str = ''
        for ctrl in to_chest_ctrl:
            fk_exp_str = fk_exp_str + (ctrl + '.scaleX * ')
        mc.expression(  s = fk_globalScale_off + '.input2X = ' + global_ctrl + '.scaleX * ' + 
                        fk_exp_str +
                        fk_ctrl_list[0] + '.scaleX * ' + 
                        fk_ctrl_list[1] + '.scaleX * ' +
                        fk_ctrl_list[2] + '.scaleX' )

        # connect ruler distance over total distance of joints
        if direction == 'left':
            mc.connectAttr( (fk_globalScale_off + '.outputX'), (fk_arm_dist_ratio + '.input1X'), f=True )
        elif direction == 'right':
            # (right) invert to negative translate X (since x is up the chain instead of down the chain)
            fk_invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_fk_arm_invert_value' )
            mc.setAttr( (fk_invert_value + '.input2X'), -1 )
            mc.connectAttr( (fk_globalScale_off + '.outputX'), (fk_invert_value + '.input1X'), f=True )
            mc.connectAttr( (fk_invert_value + '.outputX'), (fk_arm_dist_ratio + '.input1X'), f=True )

        # soft ik, a little less than total length to keep some bend in elbow joint
        mc.setAttr( (fk_arm_dist_ratio + '.input2X'), to_wrist_len )
        
        #_____________fk twist stretch___________#
        fk_ratio_mult_ls = []
        for i in arm_twist_list:
            if i != arm_twist_list[0]:
                # length of joint
                fk_to_len = mc.getAttr(i + '.tx')
                # create mult/div nodes for ratio * length
                fk_ratio_mult = mc.shadingNode('multiplyDivide', asUtility=True, n= direction + '_' + i + '_fk_ratio_mult' )
                #create condition nodes for if greater than length, to prevent negative stretching
                
                # connect length ratio to apply to x length of elbow and wrist (fraction * distance)
                mc.connectAttr( (fk_arm_dist_ratio + '.outputX'), (fk_ratio_mult + '.input2X'), f=True )
                # joint length to input 1X
                mc.setAttr( (fk_ratio_mult + '.input1X'), fk_to_len )

                # append twist condition to join with blendshape
                fk_ratio_mult_ls.append(fk_ratio_mult)

        
        # blend color twist condition switching
        blendClr_con_list = []
        #blend joints together
        # arm_twist_list[1:] b/c first uneeded jnt already removed from other lists
        for fk_ratio, ikTwst_ratio, twst_jnt in itertools.izip(fk_ratio_mult_ls, ikTwst_ratio_mult_ls, arm_twist_list[1:]):
            #create blend color nodes
            blnd_clrs_con = mc.createNode('blendColors', n= twst_jnt + '_blnd_clrs_con')
            #connect twist blend color nodes to children
            mc.connectAttr((fk_ratio + '.outputX'), (blnd_clrs_con + '.color1R'), f=True)
            mc.connectAttr((ikTwst_ratio + '.outputX'), (blnd_clrs_con + '.color2R'), f=True)
            mc.connectAttr((blnd_clrs_con + '.outputR'), (twst_jnt + '.translateX'), f=True)

            #append lists for outside loop use
            blendClr_con_list.append(blnd_clrs_con)

        #_______connect switch control to blendNodes for twist ik vs fk length_______#
        for blendClr in blendClr_con_list :
            mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (blendClr + '.blender'), f=True)
        
        
        #_________________________________________________________#
        #______________________ FINGERs___________________________#
        #_________________________________________________________#

        #______________ Hand Grp_______________________#
        #______________________________________________#

        hand_grp_list = []
        hand_grp_offset_list = []

        for jnt in [main_arm_jnts[-1]]:
            #group
            myGroup_offset = mc.group(em=True)
            myGroup = mc.group(myGroup_offset)
            #rename group
            myGroup = mc.rename(myGroup, (direction + '_hand_grp'))
            myGroup_offset = mc.rename(myGroup_offset, (direction + '_hand_grp_offset'))
            #parent and zero curveGrp to leg_fk_list
            mc.parent(myGroup, jnt, relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(myGroup)
            #add variable to list to access outside of loop
            hand_grp_list.append(myGroup)
            hand_grp_offset_list.append(myGroup_offset)

        # constrain hand group to hand jnt
        mc.parentConstraint(main_arm_jnts[-1], hand_grp_list[0])
        mc.scaleConstraint(main_arm_jnts[-1], hand_grp_list[0])


        #______________ Create Fingers _______________________#
        #_____________________________________________________#
        # finger fk chain and parent to hand grp

        finger_jnt_lists_temp = find_jnts.find_jnts()
        finger_jnt_lists = finger_jnt_lists_temp.find_finger_jnts(direction)

        # 5 colors for 5 fingers
        # cycle through finger jnt lists and create fk chain parented to hand grp
        for jnt_list in finger_jnt_lists:
            current_index = finger_jnt_lists.index(jnt_list)
            finger_ctrl_list = fk_chain.fk_chain()
            finger_ctrl_list.fk_chain(  jnt_chain = jnt_list, 
                                        parent_to = hand_grp_offset_list[0],
                                        ctrl_type='circle',
                                        size=0.5, 
                                        color_r=1, 
                                        color_g=1, 
                                        color_b=0 )

        
        #_______________________________________________________________#
        #__________________visibility, grouping_________________________#
        #_______________________________________________________________#
        # hide dist loc and tool
        mc.setAttr(ruler_loc_list_parent + '.visibility', 0)
        mc.setAttr(arm_loc_0 + '.visibility', 0)
        mc.setAttr(arm_loc_1 + '.visibility', 0)
        # hide ik handle
        mc.setAttr(ikHandle_var[0] + '.visibility', 0)
        # hide ik twist measure tool and locators
        mc.setAttr(ikTwst_ruler_loc_list_parent + '.visibility', 0)
        mc.setAttr(ikTwst_arm_loc_0 + '.visibility', 0)
        mc.setAttr(ikTwst_arm_loc_1 + '.visibility', 0)
        # hide arm twst ik handle
        mc.setAttr(arm_twist_ikHandle[0] + '.visibility', 0)
        mc.setAttr(arm_ikHandle_curve_newName + '.visibility', 0)
        # hide dist loc and tool
        mc.setAttr(fk_ruler_loc_list_parent + '.visibility', 0)
        mc.setAttr(fk_arm_loc_0 + '.visibility', 0)
        mc.setAttr(fk_arm_loc_1 + '.visibility', 0)
        # hide clavicle measure tool, locators, ik handle
        mc.setAttr(clv_measerTool_parent + '.visibility', 0)
        mc.setAttr(clavicle_var_loc[0] + '.visibility', 0)
        mc.setAttr(upperArm1_var_loc[0] + '.visibility', 0)
        mc.setAttr(clv_measerTool_grp + '.visibility', 0)
        mc.setAttr(clvGrp + '.visibility', 0)
        mc.setAttr(clavicle_ikHandle[0] + '.visibility', 0)
        # hide twist jnts
        mc.setAttr(arm_startTwist_jnt + '.visibility', 0)
        mc.setAttr(arm_endTwist_jnt + '.visibility', 0)
        mc.setAttr(arm_twist_list[0] + '.visibility', 0)
        #parent grp to global grp to organize
        mc.parent(ruler_loc_list_parent, myArmGrp)
        mc.parent(arm_loc_0, myArmGrp)
        mc.parent(arm_loc_1, myArmGrp)
        # default arm to ik
        mc.setAttr(switch_ctrl_list[0] + '.fk_ik_blend', 0)

        
        #parent under my ik grp
        mc.parent(  clvGrp,
                    hand_grp_list,
                    switch_ctrl_grp_list[0],
                    clv_measerTool_grp,
                    arm_startTwist_jnt,
                    arm_endTwist_jnt,
                    arm_twist_list[0],
                    arm_ikHandle_curve_newName,
                    arm_twist_ikHandle[0],
                    ikTwst_arm_loc_0,
                    ikTwst_arm_loc_1,
                    ikTwst_ruler_loc_list_parent,
                    fk_arm_loc_0,
                    fk_arm_loc_1,
                    fk_ruler_loc_list_parent,
                    myArmGrp )

        # parent under global misc grp
        mc.parent(myArmGrp, global_misc_grp)

        #____________________________________________________________________________#
        #__________________chest ctrl/ global ctrl parenting_________________________#
        #____________________________________________________________________________#
        # parent ik clav, shlder, and fk clav to chest ctrl
        mc.parent(ik_clav_group_list[0], fk_ctrl_grp_list[0], to_chest_ctrl[-1])  # ik_shldr_group_list[0],
        #parent pole vector grp and wrist ik grp to global ctrl
        mc.parent(pv_group_list[0], ik_group_list[0], global_ctrl)


        # return top ik and fk controls to parent to chest ctrl (if needed, though done above)
        return  ik_clav_group_list[0], \
                ik_shldr_group_list[0], \
                fk_ctrl_grp_list[0], \
                                  \
                pv_group_list[0], \
                ik_group_list[0] 
                
        
        