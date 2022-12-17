import maya.cmds as mc

def rename_script():
    mc.rename("main_R_leg_002q", "main_R_leg_002")
    mc.rename("main_R_leg_rollq", "main_R_leg_roll")

    mc.rename("main_head_end1", "main_head_antenna")
    mc.rename("main_head_end2", "main_head_antenna_end")

    mc.rename("main_L_shoulderPad", "main_shoulderPad_L")
    mc.rename("main_L_shoulderPad_end", "main_shoulderPad_L_end")

    mc.rename("main_powerPack1", "main_powerPack_rocket_L")
    mc.rename("main_powerPack6", "main_powerPack_rocket_L_end")

    mc.rename("main_powerPack_end1", "main_powerPack_turnVentA_L")
    mc.rename("main_powerPack_turnVentA_L|main_powerPack_end2", "main_powerPack_turnVentA_L_end")

    mc.rename("main_powerPack_end3", "main_powerPack_turnVentB_L")
    mc.rename("main_powerPack_turnVentB_L|main_powerPack_end2", "main_powerPack_turnVentB_L_end")

    mc.rename("main_powerPack5", "main_powerPack_rocket_R")
    mc.rename("main_powerPack2", "main_powerPack_rocket_R_end")

    mc.rename("main_powerPack_end6", "main_powerPack_turnVentA_R")
    mc.rename("main_powerPack_turnVentA_R|main_powerPack_end2", "main_powerPack_turnVentA_R_end")

    mc.rename("main_powerPack_end9", "main_powerPack_turnVentB_R")
    mc.rename("main_powerPack_turnVentB_R|main_powerPack_end2", "main_powerPack_turnVentB_R_end")

    mc.rename("power_pistol_rig_grp", "plasma_pistol_rig_grp")


def bake_all_jnts_script():
    all_jnts = mc.ls(type="joint")

    mc.bakeResults(
    all_jnts,
    simulation=True,
    time=(12, 210),
    sampleBy=1,
    oversamplingRate=1,
    disableImplicitControl=True,
    preserveOutsideKeys=True,
    sparseAnimCurveBake=False,
    removeBakedAttributeFromLayer=False,
    removeBakedAnimFromLayer=False,
    bakeOnOverrideLayer=False,
    minimizeRotation=True,
    controlPoints=False,
    shape=True
    )

def bake_all_cameras_script():
    all_cameras = mc.ls(type="camera")

    all_camera_transforms = []
    for i in all_cameras:
        cam_trans = mc.listRelatives(i, parent=True)
        if cam_trans[0] != "persp"\
        and cam_trans[0] != "front"\
        and cam_trans[0] != "side"\
        and cam_trans[0] != "top":
            print(cam_trans[0])
            #unlock camera
            mc.setAttr(cam_trans[0] + ".tx", lock=False)
            mc.setAttr(cam_trans[0] + ".ty", lock=False)
            mc.setAttr(cam_trans[0] + ".tz", lock=False)
            mc.setAttr(cam_trans[0] + ".rx", lock=False)
            mc.setAttr(cam_trans[0] + ".ry", lock=False)
            mc.setAttr(cam_trans[0] + ".rz", lock=False)

            all_camera_transforms.append(cam_trans[0])

    mc.bakeResults(
    all_camera_transforms,
    simulation=True,
    time=(12, 210),
    sampleBy=1,
    oversamplingRate=1,
    disableImplicitControl=True,
    preserveOutsideKeys=True,
    sparseAnimCurveBake=False,
    removeBakedAttributeFromLayer=False,
    removeBakedAnimFromLayer=False,
    bakeOnOverrideLayer=False,
    minimizeRotation=True,
    controlPoints=False,
    shape=True
    )


def delete_old_script():
    '''
    mc.delete("L_FK_arm_001")
    mc.delete("L_IK_arm_001")

    mc.delete("R_FK_arm_001")
    mc.delete("R_IK_arm_001")

    mc.delete("L_IK_leg_001")
    mc.delete("L_FK_leg_001")

    mc.delete("R_IK_leg_001")
    mc.delete("R_FK_leg_001")
    '''
    
    all_parentConstraint = mc.ls(type="parentConstraint")
    all_scaleConstraint = mc.ls(type="scaleConstraint")
    all_ikEffector = mc.ls(type="ikEffector")
    all_blendColors = mc.ls(type="blendColors")
    
    
    mc.select(cl=True)
    mc.select(all_parentConstraint, add=True)
    mc.select(all_scaleConstraint, add=True)
    mc.select(all_ikEffector, add=True)
    mc.select(all_blendColors, add=True)
    mc.delete()
    
    # mc.delete("marine_ctrl_ALL_grp")
    # mc.delete("power_sword_ctrl_grp")
    # mc.delete("plasma_pistol_ctrl_grp")

    # mc.delete("marine_geo_ALL_grp")
    # mc.delete("power_sword_geo_grp")
    # mc.delete("plasma_pistol_geo_grp")
    
    #mc.deleteUnusedNodes()


    


