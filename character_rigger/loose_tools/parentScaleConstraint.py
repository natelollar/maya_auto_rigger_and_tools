import maya.cmds as mc

mySel = mc.ls(sl=1)

mc.parentConstraint(mySel[0], mySel[1], mo=True)
mc.scaleConstraint(mySel[0], mySel[1])