import imp
import maya.cmds as cmds
import character_rigger.ar_functions.nurbs_ctrl
imp.reload( character_rigger.ar_functions.nurbs_ctrl )

#shelf button
#locator to test camera pivot position
if cmds.objExists("cam_pivot_loc") == False:
    character_rigger.ar_functions.nurbs_ctrl.nurbs_ctrl( 
                                                        name="cam_pivot_loc",
                                                        size=60, 
                                                        colorR=1,
                                                        colorG=0.5,
                                                        colorB=0,
                                                        ).locator_ctrl()
                                                        
    cmds.setAttr("cam_pivot_locShape.lineWidth", 10)
    #cmds.setAttr("cam_pivot_locShape.overrideDisplayType", 1)
    cmds.connectAttr("perspShape.tumblePivot", "cam_pivot_loc.translate")
    cmds.parent("cam_pivot_loc", w=True)
    cmds.delete("cam_pivot_loc_grp")

else:
    print("\ncamera pivot locator already in scene")
    pass
    

#delete locator
#import maya.cmds as cmds
#cmds.delete("cam_pivot_loc")