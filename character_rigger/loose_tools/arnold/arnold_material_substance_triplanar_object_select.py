import maya.cmds as mc

#drag and drop textures into hypershade  #select objects to apply shaders  
#object and texture names must have same base text (ex. 'human' and 'human_baseColor')
def arnold_material_substance_triplanar():  
    flip_normal_y = False #note, add checkbox
    tri_scl = 5.0  #triplanar scale 
    plc2d_scl = 0.001  #place2dTexture scale
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        myColor = i + '_Base_Color_1'
        myAO = i + '_Ambient_Occlusion_1'
        myMetal = i + '_Metallic_1'
        myRough = i + '_Roughness_1'
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

        if mc.objExists(myColor):
            # set place2dTexture scale to work better with arnold triplanar node, ctrl scale via triplanar node then and not place2dTexture
            # get child of specific connection, or will list same child multiple times from different connections
            myColor_place2dTexture = mc.listConnections(myColor + '.uvCoord', type='place2dTexture')[0]
            mc.setAttr(myColor_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
            
            #create triplanar node
            myColor_tri_node = mc.shadingNode ( 'aiTriplanar', n = i + '_baseColor_tri_node', asShader=True)
            mc.setAttr(myColor_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
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
            mc.connectAttr(myColor_tri_node + '.outColor', arn_mat + '.baseColor') 
            #color to triplanar
            mc.connectAttr(myColor + '.outColor', myColor_tri_node + '.input') 
            #to prevent color space warning
            mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)
            
            #if AO exists (and baseColor already exists)
            if mc.objExists(myAO):
                myAO_place2dTexture = mc.listConnections(myAO + '.uvCoord', type='place2dTexture')[0]      
                mc.setAttr(myAO_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
                
                # create arnold multply node for AO and baseColor
                ao_mult_node = mc.shadingNode ( 'aiMultiply', n = i + '_ao_mult_node', asShader=True)
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
            myMetal_tri_node = mc.shadingNode ( 'aiTriplanar', n = i + '_metal_tri_node', asShader=True)
            mc.setAttr(myMetal_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
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
            myMetal_lum_node = mc.shadingNode ( 'luminance', n = i + '_metal_lum_tri_node', asShader=True)
            #triplanar to luminance
            mc.connectAttr(myMetal_tri_node + '.outColor', myMetal_lum_node + '.value') 
            #luminance to arnold
            mc.connectAttr(myMetal_lum_node + '.outValue', arn_mat + '.metalness') 
            #metallic to triplanar
            mc.connectAttr(myMetal + '.outColor', myMetal_tri_node + '.input') 
            #to prevent color space warning
            mc.setAttr(myMetal + '.ignoreColorSpaceFileRules', 1)
            #set color space of metallic texture to raw
            mc.setAttr(myMetal + '.colorSpace', 'Raw', type='string')


        if mc.objExists(myRough):
            myRough_place2dTexture = mc.listConnections(myRough + '.uvCoord', type='place2dTexture')[0]
            mc.setAttr(myRough_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
            
            #create triplanar node
            myRough_tri_node = mc.shadingNode ( 'aiTriplanar', n = i + '_rough_tri_node', asShader=True)
            mc.setAttr(myRough_tri_node + ".scale", tri_scl, tri_scl, tri_scl) #set triplanar tile scale
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
            myRough_lum_node = mc.shadingNode ( 'luminance', n = i + '_rough_lum_tri_node', asShader=True)
            #triplanar to luminance
            mc.connectAttr(myRough_tri_node + '.outColor', myRough_lum_node + '.value') 
            #luminance to arnold
            mc.connectAttr(myRough_lum_node + '.outValue', arn_mat + '.specularRoughness') 
            #metallic to triplanar
            mc.connectAttr(myRough + '.outColor', myRough_tri_node + '.input') 
            #to prevent color space warning
            mc.setAttr(myRough + '.ignoreColorSpaceFileRules', 1)
            #set color space of metallic texture to raw
            mc.setAttr(myRough + '.colorSpace', 'Raw', type='string')


        if mc.objExists(myNormal):
            myNormal_place2dTexture = mc.listConnections(myNormal + '.uvCoord', type='place2dTexture')[0]
            mc.setAttr(myNormal_place2dTexture + ".repeatUV", plc2d_scl, plc2d_scl)
            
            #create arnold normal node for normal map
            normal_map_node = mc.shadingNode ( 'aiNormalMap', n = i + '_normal_map_node', asShader=True)

            #create triplanar node
            myNormal_tri_node = mc.shadingNode ( 'aiTriplanar', n = i + '_normal_tri_node', asShader=True)
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
           
        #_________________________________________# 
        #assign material
        mc.select(i)
        mc.hyperShade(assign = i + '_mat')