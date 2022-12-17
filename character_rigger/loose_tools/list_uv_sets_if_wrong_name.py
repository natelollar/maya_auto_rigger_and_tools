import maya.cmds as cmds

my_sel = cmds.ls(sl=1)
cmds.select(cl=1)
print("\n")

for sel in my_sel:
    uv_set_names = cmds.polyUVSet(sel, allUVSets=True, query=True)
    if uv_set_names[0] != "map1":
        print("#____________#")
        print(sel)
        print(uv_set_names)
        cmds.select(sel, add=1)
