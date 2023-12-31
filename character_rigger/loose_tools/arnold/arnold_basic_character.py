import maya.cmds as cmds

#drag materials into hypershade from windows explorer
#grab base color texture, or grab all textures

def arnold_basic_character():  

    flip_normal_y = True #note, add checkbox
    x_plus = -150 # default value for texture attach cube x translation #-150 so it starts at 0
    facing_ratio = True   # if you want a fresnel effect
    rough_metal_ramps = True   # if you want a roughness and metalness ramps for greater control
    
    mySel = cmds.ls(sl=True)

    for i in mySel:
        if "_BaseColor_1" in i: #only use Base_Color to get base material name
            tex_nm = i.replace("_BaseColor_1", "")  #texture name, without the Base_Color_1 text

            myColor = tex_nm + "_BaseColor_1"
            myAOMetalRough = tex_nm + "_OcclusionRoughnessMetallic_1"
            myNormal = tex_nm + "_Normal_1"
            myEmissive = tex_nm + "_Emissive_1"
            
            #_________________________________________#
            #_________________________________________#
            # create shader
            arn_mat = cmds.shadingNode ( "aiStandardSurface", n = tex_nm + "_mat", asShader=True)
            
            # create shader group
            arn_mat_SG = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name = arn_mat + "SG"  )

            # connect material to shader group
            cmds.connectAttr(arn_mat + ".outColor", arn_mat_SG + ".aiSurfaceShader", force=True)

            #_________________________________________#
            #_________________________________________#
            if cmds.objExists(myAOMetalRough):
                #rename place2dTexture
                AOMetalRough_place2d = cmds.listConnections(myAOMetalRough, source=True, type='place2dTexture')
                cmds.rename(AOMetalRough_place2d[0], 'place2dTexture_' + myAOMetalRough)

                # create arnold multply node for AO and baseColor
                ao_mult_node = cmds.shadingNode ( "aiMultiply", n = "aiMultiply_" + tex_nm + "_BaseColor_1", asShader=True)
                #reconnect baseColor to AO mult node
                cmds.connectAttr(myColor + ".outColor", ao_mult_node + ".input1", force=True) 
                #connect ao to AO mult   #to R G B, alternative to creating luminance node
                cmds.connectAttr(myAOMetalRough + ".outColorR", ao_mult_node + ".input2R", force=True)
                cmds.connectAttr(myAOMetalRough + ".outColorR", ao_mult_node + ".input2G", force=True) 
                cmds.connectAttr(myAOMetalRough + ".outColorR", ao_mult_node + ".input2B", force=True)  
                #connect AO mult to arn_mat baseColor
                cmds.connectAttr(ao_mult_node + ".outColor", arn_mat + ".baseColor", force=True)
        
                #connect a Metallic to material reflection metalness
                cmds.connectAttr(myAOMetalRough + ".outColorB", arn_mat + ".metalness", force=True)
                
                #connect Roughness to material reflection roughness
                cmds.connectAttr(myAOMetalRough + ".outColorG", arn_mat + ".specularRoughness", force=True)
                
                #to prevent color space warning (as if adjusting color space in pref may affect this)
                cmds.setAttr(myAOMetalRough + ".ignoreColorSpaceFileRules", 1)
                #set color space of metalness texture to raw
                cmds.setAttr(myAOMetalRough + ".colorSpace", "Raw", type="string")

                if rough_metal_ramps: #== True
                    metal_ramp_node = cmds.shadingNode ( 'ramp', n = 'ramp_' + tex_nm + "_Metallic_1", asShader=True) #create ramp node to better ctrl metalness
                    rough_ramp_node = cmds.shadingNode ( 'ramp', n = 'ramp_' + tex_nm + "_Roughness_1", asShader=True) #create ramp node to better ctrl roughness

                    #connect rough nodes
                    cmds.connectAttr(myAOMetalRough + ".outColorB", metal_ramp_node + ".vCoord", force=True)
                    cmds.connectAttr(metal_ramp_node + ".outAlpha", arn_mat + ".metalness", force=True)

                    #connect rough nodes
                    cmds.connectAttr(myAOMetalRough + ".outColorG", rough_ramp_node + ".vCoord", force=True)
                    cmds.connectAttr(rough_ramp_node + ".outAlpha", arn_mat + ".specularRoughness", force=True)
                    


            if cmds.objExists(myNormal):
                #rename place2dTexture
                Normal_place2d = cmds.listConnections(myNormal, source=True, type='place2dTexture')
                cmds.rename(Normal_place2d[0], 'place2dTexture_' + myNormal)

                #create arnold normal node for normal map
                normal_map_node = cmds.shadingNode ( "aiNormalMap", n = "aiNormalMap_" + tex_nm + '_Normal_1', asShader=True)

                #invert normal Y on normal map node
                if flip_normal_y: #== True
                    cmds.setAttr(normal_map_node + ".invertY", 1)
                #connect arnold normal map node to material
                cmds.connectAttr(normal_map_node + ".outValue", arn_mat + ".normalCamera", force=True)
                #connect normal texture to normal map node
                cmds.connectAttr(myNormal + ".outColor", normal_map_node + ".input", force=True)
                
                #prevent color space from changing
                cmds.setAttr(myNormal + ".ignoreColorSpaceFileRules", 1)
                #set color space of normal texture to raw (or will not work)
                cmds.setAttr(myNormal + ".colorSpace", "Raw", type="string")


            if cmds.objExists(myEmissive):
                #rename place2dTexture
                Emissive_place2d = cmds.listConnections(myEmissive, source=True, type='place2dTexture')
                cmds.rename(Emissive_place2d[0], 'place2dTexture_' + myEmissive)

                #connect arnold normal map node to material
                cmds.connectAttr(myEmissive + ".outAlpha", arn_mat + ".emission", force=True)

                #settings
                cmds.setAttr(myEmissive + ".alphaIsLuminance", 1)
                cmds.setAttr(myEmissive + ".ignoreColorSpaceFileRules", 1)
                cmds.setAttr(myEmissive + ".colorSpace", "Raw", type="string")


            if cmds.objExists(myColor):
                #rename place2dTexture
                Color_place2d = cmds.listConnections(myColor, source=True, type='place2dTexture')
                cmds.rename(Color_place2d[0], 'place2dTexture_' + myColor)

                #connect diffuse/ albedo texture file to arnold material color
                cmds.connectAttr(myColor + ".outColor", arn_mat + ".baseColor", force=True) 
                #to prevent color space warning (as if adjusting color space in pref may affect this)
                cmds.setAttr(myColor + ".ignoreColorSpaceFileRules", 1)

                if facing_ratio:  #== True
                    #------------------------------------------------------#
                    #add optional facing ratio (FRESNEL) node, off by default  #automatically works with bump
                    facing_ratio_node = cmds.shadingNode ( "aiFacingRatio", n = 'aiFacingRatio_' + tex_nm + "_BaseColor_1", asShader=True)
                    cmds.setAttr(facing_ratio_node + ".bias", 0.75) #set basic facing ratio default setting
                    cmds.setAttr(facing_ratio_node + ".gain", 0.25)
                    cmds.setAttr(facing_ratio_node + ".invert", 1)
                    #arnold layer node to layer fresnel on base color
                    layer_node = cmds.shadingNode ( "aiLayerRgba", n = "aiLayerRgba_" + tex_nm + "_BaseColor_1", asShader=True)
                    cmds.setAttr(layer_node + ".enable8", 1)  # enable layer 8 base color 
                    cmds.setAttr(layer_node + ".enable7", 1)  # enable layer 7 base color 
                    cmds.setAttr(layer_node + ".enable1", 0)  # disable layer way to not cover up others
                    cmds.setAttr(layer_node + ".input7", 0, 0.03, 0.1)   # set color of facing ratio
                    # connect facing ratio 
                    cmds.connectAttr(facing_ratio_node + ".outValue", layer_node + ".mix7", force=True) # facing ratio to color layer node
                    cmds.connectAttr(myColor + ".outColor", layer_node + ".input8", force=True)   # base color to color layer node
                    cmds.connectAttr(layer_node + ".outColor", ao_mult_node + ".input1", force=True)  # color layer node to ao multiply node
                    cmds.connectAttr(ao_mult_node + ".outColor", arn_mat + ".baseColor", force=True) # ao multiply to arnold


            #_________________________________________# 
            #create blinn material for viewport
            blinn_mat = cmds.shadingNode ( 'blinn', n = arn_mat  + '_blinn', asShader=True)
            cmds.setAttr( blinn_mat + '.specularRollOff', 0.3 ) #set specular
            cmds.setAttr( blinn_mat + '.eccentricity', 0.4 ) #set roughness

            #adjust gamma for aces viewing of srgb colors
            gamma_node = cmds.shadingNode ( 'gammaCorrect', n = 'gammaCorrect_' + tex_nm + "_BaseColor_1", asUtility=True)
            const_node = cmds.shadingNode ( 'colorConstant', n = 'colorConstant_' + tex_nm + "_BaseColor_1", asUtility=True)
            cmds.setAttr( const_node + '.inAlpha', 1.7 ) #set gamma offset
            #connect gamme node to blinn
            cmds.connectAttr(const_node + '.outAlpha', gamma_node + '.gammaX', f=True)
            cmds.connectAttr(const_node + '.outAlpha', gamma_node + '.gammaY', f=True)
            cmds.connectAttr(const_node + '.outAlpha', gamma_node + '.gammaZ', f=True)
            cmds.connectAttr(myColor + '.outColor', gamma_node + '.value', f=True)
            cmds.connectAttr(gamma_node + '.outValue', blinn_mat + '.color', f=True)

            #connect materials
            cmds.connectAttr(blinn_mat + '.outColor', arn_mat_SG + '.surfaceShader', f=True)


            #_________________________________________# 
            #create box to assign material too
            texture_box = cmds.polyCube(n=tex_nm + "_box", w=100, h=100, d=100, ch=0)[0]
            x_plus += 150
            print(x_plus)
            cmds.select(texture_box)
            cmds.move(x_plus, 50, 0 ) # move box up and over more for each iteration
            #assign material to box (as to preserve if delete unused nodes)
            cmds.hyperShade(assign = tex_nm + "_mat")
            
        else:
            pass


#notes
#added ai color correct for gamma change to space marine srgb texture
