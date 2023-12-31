# replace redshift material with arnold material
#

import maya.cmds as cmds

selection = cmds.ls(sl=True)  # select redshift material

for material in selection:
    #create arnold material named after redshift material
    arn_mat = cmds.shadingNode ( "aiStandardSurface", n = material, asShader=True)
    
    #create normal map node
    normal_map_node = cmds.shadingNode ( "aiNormalMap", n = "aiNormalMap_" + material, asShader=True)
    cmds.setAttr(normal_map_node + ".invertY", 1)  #invert normal map y
    
    #create facing ration node (fresnel equivalent)
    facing_ratio_node = cmds.shadingNode ( "aiFacingRatio", n = "aiFacingRatio_" + material, asShader=True)
    cmds.setAttr(facing_ratio_node + ".bias", 0.65) #set bias to .65

    #arnold layer node to layer fresnel on base color
    layer_node = cmds.shadingNode ( "aiLayerRgba", n = "aiLayerRgba_" + material, asShader=True)
    cmds.setAttr(layer_node + ".enable2", 1)  # enable layer 2 base color, 
    cmds.setAttr(layer_node + ".input2", 0, 0.002, 0.131, type="double3")  #set color
    
    
    cmds.connectAttr(layer_node + ".outColor", arn_mat + ".emissionColor", f=True) #connect layer node to emmision color
    cmds.connectAttr(facing_ratio_node + ".outValue", layer_node + ".mix1", f=True)  #connect facing ratio node to layer node layer1 mix
    cmds.connectAttr(normal_map_node + ".outValue", arn_mat + ".normalCamera", f=True) #connect normal node to normal camera
    
    
    cmds.connectAttr(arn_mat + ".outColor", material + "SG" + ".aiSurfaceShader", f=True) #connect arnold shader to shader group arnold input
    try:
        cmds.disconnectAttr(material + ".outColor", material + "SG" + ".rsSurfaceShader", f=True)  #disconnect redsfhit material
    except:
        print("No redshift material connected to shader group to disconnect.")
        
    
    #connect AO texture
    object_nm = material.replace("_mat", "") #remove _mat to just leave object name
    ao_texture = object_nm + "_AO_1"
    cmds.connectAttr(ao_texture + ".outAlpha", arn_mat + ".base", f=True)
    
    #connect baseColor texture
    object_nm = material.replace("_mat", "")
    base_color_texture = object_nm + "_BaseColor_1"
    cmds.connectAttr(base_color_texture + ".outColor", arn_mat + ".baseColor", f=True)
    
    #connect metallic texture
    object_nm = material.replace("_mat", "") 
    metallic_texture = object_nm + "_Metallic_1"
    cmds.connectAttr(metallic_texture + ".outAlpha", arn_mat + ".metalness", f=True)
    cmds.setAttr(metallic_texture + ".alphaIsLuminance", 1)  #set alpha is luminance as True for texture

    #connect roughness texture
    object_nm = material.replace("_mat", "") 
    roughness_texture = object_nm + "_Roughness_1"
    cmds.connectAttr(roughness_texture + ".outAlpha", arn_mat + ".specularRoughness", f=True)
    
    #connect normal texture
    object_nm = material.replace("_mat", "") 
    normal_texture = object_nm + "_Normal_1"
    cmds.connectAttr(normal_texture + ".outColor", normal_map_node + ".input", f=True) #connect normal texture to normal map node
    
    
    #set main arnold material settings
    cmds.setAttr(arn_mat + ".specularColor", 0.75, 0.796, 1, type="double3")
    cmds.setAttr(arn_mat + ".emission", 1)
    cmds.setAttr(arn_mat + ".thinFilmThickness", 575)
    cmds.setAttr(arn_mat + ".thinFilmIOR", 1.300)
    
    #delete redshift material
    cmds.delete(material)
    
    #rename arnold material without the 1 at the end
    cmds.rename(arn_mat, material)

    
    
    