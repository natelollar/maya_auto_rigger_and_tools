import maya.cmds as mc

try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass

import maya.api.OpenMaya as om

import string

#_________________Rigging Functions ___________________________#
#______________________________________________________________#
class rigging_class():
        
    def create_fk_chain(self):
        #create list for ctrl grp parenting to one another
        fk_ctrl_grp_list = []
        #create list for ctrl parenting to one another
        fk_ctrl_list = []

        #my selection
        mySel = mc.ls(sl=True)

        for i in mySel:
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
            mc.setAttr(".scaleX", 10)
            mc.setAttr(".scaleY", 10)
            mc.setAttr(".scaleZ", 10)
            #freeze transforms
            mc.makeIdentity(apply=True)
            #select curve box's shape
            itemsShape = mc.listRelatives(s=True)
            #color curve box's shape red
            mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
            mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
            mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

            #rename curve, with joint name, and then new prefix
            myCurve_name = mc.rename(i + '_ctrl')

            #group curve
            curveGroup = mc.group(myCurve_name)
            curveGroup_offset = mc.group(myCurve_name)
            #rename group
            curveGroup_name = mc.rename(curveGroup, (myCurve_name + '_grp'))
            curveGroup_offset_name = mc.rename(curveGroup_offset, (myCurve_name + '_grp_offset'))
            #parent and zero curveGrp to l_leg_fk_list
            mc.parent(curveGroup_name, i, relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(curveGroup_name)
            #create a list for the groups (for parenting to one another)
            fk_ctrl_grp_list.append(curveGroup_name)
            #create a list of the ctrl curves (to parent constrain the joints to)
            fk_ctrl_list.append(myCurve_name)

            #parent constrain ctrls to fk jnts
            mc.parentConstraint(myCurve_name, i)
            mc.scaleConstraint(myCurve_name, i)

            # to work better with scaling (maybe)
            mc.setAttr( i + '.segmentScaleCompensate', 0 )

        #remove first and last of lists to correctly parent ctrls and grps together in for loop
        fk_ctrl_grp_list.pop(0)
        fk_ctrl_list.pop(-1)

        #parent ctrls and grps together
        for i_grp, i_ctrl in zip(fk_ctrl_grp_list, fk_ctrl_list):
            mc.parent(i_grp, i_ctrl)


    #___________create IK Limb____________#
    def create_ik_limb(self):
        #my joint selection
        mySel = mc.ls(sl=True)
        #group for organization
        myIKGrp = mc.group(em=True, n=mySel[0] + '_ik_grp')
        
        #___________create IK HANDLE____________#

        ikHandle_var = mc.ikHandle(n=mySel[0] + '_ikHandkle', sj=mySel[0], ee=mySel[-1])

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
            myCurve = mc.rename(mySel[0] + '_ik_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            #parent and zero curveGrp to l_leg_fk_list
            mc.parent(myGroup, mySel[-1], relative=True)
            #unparent group (since it has correct position)
            mc.Unparent(myGroup)
            #zero ik ctrl rotations
            # mc.setAttr((myGroup + ".rotateX"), 0)
            # mc.setAttr((myGroup + ".rotateY"), 0)
            # mc.setAttr((myGroup + ".rotateZ"), 0)

            mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
            mc.parentConstraint(myCurve, mySel[-1], st=('x','y','z'))

            #parent grp to global grp to organize
            mc.parent(myGroup, myIKGrp)


        
        #_________________POLE VECTOR Start___________________#
        #_____________________________________________________#
        for items in range(0,1):
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
            mc.setAttr((myCurve + ".scaleX"), 0.7)
            mc.setAttr((myCurve + ".scaleY"), 0.7)
            mc.setAttr((myCurve + ".scaleZ"), 0.7)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
            mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
            mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
            #rename curve
            myCurve = mc.rename(mySel[0] + '_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
            
            #___more accurate mid point (for "hip_to_ankle_scaled")___
            #length of knee to ankle
            shin_len = (mc.getAttr(mySel[1] + '.translateX') + mc.getAttr(mySel[-1] + '.translateX'))
            #length of hip to knee
            upperLeg_len = mc.getAttr(mySel[1] + '.translateX')
            #divide sum of leg lengths by hip length (for more accurate mid point)
            better_midPoint_var = (shin_len / upperLeg_len)

            
            #__vector math____#
            #vector positions of hip, knee, ankle
            hip_pos = om.MVector(mc.xform(mySel[0], q=True, rp=True, ws=True))
            knee_pos = om.MVector(mc.xform(mySel[1], q=True, rp=True, ws=True))
            ankle_pos = om.MVector(mc.xform(mySel[-1], q=True, rp=True, ws=True))

            #finding vector point of pv knee (on plane of hip, knee, ankle)
            hip_to_ankle = ankle_pos - hip_pos
            hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
            mid_point = hip_pos + hip_to_ankle_scaled
            mid_point_to_knee_vec = knee_pos - mid_point
            mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 4
            mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

            #final polve vector point (to avoid knee changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

            myAimConst = mc.aimConstraint(  mySel[1], myGroup, 
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



    #______________________________________________________________#
    #____________IK/FK Limb Blend _________________________________#
    #______________________________________________________________#
    def create_fk_ik_limb(self):
        #______________________________#
        #_____Blended Joint Chain______#
        #______________________________#
        mySel = mc.ls(sl=True)
        fkJoint_list = []
        ikJoint_list = []
        for i in mySel:
            #______________________#
            #____create FK chain___#
            fkJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr(".radius", 4)
            #joint color
            mc.setAttr(".overrideEnabled", 1)
            mc.setAttr(".overrideRGBColors", 1)
            mc.setAttr(".overrideColorR", 1)
            mc.setAttr(".overrideColorG", 0)
            mc.setAttr(".overrideColorB", 0.1)
            
            fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
            mc.Unparent(fkJoint)
            
            fkJoint_list.append(fkJoint)
            
            #______________________#
            #____create _IK chain___#
            ikJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr(".radius", 3)
            #joint color
            mc.setAttr(".overrideEnabled", 1)
            mc.setAttr(".overrideRGBColors", 1)
            mc.setAttr(".overrideColorR", .1)
            mc.setAttr(".overrideColorG", .9)
            mc.setAttr(".overrideColorB", 0.1)
            
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
        for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, mySel):
            #create blend color nodes
            blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
            blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
            blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')
            #translate
            mc.connectAttr((i_FK + ".translate"), (blendColorsTran + ".color1"), f=True)
            mc.connectAttr((i_IK + ".translate"), (blendColorsTran + ".color2"), f=True)
            mc.connectAttr((blendColorsTran + ".output"), (i + ".translate"), f=True)
            #rotate
            mc.connectAttr((i_FK + ".rotate"), (blendColorsRot + ".color1"), f=True)
            mc.connectAttr((i_IK + ".rotate"), (blendColorsRot + ".color2"), f=True)
            mc.connectAttr((blendColorsRot + ".output"), (i + ".rotate"), f=True)
            #scale
            mc.connectAttr((i_FK + ".scale"), (blendColorsScale + ".color1"), f=True)
            mc.connectAttr((i_IK + ".scale"), (blendColorsScale + ".color2"), f=True)
            mc.connectAttr((blendColorsScale + ".output"), (i + ".scale"), f=True)
            #append lists for outside loop use
            blendColorsTran_list.append(blendColorsTran)
            blendColorsRot_list.append(blendColorsRot)
            blendColorsScale_list.append(blendColorsScale)


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
            mc.setAttr(".scaleX", 4)
            mc.setAttr(".scaleY", 4)
            mc.setAttr(".scaleZ", 4)
            #freeze transforms
            mc.makeIdentity(apply=True)
            #select curve box's shape
            itemsShape = mc.listRelatives(s=True)
            #color curve box's shape red
            mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
            mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
            mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

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
        print(fk_ctrl_grp_list_temp)
        fk_ctrl_list_temp = fk_ctrl_list[:-1]
        print(fk_ctrl_list_temp)

        #parent ctrls and grps together
        for i_grp, i_ctrl in zip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
            mc.parent(i_grp, i_ctrl)


        #_____________________________________#
        #______________IK Ctrls_______________#
        #_____________________________________#
        #group for organization
        myIKGrp = mc.group(em=True, n=ikJoint_list[0] + '_ik_grp')
        
        #___________create IK HANDLE____________#

        ikHandle_var = mc.ikHandle(n=ikJoint_list[0] + '_ikHandkle', sj=ikJoint_list[0], ee=ikJoint_list[-1])

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
        

        #_________________POLE VECTOR Start___________________#
        #_____________________________________________________#
        pv_group_list = []
        for items in range(0,1):
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
            mc.setAttr((myCurve + ".scaleX"), 0.7)
            mc.setAttr((myCurve + ".scaleY"), 0.7)
            mc.setAttr((myCurve + ".scaleZ"), 0.7)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((curveShape[0] + ".overrideColorRGB"), 1, 1, 0)
            #rename curve
            myCurve = mc.rename(ikJoint_list[0] + '_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
            
            #middle index value of ik joints (middle joint)
            roughMedian = round(len(ikJoint_list)/2.0)

            #___more accurate mid point (for "hip_to_ankle_scaled")___
            #length of whole limb
            limb_lenA = 0
            for i in ikJoint_list:
                if i != ikJoint_list[0]:
                    limb_lenA += mc.getAttr(i + '.translateX')
            #length of upper half of limb
            upperLimb_lenA = 0
            for i in ikJoint_list[:int(roughMedian)]:
                if i != ikJoint_list[0]:
                    upperLimb_lenA += mc.getAttr(i + '.translateX')

            #divide sum of leg lengths by upper leg length (for more accurate mid point)
            better_midPoint_var = (limb_lenA / upperLimb_lenA)

            #__vector math____#
            #vector positions of hip, knee, ankle
            hip_pos = om.MVector(mc.xform(ikJoint_list[0], q=True, rp=True, ws=True))
            knee_pos = om.MVector(mc.xform(ikJoint_list[int(roughMedian-1.0)], q=True, rp=True, ws=True))
            ankle_pos = om.MVector(mc.xform(ikJoint_list[-1], q=True, rp=True, ws=True))

            #finding vector point of pv knee (on plane of hip, knee, ankle)
            hip_to_ankle = ankle_pos - hip_pos
            hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
            mid_point = hip_pos + hip_to_ankle_scaled
            mid_point_to_knee_vec = knee_pos - mid_point
            mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 3  #pv ctrl distance from knee multiplier
            mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

            #final polve vector point (to avoid knee changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

            myAimConst = mc.aimConstraint(  ikJoint_list[int(roughMedian-1.0)], myGroup, 
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


        #organize into final group
        ik_fk_blend_grp = mc.group(em=True, n='ik_fk_blend_grp')
        mc.parent(fk_ctrl_grp_list[0], ik_fk_blend_grp)
        mc.parent(switch_ctrl_grp_list[0], ik_fk_blend_grp)
        mc.parent(myIKGrp, ik_fk_blend_grp)
        #parent joints to final group too
        mc.parent(fkJoint_list[0], ik_fk_blend_grp)
        mc.parent(ikJoint_list[0], ik_fk_blend_grp)
        

    #________________________END of FK/IK BLEND______________________________________#


    def simple_blend_joints(self):
        # Select Fk, then IK, then Main
        # Set up Switch control seperatly

        #my selection
        mySel = mc.ls(sl=True)

        blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
        blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
        blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')

        ####
        mc.connectAttr((mySel[0] + ".translate"), (blendColorsTran + ".color1"), f=True)
        mc.connectAttr((mySel[1] + ".translate"), (blendColorsTran + ".color2"), f=True)
        mc.connectAttr((blendColorsTran + ".output"), (mySel[2] + ".translate"), f=True)

        ####
        mc.connectAttr((mySel[0] + ".rotate"), (blendColorsRot + ".color1"), f=True)
        mc.connectAttr((mySel[1] + ".rotate"), (blendColorsRot + ".color2"), f=True)
        mc.connectAttr((blendColorsRot + ".output"), (mySel[2] + ".rotate"), f=True)

        ####
        mc.connectAttr((mySel[0] + ".scale"), (blendColorsScale + ".color1"), f=True)
        mc.connectAttr((mySel[1] + ".scale"), (blendColorsScale + ".color2"), f=True)
        mc.connectAttr((blendColorsScale + ".output"), (mySel[2] + ".scale"), f=True)


    def blend_joint_chain(self):
        mySel = mc.ls(sl=True)
        fkJoint_list = []
        ikJoint_list = []
        for i in mySel:
            #______________________#
            #____create FK chain___#
            fkJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr(".radius", 4)
            #joint color
            mc.setAttr(".overrideEnabled", 1)
            mc.setAttr(".overrideRGBColors", 1)
            mc.setAttr(".overrideColorR", 1)
            mc.setAttr(".overrideColorG", 0)
            mc.setAttr(".overrideColorB", 0.1)
            
            fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
            mc.Unparent(fkJoint)
            
            fkJoint_list.append(fkJoint)
            
            #______________________#
            #____create _K chain___#
            ikJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr(".radius", 3)
            #joint color
            mc.setAttr(".overrideEnabled", 1)
            mc.setAttr(".overrideRGBColors", 1)
            mc.setAttr(".overrideColorR", .1)
            mc.setAttr(".overrideColorG", .9)
            mc.setAttr(".overrideColorB", 0.1)
            
            ikJoint = mc.rename(ikJoint_orig, ('IK_' + i))
            mc.Unparent(ikJoint)
            
            ikJoint_list.append(ikJoint)
        
        currentIndex = -1
        for i in fkJoint_list:
            currentIndex += 1
            if i != fkJoint_list[0]:
                mc.parent(fkJoint_list[currentIndex], fkJoint_list[currentIndex-1])

        currentIndex = -1
        for i in ikJoint_list:
            currentIndex += 1
            print (currentIndex)
            if i != ikJoint_list[0]:
                mc.parent(ikJoint_list[currentIndex], ikJoint_list[currentIndex-1])
        
        for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, mySel):
            blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
            blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
            blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')
            #translate
            mc.connectAttr((i_FK + ".translate"), (blendColorsTran + ".color1"), f=True)
            mc.connectAttr((i_IK + ".translate"), (blendColorsTran + ".color2"), f=True)
            mc.connectAttr((blendColorsTran + ".output"), (i + ".translate"), f=True)
            #rotate
            mc.connectAttr((i_FK + ".rotate"), (blendColorsRot + ".color1"), f=True)
            mc.connectAttr((i_IK + ".rotate"), (blendColorsRot + ".color2"), f=True)
            mc.connectAttr((blendColorsRot + ".output"), (i + ".rotate"), f=True)
            #scale
            mc.connectAttr((i_FK + ".scale"), (blendColorsScale + ".color1"), f=True)
            mc.connectAttr((i_IK + ".scale"), (blendColorsScale + ".color2"), f=True)
            mc.connectAttr((blendColorsScale + ".output"), (i + ".scale"), f=True)
            

    #avaliable for reverse foot function
    def rev_foot_locators(self, direction):
        #loc_ankle
        if mc.objExists(direction + '_loc_ankle') == False:
            loc_ankle = mc.spaceLocator(n=direction + '_loc_ankle')
            mc.setAttr((loc_ankle[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_ankle[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_ankle[0] + ".overrideColorRGB"), .1, 1, 0)
            mc.setAttr((loc_ankle[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_ankle[0] + ".translate"), 10.738,9.708,-3.181)
                mc.setAttr((loc_ankle[0] + ".rotate"), 5.278, -82.31, -5.275)
            else:
                mc.setAttr((loc_ankle[0] + ".translate"), -10.738,9.708,-3.181)
                mc.setAttr((loc_ankle[0] + ".rotate"), 5.278, 97.69, -174.725)
        #loc_toe
        if mc.objExists(direction + '_loc_toe') == False:
            loc_toe = mc.spaceLocator(n=direction + '_loc_toe')
            mc.setAttr((loc_toe[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_toe[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_toe[0] + ".overrideColorRGB"), .1, 1, 0)
            mc.setAttr((loc_toe[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_toe[0] + ".translate"), 12.597,2.148,9.648)
                mc.setAttr((loc_toe[0] + ".rotate"), 5.278, -82.31, -5.275)
            else:
                mc.setAttr((loc_toe[0] + ".translate"), -12.597, 2.148, 9.648)
                mc.setAttr((loc_toe[0] + ".rotate"), 5.278, 97.69, -174.725)
        #loc_toe_end
        if mc.objExists(direction + '_loc_toe_end') == False:
            loc_toe_end = mc.spaceLocator(n=direction + '_loc_toe_end')
            mc.setAttr((loc_toe_end[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_toe_end[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_toe_end[0] + ".overrideColorRGB"), 1, 1, 0)
            mc.setAttr((loc_toe_end[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_toe_end[0] + ".translate"), 13.41,0.224,15.601)
                mc.setAttr((loc_toe_end[0] + ".rotate"), 0.156, -82.539, 0.825)
            else:
                mc.setAttr((loc_toe_end[0] + ".translate"), -13.41, 0.224, 15.601)
                mc.setAttr((loc_toe_end[0] + ".rotate"), -179.844, 82.539, -0.825)
        #loc_heel
        if mc.objExists(direction + '_loc_heel') == False:
            loc_heel = mc.spaceLocator(n=direction + '_loc_heel')
            mc.setAttr((loc_heel[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_heel[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_heel[0] + ".overrideColorRGB"), 1, 1, 0)
            mc.setAttr((loc_heel[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_heel[0] + ".translate"), 9.547,0.166,-6.787)
                mc.setAttr((loc_heel[0] + ".rotate"), 0.156, -82.539, 0.825)
            else:
                mc.setAttr((loc_heel[0] + ".translate"), -9.547, 0.166, -6.787)
                mc.setAttr((loc_heel[0] + ".rotate"), -179.844, 82.539, -0.825)
        #loc_outer_foot
        if mc.objExists(direction + '_loc_outer_foot') == False:
            loc_outer_foot = mc.spaceLocator(n=direction + '_loc_outer_foot')
            mc.setAttr((loc_outer_foot[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_outer_foot[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_outer_foot[0] + ".overrideColorRGB"), 1, .1, 0)
            mc.setAttr((loc_outer_foot[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_outer_foot[0] + ".translate"), 17.04,0.289,7.031)
                mc.setAttr((loc_outer_foot[0] + ".rotate"), 0.076, -74.621, 0.906)
            else:
                mc.setAttr((loc_outer_foot[0] + ".translate"), -17.04, 0.289, 7.031)
                mc.setAttr((loc_outer_foot[0] + ".rotate"), 180.076, 74.621, -0.906)
        #loc_inner_foot
        if mc.objExists(direction + '_loc_inner_foot') == False:
            loc_inner_foot = mc.spaceLocator(n=direction + '_loc_inner_foot')
            mc.setAttr((loc_inner_foot[0] + ".overrideEnabled"), 1)
            mc.setAttr((loc_inner_foot[0] + ".overrideRGBColors"), 1)
            mc.setAttr((loc_inner_foot[0] + ".overrideColorRGB"), 1, .1, 0)
            mc.setAttr((loc_inner_foot[0] + ".localScale"), 5, 5, 5)
            if direction == 'l' or direction == 'left':
                mc.setAttr((loc_inner_foot[0] + ".translate"), 7.205,0.119,10.571)
                mc.setAttr((loc_inner_foot[0] + ".rotate"), 0.782, -88.52, 0.198)
            else:
                mc.setAttr((loc_inner_foot[0] + ".translate"), -7.205, 0.119, 10.571)
                mc.setAttr((loc_inner_foot[0] + ".rotate"), -179.218, 88.52, -0.198)


    #___________Reverse Foot Rig_____________#
    def reverse_foot_setup(self, direction):
        rvFoot_loc_list = [ direction + '_loc_ankle', 
                            direction + '_loc_toe',
                            direction + '_loc_toe_end',
                            direction + '_loc_heel',
                            direction + '_loc_outer_foot',
                            direction + '_loc_inner_foot' ]
        try:
            # try to break the function if cannot select all foot locators
            mc.select(rvFoot_loc_list)
            # if can select all locators, do function
            ftCtrl_list = []
            ftCtrl_grp_list = []
            for i in rvFoot_loc_list:
                #name circle curves
                locCurveA_name = i.replace('loc_', 'ftCtrl_')
                locCurveB_name = i.replace('loc_', 'ftCtrl_') + 'A'
                locCurveC_name = i.replace('loc_', 'ftCtrl_') + 'B'

                #create nurbs circle
                locCurveA = mc.circle(n=locCurveA_name, ch=False, r=3, nr=(0,1,0))
                #create variable for nurbs circle shape
                locCurveA_shape = mc.listRelatives(locCurveA, s=True)
                #color nurbs circle shape
                mc.setAttr((locCurveA_shape[0] + ".overrideEnabled"), 1)
                mc.setAttr((locCurveA_shape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((locCurveA_shape[0] + ".overrideColorRGB"), .5, 1, 0)

                #create 2nd nurbs circle
                locCurveB = mc.circle(n=locCurveB_name, ch=False, r=3, nr=(0,0,0))
                #create variable for 2nd nurbs circle shape
                locCurveB_shape = mc.listRelatives(locCurveB, s=True)
                #color 2nd nurbs circle shape
                mc.setAttr((locCurveB_shape[0] + ".overrideEnabled"), 1)
                mc.setAttr((locCurveB_shape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((locCurveB_shape[0] + ".overrideColorRGB"), .5, 1, 0)
                #parent 2nd nurbs circle shape to first nurbs circle
                mc.parent(locCurveB_shape, locCurveA, r=True, shape=True)
                #delete 2nd nurbs circle transform
                mc.delete(locCurveB)

                #create 3rd nurbs circle
                locCurveC = mc.circle(n=locCurveC_name, ch=False, r=3, nr=(1,0,0))
                #create variable for 3rd nurbs circle shape
                locCurveC_shape = mc.listRelatives(locCurveC, s=True)
                #color 3rd nurbs circle shape
                mc.setAttr((locCurveC_shape[0] + ".overrideEnabled"), 1)
                mc.setAttr((locCurveC_shape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((locCurveC_shape[0] + ".overrideColorRGB"), .5, 1, 0)
                #parent 3rd nurbs circle shape to first nurbs circle
                mc.parent(locCurveC_shape, locCurveA, r=True, shape=True)
                #delete 3rd nurbs circle transform
                mc.delete(locCurveC)

                #renaming curve inturn renames all its shapes
                locCurveA_name = mc.rename(locCurveA, locCurveA[0] + '#')

                #_______group ctrl_______#
                locCurveA_grp = mc.group(locCurveA_name, n = (locCurveA_name + '_grp'))
                locCurveA_grp_offset = mc.group(locCurveA_name, n = (locCurveA_name + '_grp_offset'))
                
                #_______move ctrl grp to loc_______#
                mc.parent(locCurveA_grp, i, relative=True)
                mc.Unparent(locCurveA_grp)
                #add/ create list for ftCtrl's
                ftCtrl_list.append(locCurveA_name)
                ftCtrl_grp_list.append(locCurveA_grp)
            
            #group reverse foot ctrls together
            mc.parent(ftCtrl_grp_list[4], ftCtrl_list[5])
            mc.parent(ftCtrl_grp_list[3], ftCtrl_list[4])
            mc.parent(ftCtrl_grp_list[2], ftCtrl_list[3])
            mc.parent(ftCtrl_grp_list[1], ftCtrl_list[2])
            mc.parent(ftCtrl_grp_list[0], ftCtrl_list[1])
            

            # create extra toe offset ctrl_______
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
                mc.setAttr((myCurve + ".scaleX"), 4.5)
                mc.setAttr((myCurve + ".scaleY"), 3)
                mc.setAttr((myCurve + ".scaleZ"), 6)
                #freeze transforms
                mc.makeIdentity(myCurve, apply=True)
                #select curve box's shape
                curveShape = mc.listRelatives(myCurve, s=True)
                #color curve box's shape red
                mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
                mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
                mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
                mc.setAttr((curveShape[0] + ".overrideColorG"), 0)
                mc.setAttr((curveShape[0] + ".overrideColorB"), 1)
                #rename curve
                myCurve = mc.rename(direction + '_ftCtrl_toe_toeWiggle#')
                #group curve
                curveGrouped = mc.group(myCurve)
                curveGrouped_offset = mc.group(myCurve)
                #rename group
                myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
                myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
                #parent and zero curveGrp
                mc.parent(myGroup, ftCtrl_list[1], relative=True)
                #unparent after getting position
                mc.Unparent(myGroup)
                #reparent to toe_end
                mc.parent(myGroup, ftCtrl_list[2], relative=False)

            #clear selection
            mc.select(cl=True)

        except:
            print ('________________________________')
            print ('____Need all FOOT Locators!_____')
            print ('________________________________')
        

    def nurbs_curve_cube(self):
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
        mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), .1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename('cubeCurve_ctrl#')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))


    def nurbs_curve_sphere(self):
        #name circle curves
        curveA_name = 'circleCurveA_ctrl#'
        curveB_name = 'circleCurveB_ctrl#'
        curveC_name = 'circleCurveC_ctrl#'

        #create nurbs circle
        curveA = mc.circle(n=curveA_name, ch=False, r=3, nr=(0,1,0))
        #create variable for nurbs circle shape
        curveA_shape = mc.listRelatives(curveA, s=True)
        #color nurbs circle shape
        mc.setAttr((curveA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveA_shape[0] + ".overrideColorR"), .8)
        mc.setAttr((curveA_shape[0] + ".overrideColorG"), .8)
        mc.setAttr((curveA_shape[0] + ".overrideColorB"), 0)

        #create 2nd nurbs circle
        curveB = mc.circle(n=curveB_name, ch=False, r=3, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        curveB_shape = mc.listRelatives(curveB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((curveB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveB_shape[0] + ".overrideColorR"), .8)
        mc.setAttr((curveB_shape[0] + ".overrideColorG"), .8)
        mc.setAttr((curveB_shape[0] + ".overrideColorB"), 0)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(curveB_shape, curveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(curveB)

        #create 3rd nurbs circle
        curveC = mc.circle(n=curveC_name, ch=False, r=3, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        curveC_shape = mc.listRelatives(curveC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((curveC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveC_shape[0] + ".overrideColorR"), .8)
        mc.setAttr((curveC_shape[0] + ".overrideColorG"), .8)
        mc.setAttr((curveC_shape[0] + ".overrideColorB"), 0)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(curveC_shape, curveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(curveC)

        #_______group switch ctrl_______#
        curveA_grp = mc.group(curveA, n = (curveA[0] + '_grp'))
        curveA_grp_offset = mc.group(curveA, n = (curveA[0] + '_grp_offset'))

        
    def nurbs_curve_arrow(self):
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
        mc.setAttr((myCurve + ".scaleX"), 0.7)
        mc.setAttr((myCurve + ".scaleY"), 0.7)
        mc.setAttr((myCurve + ".scaleZ"), 0.7)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), .1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 1)
        #rename curve
        myCurve = mc.rename('arrowCurve_ctrl#')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))


    def new_bindpose(self):
        bindPose_name = mc.textField( 'bindpose_name_text', query=1, text=1)

        mySel = mc.ls(sl=True)
        myBindPose = mc.listConnections(mySel, s=1, type='dagPose')
        mc.delete(myBindPose)

        new_pose = mc.dagPose(mySel, save=True, n=(bindPose_name) )

        mc.setAttr(( new_pose + '.bindPose'), 1)

    def object_type(self):
        mySel = mc.ls(sl=1)
        mySel_type = mc.objectType(mySel)
        print('__________________')
        print ('Type: ' + mySel_type)
        print('__________________')

        return mySel_type


    def mirror_ctrl_shape(self):
        # left right prefix
        left_prefix = mc.textField('left_prefix_text', query=True, text=True)
        right_prefix = mc.textField('right_prefix_text', query=True, text=True)
        # get selection list
        mySel_list = mc.ls(sl=True)
        # itterate through selected
        for mySel in mySel_list:
            mc.select(mySel) # if error sometimes reselect will fix
            # list locked attr to unlock and relock later
            mySel_locked_attr = mc.listAttr(mySel, locked=True)
            # unlock all locked attributes
            if mySel_locked_attr: # if locked attr exist /have value
                for i in mySel_locked_attr:
                    mc.setAttr((mySel + '.' + i), lock=False, keyable=True, channelBox=True)

            # duplicate, delete children, unparent
            mySel_dup = mc.duplicate(mySel, renameChildren=True)
            mySel_dup_childs = mc.listRelatives(mySel_dup, ad=True, type='transform')
            mc.delete(mySel_dup_childs)
            mc.Unparent(mySel_dup[0])
            # parent duplicated ctrl under world origin grp
            myGrp = mc.group(em=1)
            mc.parent(mySel_dup[0], myGrp)
            # flip grp to other side and freeze scale of -1 back to 1
            mc.setAttr(myGrp + '.scaleX', -1)
            mc.Unparent(mySel_dup[0]) # unparent from flip grp
            #delete flip grp
            mc.delete(myGrp)
            
            # find opposite side ctrl of orignal duplicated
            mySel_opp = mySel.replace(left_prefix, right_prefix, 1)
            #unlock all attributes
            if mySel_locked_attr:
                for i in mySel_locked_attr:
                    mc.setAttr((mySel_opp + '.' + i), lock=False, keyable=True, channelBox=True)
            
            # get shape of opposite side ctrl to delete later
            mySel_opp_shape = mc.listRelatives(mySel_opp, s=True)
            #parent under opposite ctrl and freeze attributes to get same exact trans, rot, scale
            mc.parent(mySel_dup[0], mySel_opp)
            mc.makeIdentity(mySel_dup[0], translate=True, rotate=True, scale=True, apply=True)
            mc.Unparent(mySel_dup[0])

            #find shape of duplicated control
            mySel_dup_shape = mc.listRelatives(mySel_dup[0], s=True)
            # parent flipped shape under other side ctrl
            mc.parent(mySel_dup_shape, mySel_opp, r=True, s=True)
            # delete unused duplicate transform
            mc.delete(mySel_dup[0])
            #delete old shape under opposite ctrl
            mc.delete(mySel_opp_shape)

            #rename new shape after opposite ctrl parent
            for shape in mySel_dup_shape: # for loop in case more than one shape
                myIndex = mySel_dup_shape.index(shape)
                # alphabet_list + '_'
                alphabet_list = '_' + string.ascii_uppercase[:] 
                if shape != mySel_dup_shape[0]:
                    mc.rename(shape, mySel_opp + alphabet_list[myIndex] + 'Shape')
                elif shape == mySel_dup_shape[0]:
                    mc.rename(shape, mySel_opp + 'Shape')

            # relock and hide attritues
            if mySel_locked_attr:
                for i in mySel_locked_attr:
                    mc.setAttr((mySel + '.' + i), lock=True, keyable=False, channelBox=False)
                    mc.setAttr((mySel_opp + '.' + i), lock=True, keyable=False, channelBox=False)


    def add_shape_to_offset_grp(self):
        # offset grp suffix
        offs_grp_suffix = mc.textField('offs_grp_suffix_text', query=True, text=True)
        # get selection list
        mySel_list = mc.ls(sl=True)
        # itterate through selected
        for mySel in mySel_list:
            mc.select(mySel) # if error sometimes reselect will fix
            # list locked attr to unlock and relock later
            mySel_locked_attr = mc.listAttr(mySel, locked=True)
            # unlock all locked attributes
            if mySel_locked_attr: # if locked attr exist /have value
                for i in mySel_locked_attr:
                    mc.setAttr((mySel + '.' + i), lock=False, keyable=True, channelBox=True)

            # duplicate, delete children, unparent
            mySel_dup = mc.duplicate(mySel, renameChildren=True)
            mySel_dup_childs = mc.listRelatives(mySel_dup, ad=True, type='transform')
            mc.delete(mySel_dup_childs)
            mc.Unparent(mySel_dup[0])
            '''
            # parent duplicated ctrl under world origin grp
            myGrp = mc.group(em=1)
            mc.parent(mySel_dup[0], myGrp)
            # flip grp to other side and freeze scale of -1 back to 1
            mc.setAttr(myGrp + '.scaleX', -1)
            mc.Unparent(mySel_dup[0]) # unparent from flip grp
            #delete flip grp
            mc.delete(myGrp)
            '''

            # find opposite side ctrl of orignal duplicated
            mySel_off_grp = mySel + offs_grp_suffix
            #unlock all attributes
            if mySel_locked_attr:
                for i in mySel_locked_attr:
                    mc.setAttr((mySel_off_grp + '.' + i), lock=False, keyable=True, channelBox=True)
            '''
            # get shape of opposite side ctrl to delete later
            mySel_opp_shape = mc.listRelatives(mySel_off_grp, s=True)
            '''
            #parent under opposite ctrl and freeze attributes to get same exact trans, rot, scale
            mc.parent(mySel_dup[0], mySel_off_grp)
            mc.setAttr(mySel_dup[0] + '.scale', 0.7, 0.7, 0.7)
            mc.makeIdentity(mySel_dup[0], translate=True, rotate=True, scale=True, apply=True)
            mc.Unparent(mySel_dup[0])

            # resize new ctrl
            #mc.setAttr(mySel_dup[0] + '.scale', 0.7, 0.7, 0.7)
            #mc.makeIdentity(mySel_dup[0], translate=True, rotate=True, scale=True, apply=True)
            # set color
            mySel_dup_shape = mc.listRelatives(mySel_dup[0], s=True)
            #color nurbs circle shape
            mc.setAttr((mySel_dup_shape[0] + ".overrideEnabled"), 1)
            mc.setAttr((mySel_dup_shape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((mySel_dup_shape[0] + ".overrideColorRGB"), 0, 1, 1)

            #find shape of duplicated control
            mySel_dup_shape = mc.listRelatives(mySel_dup[0], s=True)
            # parent flipped shape under other side ctrl
            mc.parent(mySel_dup_shape, mySel_off_grp, r=True, s=True)
            # delete unused duplicate transform
            mc.delete(mySel_dup[0])
            '''
            #delete old shape under opposite ctrl
            mc.delete(mySel_opp_shape)
            '''

            #rename new shape after opposite ctrl parent
            for shape in mySel_dup_shape: # for loop in case more than one shape
                myIndex = mySel_dup_shape.index(shape)
                # alphabet_list + '_'
                alphabet_list = '_' + string.ascii_uppercase[:] 
                if shape != mySel_dup_shape[0]:
                    mc.rename(shape, mySel_off_grp + alphabet_list[myIndex] + 'Shape')
                elif shape == mySel_dup_shape[0]:
                    mc.rename(shape, mySel_off_grp + 'Shape')

            # relock and hide attritues
            if mySel_locked_attr:
                for i in mySel_locked_attr:
                    mc.setAttr((mySel + '.' + i), lock=True, keyable=False, channelBox=False)
                    mc.setAttr((mySel_off_grp + '.' + i), lock=True, keyable=False, channelBox=False)

    
    def shape_to_selected(self):
        mySel = mc.ls(sl=True)

        new_obj = mySel[0]
        old_obj = mySel[1]

        # parent and freeze to set position and avoid unwanted movement when parent shape 
        mc.parent( new_obj, old_obj )
        mc.makeIdentity( new_obj, apply=True)
        mc.Unparent(new_obj)

        # get object shape to parent
        new_obj_shp = mc.listRelatives(new_obj, s=True)
        # get object shape to use name
        old_obj_shp = mc.listRelatives(old_obj, s=True)

        mc.parent(new_obj_shp, old_obj, r=True, shape=True)

        mc.delete(old_obj_shp)
        mc.rename(new_obj_shp, old_obj_shp)

        


    def shape_vis_off(self):
        #shape vis off
        mySel = mc.ls(sl=1)

        for i in mySel:
            shape = mc.listRelatives(i, s=True)
            for i in shape:
                mc.setAttr(i + '.visibility', 0)

    def shape_vis_on(self):
        #shape vis off
        mySel = mc.ls(sl=1)

        for i in mySel:
            shape = mc.listRelatives(i, s=True)
            for i in shape:
                mc.setAttr(i + '.visibility', 1)

