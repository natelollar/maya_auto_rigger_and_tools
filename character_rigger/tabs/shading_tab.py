import maya.cmds as mc



class shader_utility():

    def redshift_displacement_off(self):
        mySel = mc.ls(sl=True)

        # scale each in selection randomly
        for i in mySel:
            mc.setAttr(i + '.rsEnableSubdivision', 0)
            mc.setAttr(i + '.rsEnableDisplacement', 0)

    def redshift_displacement_on(self):
        mySel = mc.ls(sl=True)

        # scale each in selection randomly
        for i in mySel:
            mc.setAttr(i + '.rsEnableSubdivision', 1)
            mc.setAttr(i + '.rsEnableDisplacement', 1)


    def connect_redshift_mat_all( self ): #flip_normal_y = True
        
        flip_normal_y = mc.checkBox( 'fip_normal_y_checkbox', query=1, v=1 )

        mySel = mc.ls(sl=True)

        for i in mySel:
            myColor = i + '_BaseColor_1'
            myAO = i + '_AO_1'
            myMetal = i + '_Metallic_1'
            myRough = i + '_Roughness_1'
            myGloss = i + '_Gloss_1'
            myNormal = i + '_Normal_1'
            myOpacity = i + '_Opacity_1'

            #_________________________________________#

            # create shader
            red_mat = mc.shadingNode ( 'RedshiftMaterial', n = i + '_mat', asShader=True)

            # create shader group
            red_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = red_mat + 'SG'  )

            if mc.objExists(myOpacity):
                # create sprite node for fast opacity
                red_mat_sprite = mc.shadingNode ( 'RedshiftSprite', n = i + '_mat_sprite', asShader=True)
                
                # connect material to sprite
                mc.connectAttr(red_mat + '.outColor', red_mat_sprite + '.input', f=True)

                # connect sprite to shader group
                mc.connectAttr(red_mat_sprite + '.outColor', red_mat_SG + '.surfaceShader', f=True)

                # assign redshift material to selected
                mc.select(i)
                mc.hyperShade(assign=red_mat_sprite)

            if mc.objExists(myOpacity) == False:
                # connect sprite to shader group
                mc.connectAttr(red_mat + '.outColor', red_mat_SG + '.surfaceShader', f=True)

                # assign redshift material to selected
                mc.select(i)
                mc.hyperShade(assign=red_mat)
            
            #_________________________________________#
            #_________________________________________#

            #set redshift material reflection BRDF to GGX
            mc.setAttr(red_mat + '.refl_brdf', 1)
            #set redshift material fresnel type to Metalness
            mc.setAttr(red_mat + '.refl_fresnel_mode', 2)
            

            if mc.objExists(myColor):
                #connect diffuse/ albedo texture file to redshift material color
                mc.connectAttr(myColor + '.outColor', red_mat + '.diffuse_color') 
                #to prevent color space warning (as if adjusting color space in pref may affect this)
                mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
            

            if mc.objExists(myAO):
                #connect ambient occlusion grayscale to color weight
                mc.connectAttr(myAO + '.outAlpha', red_mat + '.diffuse_weight')
                #to prevent color space warning (as if adjusting color space in pref may affect this)
                mc.setAttr(myAO + '.ignoreColorSpaceFileRules', 1)


            if mc.objExists(myMetal):
                #connect aroughness grayscale to material reflection metalness
                mc.connectAttr(myMetal + '.outAlpha', red_mat + '.refl_metalness')
                #to use alpha channel as single luminance output
                mc.setAttr(myMetal + '.alphaIsLuminance', 1)
                # prevent color space from changing
                mc.setAttr(myMetal + '.ignoreColorSpaceFileRules', 1)
                #set color space of metalness texture to raw
                mc.setAttr(myMetal + '.colorSpace', 'Raw', type='string')
            

            if mc.objExists(myRough):
                #connect aroughness grayscale to material reflection roughness
                mc.connectAttr(myRough + '.outAlpha', red_mat + '.refl_roughness')
                #to use alpha channel as single luminance output
                mc.setAttr(myRough + '.alphaIsLuminance', 1)
                # prevent color space from changing
                mc.setAttr(myRough + '.ignoreColorSpaceFileRules', 1)
                #set color space of roughness texture to raw
                mc.setAttr(myRough + '.colorSpace', 'Raw', type='string')
            

            if mc.objExists(myGloss):
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
            

            if mc.objExists(myNormal):
                #create bump node for normal map
                bumpNode = mc.shadingNode('RedshiftBumpMap', asTexture=True, n=myNormal + '_bumpNode')
                # set bump node scale to 1
                mc.setAttr(bumpNode + '.scale', 1)
                #set bump node input type to tangent space
                mc.setAttr(bumpNode + '.inputType', 1)
                #flip normal Y on bump node
                if flip_normal_y == True: 
                    mc.setAttr(bumpNode + '.flipY', 1)
                #connect redshift bump node to material
                mc.connectAttr(bumpNode + '.out', red_mat + '.bump_input')
            
                #connect normal texture to bump node
                mc.connectAttr(myNormal + '.outColor', bumpNode + '.input')
                # prevent color space from changing
                mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
                #set color space of normal texture to raw (or will not work)
                mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')

            if mc.objExists(myOpacity):
                # get file path and name of opacity texture
                opacity_file = mc.getAttr(myOpacity + '.fileTextureName')
                # set sprite opacity texture
                mc.setAttr(red_mat_sprite + '.tex0', opacity_file, type='string' )


    def connect_mat(self):
        
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.select(i)
            mc.hyperShade(assign = i + '_mat')


    def connect_mat_sprite(self):
        
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.select(i)
            mc.hyperShade(assign = i + '_mat_sprite')



    def stingray_mat_add(self):
        mySel = mc.ls(sl=True)
        
        # add stingray material for pbr viewport, but keep redshift material
        for i in mySel:

            red_mat = i + '_mat'
            shader_grp = red_mat + 'SG'

            myColor = i + '_BaseColor_1'
            myAO = i + '_AO_1'
            myMetal = i + '_Metallic_1'
            myRough = i + '_Roughness_1'
            myNormal = i + '_Normal_1'

            stingray_mat = mc.shadingNode('StingrayPBS', n = red_mat + '_StingrayPBS', asShader=True)

            #stingray material settings
            mc.setAttr(stingray_mat + '.initgraph', True)

            mc.setAttr(stingray_mat + '.use_color_map', 1)
            mc.setAttr(stingray_mat + '.use_normal_map', 1)
            mc.setAttr(stingray_mat + '.use_metallic_map', 1)
            mc.setAttr(stingray_mat + '.use_roughness_map', 1)
            mc.setAttr(stingray_mat + '.use_ao_map', 1)


            #connect materials
            mc.connectAttr(stingray_mat + '.outColor', shader_grp + '.surfaceShader', f=True)

            mc.connectAttr(red_mat + '.outColor', shader_grp + '.rsSurfaceShader', f=True)

            # connect textures
            if mc.objExists(myColor):
                mc.connectAttr(myColor + '.outColor', stingray_mat + '.TEX_color_map', f=True)
                
            if mc.objExists(myNormal):
                mc.connectAttr(myNormal + '.outColor', stingray_mat + '.TEX_normal_map', f=True)

            if mc.objExists(myMetal):
                mc.connectAttr(myMetal + '.outColor', stingray_mat + '.TEX_metallic_map', f=True)

            if mc.objExists(myRough):
                mc.connectAttr(myRough + '.outColor', stingray_mat + '.TEX_roughness_map', f=True)

            if mc.objExists(myAO):
                mc.connectAttr(myAO + '.outColor', stingray_mat + '.TEX_ao_map', f=True)






        
#shader_utility().connect_redshift_mat_all()
#shader_utility().stingray_mat_add()