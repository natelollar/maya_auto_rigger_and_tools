import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds

#set perspective camera Tumble pivot to mouse click using raycast
#select the raycast intersection with mesh that's closest to camera
#set to prefered hotkey, maybe 'ctrl + f'  

#create function that locates and sets Tumble pivot on click
def onPress():
    ctx = 'myCtx'  #tool name
    #find mouse position in 2d space
    vpX, vpY, _ = cmds.draggerContext(ctx, query=True, anchorPoint=True)  #viewport window X and Y

    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()

    omui.M3dView().active3dView().viewToWorld(int(vpX), int(vpY), pos, dir)
    pos2 = om.MFloatPoint(pos.x, pos.y, pos.z)
    
    #mesh list to check for intersections
    #does not work on instances and standins currently
    scene_mesh_list0 = cmds.ls(type='mesh', visible=True) #only select visible
    scene_mesh_list1 = [mesh for mesh in scene_mesh_list0 if "Orig" not in mesh] #remove origin meshes (from meshes with deformers)
    
    #find intersections
    intersection_list = []
    intersection_mesh_list = []
    for mesh in scene_mesh_list1:
        selectionList = om.MSelectionList()
        selectionList.add(mesh)
        dagPath = om.MDagPath()
        selectionList.getDagPath(0, dagPath)
        fnMesh = om.MFnMesh(dagPath)
        intersection = fnMesh.closestIntersection(
        om.MFloatPoint(pos2),
        om.MFloatVector(dir),
        None,
        None,
        False,
        om.MSpace.kWorld,
        99999,
        False,
        None,
        hitpoint,
        None,
        None,
        None,
        None,
        None)
        
        if intersection:
            x = hitpoint.x
            y = hitpoint.y
            z = hitpoint.z
            inter_xyz = [x, y, z]
            #create list of intersection XYZ positions
            intersection_list.append(inter_xyz)
            intersection_mesh_list.append(mesh)
        else:
            pass
    
    #if intersections from raycast mouse 2d position exist
    if intersection_list:
        cam_transform = "persp"
        cam_pos = cmds.xform(cam_transform, query=True, worldSpace=True, translation=True)
        
        #find distance to camera of each position
        distance_between_list = []
        distance_between_list_abs = []
        for inter in intersection_list:
            # xyz pos of camera
            x1 = cam_pos[0]
            y1 = cam_pos[1]
            z1 = cam_pos[2]
            #xyz position of intersection
            x2 = inter[0]
            y2 = inter[1]
            z2 = inter[2]
            
            #part of following equation.  seperated to make easier to understand
            equationX = (x2 - x1) **2 #squared
            equationY = (y2 - y1) **2 
            equationZ = (z2 - z1) **2 

            #distance between two 3d points standard math equation
            dist_between = ( equationX + equationY + equationZ ) **0.5   # **0.5 is square root
            
            # mouse raycast generates multiple intersections if there are multiple meshes in mouse line of site
            # add the distances between camera and intersection to list
            distance_between_list_abs.append(abs(dist_between)) #set to absolute so distance is not negative
        else:
            pass
        
        #get index list inex of smallest distance
        closest_inters_index = distance_between_list_abs.index(min(distance_between_list_abs) )
        #apply that index to original intersection position list
        closest_inters_pos = intersection_list[closest_inters_index]
        
        #set camera to first intersection point  (smallest distance between cam and intersection)
        cam_shape = "perspShape"
        cmds.setAttr(cam_shape + ".tumblePivotX", closest_inters_pos[0])
        cmds.setAttr(cam_shape + ".tumblePivotY", closest_inters_pos[1])
        cmds.setAttr(cam_shape + ".tumblePivotZ", closest_inters_pos[2])
        
        #get mesh intersected with for debugging
        closest_inters_mesh = intersection_mesh_list[closest_inters_index]
        print("--------- Intersected with " + str(closest_inters_mesh) + " at " + str(closest_inters_pos) + " ----------")
        
        #set locator to first intersection point
        #locator = cmds.spaceLocator()
        #cmds.setAttr(locator[0] + ".translate", closest_inters_pos[0], closest_inters_pos[1], closest_inters_pos[2] )
        #cmds.setAttr(locator[0] + ".localScale", 20, 20, 20)


#run tool. allows manual click on mesh to set camera Tumble Pivot
def pick_camera_pivot():
    ctx = 'myCtx'  #tool name
    if cmds.draggerContext(ctx, exists=True):
        cmds.deleteUI(ctx)
    cmds.draggerContext(ctx, pressCommand=onPress, name=ctx, cursor='crossHair')
    cmds.setToolTo(ctx)


