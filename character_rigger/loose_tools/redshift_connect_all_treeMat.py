import maya.cmds as mc

def leaf_mat():
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        #_________________________________________#

        # create shader
        red_mat = mc.shadingNode ( 'RedshiftMaterial', n = i + '_mat', asShader=True)

        # create sprite node for fast opacity
        red_mat_sprite = mc.shadingNode ( 'RedshiftSprite', n = i + '_mat_sprite', asShader=True)
        
        # create shader group
        red_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = red_mat + 'SG'  )
        
        # connect material to sprite
        mc.connectAttr(red_mat + '.outColor', red_mat_sprite + '.input', f=True)

        # connect sprite to shader group
        mc.connectAttr(red_mat_sprite + '.outColor', red_mat_SG + '.surfaceShader', f=True)
        
        # assign redshift material to selected
        mc.select(i)
        mc.hyperShade(assign=red_mat_sprite)
        
        #_________________________________________#
        print(red_mat)
        
        print(i)
        
        myColor = i + '_BaseColor_1'
        myAO = i + '_AO_1'
        #myMetal = i + '_Metallic_1'
        #myRough = i + '_Roughness_1'
        myGloss = i + '_Gloss_1'
        myNormal = i + '_Normal_1'
        myOpacity = i + '_Opacity_1'
        
        
        #set redshift material reflection BRDF to GGX
        mc.setAttr(red_mat + '.refl_brdf', 1)
        #set redshift material fresnel type to Metalness
        mc.setAttr(red_mat + '.refl_fresnel_mode', 2)
        
        #connect diffuse/ albedo texture file to redshift material color
        mc.connectAttr(myColor + '.outColor', red_mat + '.diffuse_color') 
        #to prevent color space warning (as if adjusting color space in pref may affect this)
        mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
        
        if mc.objExists(myAO):
            #connect ambient occlusion grayscale to color weight
            mc.connectAttr(myAO + '.outAlpha', red_mat + '.diffuse_weight')
            #to prevent color space warning (as if adjusting color space in pref may affect this)
            mc.setAttr(myAO + '.ignoreColorSpaceFileRules', 1)
        

        # convert gloss texture to redshift default roughness
        mc.setAttr( red_mat + '.refl_isGlossiness', 1 )
        #connect roughness grayscale to material reflection roughness
        mc.connectAttr(myGloss + '.outAlpha', red_mat + '.refl_roughness')
        #to use alpha channel as single luminance output
        mc.setAttr(myGloss + '.alphaIsLuminance', 1)
        # prevent color space from changing
        mc.setAttr(myGloss + '.ignoreColorSpaceFileRules', 1)
        #set color space of roughness texture to raw
        mc.setAttr(myGloss + '.colorSpace', 'Raw', type='string')
        
        

        #create bump node for normal map
        bumpNode = mc.shadingNode('RedshiftBumpMap', asTexture=True, n=myNormal + '_bumpNode')
        # set bump node scale to 1
        mc.setAttr(bumpNode + '.scale', 1)
        #set bump node input type to tangent space
        mc.setAttr(bumpNode + '.inputType', 1)
        #flip normal Y on bump node
        #mc.setAttr(bumpNode + '.flipY', 1)
        #connect redshift bump node to material
        mc.connectAttr(bumpNode + '.out', red_mat + '.bump_input')
        
        #connect normal texture to bump node
        mc.connectAttr(myNormal + '.outColor', bumpNode + '.input')
        # prevent color space from changing
        mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
        #set color space of normal texture to raw (or will not work)
        mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')


        # set sprite opacity texture
        # get file path and name of opacity texture
        opacity_file = mc.getAttr(myOpacity + '.fileTextureName')

        mc.setAttr(red_mat_sprite + '.tex0', opacity_file, type='string' ) #type='string',
        

# does not include sprite opacity
def bark_mat():
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        #_________________________________________#

        # create shader
        red_mat = mc.shadingNode ( 'RedshiftMaterial', n = i + '_mat', asShader=True)

        # create shader group
        red_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = red_mat + 'SG'  )
        
        # connect sprite to shader group
        mc.connectAttr(red_mat + '.outColor', red_mat_SG + '.surfaceShader', f=True)
        
        # assign redshift material to selected
        mc.select( i )
        mc.hyperShade( assign = red_mat )
        
        #_________________________________________#
        
        myColor = i + '_BaseColor_1'
        myAO = i + '_AO_1'
        myGloss = i + '_Gloss_1'
        myNormal = i + '_Normal_1'

        #set redshift material reflection BRDF to GGX
        mc.setAttr(red_mat + '.refl_brdf', 1)
        #set redshift material fresnel type to Metalness
        mc.setAttr(red_mat + '.refl_fresnel_mode', 2)
        
        #connect diffuse/ albedo texture file to redshift material color
        mc.connectAttr(myColor + '.outColor', red_mat + '.diffuse_color') 
        #to prevent color space warning (as if adjusting color space in pref may affect this)
        mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
        
        if mc.objExists(myAO):
            #connect ambient occlusion grayscale to color weight
            mc.connectAttr(myAO + '.outAlpha', red_mat + '.diffuse_weight')
            #to prevent color space warning (as if adjusting color space in pref may affect this)
            mc.setAttr(myAO + '.ignoreColorSpaceFileRules', 1)
        

        # convert gloss texture to redshift default roughness
        mc.setAttr( red_mat + '.refl_isGlossiness', 1 )
        #connect roughness grayscale to material reflection roughness
        mc.connectAttr(myGloss + '.outAlpha', red_mat + '.refl_roughness')
        #to use alpha channel as single luminance output
        mc.setAttr(myGloss + '.alphaIsLuminance', 1)
        # prevent color space from changing
        mc.setAttr(myGloss + '.ignoreColorSpaceFileRules', 1)
        #set color space of roughness texture to raw
        mc.setAttr(myGloss + '.colorSpace', 'Raw', type='string')
        
        

        #create bump node for normal map
        bumpNode = mc.shadingNode('RedshiftBumpMap', asTexture=True, n=myNormal + '_bumpNode')
        # set bump node scale to 1
        mc.setAttr(bumpNode + '.scale', 1)
        #set bump node input type to tangent space
        mc.setAttr(bumpNode + '.inputType', 1)
        #flip normal Y on bump node
        #mc.setAttr(bumpNode + '.flipY', 1)
        #connect redshift bump node to material
        mc.connectAttr(bumpNode + '.out', red_mat + '.bump_input')
        
        #connect normal texture to bump node
        mc.connectAttr(myNormal + '.outColor', bumpNode + '.input')
        # prevent color space from changing
        mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
        #set color space of normal texture to raw (or will not work)
        mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')




def connect_mat():
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        mc.select(i)
        mc.hyperShade(assign = i + '_mat')

def connect_mat_sprite():
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        mc.select(i)
        mc.hyperShade(assign = i + '_mat_sprite')

#leaf_mat()

#bark_mat()

#connect_mat()

connect_mat_sprite()
