import maya.cmds as cmds

selection = cmds.ls(sl=True)
print(selection)
for object in selection:
    print(object)
    #new_name = object.replace("_1", "")
    #new_name = object + "_BaseColor_1"
    #cmds.rename(object, new_name)

