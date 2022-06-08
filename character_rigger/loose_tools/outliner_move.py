import maya.cmds as mc

mySel = mc.ls(sl=True)

# go down 1 in outliner
for i in mySel:
    mc.reorder(i, relative=1)

mySel = mc.ls(sl=True)
  
# go up 1 in outliner
for i in mySel:
    mc.reorder(i, relative=-1)