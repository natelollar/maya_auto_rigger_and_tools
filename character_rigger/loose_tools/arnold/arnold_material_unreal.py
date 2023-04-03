import maya.cmds as mc

#drag and drop textures into hypershade  #select objects to apply shaders  
#object and texture names must have same base text (ex. 'human' and 'human_baseColor')
def arnold_material_unreal():  
    flip_normal_y = True #note, add checkbox

    mySel = mc.ls(sl=True)

    for i in mySel:
        myColor = i + '_BaseColor_1'
        myAOMetalRough = i + '_OcclusionRoughnessMetallic_1'
        myNormal = i + '_Normal_1'

        #_________________________________________#

        # create shader
        arn_mat = mc.shadingNode ( 'aiStandardSurface', n = i + '_mat', asShader=True)
        
        # create shader group
        arn_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = arn_mat + 'SG'  )

        # connect material to shader group
        mc.connectAttr(arn_mat + '.outColor', arn_mat_SG + '.surfaceShader', f=True)

        #_________________________________________#
        #_________________________________________#

        #set redshift material reflection BRDF to GGX
        #mc.setAttr(red_mat + '.refl_brdf', 1)
        #set redshift material fresnel type to Metalness
        #mc.setAttr(red_mat + '.refl_fresnel_mode', 2)
        

        if mc.objExists(myColor):
            #connect diffuse/ albedo texture file to arnold material color
            mc.connectAttr(myColor + '.outColor', arn_mat + '.baseColor') 
            #to prevent color space warning (as if adjusting color space in pref may affect this)
            mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
        

        if mc.objExists(myAOMetalRough):
            # create arnold multply node for AO and baseColor
            ao_mult_node = mc.shadingNode ( 'aiMultiply', n = i + '_ao_mult_node', asShader=True)
            #reconnect baseColor to AO mult node
            mc.connectAttr(myColor + '.outColor', ao_mult_node + '.input1') 
            #connect ao to AO mult   #to R G B, alternative to creating luminance node
            mc.connectAttr(myAOMetalRough + '.outColorR', ao_mult_node + '.input2R')
            mc.connectAttr(myAOMetalRough + '.outColorR', ao_mult_node + '.input2G') 
            mc.connectAttr(myAOMetalRough + '.outColorR', ao_mult_node + '.input2B')  
            #connect AO mult to arn_mat baseColor
            mc.connectAttr(ao_mult_node + '.outColor', arn_mat + '.baseColor', force=True)
       
            #connect a Metallic to material reflection metalness
            mc.connectAttr(myAOMetalRough + '.outColorB', arn_mat + '.metalness')
            
            #connect Roughness to material reflection roughness
            mc.connectAttr(myAOMetalRough + '.outColorG', arn_mat + '.specularRoughness')
            
            #to prevent color space warning (as if adjusting color space in pref may affect this)
            mc.setAttr(myAOMetalRough + '.ignoreColorSpaceFileRules', 1)
            #set color space of metalness texture to raw
            mc.setAttr(myAOMetalRough + '.colorSpace', 'Raw', type='string')


        if mc.objExists(myNormal):
            #create arnold normal node for normal map
            normal_map_node = mc.shadingNode ( 'aiNormalMap', n = i + '_normal_map_node', asShader=True)

            #invert normal Y on normal map node
            if flip_normal_y == True: 
                mc.setAttr(normal_map_node + '.invertY', 1)
            #connect arnold normal map node to material
            mc.connectAttr(normal_map_node + '.outValue', arn_mat + '.normalCamera')
            #connect normal texture to normal map node
            mc.connectAttr(myNormal + '.outColor', normal_map_node + '.input')
            
            #prevent color space from changing
            mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
            #set color space of normal texture to raw (or will not work)
            mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')
           
        #_________________________________________# 
        #assign material
        mc.select(i)
        mc.hyperShade(assign = i + '_mat')
