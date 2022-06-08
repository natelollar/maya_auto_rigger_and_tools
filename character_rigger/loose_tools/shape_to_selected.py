# switch out second selected ctrl shape for first selected curve shape

import maya.cmds as mc

def shape_to_selected():
    mySel = mc.ls(sl=True)

    new_obj = mySel[0]
    old_obj = mySel[1]

    # parent and freeze to set position and avoid unwanted movement when parent shape 
    mc.parent( new_obj, old_obj )
    mc.makeIdentity( new_obj, apply=True)
    mc.Unparent(new_obj)

    # get object shape to parent
    new_obj_shp = mc.listRelatives(new_obj, s=True)
    # get object shape to use name
    old_obj_shp = mc.listRelatives(old_obj, s=True)

    mc.parent(new_obj_shp, old_obj, r=True, shape=True)

    mc.delete(old_obj_shp)
    mc.rename(new_obj_shp, old_obj_shp)

#shape_to_selected()
