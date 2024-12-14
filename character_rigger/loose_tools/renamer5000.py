import maya.api.OpenMaya as om2
from maya import cmds

def rename_objects(to_replace, replace):
    selection = om2.MGlobal.getActiveSelectionList()

    for i in range(selection.length()):
        obj = selection.getDagPath(i) 
        fn_dag = om2.MFnDagNode(obj)
        
        base_name = fn_dag.name() 
        new_name = base_name.replace(to_replace, replace)
        fn_dag.setName(new_name)

def prefix_objects(prefix):
    selection = om2.MGlobal.getActiveSelectionList()

    for i in range(selection.length()):
        obj = selection.getDagPath(i) 
        fn_dag = om2.MFnDagNode(obj)
        
        base_name = fn_dag.name() 
        new_name = prefix + base_name
        fn_dag.setName(new_name)

to_replace = "l_"
replace = "r_"

prefix = "l_"

rename_objects(to_replace, replace)
#prefix_objects(prefix)

# cmds.undoInfo(openChunk=True)
# try:
# except:
#     pass
# finally:
#     cmds.undoInfo(closeChunk=True)