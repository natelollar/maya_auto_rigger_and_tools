import maya.cmds as mc

mySel = mc.ls(sl=True)

for i in mySel:
    mc.setAttr(i +  '.lockInfluenceWeights', k=0) #keyable/ channel box to 'off'
