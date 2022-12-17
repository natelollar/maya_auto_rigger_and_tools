import maya.cmds as mc

mySel = mc.ls(sl=True)
new_name = "tri"


for i in mySel:
    (mc.rename(i, new_name + "#")) 