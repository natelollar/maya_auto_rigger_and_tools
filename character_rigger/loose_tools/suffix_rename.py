import maya.cmds as mc

mySel = mc.ls(sl=True)
suffix = "_jnt"

for i in mySel:
    new_name = (mc.rename(i, i + suffix)) 