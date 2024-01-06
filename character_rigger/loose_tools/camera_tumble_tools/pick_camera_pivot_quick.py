import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QCursor
from shiboken2 import wrapInstance

#set perspective camera Tumble pivot, no mouse click needed. sets point upon hotkey click
#select the raycast intersection with mesh that's closest to camera
#set to prefered hotkey, maybe 'ctrl + f'  

def viewport_mouse_pos():
    #get active viewport
    activeView = omui.M3dView.active3dView()
    #get cursor position
    globalPos = QCursor.pos()
    viewWidget = wrapInstance(int(activeView.widget()), QWidget)
    #get cursor x y screenspace position
    mousePos = viewWidget.mapFromGlobal(globalPos)
    flippedY0 = viewWidget.height() - mousePos.y()  #Y is fipped, up is down and down is up.   Fix.
    flippedY1 = flippedY0 - 1  #flip causes it to be one off from cmds.draggerContext()
    return mousePos.x(), flippedY1

#create function that locates and sets Tumble pivot on click
def onPress():
    #find mouse position in 2d space without cmds.draggerContext()
    vpX, vpY = viewport_mouse_pos() #viewport window X and Y

    pos = om.MPoint()
    dir = om.MVector()
    hitpoint = om.MFloatPoint()

    activeView = omui.M3dView.active3dView()
    activeView.viewToWorld(int(vpX), int(vpY), pos, dir)
    
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
        om.MFloatPoint(pos),
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
        viewport = cmds.getPanel(withFocus=True)
        print("Viewport = " + str(viewport))
        current_cam_query = cmds.modelEditor(viewport, q=1, av=1, cam=1)
        current_cam = current_cam_query.split('|')[-1]
        print("Current Camera: " + current_cam) 
        cam_pos = cmds.xform(current_cam, query=True, worldSpace=True, translation=True)
        
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
        cmds.setAttr(current_cam + ".tumblePivotX", closest_inters_pos[0])
        cmds.setAttr(current_cam + ".tumblePivotY", closest_inters_pos[1])
        cmds.setAttr(current_cam + ".tumblePivotZ", closest_inters_pos[2])

        #get distance for center of interest (affects zooming in and out)
        closest_inters_dist = min(distance_between_list_abs)
        print("Closest geo intersection: " + str(closest_inters_dist))
        #set center of interest for current camera
        cmds.setAttr(current_cam + ".centerOfInterest", closest_inters_dist)


        #----- Set locator position ----# (nead to for when camera changes)
        if cmds.objExists("cam_pivot_loc"):
            connected_cam = cmds.listConnections("cam_pivot_loc.translate")[0]
            print("Current camera connected to locator: " + connected_cam)
            
            same_cam = (current_cam == connected_cam)
            print("Same Camera: " + str(same_cam))
            
            if same_cam:
                pass
            else:
                cmds.connectAttr(current_cam + ".tumblePivot", "cam_pivot_loc.translate", f=True)
                
            new_connected_cam = cmds.listConnections("cam_pivot_loc.translate")[0]
            print("New camera connected to locator: " + new_connected_cam)
        else:
            print("No 'cam_pivot_loc' in scene.")


        #get mesh intersected with for debugging
        closest_inters_mesh = intersection_mesh_list[closest_inters_index]
        print("--------- Intersected with " + str(closest_inters_mesh) + " at " + str(closest_inters_pos) + " ----------")
        
        #set locator to first intersection point
        #locator = cmds.spaceLocator()
        #cmds.setAttr(locator[0] + ".translate", closest_inters_pos[0], closest_inters_pos[1], closest_inters_pos[2] )
        #cmds.setAttr(locator[0] + ".localScale", 20, 20, 20)


# run onPress function 
onPress()