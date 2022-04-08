#change material, maybe blinn, to redshift material with same name and attach to object instead
import maya.cmds as mc
#get blinn, first selection
myOldMat = mc.ls(sl=True)
#find shading group node of blinn
shadingGroupNode = mc.listConnections(d=True, s=False, type='shadingEngine')
#create redshift material
redMat = mc.shadingNode('RedshiftMaterial', asShader=True)
#connect new redshift material to old material shading group
mc.connectAttr(redMat + '.outColor', shadingGroupNode[0] + '.surfaceShader', f=True)
#rename shader group node, incase not
mc.rename(shadingGroupNode, myOldMat[0] + 'SG')
mc.delete(myOldMat)
mc.rename(redMat, myOldMat)