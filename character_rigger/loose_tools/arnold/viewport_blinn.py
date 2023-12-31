# create blinn material for viewport
#

import maya.cmds as cmds

selection = cmds.ls(sl=True)  # select arnold material

for arn_mat in selection:
    # create blinn shader
    blinn_mat = cmds.shadingNode ( "blinn", n = arn_mat + "_blinn", asShader=True)
    # create bump node for blinn
    #bump_node = cmds.shadingNode ( "bump2d", n = "bump2d" + blinn_mat, asUtility=True)

    # connect material to shader group
    cmds.connectAttr(blinn_mat + '.outColor', arn_mat + "SG" + '.surfaceShader', f=True)
    #connect bump node to blinn mat
    #cmds.connectAttr(bump_node + '.outNormal', blinn_mat + '.normalCamera', f=True)
    
    #connect base color texture to blinn
    object_nm = arn_mat.replace("_mat", "")
    base_color_texture = object_nm + "_BaseColor_1"
    cmds.connectAttr(base_color_texture + ".outColor", blinn_mat + ".color", f=True)
    
    #connect normal texture to blinn bump node
    #normal_texture = object_nm + "_Normal_1"
    #cmds.connectAttr(normal_texture + ".outAlpha", bump_node + ".bumpValue", f=True)
    
    #set blinn settings
    cmds.setAttr(blinn_mat + ".eccentricity", 0.4)
    cmds.setAttr(blinn_mat + ".specularRollOff", 0.2)
    
    #set bump node settings
    
    
    
  