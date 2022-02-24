import maya.cmds as mc

import maya.api.OpenMaya as om

import itertools

from ..ar_functions import find_jnts
from ..ar_functions import sel_joints

# find left hip joint

class leg_rig():

    def find_leg_jnts(self, direction):
        l_hip_var = find_jnts.find_jnts()

        l_hip_var_info = l_hip_var.l_r_hip_jnt(direction)

        find_leg_chain = sel_joints.sel_joints(l_hip_var_info[0])

        leg_chain = find_leg_chain.sel_jnt_chain()

        hip_jnt = l_hip_var_info[0]

        ankle_jnt = leg_chain[-2]

        return leg_chain, hip_jnt, ankle_jnt

    #reverse foot rig locators
    def rev_foot_locators( self, direction ):

        jnt_info = self.find_leg_jnts(direction)
        leg_chain = jnt_info[0]

        leg_chain_pos = []
        leg_chain_rot = []
        for i in leg_chain:
            #query translation
            i_pos = mc.xform(i, query=True, ws=True, t=True)
            #query rotation
            i_rot = mc.xform(i, query=True, ws=True, ro=True)
            leg_chain_pos.append(i_pos)
            leg_chain_rot.append(i_rot)

        ankle_jnt_pos = [leg_chain_pos[-2]][0]
        ankle_jnt_rot = [leg_chain_rot[-2]][0]

        toe_jnt_pos = [leg_chain_pos[-1]][0]
        toe_jnt_rot = [leg_chain_rot[-1]][0]
        #create ankle locator
        if mc.objExists(direction + '_loc_ankle') == False:
            loc_ankle = mc.spaceLocator(n = direction + '_loc_ankle')
            mc.setAttr((loc_ankle[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_ankle[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_ankle[0] + '.translate'), ankle_jnt_pos[0], ankle_jnt_pos[1], ankle_jnt_pos[2])
            mc.setAttr((loc_ankle[0] + '.rotate'), ankle_jnt_rot[0], ankle_jnt_rot[1], ankle_jnt_rot[2])
        else:
            print(direction + '_loc_ankle' + ' Already Exists!')
            mc.select(cl=True)
        #create toe locator
        if mc.objExists(direction + '_loc_toe') == False:
            loc_toe = mc.spaceLocator(n = direction + '_loc_toe')
            mc.setAttr((loc_toe[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe[0] + '.translate'), toe_jnt_pos[0], toe_jnt_pos[1], toe_jnt_pos[2])
            mc.setAttr((loc_toe[0] + '.rotate'), toe_jnt_rot[0], toe_jnt_rot[1], toe_jnt_rot[2])
        else:
            print(direction + '_loc_toe' + ' Already Exists!')
            mc.select(cl=True)

        if mc.objExists(direction + '_loc_toe_end') == False:
            loc_toe_end = mc.spaceLocator(n = direction + '_loc_toe_end')
            mc.setAttr((loc_toe_end[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe_end[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe_end[0] + '.translate'), toe_jnt_pos[0], 0, toe_jnt_pos[2])
            mc.setAttr((loc_toe_end[0] + '.rotate'), toe_jnt_rot[0], toe_jnt_rot[1], toe_jnt_rot[2])
            if direction == 'left':
                mc.move( 0, 16, 0, (loc_toe_end[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_toe_end[0] + '.ty'),  0)  #set at gound level
            if direction == 'right':
                mc.move( 0, -16, 0, (loc_toe_end[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_toe_end[0] + '.ty'),  0)  #set at gound level
        else:
            print(direction + '_loc_toe_end' + ' Already Exists!')
            mc.select(cl=True)

        if mc.objExists(direction + '_loc_heel') == False:
            loc_heel = mc.spaceLocator(n = direction + '_loc_heel')
            mc.setAttr((loc_heel[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_heel[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_heel[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_heel[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_heel[0] + '.translate'), ankle_jnt_pos[0], 0, ankle_jnt_pos[2])
            mc.setAttr((loc_heel[0] + '.rotate'), ankle_jnt_rot[0], ankle_jnt_rot[1], ankle_jnt_rot[2])
            if direction == 'left':
                mc.move( 0, -15, 0, (loc_heel[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_heel[0] + '.ty'),  0)  #set at gound level
            if direction == 'right':
                mc.move( 0, 15, 0, (loc_heel[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_heel[0] + '.ty'),  0) #set at gound level
        else:
            print(direction + '_loc_heel' + ' Already Exists!')
            mc.select(cl=True)

        if mc.objExists(direction + '_loc_outer_foot') == False:
            loc_outer_foot = mc.spaceLocator(n = direction + '_loc_outer_foot')
            mc.setAttr((loc_outer_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_outer_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_outer_foot[0] + '.translate'), toe_jnt_pos[0], 0, toe_jnt_pos[2])
            mc.setAttr((loc_outer_foot[0] + '.rotate'), toe_jnt_rot[0], toe_jnt_rot[1], toe_jnt_rot[2])
            if direction == 'left':
                mc.move( 0, 0, -15, (loc_outer_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_outer_foot[0] + '.ty'),  0)  #set at gound level
            if direction == 'right':
                mc.move( 0, 0, 15, (loc_outer_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_outer_foot[0] + '.ty'),  0)  #set at gound level
        else:
            print(direction + '_loc_outer_foot' + ' Already Exists!')
            mc.select(cl=True)

        if mc.objExists(direction + '_loc_inner_foot') == False:
            loc_inner_foot = mc.spaceLocator(n = direction + '_loc_inner_foot')
            mc.setAttr((loc_inner_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_inner_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_inner_foot[0] + '.translate'), toe_jnt_pos[0], 0, toe_jnt_pos[2])
            mc.setAttr((loc_inner_foot[0] + '.rotate'), toe_jnt_rot[0], toe_jnt_rot[1], toe_jnt_rot[2])
            if direction == 'left':
                mc.move( 0, 0, 15, (loc_inner_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_inner_foot[0] + '.ty'),  0)  #set at gound level
            if direction == 'right':
                mc.move( 0, 0, -15, (loc_inner_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_inner_foot[0] + '.ty'),  0)  #set at gound level
        else:
            print(direction + '_loc_inner_foot' + ' Already Exists!')
            mc.select(cl=True)




    def create_fk_ik_leg(self, direction, offset_parent_jnt, fk_ctrl_size, ik_ctrl_size, pv_ctrl_size, knee_dist_mult):
        jnt_info = self.find_leg_jnts(direction)
        leg_chain = jnt_info[0]
        leg_chain_no_foot = leg_chain[0:-1]
        hip_jnt = jnt_info[1]
        ankle_jnt = jnt_info[2]

        #______________________________#
        #_____Blended Joint Chain______#
        #______________________________#

        fkJoint_list = []
        ikJoint_list = []
        for i in leg_chain:
            #______________________#
            #____create FK chain___#
            fkJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 5)
            #joint color
            mc.setAttr('.overrideEnabled', 1)
            mc.setAttr('.overrideRGBColors', 1)
            mc.setAttr('.overrideColorRGB', 1, 0, 0.1)
            
            fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
            mc.Unparent(fkJoint)
            
            fkJoint_list.append(fkJoint)
            
            #______________________#
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
            print (currentIndex)
            if i != ikJoint_list[0]:
                mc.parent(ikJoint_list[currentIndex], ikJoint_list[currentIndex-1])
        
        #blend color node lists
        blendColorsTran_list = []
        blendColorsRot_list = []
        blendColorsScale_list = []
        #blend joints together
        for i_FK, i_IK, i in itertools.izip(fkJoint_list, ikJoint_list, leg_chain):
            #create blend color nodes
            blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
            blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
            blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')
            #translate
            mc.connectAttr((i_FK + '.translate'), (blendColorsTran + '.color1'), f=True)
            mc.connectAttr((i_IK + '.translate'), (blendColorsTran + '.color2'), f=True)
            mc.connectAttr((blendColorsTran + '.output'), (i + '.translate'), f=True)
            #rotate
            mc.connectAttr((i_FK + '.rotate'), (blendColorsRot + '.color1'), f=True)
            mc.connectAttr((i_IK + '.rotate'), (blendColorsRot + '.color2'), f=True)
            mc.connectAttr((blendColorsRot + '.output'), (i + '.rotate'), f=True)
            #scale
            mc.connectAttr((i_FK + '.scale'), (blendColorsScale + '.color1'), f=True)
            mc.connectAttr((i_IK + '.scale'), (blendColorsScale + '.color2'), f=True)
            mc.connectAttr((blendColorsScale + '.output'), (i + '.scale'), f=True)
            #append lists for outside loop use
            blendColorsTran_list.append(blendColorsTran)
            blendColorsRot_list.append(blendColorsRot)
            blendColorsScale_list.append(blendColorsScale)

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

            #parent constrain ctrls to fk jnts
            mc.parentConstraint(myCurve_name, i)

        
        #remove first and last of lists to correctly parent ctrls and grps together in for loop
        fk_ctrl_grp_list_temp = fk_ctrl_grp_list[1:]

        fk_ctrl_list_temp = fk_ctrl_list[:-1]


        #parent ctrls and grps together
        for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
            mc.parent(i_grp, i_ctrl)

        
        #_____________________________________#
        #______________IK Ctrls_______________#
        #_____________________________________#
        ikJoint_list_noFoot = ikJoint_list[0:-1]
        #group for organization
        myIKGrp = mc.group(em=True, n=ikJoint_list_noFoot[0] + '_ik_grp')
        
        #___________create IK HANDLE____________#

        ikHandle_var = mc.ikHandle(n=ikJoint_list_noFoot[0] + '_ikHandkle', sj=ikJoint_list_noFoot[0], ee=ikJoint_list_noFoot[-1])

        mc.setAttr((ikHandle_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandle_var[0] + '.poleVectorZ'), 0)

        ikHandle_effector_var = mc.listConnections(ikHandle_var, s=True, type='ikEffector')

        mc.rename(ikHandle_effector_var, ikHandle_var[0] + '_effector')

        #hide ik handle
        mc.setAttr(ikHandle_var[0] + '.visibility', 0)

        #parent ik handle global grp to organize
        mc.parent(ikHandle_var[0], myIKGrp)


        #___________ik handle CTRL____________#
        ik_group_list = []
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
            myCurve = mc.rename(ikJoint_list_noFoot[0] + '_ik_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            #parent and zero curveGrp to joints
            mc.parent(myGroup, ikJoint_list_noFoot[-1], relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(myGroup)

            #translate contrain ik ctrl to ik handle
            mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
            #rotate constrain ik ctrl to ankle joint
            mc.parentConstraint(myCurve, ikJoint_list_noFoot[-1], st=('x','y','z'))

            #parent grp to global grp to organize
            mc.parent(myGroup, myIKGrp)

            #append grp for outside use
            ik_group_list.append(myGroup)
        
        
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
            myCurve = mc.rename(ikJoint_list_noFoot[0] + '_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
            
            #middle index value of ik joints (middle joint)
            roughMedian = round(len(ikJoint_list_noFoot)/2.0)

            #___more accurate mid point (for 'hip_to_ankle_scaled')___
            #length of whole limb
            limb_lenA = 0
            for i in ikJoint_list_noFoot:
                if i != ikJoint_list_noFoot[0]:
                    limb_lenA += mc.getAttr(i + '.translateX')
            #length of upper half of limb
            upperLimb_lenA = 0
            for i in ikJoint_list_noFoot[:int(roughMedian)]:
                if i != ikJoint_list_noFoot[0]:
                    upperLimb_lenA += mc.getAttr(i + '.translateX')

            #divide sum of leg lengths by upper leg length (for more accurate mid point)
            better_midPoint_var = (limb_lenA / upperLimb_lenA)

            #__vector math____#
            #vector positions of hip, knee, ankle
            hip_pos = om.MVector(mc.xform(ikJoint_list_noFoot[0], q=True, rp=True, ws=True))
            knee_pos = om.MVector(mc.xform(ikJoint_list_noFoot[int(roughMedian-1.0)], q=True, rp=True, ws=True))
            ankle_pos = om.MVector(mc.xform(ikJoint_list_noFoot[-1], q=True, rp=True, ws=True))

            #finding vector point of pv knee (on plane of hip, knee, ankle)
            hip_to_ankle = ankle_pos - hip_pos
            hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
            mid_point = hip_pos + hip_to_ankle_scaled
            mid_point_to_knee_vec = knee_pos - mid_point
            mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * knee_dist_mult  #pv ctrl distance from knee multiplier
            mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

            #final polve vector point (to avoid knee changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

            myAimConst = mc.aimConstraint(  ikJoint_list_noFoot[int(roughMedian-1.0)], myGroup, 
                                            offset=(0, 0, 0), 
                                            weight=1, 
                                            aimVector=(0, 0, -1), 
                                            upVector=(0, 1, 0), 
                                            worldUpType=('vector'), 
                                            worldUpVector=(0, 1, 0))
            mc.delete(myAimConst)

            #___connect pole vector
            mc.poleVectorConstraint(myCurve, ikHandle_var[0])

            #parent grp to global grp to organize
            mc.parent(myGroup, myIKGrp)

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
                mc.setAttr((switchCurveA[0] + '.ty'), -40)
            elif direction == 'right':
                mc.setAttr((switchCurveA[0] + '.ty'), 40)
            mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
            mc.makeIdentity(switchCurveA, apply=True)

            #_______move joint to ankle and parent_______#
            #parent and zero joints to last joint in selection
            mc.parent(switchCurveA_grp, leg_chain[-2], relative=True)
            #parent joints to world space
            mc.Unparent(switchCurveA_grp)

            # parent constrain switch ctrl to ankle
            mc.parentConstraint(leg_chain[-2], switchCurveA_grp, mo=True)

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
        for items_trans, items_rot, items_scale in itertools.izip(  blendColorsTran_list, 
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

    '''
    #________________________________________________________________________________#
    #________________________END of FK/IK BLEND______________________________________#

        #_________________Reverse Foot Rig___________________#
        #____________________________________________________#

        l_ftCtrl_list = []
        l_ftCtrl_grp_list = []

        for items in loc_l_foot_list:
            
            #name circle curves
            locCurveA_l_name = items.replace('loc_', reverseFootCtrlPrefix)
            locCurveB_l_name = items.replace('loc_', reverseFootCtrlPrefix) + '0'
            locCurveC_l_name = items.replace('loc_', reverseFootCtrlPrefix) + '1'

            #create nurbs circle
            locCurveA_l = mc.circle(n=locCurveA_l_name, ch=False, r=4, nr=(0,1,0))
            #create variable for nurbs circle shape
            locCurveA_l_shape = mc.listRelatives(locCurveA_l, s=True)
            #color nurbs circle shape
            mc.setAttr((locCurveA_l_shape[0] + '.overrideEnabled'), 1)
            mc.setAttr((locCurveA_l_shape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((locCurveA_l_shape[0] + '.overrideColorR'), .5)
            mc.setAttr((locCurveA_l_shape[0] + '.overrideColorG'), 1)
            mc.setAttr((locCurveA_l_shape[0] + '.overrideColorB'), 0)

            #create 2nd nurbs circle
            locCurveB_l = mc.circle(n=locCurveB_l_name, ch=False, r=4, nr=(0,0,0))
            #create variable for 2nd nurbs circle shape
            locCurveB_l_shape = mc.listRelatives(locCurveB_l, s=True)
            #color 2nd nurbs circle shape
            mc.setAttr((locCurveB_l_shape[0] + '.overrideEnabled'), 1)
            mc.setAttr((locCurveB_l_shape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((locCurveB_l_shape[0] + '.overrideColorR'), .5)
            mc.setAttr((locCurveB_l_shape[0] + '.overrideColorG'), 1)
            mc.setAttr((locCurveB_l_shape[0] + '.overrideColorB'), 0)
            #parent 2nd nurbs circle shape to first nurbs circle
            mc.parent(locCurveB_l_shape, locCurveA_l, r=True, shape=True)
            #delete 2nd nurbs circle transform
            mc.delete(locCurveB_l)

            #create 3rd nurbs circle
            locCurveC_l = mc.circle(n=locCurveC_l_name, ch=False, r=4, nr=(1,0,0))
            #create variable for 3rd nurbs circle shape
            locCurveC_l_shape = mc.listRelatives(locCurveC_l, s=True)
            #color 3rd nurbs circle shape
            mc.setAttr((locCurveC_l_shape[0] + '.overrideEnabled'), 1)
            mc.setAttr((locCurveC_l_shape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((locCurveC_l_shape[0] + '.overrideColorR'), .5)
            mc.setAttr((locCurveC_l_shape[0] + '.overrideColorG'), 1)
            mc.setAttr((locCurveC_l_shape[0] + '.overrideColorB'), 0)
            #parent 3rd nurbs circle shape to first nurbs circle
            mc.parent(locCurveC_l_shape, locCurveA_l, r=True, shape=True)
            #delete 3rd nurbs circle transform
            mc.delete(locCurveC_l)

            #_______group ctrl_______#
            locCurveA_l_grp = mc.group(locCurveA_l, n = (locCurveA_l_name + '_grp'))
            locCurveA_l_grp_offset = mc.group(locCurveA_l, n = (locCurveA_l_name + '_grp_offset'))


            #_______move ctrl grp to loc_______#

            #parent and zero joints to l_leg_list
            mc.parent(locCurveA_l_grp, items, relative=True)
            #parent joints to world space
            mc.Unparent(locCurveA_l_grp)
            #add/ create list for ftCtrl's
            l_ftCtrl_list.append(locCurveA_l)
            l_ftCtrl_grp_list.append(locCurveA_l_grp)

        #group reverse foot ctrls together
        mc.parent(l_ftCtrl_grp_list[4], l_ftCtrl_list[5])
        mc.parent(l_ftCtrl_grp_list[3], l_ftCtrl_list[4])
        mc.parent(l_ftCtrl_grp_list[2], l_ftCtrl_list[3])
        mc.parent(l_ftCtrl_grp_list[1], l_ftCtrl_list[2])
        mc.parent(l_ftCtrl_grp_list[0], l_ftCtrl_list[1])
        #group reverse foot ctrls under ankle ctrl
        mc.parent(ftCtrl_l_foot_inner_grp, ikFootCtrl_l)

        # create extra toe offset ctrl_______
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
            mc.setAttr((myCurve + '.scaleX'), 4.5)
            mc.setAttr((myCurve + '.scaleY'), 3)
            mc.setAttr((myCurve + '.scaleZ'), 6)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorR'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorG'), 0)
            mc.setAttr((curveShape[0] + '.overrideColorB'), 1)
            #rename curve
            myCurve = loc_l_foot_toe.replace('loc_', reverseFootCtrlPrefix)
            myCurve = mc.rename(myCurve + '_toeWiggle')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            #parent and zero curveGrp
            mc.parent(myGroup, ftCtrl_l_foot_toe, relative=True)
            #unparent after getting position
            mc.Unparent(myGroup)
            #reparent to toe_end
            mc.parent(myGroup, ftCtrl_l_foot_toe_end, relative=False)


        #___________reverse foot joint parenting___________#

        #parent reverse foot ankle ctrl to ikHandle trans and ankle joint rotate
        mc.parentConstraint(ftCtrl_l_foot_ankle, l_leg_ikHandle[0], mo=True, sr=('x', 'y', 'z'))
        mc.parentConstraint(ftCtrl_l_foot_ankle, ik_l_leg_ankle, mo=True, st=('x', 'y', 'z'))
        #parent toe
        mc.parentConstraint(ftCtrl_l_foot_toe_toeWiggle, ik_l_leg_toes, mo=True)

        #___________________________________________#
        #____l leg cleanup____ visibility, etc______#
        #___________________________________________#

        #hide ankle ctrl (not needed)
        mc.setAttr((ftCtrl_l_foot_ankle + '_grp' + '.visibility'), 0)
        #set driven key to hide ctrls for blend
        mc.setAttr((switchCtrl_l_leg + '.fk_ik_blend'), 0)
        mc.setAttr((ikFootCtrl_l_foot1_grp + '.visibility'), 1)
        mc.setAttr((pvCtrl_l_leg_grp + '.visibility'), 1)
        mc.setAttr((fkCtrl_l_hip_grp + '.visibility'), 0)
        mc.setDrivenKeyframe((ikFootCtrl_l_foot1_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pvCtrl_l_leg_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fkCtrl_l_hip_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
        mc.setAttr((switchCtrl_l_leg + '.fk_ik_blend'), 1)
        mc.setAttr((ikFootCtrl_l_foot1_grp + '.visibility'), 0)
        mc.setAttr((pvCtrl_l_leg_grp + '.visibility'), 0)
        mc.setAttr((fkCtrl_l_hip_grp + '.visibility'), 1)
        mc.setDrivenKeyframe((ikFootCtrl_l_foot1_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pvCtrl_l_leg_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fkCtrl_l_hip_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))

        '''