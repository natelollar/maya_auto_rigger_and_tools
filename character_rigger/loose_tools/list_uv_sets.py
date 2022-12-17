import maya.cmds as cmds


my_sel = cmds.ls(sl=1)

for sel in my_sel:
    uv_set_names = cmds.polyUVSet(sel, allUVSets=True, query=True)
    print("#____________#")
    print(sel)
    print(uv_set_names)