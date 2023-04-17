import maya.cmds as mc

#drag materials into hypershade from windows explorer
#grab base color texture, or grab all textures
#Enable Cell for less seams when distorting
#larger triplanar scale for smaller cell sizes

def arnold_material_substance_triplanar():  
    flip_normal_y = False #note, add checkbox
    tri_scl = 0.001  #triplanar scale 
    tri_blend = 0.25  #default triplanar blend amount
    tri_cellBlend = 0.25
    bump_value = 3.0  #default bump value
    x_plus = -150 # default value for texture attach cube x translation #-150 so it starts at 0
    

    mySel = mc.ls(sl=True)

    for i in mySel:
        if '_Base_Color_1' in i: #only use Base_Color to get base material name
            tex_nm = i.replace("_Base_Color_1", "")  #texture name, without the Base_Color_1 text
        
            myColor = tex_nm + '_Base_Color_1'
            myColor_nm = myColor.replace("_1", "") 
            myAO = tex_nm + '_Ambient_Occlusion_1'
            myAO_nm = myAO.replace("_1", "") 
            myMetal = tex_nm + '_Metallic_1'
            myMetal_nm = myMetal.replace("_1", "") 
            myRough = tex_nm + '_Roughness_1'
            myRough_nm = myRough.replace("_1", "") 
            myHeight = tex_nm + '_Height_1'   # height bump looks better than normal in arnold for tileable textures :( 
            myHeight_nm = myHeight.replace("_1", "") 
            
            #_________________________________________#
            # create shader
            arn_mat = mc.shadingNode ( 'aiStandardSurface', n = tex_nm + '_mat', asShader=True)
            
            # create shader group
            arn_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = arn_mat + 'SG'  )

            # connect material to shader group
            mc.connectAttr(arn_mat + '.outColor', arn_mat_SG + '.surfaceShader', f=True)
            
            #_________________________________________#
            #create UV distort ramp
            uv_distort_ramp_node = mc.shadingNode ( 'ramp', n = tex_nm + '_uv_distort_ramp_node', asShader=True)
            mc.setAttr('.type', 7)  #Four Corner Ramp
            #ramp points create and position
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[0].position', 0.0)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[2].position', 0.333)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[3].position', 0.666)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[1].position', 1.0)
            #ramp colors
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[0].color', 1, 0, 0)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[2].color', 1, 1, 0)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[3].color', 0, 1, 0)
            mc.setAttr(uv_distort_ramp_node + '.colorEntryList[1].color', 0, 0, 1)
            
            #_________________________________________#

            if mc.objExists(myColor):
                #create arnold image node to replace default image file node
                myColor_image_node = mc.shadingNode( 'aiImage', n = myColor_nm + '_image_node', asShader=True)
                mc.setAttr(myColor_image_node + '.ignoreColorSpaceFileRules', 1) #to prevent color space warning
                myColor_file_path = mc.getAttr(myColor + ".fileTextureName") #get texture file path for new versiom of node
                mc.setAttr(myColor_image_node + '.filename', myColor_file_path, type='string') #set arnold image node file path
                #add to channel box
                mc.setAttr(myColor_image_node + '.sscale', k=True); mc.setAttr(myColor_image_node + '.tscale', k=True)
                mc.setAttr(myColor_image_node + '.soffset', k=True); mc.setAttr(myColor_image_node + '.toffset', k=True)
                
                #create arnold uv transform node
                myColor_uv_transform_node = mc.shadingNode( 'aiUvTransform', n = myColor_nm + '_uv_transform_node', asShader=True)
                #add to channel box for group control                
                mc.setAttr(myColor_uv_transform_node + '.scaleFrameX', k=True); mc.setAttr(myColor_uv_transform_node + '.scaleFrameY', k=True)
                mc.setAttr(myColor_uv_transform_node + '.translateFrameX', k=True); mc.setAttr(myColor_uv_transform_node + '.translateFrameY', k=True)
                mc.setAttr(myColor_uv_transform_node + '.rotateFrame', k=True)
                mc.setAttr(myColor_uv_transform_node + '.wrapFrameU', k=True); mc.setAttr(myColor_uv_transform_node + '.wrapFrameV', k=True)
                mc.setAttr(myColor_uv_transform_node + '.repeatX', k=True); mc.setAttr(myColor_uv_transform_node + '.repeatY', k=True)
                mc.setAttr(myColor_uv_transform_node + '.offsetX', k=True); mc.setAttr(myColor_uv_transform_node + '.offsetY', k=True)
                mc.setAttr(myColor_uv_transform_node + '.rotate', k=True)
                mc.setAttr(myColor_uv_transform_node + '.coverageX', k=True); mc.setAttr(myColor_uv_transform_node + '.coverageY', k=True)
                
                #create triplanar node
                myColor_tri_node = mc.shadingNode ( 'aiTriplanar', n = myColor_nm + '_tri_node', asShader=True)
                mc.setAttr(myColor_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myColor_tri_node + ".blend", tri_blend)
                mc.setAttr(myColor_tri_node + ".cellBlend", tri_cellBlend)
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


                #uv distor ramp to arnold texture node  #uvs are red and green
                mc.connectAttr(uv_distort_ramp_node + '.outColorR', myColor_image_node + '.uvcoordsX')
                mc.connectAttr(uv_distort_ramp_node + '.outColorG', myColor_image_node + '.uvcoordsY')
                #arnold image node to arnold uv transform
                mc.connectAttr(myColor_image_node + '.outColor', myColor_uv_transform_node + '.passthrough')
                #uv transform to triplanar
                mc.connectAttr(myColor_uv_transform_node + '.outColor', myColor_tri_node + '.input') 
                
                
                #------------------------------------------------------#
                #add optional use facing ratio (FRESNEL) node, off by default  #automatically works with bump
                facing_ratio_node = mc.shadingNode ( 'aiFacingRatio', n = myColor_nm + '_facing_ratio_node', asShader=True)
                mc.setAttr(facing_ratio_node + '.bias', 0.75) #set basic facing ratio default setting
                mc.setAttr(facing_ratio_node + '.gain', 0.25)
                mc.setAttr(facing_ratio_node + '.invert', 1)
                #create ramp node to better control
                facing_ratio_ramp_node = mc.shadingNode ( 'ramp', n = myColor_nm + '_facing_ratio_ramp_node', asShader=True)
                #arnold layer node to layer fresnel on base color
                layer_node = mc.shadingNode ( 'aiLayerRgba', n = myColor_nm + '_layer_node', asShader=True)
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
                    #create arnold image node to replace default image file node
                    myAO_image_node = mc.shadingNode( 'aiImage', n = myAO_nm + '_image_node', asShader=True)
                    mc.setAttr(myAO_image_node + '.ignoreColorSpaceFileRules', 1) #to prevent color space warning
                    myAO_file_path = mc.getAttr(myAO + ".fileTextureName") #get texture file path for new versiom of node
                    mc.setAttr(myAO_image_node + '.filename', myAO_file_path, type='string') #set arnold image node file path
                    #add to channel box
                    mc.setAttr(myAO_image_node + '.sscale', k=True); mc.setAttr(myAO_image_node + '.tscale', k=True)
                    mc.setAttr(myAO_image_node + '.soffset', k=True); mc.setAttr(myAO_image_node + '.toffset', k=True)
                
                    # create arnold multply node for AO and baseColor
                    ao_mult_node = mc.shadingNode ( 'aiMultiply', n = myAO_nm + '_mult_node', asShader=True)
                    
                    #uv distor ramp to arnold texture node  #uvs are red and green
                    mc.connectAttr(uv_distort_ramp_node + '.outColorR', myAO_image_node + '.uvcoordsX')
                    mc.connectAttr(uv_distort_ramp_node + '.outColorG', myAO_image_node + '.uvcoordsY')
                    
                    #reconnect baseColor uv transform to AO mult node
                    mc.connectAttr(myColor_image_node + '.outColor', ao_mult_node + '.input1') 
                    #connect ao to AO mult 
                    mc.connectAttr(myAO_image_node + '.outColor', ao_mult_node + '.input2')
                    
                    #connect AO mult to baseColor uv transform
                    mc.connectAttr(ao_mult_node + '.outColor', myColor_uv_transform_node + '.passthrough', force=True)
                    
                    #to prevent color space warning
                    mc.setAttr(myAO_image_node + '.ignoreColorSpaceFileRules', 1)
                    #set color space of texture to raw
                    mc.setAttr(myAO_image_node + '.colorSpace', 'Raw', type='string')
                    
            
            if mc.objExists(myMetal):
                #create arnold image node to replace default image file node
                myMetal_image_node = mc.shadingNode( 'aiImage', n = myMetal_nm + '_image_node', asShader=True)
                mc.setAttr(myMetal_image_node + '.ignoreColorSpaceFileRules', 1) #to prevent color space warning
                myMetal_file_path = mc.getAttr(myMetal + ".fileTextureName") #get texture file path for new versiom of node
                mc.setAttr(myMetal_image_node + '.filename', myMetal_file_path, type='string') #set arnold image node file path
                #add to channel box
                mc.setAttr(myMetal_image_node + '.sscale', k=True); mc.setAttr(myMetal_image_node + '.tscale', k=True)
                mc.setAttr(myMetal_image_node + '.soffset', k=True); mc.setAttr(myMetal_image_node + '.toffset', k=True)
                
                #create arnold uv transform node
                myMetal_uv_transform_node = mc.shadingNode( 'aiUvTransform', n = myMetal_nm + '_uv_transform_node', asShader=True)
                #add to channel box for group control                
                mc.setAttr(myMetal_uv_transform_node + '.scaleFrameX', k=True); mc.setAttr(myMetal_uv_transform_node + '.scaleFrameY', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.translateFrameX', k=True); mc.setAttr(myMetal_uv_transform_node + '.translateFrameY', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.rotateFrame', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.wrapFrameU', k=True); mc.setAttr(myMetal_uv_transform_node + '.wrapFrameV', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.repeatX', k=True); mc.setAttr(myMetal_uv_transform_node + '.repeatY', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.offsetX', k=True); mc.setAttr(myMetal_uv_transform_node + '.offsetY', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.rotate', k=True)
                mc.setAttr(myMetal_uv_transform_node + '.coverageX', k=True); mc.setAttr(myMetal_uv_transform_node + '.coverageY', k=True)
                
                
                #create triplanar node
                myMetal_tri_node = mc.shadingNode ( 'aiTriplanar', n = myMetal_nm + '_tri_node', asShader=True)
                mc.setAttr(myMetal_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myMetal_tri_node + ".blend", tri_blend)
                mc.setAttr(myMetal_tri_node + ".cellBlend", tri_cellBlend)
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
                myMetal_lum_node = mc.shadingNode ( 'luminance', n = myMetal_nm + '_lum_node', asShader=True)
                #create ramp node to better ctrl metalness
                myMetal_ramp_node = mc.shadingNode ( 'ramp', n = myMetal_nm + '_ramp_node', asShader=True)
                
                
                #uv distort ramp to arnold texture node  #uvs are red and green
                mc.connectAttr(uv_distort_ramp_node + '.outColorR', myMetal_image_node + '.uvcoordsX')
                mc.connectAttr(uv_distort_ramp_node + '.outColorG', myMetal_image_node + '.uvcoordsY')
                #arnold image node to arnold uv transform
                mc.connectAttr(myMetal_image_node + '.outColor', myMetal_uv_transform_node + '.passthrough')
                #uv transform to triplanar
                mc.connectAttr(myMetal_uv_transform_node + '.outColor', myMetal_tri_node  + '.input') 
                #triplanar to luminance
                mc.connectAttr(myMetal_tri_node + '.outColor', myMetal_lum_node + '.value') 
                #luminance to ramp
                mc.connectAttr(myMetal_lum_node + '.outValue', myMetal_ramp_node + '.vCoord') 
                #luminance to arnold
                mc.connectAttr(myMetal_ramp_node + '.outAlpha', arn_mat + '.metalness') 
                
                #to prevent color space warning
                mc.setAttr(myMetal_image_node + '.ignoreColorSpaceFileRules', 1)
                #set color space of metallic texture to raw
                mc.setAttr(myMetal_image_node + '.colorSpace', 'Raw', type='string')


            if mc.objExists(myRough):
                #create arnold image node to replace default image file node
                myRough_image_node = mc.shadingNode( 'aiImage', n = myRough_nm + '_image_node', asShader=True)
                mc.setAttr(myRough_image_node + '.ignoreColorSpaceFileRules', 1) #to prevent color space warning
                myRough_file_path = mc.getAttr(myRough + ".fileTextureName") #get texture file path for new versiom of node
                mc.setAttr(myRough_image_node + '.filename', myRough_file_path, type='string') #set arnold image node file path
                #add to channel box
                mc.setAttr(myRough_image_node + '.sscale', k=True); mc.setAttr(myRough_image_node + '.tscale', k=True)
                mc.setAttr(myRough_image_node + '.soffset', k=True); mc.setAttr(myRough_image_node + '.toffset', k=True)
                
                #create arnold uv transform node
                myRough_uv_transform_node = mc.shadingNode( 'aiUvTransform', n = myRough_nm + '_uv_transform_node', asShader=True)
                #add to channel box for group control                
                mc.setAttr(myRough_uv_transform_node + '.scaleFrameX', k=True); mc.setAttr(myRough_uv_transform_node + '.scaleFrameY', k=True)
                mc.setAttr(myRough_uv_transform_node + '.translateFrameX', k=True); mc.setAttr(myRough_uv_transform_node + '.translateFrameY', k=True)
                mc.setAttr(myRough_uv_transform_node + '.rotateFrame', k=True)
                mc.setAttr(myRough_uv_transform_node + '.wrapFrameU', k=True); mc.setAttr(myRough_uv_transform_node + '.wrapFrameV', k=True)
                mc.setAttr(myRough_uv_transform_node + '.repeatX', k=True); mc.setAttr(myRough_uv_transform_node + '.repeatY', k=True)
                mc.setAttr(myRough_uv_transform_node + '.offsetX', k=True); mc.setAttr(myRough_uv_transform_node + '.offsetY', k=True)
                mc.setAttr(myRough_uv_transform_node + '.rotate', k=True)
                mc.setAttr(myRough_uv_transform_node + '.coverageX', k=True); mc.setAttr(myRough_uv_transform_node + '.coverageY', k=True)
                
                
                #create triplanar node
                myRough_tri_node = mc.shadingNode ( 'aiTriplanar', n = myRough_nm + '_tri_node', asShader=True)
                mc.setAttr(myRough_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
                mc.setAttr(myRough_tri_node + ".blend", tri_blend)
                mc.setAttr(myRough_tri_node + ".cellBlend", tri_cellBlend)
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
                myRough_lum_node = mc.shadingNode ( 'luminance', n = myRough_nm + '_lum_node', asShader=True)
                #create ramp node to better ctrl metalness
                myRough_ramp_node = mc.shadingNode ( 'ramp', n = myRough_nm + '_ramp_node', asShader=True)
                
                
                #uv distort ramp to arnold texture node  #uvs are red and green
                mc.connectAttr(uv_distort_ramp_node + '.outColorR', myRough_image_node + '.uvcoordsX')
                mc.connectAttr(uv_distort_ramp_node + '.outColorG', myRough_image_node + '.uvcoordsY')
                #arnold image node to arnold uv transform
                mc.connectAttr(myRough_image_node + '.outColor', myRough_uv_transform_node + '.passthrough')
                #uv transform to triplanar
                mc.connectAttr(myRough_uv_transform_node + '.outColor', myRough_tri_node  + '.input') 
                #triplanar to luminance
                mc.connectAttr(myRough_tri_node + '.outColor', myRough_lum_node + '.value') 
                #luminance to ramp
                mc.connectAttr(myRough_lum_node + '.outValue', myRough_ramp_node + '.vCoord') 
                #luminance to arnold
                mc.connectAttr(myRough_ramp_node + '.outAlpha', arn_mat + '.specularRoughness') 
                
                #to prevent color space warning
                mc.setAttr(myRough_image_node + '.ignoreColorSpaceFileRules', 1)
                #set color space of metallic texture to raw
                mc.setAttr(myRough_image_node + '.colorSpace', 'Raw', type='string')
            
            
            if mc.objExists(myHeight):    
                #create arnold image node to replace default image file node
                myHeight_image_node = mc.shadingNode( 'aiImage', n = myHeight_nm + '_image_node', asShader=True)
                mc.setAttr(myHeight_image_node + '.ignoreColorSpaceFileRules', 1) #to prevent color space warning
                myHeight_file_path = mc.getAttr(myHeight + ".fileTextureName") #get texture file path for new versiom of node
                mc.setAttr(myHeight_image_node + '.filename', myHeight_file_path, type='string') #set arnold image node file path
                #add to channel box
                mc.setAttr(myHeight_image_node + '.sscale', k=True); mc.setAttr(myHeight_image_node + '.tscale', k=True)
                mc.setAttr(myHeight_image_node + '.soffset', k=True); mc.setAttr(myHeight_image_node + '.toffset', k=True)
                
                #create arnold uv transform node
                myHeight_uv_transform_node = mc.shadingNode( 'aiUvTransform', n = myHeight_nm + '_uv_transform_node', asShader=True)
                #add to channel box for group control                
                mc.setAttr(myHeight_uv_transform_node + '.scaleFrameX', k=True); mc.setAttr(myHeight_uv_transform_node + '.scaleFrameY', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.translateFrameX', k=True); mc.setAttr(myHeight_uv_transform_node + '.translateFrameY', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.rotateFrame', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.wrapFrameU', k=True); mc.setAttr(myHeight_uv_transform_node + '.wrapFrameV', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.repeatX', k=True); mc.setAttr(myHeight_uv_transform_node + '.repeatY', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.offsetX', k=True); mc.setAttr(myHeight_uv_transform_node + '.offsetY', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.rotate', k=True)
                mc.setAttr(myHeight_uv_transform_node + '.coverageX', k=True); mc.setAttr(myHeight_uv_transform_node + '.coverageY', k=True)
                
                
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
                mc.setAttr(myHeight_tri_node + ".cellBlend", tri_cellBlend)
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
                
                #uv distort ramp to arnold texture node  #uvs are red and green
                mc.connectAttr(uv_distort_ramp_node + '.outColorR', myHeight_image_node + '.uvcoordsX')
                mc.connectAttr(uv_distort_ramp_node + '.outColorG', myHeight_image_node + '.uvcoordsY')
                #arnold image node to arnold uv transform
                mc.connectAttr(myHeight_image_node + '.outColor', myHeight_uv_transform_node + '.passthrough')
                #uv transform to triplanar
                mc.connectAttr(myHeight_uv_transform_node + '.outColor', myHeight_tri_node  + '.input') 
                
                #connect triplanar to color correct node for rgb to alpha
                mc.connectAttr(myHeight_tri_node + '.outColor', color_correct_node + '.input')
                #connect arnold color correct node to arnold bump 2d node
                mc.connectAttr(color_correct_node + '.outAlpha', bump_2d_node + '.bumpMap')
                #bump node to arnold material normal camera
                mc.connectAttr(bump_2d_node + '.outValue', arn_mat + '.normalCamera')
                
                #prevent color space from changing
                mc.setAttr(myHeight_image_node + '.ignoreColorSpaceFileRules', 1)
                #set color space of height texture to raw (or will not work)
                mc.setAttr(myHeight_image_node + '.colorSpace', 'Raw', type='string')


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