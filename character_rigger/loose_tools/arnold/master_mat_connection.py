# create master material
#  too control multiple attributes at once

import maya.cmds as cmds

peasant_mat_lst = ["wyvern_head_mat", "wyvern_wings_mat", "wyvern_body_mat"]

master_mat = "wyvern_mat_MASTER" 

master_mat_normal = "aiNormalMap_wyvern_mat_MASTER"

master_mat_rgb_layer = "aiLayerRgba_wyvern_mat_MASTER"

master_mat_facing_ratio = "aiFacingRatio_wyvern_mat_MASTER"

for material in peasant_mat_lst:
    material_normal = "aiNormalMap_" + material

    material_rgb_layer = "aiLayerRgba_" + material

    material_facing_ratio = "aiFacingRatio_" + material
    
    
    cmds.connectAttr(master_mat + ".specular", material + ".specular", f=True)
    cmds.connectAttr(master_mat + ".specularColor", material + ".specularColor", f=True)
    
    cmds.connectAttr(master_mat + ".emission", material + ".emission", f=True)
    cmds.connectAttr(master_mat + ".thinFilmThickness", material + ".thinFilmThickness", f=True)
    cmds.connectAttr(master_mat + ".thinFilmIOR", material + ".thinFilmIOR", f=True)
    
    cmds.connectAttr(master_mat_normal + ".strength", material_normal + ".strength", f=True)
    
    cmds.connectAttr(master_mat_rgb_layer + ".input2", material_rgb_layer + ".input2", f=True)
    
    cmds.connectAttr(master_mat_facing_ratio + ".bias", material_facing_ratio + ".bias", f=True)
    cmds.connectAttr(master_mat_facing_ratio + ".gain", material_facing_ratio + ".gain", f=True)

