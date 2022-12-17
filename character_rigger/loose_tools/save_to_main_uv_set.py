import maya.cmds as mc

my_sel = mc.ls(sl=True)

for i in my_sel:
    mc.polyCopyUV(i, uvSetNameInput="singleUDIM", uvSetName="UVMap", ch=1)