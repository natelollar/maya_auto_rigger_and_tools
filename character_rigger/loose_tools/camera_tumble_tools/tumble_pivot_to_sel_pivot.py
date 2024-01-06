## camera tumble pivot to rotation pivot of selected
import maya.cmds as cmds

sel = cmds.ls(sl=True)[0]
print("\n")

viewport = cmds.getPanel(withFocus=True)
print("Viewport = " + str(viewport))
if "modelPanel" in viewport:
    current_cam_query = cmds.modelEditor(viewport, q=1, av=1, cam=1)
    current_cam = current_cam_query.split('|')[-1]
    print("Current Camera: " + current_cam) 
    
    if sel != []:  #if list is not empty
        #---- tumble pibot ------#
        sel_pivot_pos = cmds.xform(sel, q=True, ws=True, rp=True) #get selected obejct rotate pivot world space position
        print("Current Camera Pivot Position: " + str(sel_pivot_pos))
        cmds.setAttr((current_cam + ".tumblePivotX"), sel_pivot_pos[0])
        cmds.setAttr((current_cam + ".tumblePivotY"), sel_pivot_pos[1])
        cmds.setAttr((current_cam + ".tumblePivotZ"), sel_pivot_pos[2])
        
        #------ center of interest--------#
        # get distance between camera and rotate pivot of object, to set center of interest distance
        cam_pos = cmds.xform(current_cam, query=True, worldSpace=True, translation=True)
        
        #- distance between 2 points in 3d space equation -#
        x1 = cam_pos[0]
        y1 = cam_pos[1]
        z1 = cam_pos[2]
        #xyz position of intersection
        x2 = sel_pivot_pos[0]
        y2 = sel_pivot_pos[1]
        z2 = sel_pivot_pos[2]
        
        #part of following equation.  seperated to make easier to understand
        equationX = (x2 - x1) **2 #squared
        equationY = (y2 - y1) **2 
        equationZ = (z2 - z1) **2 

        #distance between two 3d points standard math equation
        dist_between = ( equationX + equationY + equationZ ) **0.5   # **0.5 is square root
        
        #set to absolute so distance is not negative
        dist_between_abs = abs(dist_between)
        print("Camera distance to object pivot: " + str(dist_between_abs))
        #set center of interest for current camera
        cmds.setAttr(current_cam + ".centerOfInterest", dist_between_abs)
        
        
        #-------------------------------#
        #----- Set locator position ----#
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
    else:
        print("Nothing selected for pivot.")
else:
    print("Not in viewport.")




    
    