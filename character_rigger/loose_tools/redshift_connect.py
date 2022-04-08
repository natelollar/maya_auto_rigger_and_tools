#Select in this order
#1.Color
#2.AO
#3.Roughness
#4.Metalness
#5.Normal
#6.Redshift Material
import maya.cmds as mc

mySel = mc.ls(sl=True)
myColor = mySel[0]
myAO = mySel[1]
myMetal = mySel[2]
myRough = mySel[3]
myNormal = mySel[4]
myRedMat = mySel[-1]

#set redshift material reflection BRDF to GGX
mc.setAttr(myRedMat + '.refl_brdf', 1)
#set redshift material fresnel type to Metalness
mc.setAttr(myRedMat + '.refl_fresnel_mode', 2)

#connect diffuse/ albedo texture file to redshift material color
mc.connectAttr(myColor + '.outColor', myRedMat + '.diffuse_color') 
#to prevent color space warning (as if adjusting color space in pref may affect this)
mc.setAttr(myColor + '.ignoreColorSpaceFileRules', 1)

#connect ambient occlusion grayscale to color weight
mc.connectAttr(myAO + '.outAlpha', myRedMat + '.diffuse_weight')
#to prevent color space warning (as if adjusting color space in pref may affect this)
mc.setAttr(myAO + '.ignoreColorSpaceFileRules', 1)


#connect aroughness grayscale to material reflection metalness
mc.connectAttr(myMetal + '.outAlpha', myRedMat + '.refl_metalness')
#to use alpha channel as single luminance output
mc.setAttr(myMetal + '.alphaIsLuminance', 1)
# prevent color space from changing
mc.setAttr(myMetal + '.ignoreColorSpaceFileRules', 1)
#set color space of metalness texture to raw
mc.setAttr(myMetal + '.colorSpace', 'Raw', type='string')


#connect aroughness grayscale to material reflection roughness
mc.connectAttr(myRough + '.outAlpha', myRedMat + '.refl_roughness')
#to use alpha channel as single luminance output
mc.setAttr(myRough + '.alphaIsLuminance', 1)
# prevent color space from changing
mc.setAttr(myRough + '.ignoreColorSpaceFileRules', 1)
#set color space of roughness texture to raw
mc.setAttr(myRough + '.colorSpace', 'Raw', type='string')



#create bump node for normal map
bumpNode = mc.shadingNode('RedshiftBumpMap', asTexture=True, n=myNormal + '_bumpNode')
# set bump node scale to 1
mc.setAttr(bumpNode + '.scale', 1)
#set bump node input type to tangent space
mc.setAttr(bumpNode + '.inputType', 1)
#flip normal Y on bump node
mc.setAttr(bumpNode + '.flipY', 1)
#connect redshift bump node to material
mc.connectAttr(bumpNode + '.out', myRedMat + '.bump_input')

#connect normal texture to bump node
mc.connectAttr(myNormal + '.outColor', bumpNode + '.input')
# prevent color space from changing
mc.setAttr(myNormal + '.ignoreColorSpaceFileRules', 1)
#set color space of normal texture to raw (or will not work)
mc.setAttr(myNormal + '.colorSpace', 'Raw', type='string')

'''
#trying to pin nodes
import maya.cmds as mc

mySel = mc.ls(sl=True)

mc.nodeEditor(mySel, e=True, pinSelectedNodes=1)
'''


