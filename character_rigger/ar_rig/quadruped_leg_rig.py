import maya.cmds as mc

import maya.mel as mel

import maya.api.OpenMaya as om

try:
    from itertools import izip as zip
except: # will be python 3.x series
    pass

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

        ankle_jnt = leg_chain[2]

        return leg_chain, hip_jnt, ankle_jnt


    #reverse foot rig locators
    def rev_foot_locators( self, direction, ft_loc_dist ):
        jnt_info = self.find_leg_jnts(direction)
        leg_chain = jnt_info[0]

        leg_chain_pos = []
        leg_chain_rot = []
        for i in leg_chain:
            #query translation
            i_pos = mc.xform(i, query=True, ws=True, t=True)
            #query rotation
            # different rotation order can cause locators to flip 180
            i_rot = mc.xform(i, query=True, ws=True, ro=True)
            leg_chain_pos.append(i_pos)
            leg_chain_rot.append(i_rot)

        ankle_jnt_pos = [leg_chain_pos[2]][0]
        ankle_jnt_rot = [leg_chain_rot[2]][0]

        toe_jnt_pos = [leg_chain_pos[3]][0]
        toe_jnt_rot = [leg_chain_rot[3]][0]
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
            if direction == 'l':
                mc.move( (ft_loc_dist), 0, 0, (loc_toe_end[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_toe_end[0] + '.ty'),  0)  #set at gound level
            if direction == 'r':
                mc.move( -(ft_loc_dist), 0, 0, (loc_toe_end[0]), r=1, os=1, wd=1)
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
            if direction == 'l':
                mc.move( -(ft_loc_dist), 0, 0, (loc_heel[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_heel[0] + '.ty'),  0)  #set at gound level
            if direction == 'r':
                mc.move( (ft_loc_dist), 0, 0, (loc_heel[0]), r=1, os=1, wd=1)
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
            if direction == 'l':
                mc.move( 0, 0, -(ft_loc_dist), (loc_outer_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_outer_foot[0] + '.ty'),  0)  #set at gound level
            if direction == 'r':
                mc.move( 0, 0, (ft_loc_dist), (loc_outer_foot[0]), r=1, os=1, wd=1)
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
            if direction == 'l':
                mc.move( 0, 0, (ft_loc_dist), (loc_inner_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_inner_foot[0] + '.ty'),  0)  #set at gound level
            if direction == 'r':
                mc.move( 0, 0, -(ft_loc_dist), (loc_inner_foot[0]), r=1, os=1, wd=1)
                mc.setAttr((loc_inner_foot[0] + '.ty'),  0)  #set at gound level
        else:
            print(direction + '_loc_inner_foot' + ' Already Exists!')
            mc.select(cl=True)


    # create leg rig ('global_ctrl' for scale offset)
    def create_fk_ik_leg(   self, 
                            direction, 
                            ft_loc_dist,
                            offset_parent_jnt, 
                            swch_ctrl_dist,
                            toe_wiggle_size,
                            rev_foot_size,
                            fk_ctrl_size, 
                            ik_ctrl_size, 
                            pv_ctrl_size, 
                            knee_dist_mult,
                            spine_root_ctrl, 
                            global_ctrl):
        
        # find leg joints using method from own class
        jnt_info = self.find_leg_jnts(direction)
        leg_chain = jnt_info[0]

        '''
        leg_chain = [
                    'tmpJnt_l_leg1',
                    'tmpJnt_l_leg2',
                    'tmpJnt_l_leg3',
                    'tmpJnt_l_foot1',
                    'tmpJnt_l_foot2',
                    'tmpJnt_l_foot3_End'
                    ]
        '''
        sknJnt_preSuff = 'sknJnt_'
        

        #group for organization
        myLegGrp = mc.group(em=True, n= direction + '_leg_grp')

        #______________________________#
        #_____Blended Joint Chain______#
        #______________________________#

        fkJoint_list = []
        ikJoint_list = []
        ikDriverJoint_list = []
        for i in leg_chain:
            #______________________#
            #____create FK chain___#
            fkJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 4)
            #joint color
            mc.setAttr('.useObjectColor', 2)
            mc.setAttr('.wireColorRGB', 1, 0, 0.1)
            
            fkJoint_rename = i.replace(sknJnt_preSuff, 'fkJnt_')
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
            
            ikJoint_rename = i.replace(sknJnt_preSuff, 'ikJnt_')
            ikJoint = mc.rename(ikJoint_orig, ikJoint_rename)
            mc.Unparent(ikJoint)


            # create list of ik joints
            ikJoint_list.append(ikJoint)

            #______________________________#
            #____create _IK Driver chain___#
            ikDriverJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 6)
            #joint color
            mc.setAttr('.useObjectColor', 2)
            mc.setAttr('.wireColorRGB', 0, 0, 1)
            
            ikDriverJoint_rename = i.replace(sknJnt_preSuff, 'drvJnt_')
            ikDriverJoint = mc.rename(ikDriverJoint_orig, ikDriverJoint_rename)
            mc.Unparent(ikDriverJoint)

            # create list of ik joints
            ikDriverJoint_list.append(ikDriverJoint)


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

        #delete unneeded ik driver joints
        mc.delete(ikDriverJoint_list[4])
        mc.delete(ikDriverJoint_list[5])
        #delete unneeded ik driver joint names from their list
        ikDriverJoint_list.pop(5)
        ikDriverJoint_list.pop(4)
        #parent IK Driver joints together based on current index
        currentIndex = -1
        for i in ikDriverJoint_list:
            currentIndex += 1
            if i != ikDriverJoint_list[0]:
                mc.parent(ikDriverJoint_list[currentIndex], ikDriverJoint_list[currentIndex-1])
        
        #blend color node lists
        blendColorsTran_list = []
        blendColorsRot_list = []
        #blend joints together
        for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, leg_chain):
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
        mc.parent(fkJoint_list[0], offset_parent_jnt)

        mc.parent(ikJoint_list[0], offset_parent_jnt)

        mc.parent(ikDriverJoint_list[0], offset_parent_jnt)


        #_______________Stretch Length Joints___________________#
        #_______________________________________________________#
        leg_chain_strchJnts = [ leg_chain[0], leg_chain[3] ]
        strchJnt_lst = []
        for i in leg_chain_strchJnts:
            #______________________#
            #____create FK chain___#
            strchJoint_orig = mc.joint(i)
            
            #joint visual size
            mc.setAttr('.radius', 7)
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
            strchJoint_rename = i.replace(sknJnt_preSuff, 'strchJnt_')
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
        ikHndl_strch = mc.ikHandle(n=direction + '_strchJnts_ikHndl', sj=strchJnt_lst[0], ee=strchJnt_lst[1], sol='ikSCsolver')
        # rename effector
        ikHndl_strch_eff = mc.listConnections(ikHndl_strch, s=True, type='ikEffector')
        mc.rename(ikHndl_strch_eff, ikHndl_strch[0] + '_effector')
        # parented at bottom
        

        #___________create IK HANDLE, driver chain hip to foot, Spring Solver____________#
        # activate/ import spring solver
        mel.eval('ikSpringSolver')

        ikHandleDriver_var = mc.ikHandle( n=direction + '_driverChain_ikHandkle', 
                                    sj=ikDriverJoint_list[0], 
                                    ee=ikDriverJoint_list[3],
                                    sol='ikSpringSolver' )

        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorZ'), 1)

        # rename effector
        ikHandleDriver_effector_var = mc.listConnections(ikHandleDriver_var, s=True, type='ikEffector')
        mc.rename(ikHandleDriver_effector_var, direction + '_driverChain_effector')

        #hide ikHandle
        mc.setAttr(ikHandleDriver_var[0] + '.visibility', 0)

        #parent grp to global grp to organize
        #mc.parent(ikHandleDriver_var[0], myLegGrp)


        

        
        #___________create IK HANDLE, hip to ankle, Rotate Plane Solver____________#

        ikHandleAnkle_var = mc.ikHandle(n=direction + '_ankle_ikHandkle', sj=ikJoint_list[0], ee=ikJoint_list[2])

        mc.setAttr((ikHandleAnkle_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandleAnkle_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandleAnkle_var[0] + '.poleVectorZ'), 0)

        ikHandle_effector_var = mc.listConnections(ikHandleAnkle_var, s=True, type='ikEffector')

        mc.rename(ikHandle_effector_var, ikHandleAnkle_var[0] + '_effector')

        #hide ikHandle
        mc.setAttr(ikHandleAnkle_var[0] + '.visibility', 0)


        #___________create IK HANDLE, knee to foot, Rotate Plane Solver____________#

        ikHandleFoot_var = mc.ikHandle( n=direction + '_foot_ikHandkle', sj=ikJoint_list[1], ee=ikJoint_list[3] )

        mc.setAttr((ikHandleFoot_var[0] + '.poleVectorX'), 0)
        mc.setAttr((ikHandleFoot_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandleFoot_var[0] + '.poleVectorZ'), 0)

        ikHandleFoot_effector_var = mc.listConnections(ikHandleFoot_var, s=True, type='ikEffector')

        mc.rename(ikHandleFoot_effector_var, direction + '_foot_effector')

        #hide ikHandle
        mc.setAttr(ikHandleFoot_var[0] + '.visibility', 0)

        #parent ikHandle ankle to ikDriver foot joint
        mc.parent(ikHandleFoot_var[0], ikDriverJoint_list[3])




        #___________ikHandle ankle offset ctrl____________#
        ikAnkleOff_group_list = []
        ikAnkleOff_ctrl_list = []
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
            mc.setAttr((myCurve + '.scale'), ik_ctrl_size * .5, ik_ctrl_size * .5, ik_ctrl_size * .5)
            mc.setAttr((myCurve + '.translate'), -13, 40, 0)
            # pivot to world origin
            mc.xform (myCurve, ws=True, piv= (0, 0, 0))
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorRGB'), 0.5, 1, 0)

            #rename curve
            myCurve = mc.rename(direction + '_ikAnkleOff_ctrl')
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
            ikAnkleOff_group_list.append(myGroup)
            ikAnkleOff_ctrl_list.append(myCurve)

        #so that l is oriented same as right
        #mc.setAttr((ikAnkleOff_group_list[0] + '.rotate'), 0, -90, 0)

        #lock and hide unneeded ankle offset ctrl attributes
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.tx'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.ty'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.tz'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.sx'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.sy'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.sz'), lock=True, keyable=False, channelBox=False)
        # mc.setAttr((ikAnkleOff_ctrl_list[0] + '.visibility'), lock=True, keyable=False, channelBox=False)

        #________________________#
        # parent constain ankle ik handle to offset ctrl
        #mc.parentConstraint( ikAnkleOff_ctrl_list[0], ikHandleAnkle_var[0], mo=True , sr=('x','y','z') )
        mc.parent( ikHandleAnkle_var[0], ikAnkleOff_ctrl_list[0])
        mc.parent( ikAnkleOff_group_list[0], myLegGrp)
        mc.parentConstraint(ikDriverJoint_list[2], ikAnkleOff_group_list[0], mo=True)
        mc.scaleConstraint(ikDriverJoint_list[2], ikAnkleOff_group_list[0]) # for global scale

        # parent constrain offset ctrl grp to driver ankle joint
        #mc.parentConstraint( ikDriverJoint_list[3], ikAnkleOff_group_list[0], mo=True )


        #___________ikHandle foot CTRL____________#
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
            myCurve = mc.rename(direction + '_ikFoot_ctrl')
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
            ik_group_list.append(myGroup)
            ik_ctrl_list.append(myCurve)

            # add Soft Ik/ No Ik stretch ctrl
            mc.addAttr(myCurve, ln='Stretch_Blend', nn='Stretch_Blend', min=0, max=1, at='double', dv=1, k=1)
        
        #so that l is oriented same as right
        mc.setAttr((ik_group_list[0] + '.rotate'), 0, -90, 0)


        #___________ik hip CTRL____________#
        # not needed, but added for extra hip translation, (and to parent measure control to)
        ik_hip_group_list = []
        ik_hip_ctrl_list = []
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
            myCurve = mc.rename(direction + '_ikHip_ctrl')
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
            ik_hip_group_list.append(myGroup)
            ik_hip_ctrl_list.append(myCurve)


        #set ctrl grp rotate to (to be world space flat, and similar to joint orient)
        mc.setAttr((ik_hip_group_list[0] + '.rotate'), 0, 0, 0)

        # parent constrain hip ctrl to hip jnt (translation only)
        mc.parentConstraint(ik_hip_ctrl_list[0], ikJoint_list[0], sr=('x', 'y', 'z'))
        # parent constrain hip ctrl to drv jnt top
        mc.parentConstraint(ik_hip_ctrl_list[0], ikDriverJoint_list[0], sr=('x', 'y', 'z'))
        # parent constrain hip ctrl to top strch jnt
        mc.parentConstraint(ik_hip_ctrl_list[0], strchJnt_lst[0], sr=('x', 'y', 'z'))

        # lock and hide rotation values for hip control
        mc.setAttr((ik_hip_ctrl_list[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_hip_ctrl_list[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((ik_hip_ctrl_list[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        
        

        #_________________POLE VECTOR KNEE___________________#
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
            myCurve = mc.rename(direction + '_knee_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
            

            #length of main limb (knee .tx + ankle .tx)
            limb_lenA = 0
            for i in ikJoint_list[1:3]:
                limb_lenA += mc.getAttr(i + '.translateX')

            #length of upper half of limb (knee jnt translate x)
            upperLimb_lenA = mc.getAttr(ikJoint_list[1] + '.translateX')

            #divide sum of leg lengths by upper leg length (for more accurate mid point)
            better_midPoint_var = (limb_lenA / upperLimb_lenA)

            #__vector math____#
            #vector positions of hip, knee, ankle
            hip_pos = om.MVector(mc.xform(ikJoint_list[0], q=True, rp=True, ws=True))
            knee_pos = om.MVector(mc.xform(ikJoint_list[1], q=True, rp=True, ws=True))
            ankle_pos = om.MVector(mc.xform(ikJoint_list[2], q=True, rp=True, ws=True))

            #finding vector point of pv knee (on plane of hip, knee, ankle)
            hip_to_ankle = ankle_pos - hip_pos
            hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
            mid_point = hip_pos + hip_to_ankle_scaled
            mid_point_to_knee_vec = knee_pos - mid_point
            mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * knee_dist_mult  #pv ctrl distance from knee multiplier
            mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

            #final polve vector point (to avoid knee changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

            myAimConst = mc.aimConstraint(  ikJoint_list[1], 
                                            myGroup, 
                                            offset=(0, 0, 0), 
                                            weight=1, 
                                            aimVector=(0, 0, -1), 
                                            upVector=(0, 1, 0), 
                                            worldUpType=('vector'), 
                                            worldUpVector=(0, 1, 0) )
            mc.delete(myAimConst)

            #___connect pole vector
            mc.poleVectorConstraint(myCurve, ikHandleAnkle_var[0])

            # connect scale of knee and pole vector control (scale constraint creates cyclical error)
            #mc.connectAttr( (myCurve + '.scale'), ( ikJoint_list[1] ) + '.scale', f=True)

            #parent grp to global grp to organize
            mc.parent(myGroup, global_ctrl)

            pv_group_list.append(myGroup)
            pv_ctrl_list.append(myCurve)

        #parent pole vector control under ik foot ctrl
        #mc.parent(pv_group_list[0], ik_ctrl_list[0])
        #mc.parent(pv_group_list[0], global_ctrl[0])


        #_________________POLE VECTOR ANKLE___________________#
        #_____________________________________________________#
        anklePV_group_list = []
        anklePV_ctrl_list = []
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
            myCurve = mc.rename(direction + '_ankle_poleVector_ctrl')
            #group curve
            curveGrouped = mc.group(myCurve)
            curveGrouped_offset = mc.group(myCurve)
            #rename group
            myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
            myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
            
            #length of main limb
            limb_lenA = 0
            for i in ikJoint_list[1:3]:
                limb_lenA += mc.getAttr(i + '.translateX')

            #length of upper half of limb 
            upperLimb_lenA = mc.getAttr(ikJoint_list[1] + '.translateX')

            #divide sum of leg lengths by upper leg length (for more accurate mid point)
            better_midPoint_var = (limb_lenA / upperLimb_lenA)

            #__vector math____#
            #vector positions of knee, ankle, foot
            knee_pos = om.MVector(mc.xform(ikJoint_list[1], q=True, rp=True, ws=True))
            ankle_pos = om.MVector(mc.xform(ikJoint_list[2], q=True, rp=True, ws=True))
            foot_pos = om.MVector(mc.xform(ikJoint_list[3], q=True, rp=True, ws=True))

            #finding vector point of pv ankle (on plane of knee, ankle, foot)
            knee_to_foot = foot_pos - knee_pos
            knee_to_foot_scaled = knee_to_foot / better_midPoint_var #/two-ish
            mid_point = knee_pos + knee_to_foot_scaled
            mid_point_to_ankle_vec = ankle_pos - mid_point
            mid_point_to_ankle_vec_scaled = mid_point_to_ankle_vec * knee_dist_mult  #pv ctrl distance from ankle multiplier
            mid_point_to_ankle_point = mid_point + mid_point_to_ankle_vec_scaled

            #final polve vector point (to avoid ankle changing position on creation)
            final_PV_point = mc.xform(myGroup, t=mid_point_to_ankle_point)

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
            mc.poleVectorConstraint(myCurve, ikHandleFoot_var[0])

            #parent grp to global grp to organize
            mc.parent(myGroup, global_ctrl)

            anklePV_group_list.append(myGroup)
            anklePV_ctrl_list.append(myCurve)

        #parent pole vector control under ik foot ctrl
        #mc.parent(anklePV_group_list[0], ik_ctrl_list[0])
        #mc.parent(anklePV_group_list[0], global_ctrl[0])



        
        #______________________________________________________________________________#
        #____________________________IK/ FK Switch Ctrl _______________________________#
        #______________________________________________________________________________#

        switch_ctrl_list = []
        switch_ctrl_grp_list = []
        for i in range(0,1):
            #name circle curves
            if direction == 'l':
                switchCurveA_name = 'l_legSwtch_ctrl'
                switchCurveB_name = 'l_legSwtch_ctrlA'
                switchCurveC_name = 'l_legSwtch_ctrlB'
            if direction == 'r':
                switchCurveA_name = 'r_legSwtch_ctrl'
                switchCurveB_name = 'r_legSwtch_ctrlA'
                switchCurveC_name = 'r_legSwtch_ctrlB'

            #create nurbs circle
            switchCurveA = mc.circle(n=switchCurveA_name, ch=False, r=rev_foot_size, nr=(0,1,0))
            #create variable for nurbs circle shape
            switchCurveA_shape = mc.listRelatives(switchCurveA, s=True)
            #color nurbs circle shape
            mc.setAttr((switchCurveA_shape[0] + '.overrideEnabled'), 1)
            mc.setAttr((switchCurveA_shape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((switchCurveA_shape[0] + '.overrideColorRGB'), 0, .5, 1)

            #create 2nd nurbs circle
            switchCurveB = mc.circle(n=switchCurveB_name, ch=False, r=rev_foot_size, nr=(0,0,0))
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
            switchCurveC = mc.circle(n=switchCurveC_name, ch=False, r=rev_foot_size, nr=(1,0,0))
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


            
            # #_______move ctrl shapes in -z_______#
            # if direction == 'l':
            #     mc.setAttr((switchCurveA[0] + '.tx'), -(swch_ctrl_dist))
            # elif direction == 'r':
            #     mc.setAttr((switchCurveA[0] + '.tx'), (swch_ctrl_dist))
            
            mc.setAttr((switchCurveA[0] + '.tx'), -(swch_ctrl_dist))

            mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
            mc.makeIdentity(switchCurveA, apply=True)

            #_______move joint to ankle and parent_______#
            #parent and zero joints to last joint in selection
            mc.parent(switchCurveA_grp, leg_chain[3], relative=True)
            #parent joints to world space
            mc.Unparent(switchCurveA_grp)

            # parent and scale constrain switch ctrl to ankle
            mc.parentConstraint(leg_chain[3], switchCurveA_grp, mo=True)
            mc.scaleConstraint(leg_chain[3], switchCurveA_grp)

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
            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
            mc.setAttr((ik_group_list[0] + '.visibility'), 1)
            mc.setAttr((ikAnkleOff_group_list[0] + '.visibility'), 1)
            mc.setAttr((pv_group_list[0] + '.visibility'), 1)
            mc.setAttr((anklePV_group_list[0] + '.visibility'), 1)
            mc.setAttr((ik_hip_group_list[0] + '.visibility'), 1)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)


            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ikAnkleOff_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((anklePV_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_hip_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


            mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
            mc.setAttr((ik_group_list[0] + '.visibility'), 0)
            mc.setAttr((ikAnkleOff_group_list[0] + '.visibility'), 0)
            mc.setAttr((pv_group_list[0] + '.visibility'), 0)
            mc.setAttr((anklePV_group_list[0] + '.visibility'), 0)
            mc.setAttr((ik_hip_group_list[0] + '.visibility'), 0)
            mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)


            mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ikAnkleOff_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((anklePV_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((ik_hip_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
            mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


    
    #________________________________________________________________________________#
    #________________________END of FK/IK BLEND______________________________________#

        #_________________Reverse Foot Rig___________________#
        #____________________________________________________#

        # create locators for reverse foot if not exist, also declare locator list
        if direction == 'r':
            self.rev_foot_locators(direction ='r', ft_loc_dist = ft_loc_dist)
            # declare locator list          
            rvFoot_loc_list = ( 'r_loc_ankle', 
                                'r_loc_toe', 
                                'r_loc_toe_end', 
                                'r_loc_heel', 
                                'r_loc_outer_foot', 
                                'r_loc_inner_foot')
        elif direction == 'l':
            self.rev_foot_locators(direction ='l', ft_loc_dist = ft_loc_dist)
            # declare locator list          
            rvFoot_loc_list = ( 'l_loc_ankle', 
                                'l_loc_toe', 
                                'l_loc_toe_end', 
                                'l_loc_heel', 
                                'l_loc_outer_foot', 
                                'l_loc_inner_foot')

        # create controls for locators
        ftCtrl_list = []
        ftCtrl_grp_list = []
        for i in rvFoot_loc_list:
            #name circle curves
            locCurveA_name = i.replace('loc_', 'ftCtrl_')
            locCurveB_name = i.replace('loc_', 'ftCtrl_') + 'A'
            locCurveC_name = i.replace('loc_', 'ftCtrl_') + 'B'

            #create nurbs circle
            locCurveA = mc.circle(n=locCurveA_name, ch=False, r=rev_foot_size, nr=(0,1,0))
            #create variable for nurbs circle shape
            locCurveA_shape = mc.listRelatives(locCurveA, s=True)
            #color nurbs circle shape
            mc.setAttr((locCurveA_shape[0] + ".overrideEnabled"), 1)
            mc.setAttr((locCurveA_shape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((locCurveA_shape[0] + ".overrideColorRGB"), .5, 1, 0)

            #create 2nd nurbs circle
            locCurveB = mc.circle(n=locCurveB_name, ch=False, r=rev_foot_size, nr=(0,0,0))
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
            locCurveC = mc.circle(n=locCurveC_name, ch=False, r=rev_foot_size, nr=(1,0,0))
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

            #_______group ctrl_______#
            locCurveA_grp = mc.group(locCurveA, n = (locCurveA[0] + '_grp'))
            locCurveA_grp_offset = mc.group(locCurveA, n = (locCurveA[0] + '_grp_offset'))

            #_______move ctrl grp to loc_______#
            mc.parent(locCurveA_grp, i, relative=True)
            mc.Unparent(locCurveA_grp)
            #add/ create list for ftCtrl's
            ftCtrl_list.append(locCurveA)
            ftCtrl_grp_list.append(locCurveA_grp)

        #group reverse foot ctrls together
        mc.parent(ftCtrl_grp_list[4], ftCtrl_list[5])
        mc.parent(ftCtrl_grp_list[3], ftCtrl_list[4])
        mc.parent(ftCtrl_grp_list[2], ftCtrl_list[3])
        mc.parent(ftCtrl_grp_list[1], ftCtrl_list[2])
        mc.parent(ftCtrl_grp_list[0], ftCtrl_list[1])

        #group reverse foot ctrls under ankle ctrl
        mc.parent(ftCtrl_grp_list[-1], ik_ctrl_list[0])
        
        # create extra toe offset ctrl_______
        toe_wiggle_list = []
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
            mc.setAttr((myCurve + '.scale'), 4.5, 3, 6)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            # scale again after shape created
            mc.setAttr((myCurve + '.scale'), toe_wiggle_size, toe_wiggle_size, toe_wiggle_size)
            #freeze transforms
            mc.makeIdentity(myCurve, apply=True)
            #select curve box's shape
            curveShape = mc.listRelatives(myCurve, s=True)
            #color curve box's shape red
            mc.setAttr((curveShape[0] + '.overrideEnabled'), 1)
            mc.setAttr((curveShape[0] + '.overrideRGBColors'), 1)
            mc.setAttr((curveShape[0] + '.overrideColorRGB'), 1, 0, 1)
            #rename curve
            myCurve = mc.rename(direction + '_ftCtrl' + '_toe_wiggle')
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
            # append to list for later use
            toe_wiggle_list.append(myCurve)

        
        #___________reverse foot joint parenting___________#

        #parent reverse foot ankle ctrl to ikHandle trans and ankle joint rotate
        mc.parentConstraint(ftCtrl_list[0], ikJoint_list[3], mo=True, st=('x', 'y', 'z')) 

        # parent toe
        mc.parentConstraint(toe_wiggle_list[0], ikJoint_list[4], mo=True, st=('x', 'y', 'z')) #rotation only parent
        
        # direct translation connect with offset #(i believe this was to avoid toe/ foot stretch glitch)
        toe_plusMinusAv = mc.shadingNode('plusMinusAverage', asUtility=True, n= direction + '_toe_plusMinusAv' )
        #connect to get trans attr, then disconnect, versus parent/ point constraint acts weird on non stretch IK
        mc.connectAttr(ikJoint_list[4] + '.translate', toe_plusMinusAv + '.input3D[1]', f=True) #get offset 
        mc.disconnectAttr(ikJoint_list[4] + '.translate', toe_plusMinusAv + '.input3D[1]')  #then disconnect
        #connect toe translation now with offset
        mc.connectAttr(toe_wiggle_list[0] + '.translate', toe_plusMinusAv + '.input3D[0]', f=True) #get offset 
        #connect plusMinus with offset toe value into ik toe jnt, to replace the clunky point constraint alternative
        mc.connectAttr(toe_plusMinusAv + '.output3D', ikJoint_list[4] + '.translate', f=True)

        
        # ______________________________________________________#
        # post reverse foot parenting
        #________________________________#
        # stretch jnt ik handle parenting
        
        ikHndl_strch_grp0 = mc.group(em=1)
        ikHndl_strch_grp_offs0 = mc.group(em=1)
        #rename group
        ikHndl_strch_grp1 = mc.rename(ikHndl_strch_grp0, (ikHndl_strch[0] + '_grp'))
        ikHndl_strch_grp_offs1 = mc.rename(ikHndl_strch_grp_offs0, (ikHndl_strch[0] + '_grp_offset'))
        
        #pos parent grp
        mc.parent(ikHndl_strch_grp_offs1, ikHndl_strch_grp1)
        mc.parent(ikHndl_strch_grp1, ftCtrl_list[0], r=1) # to position
        mc.parent(ikHndl_strch_grp1, myLegGrp) # final spot
        mc.parent(ikHndl_strch[0], ikHndl_strch_grp_offs1)
        # point constrain to foot ctrl
        mc.pointConstraint( ftCtrl_list[0], ikHndl_strch_grp1, mo=True )
        # orient constrain to global ctrl
        mc.orientConstraint( global_ctrl, ikHndl_strch_grp1, mo=True )
        
        
        #______________________________________#
        # spring solver jnt ik handle parenting
        # ikHndl grp
        ikHndl_drv_grp0 = mc.group(em=1)
        ikHndl_drv_grp_offs0 = mc.group(em=1)
        #rename group
        ikHndl_drv_grp1 = mc.rename(ikHndl_drv_grp0, (ikHandleDriver_var[0] + '_grp'))
        ikHndl_drv_grp_offs1 = mc.rename(ikHndl_drv_grp_offs0, (ikHandleDriver_var[0] + '_grp_offset'))
        #pos parent grp
        mc.parent(ikHndl_drv_grp_offs1, ikHndl_drv_grp1, r=1)
        #parent to bottom stretch joint
        mc.parent(ikHndl_drv_grp1, strchJnt_lst[1], r=1)
        mc.parent(ikHandleDriver_var[0], ikHndl_drv_grp_offs1)
        


        # ______________________________________________________#
        # __________________ IK stretchy leg ___________________#
        # ______________________________________________________#

        # get joint x lengths
        to_knee_len = mc.getAttr(ikJoint_list[1] + '.tx')
        to_ankle_len = mc.getAttr(ikJoint_list[2] + '.tx')
        to_foot_len = mc.getAttr(ikJoint_list[3] + '.tx')
        # create ruler tool
        ik_jnt_ruler_temp = mc.distanceDimension( sp=(0, 0, 0), ep=(0, 0, 10) )
        ik_jnt_ruler = mc.rename(ik_jnt_ruler_temp, ( direction + '_ik_jnt_rulerShape' ) )
        # rename transform parent of distanceDimesion tool
        ruler_loc_list_rel = mc.listRelatives( ik_jnt_ruler, ap=1, type='transform' )
        ruler_loc_list_parent = mc.rename(ruler_loc_list_rel, direction + '_ik_jnt_ruler')

        # get locators controling length
        ruler_loc_list = mc.listConnections( ik_jnt_ruler, type='locator' )
        # rename and hide distance locators
        leg_loc_0 = mc.rename(ruler_loc_list[0], direction + '_hip_dist_loc')
        leg_loc_1 = mc.rename(ruler_loc_list[1], direction + '_ankle_dist_loc')
        # parent constraint measure locators to ctrls (ruler loc is ends of distanceMeasure tool)
        mc.parentConstraint(ik_hip_ctrl_list[0], leg_loc_0 )
        mc.parentConstraint(ftCtrl_list[0], leg_loc_1 )


        #______________________________#

        prefix = 'leg'

        #______Function Variables_______#
        #variable ... ruler distance output
        ruler_dist = ik_jnt_ruler + '.distance'
        ruler_dist_result = mc.getAttr(ik_jnt_ruler + '.distance')

        #variable ... global_ctrl scale X
        global_ctrl_sclX = global_ctrl + '.scaleX'

        #variable
        stretch_blend = ik_ctrl_list[0] + '.Stretch_Blend'



        # _______________create nodes____________________#

        # part1 ... ikHandle grp nodes
        stretch_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_stretch_dist_ratio' ) # create multDiv node
        mc.setAttr(stretch_dist_ratio + '.operation', 2) # set to Divide

        global_scale_offs = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_global_scale_offs' ) # default is multiply

        ikHndl_fllw_pma = mc.shadingNode('plusMinusAverage', asUtility=1, n = direction + '_' + prefix + '_ikHandle_follow_pma' ) # for ik handle to follow hip ctrl
        mc.setAttr(ikHndl_fllw_pma + '.operation', 2) # set to Subtract

        glbl_offs_ikHndl_fllw = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_global_scale_offs_ikHndl_follow' ) # global scale offset for ikHandle follow grp
        mc.setAttr(glbl_offs_ikHndl_fllw + '.operation', 2) # set to Divide

        clamp_end_stop = mc.shadingNode('clamp', asUtility=1, n = direction + '_' + prefix + '_clamp_end_stop' ) # limit ikHndl follow grp from going past ankle/ wrist

        invert_node = mc.shadingNode('multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_invert_node' ) # invert value to negative, or positive, if already neg

        softIk_fllw_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + prefix + '_softIk_fllw_grp_blend' ) # blend between 0 or follow

        softIk_fllw_offs_grp_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + prefix + '_softIk_fllw_offs_grp_blend' ) # smooth ikHndl grp follow


        # part2 ... joint nodes

        drvJnt_strch_ratio = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_drvJnt_strch_ratio' )

        ikHdl_grp_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = direction + '_' + prefix + '_ikHdl_grp_smooth_setDrvKey' )


        # knee joints nodes

        knee_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_knee_strch' )

        mainJnts_smooth_setDrvKey = mc.shadingNode( 'animCurveUU', asUtility=1, n = direction + '_' + prefix + '_mainJnts_smooth_setDrvKey' )
        mc.setAttr(mainJnts_smooth_setDrvKey + '.preInfinity', 1)

        knee_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_knee_smooth_offs' )

        knee_stretch_clamp = mc.shadingNode('clamp', asUtility=1, n = direction + '_' + prefix + '_knee_stretch_clamp' )

        knee_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + prefix + '_knee_stretch_blend' )


        # ankle jnt nodes

        ankle_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_ankle_strch' )

        ankle_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_ankle_smooth_offs' )

        ankle_stretch_clamp = mc.shadingNode('clamp', asUtility=1, n = direction + '_' + prefix + '_ankle_stretch_clamp' )

        ankle_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + prefix + '_ankle_stretch_blend' )


        # foot jnt nodes

        foot_strch = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_foot_strch' )

        foot_smooth_offs = mc.shadingNode( 'multiplyDivide', asUtility=1, n = direction + '_' + prefix + '_foot_smooth_offs' )

        foot_stretch_clamp = mc.shadingNode('clamp', asUtility=1, n = direction + '_' + prefix + '_foot_stretch_clamp' )

        foot_stretch_blend = mc.shadingNode('blendColors', asUtility=1, n = direction + '_' + prefix + '_foot_stretch_blend' )

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

        #mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=0, value=0, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change
        #mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=50, value=15)
        #mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=150, value=23.5)

        mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=0, value=0, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change
        mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=35, value=25)
        mc.setKeyframe(ikHdl_grp_smooth_setDrvKey, float=100, value=29.3)

        mc.connectAttr( clamp_end_stop + '.outputR', softIk_fllw_grp_blend + '.color2R', f=1 )  # sets follow grp to follow constant distance from hip ctrl
        mc.setAttr(softIk_fllw_grp_blend + '.color1R', 0) # set ikHndl grp follow to 0, to stay at ankle/ wrist
        mc.connectAttr( stretch_blend, softIk_fllw_grp_blend + '.blender', f=1 )

        mc.connectAttr( ikHdl_grp_smooth_setDrvKey + '.output', softIk_fllw_offs_grp_blend + '.color2R', f=1 )  # sets follow offset grp to smoothly adjust follow distance for softIK
        mc.setAttr(softIk_fllw_offs_grp_blend + '.color1R', 0) # set ikHndl offset grp follow to 0, to have no effect
        mc.connectAttr( stretch_blend, softIk_fllw_offs_grp_blend + '.blender', f=1 )

        mc.connectAttr( softIk_fllw_offs_grp_blend + '.outputR', ikHndl_drv_grp_offs1 + '.tx', f=1 ) # connect to ikHandle Grp
        mc.connectAttr( softIk_fllw_grp_blend + '.outputR', ikHndl_drv_grp1 + '.tx', f=1 ) # connect to ikHandle Grp offset

        

        # part2 ... joint connections

        mc.connectAttr( ruler_dist, stretch_dist_ratio + '.input1X', f=1 ) # create stretch ratio
        mc.connectAttr( global_scale_offs + '.outputX', stretch_dist_ratio + '.input2X', f=1 ) # create stretch ratio

        mc.connectAttr( stretch_dist_ratio + '.outputX', drvJnt_strch_ratio + '.input1X', f=1 ) # create drv jnt stretch ratio
        mc.setAttr(drvJnt_strch_ratio + '.input2X', ruler_dist_result) #set drv jnt stretch ratio 2X to static ruler distance default
        mc.connectAttr( drvJnt_strch_ratio + '.outputX', strchJnt_lst[1] + '.translateX', f=1 ) # create drv jnt stretch ratio



        # knee / elbow jnt connections _______________________________
        mc.connectAttr( stretch_dist_ratio + '.outputX', knee_strch + '.input1X', f=1 ) # knee stretch amount, base length multiplied by stretch ratio
        mc.setAttr(knee_strch + '.input2X', to_knee_len)
        
        mc.connectAttr( stretch_dist_ratio + '.outputX', mainJnts_smooth_setDrvKey + '.input', f=1 ) # smooth offset keys
        
        #mc.setKeyframe(mainJnts_smooth_setDrvKey, float=0.5, value=1.75, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change # also ajust spline afterwards
        #mc.setKeyframe(mainJnts_smooth_setDrvKey, float=1, value=1)
        #mc.setKeyframe(mainJnts_smooth_setDrvKey, float=2, value=0.865)

        mc.setKeyframe(mainJnts_smooth_setDrvKey, float=0.5, value=1.7, inTangentType='spline', outTangentType='spline')  #set keys for jnt length change # also ajust spline afterwards
        mc.setKeyframe(mainJnts_smooth_setDrvKey, float=1, value=1)
        mc.setKeyframe(mainJnts_smooth_setDrvKey, float=2, value=0.83)
        

        mc.connectAttr( knee_strch + '.outputX', knee_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
        mc.connectAttr( mainJnts_smooth_setDrvKey + '.output', knee_smooth_offs + '.input2X', f=1 )

        #mc.connectAttr( knee_smooth_offs + '.outputX', knee_stretch_clamp + '.inputR', f=1 ) # connect jnt length to have bottom value clamped during stretch
        #mc.setAttr(knee_stretch_clamp + '.minR', ( to_knee_len * 0.80) ) #clamp smallest length value  #0.83, exact from test  
        #mc.setAttr(knee_stretch_clamp + '.maxR', 1000) # just to have a high that will not be reached

        mc.connectAttr( knee_smooth_offs + '.outputX', knee_stretch_blend + '.color1R', f=1 )
        #mc.connectAttr( knee_stretch_clamp + '.outputR', knee_stretch_blend + '.color1R', f=1 ) # blend between stretch and no stretch default static length
        mc.setAttr(knee_stretch_blend + '.color2R', to_knee_len )  # set to default jnt length, static value

        mc.connectAttr( knee_stretch_blend + '.outputR', ikJoint_list[1] + '.translateX', f=1 ) # connect blend to jnt translate X length
        mc.connectAttr( knee_stretch_blend + '.outputR', ikDriverJoint_list[1] + '.translateX', f=1 ) # connect blend to drvJnt translate X length

        mc.connectAttr( stretch_blend, knee_stretch_blend + '.blender', f=1 )  # foot ctrl stretch blend attr


        # ankle jnt _______________________________
        mc.connectAttr( stretch_dist_ratio + '.outputX', ankle_strch + '.input1X', f=1 )
        mc.setAttr(ankle_strch + '.input2X', to_ankle_len)
        

        mc.connectAttr( ankle_strch + '.outputX', ankle_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
        mc.connectAttr( mainJnts_smooth_setDrvKey + '.output', ankle_smooth_offs + '.input2X', f=1 )

        #mc.connectAttr( ankle_smooth_offs + '.outputX', ankle_stretch_clamp + '.inputR', f=1 ) # connect jnt length to have bottom value clamped during stretch
        #mc.setAttr(ankle_stretch_clamp + '.minR', ( to_ankle_len * 0.80) ) #clamp smallest length value  #0.83, exact from test  
        #mc.setAttr(ankle_stretch_clamp + '.maxR', 1000) # just to have a high that will not be reached

        mc.connectAttr( ankle_smooth_offs + '.outputX', ankle_stretch_blend + '.color1R', f=1 )
        #mc.connectAttr( ankle_stretch_clamp + '.outputR', ankle_stretch_blend + '.color1R', f=1 ) # blend between stretch and no stretch default static length
        mc.setAttr(ankle_stretch_blend + '.color2R', to_ankle_len )  # set to default jnt length, static value

        mc.connectAttr( ankle_stretch_blend + '.outputR', ikJoint_list[2] + '.translateX', f=1 ) # connect blend to jnt translate X length
        mc.connectAttr( ankle_stretch_blend + '.outputR', ikDriverJoint_list[2] + '.translateX', f=1 ) # connect blend to drvJnt translate X length

        mc.connectAttr( stretch_blend, ankle_stretch_blend + '.blender', f=1 )  # foot ctrl stretch blend attr


        # foot jnt _______________________________
        mc.connectAttr( stretch_dist_ratio + '.outputX', foot_strch + '.input1X', f=1 )
        mc.setAttr(foot_strch + '.input2X', to_foot_len)
        

        mc.connectAttr( foot_strch + '.outputX', foot_smooth_offs + '.input1X', f=1 ) # smooth stretch offset, with set driven key
        mc.connectAttr( mainJnts_smooth_setDrvKey + '.output', foot_smooth_offs + '.input2X', f=1 )

        #mc.connectAttr( foot_smooth_offs + '.outputX', foot_stretch_clamp + '.inputR', f=1 ) # connect jnt length to have bottom value clamped during stretch
        #mc.setAttr(foot_stretch_clamp + '.minR', ( to_foot_len * 0.80) ) #clamp smallest length value  #0.83, exact from test  
        #mc.setAttr(foot_stretch_clamp + '.maxR', 1000) # just to have a high that will not be reached

        mc.connectAttr( foot_smooth_offs + '.outputX', foot_stretch_blend + '.color1R', f=1 )
        #mc.connectAttr( foot_stretch_clamp + '.outputR', foot_stretch_blend + '.color1R', f=1 ) # blend between stretch and no stretch default static length
        mc.setAttr(foot_stretch_blend + '.color2R', to_foot_len )  # set to default jnt length, static value

        mc.connectAttr( foot_stretch_blend + '.outputR', ikJoint_list[3] + '.translateX', f=1 ) # connect blend to jnt translate X length
        mc.connectAttr( foot_stretch_blend + '.outputR', ikDriverJoint_list[3] + '.translateX', f=1 ) # connect blend to drvJnt translate X length

        mc.connectAttr( stretch_blend, foot_stretch_blend + '.blender', f=1 )  # foot ctrl stretch blend attr


        #________________#
        #________________#


        
        #___________________________________________________________________#
        #___________________Visibility and Parenting________________________#
        #___________________________________________________________________#

        # set ankle reverse foot control to invisible (not needed to be seen)
        mc.setAttr(ftCtrl_grp_list[0] + '.visibility', 0)
        # stretch joint ik handle grp to invisible
        mc.setAttr(ikHndl_strch_grp1 + '.visibility', 0)
        # hide dist loc and tool
        mc.setAttr(ruler_loc_list_parent + '.visibility', 0)
        mc.setAttr(leg_loc_0 + '.visibility', 0)
        mc.setAttr(leg_loc_1 + '.visibility', 0)
        #parent grp to global grp to organize
        mc.parent(ruler_loc_list_parent, myLegGrp)
        mc.parent(leg_loc_0, myLegGrp)
        mc.parent(leg_loc_1, myLegGrp)
        # delete or hide foot locators
        for i in rvFoot_loc_list: mc.setAttr(i + '.visibility', 0)
        #mc.delete(rvFoot_loc_list)
        
        # parent switch grp to main leg grp
        mc.parent(switch_ctrl_grp_list, myLegGrp)

        # set default to ik leg
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)


        #_______Other_________#
        #_____________________#
        # set pole vector to avoid knee flipping
        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorX'), 1)
        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorY'), 0)
        mc.setAttr((ikHandleDriver_var[0] + '.poleVectorZ'), 0)


        # return top ik and fk controls to parent to hip
        return ik_hip_group_list[0], fk_ctrl_grp_list[0], myLegGrp

        

# NOTES
#______
# Pole Vector for Driver Ik chain may need to be adjust if driver chain oriented wrong on direction

# adjust set driven key for soft ik stretch and non stretch after creation

# make sure to have reverse foot placement locators, and pv elbow locators, and bounding box for joints

# Misc Values
# wyvern
# non_stetch leg soft ik
# 0, 35, 100.... 0, 25, 29.3
# stetch leg soft ik
# 0.5, 1, 2.... 1.7, 1, 0.83

# non_stetch arm soft ik
# 0, 50, 150.... 0, 17, 22.05
# stetch arm soft ik
# 0.3, .0.5, 1, 2.... 3, 2, 1, 0.883