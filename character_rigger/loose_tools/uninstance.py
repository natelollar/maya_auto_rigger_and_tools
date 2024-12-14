from maya import cmds

my_sel = cmds.ls(selection=True)

for inst in my_sel:
    cmds.duplicate(inst)
    cmds.delete(inst)