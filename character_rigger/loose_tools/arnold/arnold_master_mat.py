# create master material
#  too control multiple attributes at once

import maya.cmds as cmds

def arnold_master_mat():
    cmds.select(cl=True)
    material_list = ['MASTER_mat', 'leg_mat', 'helmet_mat', 'backpack_mat', 'arm_mat', 'torso_mat']
    cmds.select(material_list)

    selection = cmds.ls(sl=True)

    master_mat = selection[0] #first selection
    master_simple_nm = master_mat.replace("_mat", "")  #simple_name
    master_mat_blinn = master_mat + "_blinn"

    peasant_mat_lst = selection[1:] #skip first selection

    master_mat_normal = "aiNormalMap_" + master_simple_nm + "_Normal_1"
    master_mat_color_correct = "aiColorCorrect_" + master_simple_nm + "_BaseColor_1"
    master_mat_facing_ratio = "aiFacingRatio_" + master_simple_nm + "_BaseColor_1"
    master_mat_rgb_lyr = "aiLayerRgba_" + master_simple_nm + "_BaseColor_1"
    master_mat_ramp_rough = "ramp_" + master_simple_nm + "_Roughness_1"
    master_mat_ramp_metal = "ramp_" + master_simple_nm + "_Metallic_1"

    #base_clr_lyr_nd = "aiLayerRgba_" + simple_nm
    
    

    
    for peasant_mat in peasant_mat_lst:
        peasant_mat = peasant_mat
        peasant_simple_nm = peasant_mat.replace("_mat", "")  #simple_name
        peasant_mat_blinn = peasant_mat + "_blinn"

        peasant_mat_normal = "aiNormalMap_" + peasant_simple_nm + "_Normal_1"
        peasant_mat_color_correct = "aiColorCorrect_" + peasant_simple_nm + "_BaseColor_1"
        peasant_mat_facing_ratio = "aiFacingRatio_" + peasant_simple_nm + "_BaseColor_1"
        peasant_mat_rgb_lyr = "aiLayerRgba_" + peasant_simple_nm + "_BaseColor_1"
        peasant_mat_ramp_rough = "ramp_" + peasant_simple_nm + "_Roughness_1"
        peasant_mat_ramp_metal = "ramp_" + peasant_simple_nm + "_Metallic_1"
        #material_facing_ratio = "aiFacingRatio_" + peasant_mat
        
        #_____________________________#
        #main connections
        #_____________________________#
        cmds.connectAttr(master_mat + ".base", peasant_mat + ".base", f=True)
        cmds.connectAttr(master_mat + ".diffuseRoughness", peasant_mat + ".diffuseRoughness", f=True)
        cmds.connectAttr(master_mat + ".specular", peasant_mat + ".specular", f=True)
        cmds.connectAttr(master_mat + ".specularColor", peasant_mat + ".specularColor", f=True)
        cmds.connectAttr(master_mat + ".sheen", peasant_mat + ".sheen", f=True)
        cmds.connectAttr(master_mat + ".sheenColor", peasant_mat + ".sheenColor", f=True)
        cmds.connectAttr(master_mat + ".sheenRoughness", peasant_mat + ".sheenRoughness", f=True)
        cmds.connectAttr(master_mat + ".thinFilmThickness", peasant_mat + ".thinFilmThickness", f=True)
        cmds.connectAttr(master_mat + ".thinFilmIOR", peasant_mat + ".thinFilmIOR", f=True)

        
        cmds.connectAttr(master_mat_normal + ".strength", peasant_mat_normal  + ".strength", f=True)

        cmds.connectAttr(master_mat_color_correct + ".gamma", peasant_mat_color_correct  + ".gamma", f=True)
        cmds.connectAttr(master_mat_color_correct + ".hueShift", peasant_mat_color_correct  + ".hueShift", f=True)
        cmds.connectAttr(master_mat_color_correct + ".saturation", peasant_mat_color_correct  + ".saturation", f=True)
        cmds.connectAttr(master_mat_color_correct + ".contrast", peasant_mat_color_correct  + ".contrast", f=True)
        cmds.connectAttr(master_mat_color_correct + ".contrastPivot", peasant_mat_color_correct  + ".contrastPivot", f=True)
        cmds.connectAttr(master_mat_color_correct + ".exposure", peasant_mat_color_correct  + ".exposure", f=True)

        cmds.connectAttr(master_mat_facing_ratio + ".bias", peasant_mat_facing_ratio  + ".bias", f=True)
        cmds.connectAttr(master_mat_facing_ratio + ".gain", peasant_mat_facing_ratio  + ".gain", f=True)

        cmds.connectAttr(master_mat_rgb_lyr + ".input7", peasant_mat_rgb_lyr  + ".input7", f=True) #fresnel color

        cmds.connectAttr(master_mat_ramp_rough + ".colorEntryList[0].position", peasant_mat_ramp_rough  + ".colorEntryList[0].position", f=True)
        cmds.connectAttr(master_mat_ramp_rough + ".colorEntryList[1].position", peasant_mat_ramp_rough  + ".colorEntryList[1].position", f=True)
        cmds.connectAttr(master_mat_ramp_rough + ".colorEntryList[0].color", peasant_mat_ramp_rough  + ".colorEntryList[0].color", f=True)
        cmds.connectAttr(master_mat_ramp_rough + ".colorEntryList[1].color", peasant_mat_ramp_rough  + ".colorEntryList[1].color", f=True)

        cmds.connectAttr(master_mat_ramp_metal + ".colorEntryList[0].position", peasant_mat_ramp_metal  + ".colorEntryList[0].position", f=True)
        cmds.connectAttr(master_mat_ramp_metal + ".colorEntryList[1].position", peasant_mat_ramp_metal  + ".colorEntryList[1].position", f=True)
        cmds.connectAttr(master_mat_ramp_metal + ".colorEntryList[0].color", peasant_mat_ramp_metal  + ".colorEntryList[0].color", f=True)
        cmds.connectAttr(master_mat_ramp_metal + ".colorEntryList[1].color", peasant_mat_ramp_metal  + ".colorEntryList[1].color", f=True)

        
        #cmds.connectAttr(master_mat_facing_ratio + ".bias", material_facing_ratio + ".bias", f=True)
        #cmds.connectAttr(master_mat_facing_ratio + ".gain", material_facing_ratio + ".gain", f=True)

        #_____________________________#
        #blinn connections
        #_____________________________#
        cmds.connectAttr( master_mat_blinn + ".specularRollOff", peasant_mat_blinn + ".specularRollOff", f=True) 
        cmds.connectAttr( master_mat_blinn + ".eccentricity", peasant_mat_blinn + ".eccentricity", f=True) 
