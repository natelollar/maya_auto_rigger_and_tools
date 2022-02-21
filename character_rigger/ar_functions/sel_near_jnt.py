import maya.cmds as mc

# select joint/s in bounding box (of nurbs standin objects)
def sel_near_jnt(standin_obj):
    #query joints in scene
    scene_jnt_list = mc.ls(type='joint')

    #select root standin object
    root_selection_box = mc.select(standin_obj, r=True)

    #get bounding box points of standin object (order: xmin ymin zmin xmax ymax zmax)
    root_selection_box_bb = mc.xform(root_selection_box, ws=True, bb=True, q=True)

    bb_x_min = root_selection_box_bb[0]
    bb_y_min = root_selection_box_bb[1]
    bb_z_min = root_selection_box_bb[2]
    bb_x_max = root_selection_box_bb[3]
    bb_y_max = root_selection_box_bb[4]
    bb_z_max = root_selection_box_bb[5]

    #select joint if in bounding box of standin object
    myJoint_list = []
    for jnts in scene_jnt_list:
        scene_jnt_list_position = mc.xform(jnts, query=True, translation=True, worldSpace=True )

        jnt_x_pos = scene_jnt_list_position[0]
        jnt_y_pos = scene_jnt_list_position[1]
        jnt_z_pos = scene_jnt_list_position[2]

        if jnt_x_pos >= bb_x_min:
            if jnt_y_pos >= bb_y_min:
                if jnt_z_pos >= bb_z_min:

                    if jnt_x_pos <= bb_x_max:
                        if jnt_y_pos <= bb_y_max:
                            if jnt_z_pos <= bb_z_max:
                                myJoint_list.append(jnts)
    
    mc.select(myJoint_list)
    return myJoint_list
    











