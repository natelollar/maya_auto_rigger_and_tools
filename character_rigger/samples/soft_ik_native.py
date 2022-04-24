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

    #main ik handle, RPS ___________
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




    # create node graph
    
    













'''
## import _____ ## use in maya script editor to execute script

import maya.cmds as mc

import imp

import character_rigger.samples.soft_ik_native

imp.reload( character_rigger.samples.soft_ik_native)

character_rigger.samples.soft_ik_native.soft_ik_native()

'''