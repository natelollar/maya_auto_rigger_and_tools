import maya.cmds as mc

#drag materials into hypershade from windows explorer
#grab base color texture, or grab all textures

def arnold_material_substance_triplanar():  
    flip_normal_y = False #note, add checkbox
    tri_scl = 5.0  #triplanar scale 
    tri_blend = 0.25  #default triplanar blend amount
    plc2d_scl = 0.001  #place2dTexture scale
    bump_value = 3.0  #default bump value
    x_plus = -150 # default value for texture attach cube x translation #-150 so it starts at 0
    
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        if '_Base_Color_1' in i: #only use Base_Color to get base material name
            tex_nm = i.replace("_Base_Color_1", "")  #texture name, without the Base_Color_1 text
        
            myColor = tex_nm + '_Base_Color_1'
            myAO = tex_nm + '_Ambient_Occlusion_1'
            myMetal = tex_nm + '_Metallic_1'
            myRough = tex_nm + '_Roughness_1'
            #myNormal = tex_nm + '_Normal_1'  # triplanar uv seams glitch for normal map
            myHeight = tex_nm + '_Height_1'   # height bump looks better than normal in arnold for tileable textures :( 
            
            #_________________________________________#

            # create shader
            arn_mat = mc.shadingNode ( 'aiStandardSurface', n = tex_nm + '_mat', asShader=True)
            
            # create shader group
            arn_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = arn_mat + 'SG'  )

            # connect material to shader group
            mc.connectAttr(arn_mat + '.outColor', arn_mat_SG + '.surfaceShader', f=True)
            
            #_________________________________________#
            #_________________________________________#

            if mc.objExists(myColor):
                # set place2dTexture scale to work better with arnold triplanar node, ctrl scale via triplanar node then and not place2dTexture
                # get child of specific connection, or will list same child multiple times from different connections
                myColor_place2dTexture = mc.listConnections(myColor + '.uvCoord', type='place2dTexture')[0]
                mc.setAttr(myColor_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                #create triplanar node
                myColor_tri_node = mc.shadingNode ( 'aiTriplanar', n = tex_nm + '_baseColor_tri_node', asShader=True)
                mc.setAttr(myColor_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myColor_tri_node + ".blend", tri_blend)
                #add to channel box for group control
                mc.setAttr(myColor_tri_node + '.offsetX', k=True); mc.setAttr(myColor_tri_node + '.offsetY', k=True); mc.setAttr(myColor_tri_node + '.offsetZ', k=True) 
                mc.setAttr(myColor_tri_node + '.rotateX', k=True); mc.setAttr(myColor_tri_node + '.rotateY', k=True); mc.setAttr(myColor_tri_node + '.rotateZ', k=True)
                mc.setAttr(myColor_tri_node + '.scaleX', k=True); mc.setAttr(myColor_tri_node + '.scaleY', k=True); mc.setAttr(myColor_tri_node + '.scaleZ', k=True)
                mc.setAttr(myColor_tri_node + '.blend', k=True)
                mc.setAttr(myColor_tri_node + '.coordSpace', k=True)
                mc.setAttr(myColor_tri_node + '.cell', k=True)
                mc.setAttr(myColor_tri_node + '.cellBlend', k=True)
                mc.setAttr(myColor_tri_node + '.cellRotate', k=True)
                mc.setAttr(myColor_tri_node + '.flipOnOppositeDirection', k=True)

                #triplanar to arnold material
                #mc.connectAttr(myColor_tri_node + '.outColor', arn_mat + '.baseColor')  #layer node instead
                #color to triplanar
                mc.connectAttr(myColor + '.outColor', myColor_tri_node + '.input') 
                #to prevent color space warning
                mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
                
                #------------------------------------------------------#
                #add optional facing ratio (FRESNEL) node, off by default  #automatically works with bump
                facing_ratio_node = mc.shadingNode ( 'aiFacingRatio', n = tex_nm + '_facing_ratio_node', asShader=True)
                mc.setAttr(facing_ratio_node + '.bias', 0.75) #set basic facing ratio default setting
                mc.setAttr(facing_ratio_node + '.gain', 0.25)
                mc.setAttr(facing_ratio_node + '.invert', 1)
                #create ramp node to better control
                facing_ratio_ramp_node = mc.shadingNode ( 'ramp', n = tex_nm + '_facing_ratio_ramp_node', asShader=True)
                #arnold layer node to layer fresnel on base color
                layer_node = mc.shadingNode ( 'aiLayerRgba', n = tex_nm + '_layer_node', asShader=True)
                mc.setAttr(layer_node + '.enable8', 1)  # enable layer 8 base color, 
                #mc.setAttr(layer_node + '.enable7', 1)  # maybe or maybe not leave fresnel layer 7 off by default
                mc.setAttr(layer_node + '.enable1', 0)  # disable layer way to not cover up others
                
                #facing ratio to ramp
                mc.connectAttr(facing_ratio_node + '.outValue', facing_ratio_ramp_node + '.vCoord') 
                #triplanar to layer node
                mc.connectAttr(myColor_tri_node + '.outColor', layer_node + '.input8') 
                #facing ratio ramp to layer node mask
                mc.connectAttr(facing_ratio_ramp_node + '.outAlpha', layer_node + '.mix7') 
                #layer node to arnold material
                mc.connectAttr(layer_node + '.outColor', arn_mat + '.baseColor') 
                
                #if AO exists (and baseColor already exists)
                if mc.objExists(myAO):
                    myAO_place2dTexture = mc.listConnections(myAO + '.uvCoord', type='place2dTexture')[0]      
                    mc.setAttr(myAO_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                    
                    # create arnold multply node for AO and baseColor
                    ao_mult_node = mc.shadingNode ( 'aiMultiply', n = tex_nm + '_ao_mult_node', asShader=True)
                    #reconnect baseColor to AO mult node
                    mc.connectAttr(myColor + '.outColor', ao_mult_node + '.input1') 
                    #connect ao to AO mult 
                    mc.connectAttr(myAO + '.outColor', ao_mult_node + '.input2')
                    #connect AO mult to triplanar
                    mc.connectAttr(ao_mult_node + '.outColor', myColor_tri_node + '.input', force=True)
                    
                    #to prevent color space warning
                    mc.setAttr(myAO + '.ignoreColorSpaceFileRules', 1)
                    #set color space of texture to raw
                    mc.setAttr(myAO + '.colorSpace', 'Raw', type='string')
                    
                    
            if mc.objExists(myMetal):
                myMetal_place2dTexture = mc.listConnections(myMetal + '.uvCoord', type='place2dTexture')[0]
                mc.setAttr(myMetal_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                #create triplanar node
                myMetal_tri_node = mc.shadingNode ( 'aiTriplanar', n = tex_nm + '_metal_tri_node', asShader=True)
                mc.setAttr(myMetal_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myMetal_tri_node + ".blend", tri_blend)
                #add to channel box for group control
                mc.setAttr(myMetal_tri_node + '.offsetX', k=True); mc.setAttr(myMetal_tri_node + '.offsetY', k=True); mc.setAttr(myMetal_tri_node + '.offsetZ', k=True) 
                mc.setAttr(myMetal_tri_node + '.rotateX', k=True); mc.setAttr(myMetal_tri_node + '.rotateY', k=True); mc.setAttr(myMetal_tri_node + '.rotateZ', k=True)
                mc.setAttr(myMetal_tri_node + '.scaleX', k=True); mc.setAttr(myMetal_tri_node + '.scaleY', k=True); mc.setAttr(myMetal_tri_node + '.scaleZ', k=True)
                mc.setAttr(myMetal_tri_node + '.blend', k=True)
                mc.setAttr(myMetal_tri_node + '.coordSpace', k=True)
                mc.setAttr(myMetal_tri_node + '.cell', k=True)
                mc.setAttr(myMetal_tri_node + '.cellBlend', k=True)
                mc.setAttr(myMetal_tri_node + '.cellRotate', k=True)
                mc.setAttr(myMetal_tri_node + '.flipOnOppositeDirection', k=True)
                
                #create luminance node (convert rgb into single out)
                myMetal_lum_node = mc.shadingNode ( 'luminance', n = tex_nm + '_metal_lum_node', asShader=True)
                #create ramp node to better ctrl metalness
                myMetal_ramp_node = mc.shadingNode ( 'ramp', n = tex_nm + '_metal_ramp_node', asShader=True)
                
                #texture to triplanar
                mc.connectAttr(myMetal + '.outColor', myMetal_tri_node + '.input') 
                #triplanar to luminance
                mc.connectAttr(myMetal_tri_node + '.outColor', myMetal_lum_node + '.value') 
                #luminance to ramp
                mc.connectAttr(myMetal_lum_node + '.outValue', myMetal_ramp_node + '.vCoord') 
                #luminance to arnold
                mc.connectAttr(myMetal_ramp_node + '.outAlpha', arn_mat + '.metalness') 
                
                #to prevent color space warning
                mc.setAttr(myMetal + '.ignoreColorSpaceFileRules', 1)
                #set color space of metallic texture to raw
                mc.setAttr(myMetal + '.colorSpace', 'Raw', type='string')


            if mc.objExists(myRough):
                #2d placement node settings
                myRough_place2dTexture = mc.listConnections(myRough + '.uvCoord', type='place2dTexture')[0]
                mc.setAttr(myRough_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                #create triplanar node
                myRough_tri_node = mc.shadingNode ( 'aiTriplanar', n = tex_nm + '_rough_tri_node', asShader=True)
                mc.setAttr(myRough_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myRough_tri_node + ".blend", tri_blend)
                #add to channel box for group control
                mc.setAttr(myRough_tri_node + '.offsetX', k=True); mc.setAttr(myRough_tri_node + '.offsetY', k=True); mc.setAttr(myRough_tri_node + '.offsetZ', k=True) 
                mc.setAttr(myRough_tri_node + '.rotateX', k=True); mc.setAttr(myRough_tri_node + '.rotateY', k=True); mc.setAttr(myRough_tri_node + '.rotateZ', k=True)
                mc.setAttr(myRough_tri_node + '.scaleX', k=True); mc.setAttr(myRough_tri_node + '.scaleY', k=True); mc.setAttr(myRough_tri_node + '.scaleZ', k=True)
                mc.setAttr(myRough_tri_node + '.blend', k=True)
                mc.setAttr(myRough_tri_node + '.coordSpace', k=True)
                mc.setAttr(myRough_tri_node + '.cell', k=True)
                mc.setAttr(myRough_tri_node + '.cellBlend', k=True)
                mc.setAttr(myRough_tri_node + '.cellRotate', k=True)
                mc.setAttr(myRough_tri_node + '.flipOnOppositeDirection', k=True)
                
                #create luminance node (convert rgb into single out)
                myRough_lum_node = mc.shadingNode ( 'luminance', n = tex_nm + '_rough_lum_node', asShader=True)
                #create ramp node to better ctrl roughness
                myRough_ramp_node = mc.shadingNode ( 'ramp', n = tex_nm + '_rough_ramp_node', asShader=True)
                
                #texture to triplanar
                mc.connectAttr(myRough + '.outColor', myRough_tri_node + '.input') 
                #triplanar to luminance
                mc.connectAttr(myRough_tri_node + '.outColor', myRough_lum_node + '.value') 
                #luminance to ramp
                mc.connectAttr(myRough_lum_node + '.outValue', myRough_ramp_node + '.vCoord') 
                #ramp to arnold
                mc.connectAttr(myRough_ramp_node + '.outAlpha', arn_mat + '.specularRoughness') 
                
                #to prevent color space warning
                mc.setAttr(myRough + '.ignoreColorSpaceFileRules', 1)
                #set color space of metallic texture to raw
                mc.setAttr(myRough + '.colorSpace', 'Raw', type='string')


            if mc.objExists(myHeight):
                myHeight_place2dTexture = mc.listConnections(myHeight + '.uvCoord', type='place2dTexture')[0]
                mc.setAttr(myHeight_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                #create arnold height node for height map
                bump_2d_node = mc.shadingNode ( 'aiBump2d', n = tex_nm + '_bump_2d_node', asShader=True)
                mc.setAttr(bump_2d_node + ".bumpHeight", bump_value)
                #create arnold color correct node, to convert rgb to alpha value, for bump node
                color_correct_node = mc.shadingNode ( 'aiColorCorrect', n = tex_nm + '_color_correct_node', asShader=True)
                mc.setAttr(color_correct_node + ".alphaIsLuminance", 1) #check is luminance or won't work

                #create triplanar node
                myHeight_tri_node = mc.shadingNode ( 'aiTriplanar', n = tex_nm + '_height_tri_node', asShader=True)
                mc.setAttr(myHeight_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myHeight_tri_node + ".blend", tri_blend)
                #add to channel box for group control
                mc.setAttr(myHeight_tri_node + '.offsetX', k=True); mc.setAttr(myHeight_tri_node + '.offsetY', k=True); mc.setAttr(myHeight_tri_node + '.offsetZ', k=True) 
                mc.setAttr(myHeight_tri_node + '.rotateX', k=True); mc.setAttr(myHeight_tri_node + '.rotateY', k=True); mc.setAttr(myHeight_tri_node + '.rotateZ', k=True)
                mc.setAttr(myHeight_tri_node + '.scaleX', k=True); mc.setAttr(myHeight_tri_node + '.scaleY', k=True); mc.setAttr(myHeight_tri_node + '.scaleZ', k=True)
                mc.setAttr(myHeight_tri_node + '.blend', k=True)
                mc.setAttr(myHeight_tri_node + '.coordSpace', k=True)
                mc.setAttr(myHeight_tri_node + '.cell', k=True)
                mc.setAttr(myHeight_tri_node + '.cellBlend', k=True)
                mc.setAttr(myHeight_tri_node + '.cellRotate', k=True)
                mc.setAttr(myHeight_tri_node + '.flipOnOppositeDirection', k=True)
                
                #texture to triplanar
                mc.connectAttr(myHeight + '.outColor', myHeight_tri_node + '.input') 
                #connect triplanar to color correct node for rgb to alpha
                mc.connectAttr(myHeight_tri_node + '.outColor', color_correct_node + '.input')
                #connect arnold color correct node to arnold bump 2d node
                mc.connectAttr(color_correct_node + '.outAlpha', bump_2d_node + '.bumpMap')
                #bump node to arnold material normal camera
                mc.connectAttr(bump_2d_node + '.outValue', arn_mat + '.normalCamera')
                
                #prevent color space from changing
                mc.setAttr(myHeight + '.ignoreColorSpaceFileRules', 1)
                #set color space of height texture to raw (or will not work)
                mc.setAttr(myHeight + '.colorSpace', 'Raw', type='string')

            '''
            if mc.objExists(myNormal):
                myNormal_place2dTexture = mc.listConnections(myNormal + '.uvCoord', type='place2dTexture')[0]
                mc.setAttr(myNormal_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                #create arnold normal node for normal map
                normal_map_node = mc.shadingNode ( 'aiNormalMap', n = tex_nm + '_normal_map_node', asShader=True)

                #create triplanar node
                myNormal_tri_node = mc.shadingNode ( 'aiTriplanar', n = tex_nm + '_normal_tri_node', asShader=True)
                mc.setAttr(myNormal_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                #add to channel box for group control
                mc.setAttr(myNormal_tri_node + '.offsetX', k=True); mc.setAttr(myNormal_tri_node + '.offsetY', k=True); mc.setAttr(myNormal_tri_node + '.offsetZ', k=True) 
                mc.setAttr(myNormal_tri_node + '.rotateX', k=True); mc.setAttr(myNormal_tri_node + '.rotateY', k=True); mc.setAttr(myNormal_tri_node + '.rotateZ', k=True)
                mc.setAttr(myNormal_tri_node + '.scaleX', k=True); mc.setAttr(myNormal_tri_node + '.scaleY', k=True); mc.setAttr(myNormal_tri_node + '.scaleZ', k=True)
                mc.setAttr(myNormal_tri_node + '.blend', k=True)
                mc.setAttr(myNormal_tri_node + '.coordSpace', k=True)
                mc.setAttr(myNormal_tri_node + '.cell', k=True)
                mc.setAttr(myNormal_tri_node + '.cellBlend', k=True)
                mc.setAttr(myNormal_tri_node + '.cellRotate', k=True)
                mc.setAttr(myNormal_tri_node + '.flipOnOppositeDirection', k=True)
                
                #texture to triplanar
                mc.connectAttr(myNormal + '.outColor', myNormal_tri_node + '.input') 
                #connect triplanar to normal map node
                mc.connectAttr(myNormal_tri_node + '.outColor', normal_map_node + '.input')
                #connect arnold normal map node to material
                mc.connectAttr(normal_map_node + '.outValue', arn_mat + '.normalCamera')
                
                #invert normal Y on normal map node
                if flip_normal_y == True: 
                    mc.setAttr(normal_map_node + '.invertY', 1)
                else:
                    pass
                #prevent color space from changing
                mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
                #set color space of normal texture to raw (or will not work)
                mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')
                '''
            
            #_________________________________________# 
            #create box to assign material too
            texture_box = mc.polyCube(n=tex_nm + '_box', w=100, h=100, d=100, ch=0)[0]
            x_plus += 150
            print(x_plus)
            mc.select(texture_box)
            mc.move(x_plus, 50, 0 ) # move box up and over more for each iteration
            #assign material to box (as to preserve if delete unused nodes)
            mc.hyperShade(assign = tex_nm + '_mat')
        
        else:
            pass