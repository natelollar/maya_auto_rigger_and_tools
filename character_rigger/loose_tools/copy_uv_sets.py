from maya import cmds

my_sel = cmds.ls(selection=True)

for object in my_sel:
    source_uv_set = "map1"
    new_uv_set = "map2" 

    # Get the list of UV sets before copying
    initial_uv_sets = cmds.polyUVSet(object, query=True, allUVSets=True)

    # --------------------- MAIN CODE ------------------------------ # 
    if not cmds.polyUVSet(object, query=True, uvSet=new_uv_set): # Create new UV set if needed
        cmds.polyUVSet(object, create=True, uvSet=new_uv_set) 
    # copy 'map1' to 'map2'
    cmds.polyCopyUV(object, uvSetNameInput=source_uv_set, uvSetName=new_uv_set, ch=False)

    # Get the list of UV sets after copying
    final_uv_sets = cmds.polyUVSet(object, query=True, allUVSets=True)
    # -------------------------------------------------------------- # 

    # Find the extra UV sets that may have been created
    extra_uv_sets = [uv for uv in final_uv_sets if uv not in initial_uv_sets and uv != new_uv_set]

    # Delete any extra UV sets
    for uv_set in extra_uv_sets:
        cmds.polyUVSet(object, delete=True, uvSet=uv_set)

    print(f"Copied UVs from {source_uv_set} to {new_uv_set} on {object}")
