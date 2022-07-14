import maya.cmds as cmds

sel = cmds.ls(sl=True)

for obj_id in sel:
    obj_id_shp = cmds.listRelatives(obj_id, s=True)
    cmds.setAttr( (obj_id_shp[0] + '.rsObjectId'), k=True )