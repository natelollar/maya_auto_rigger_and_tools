# main rig

import maya.cmds as mc
import character_rigger
import character_rigger.ar_functions.nurbs_ctrl
import character_rigger.ar_rig.fk_spine_rig


# global control
global_ctrl_var = character_rigger.ar_functions.nurbs_ctrl.nurbs_ctrl(  name='character_global_ctrl', 
                                                                        size=1, 
                                                                        colorR=1, 
                                                                        colorG=1, 
                                                                        colorB=0 )

global_ctrl_info = global_ctrl_var.global_ctrl()

# fk spine controls
fk_spine_rig_var = character_rigger.ar_rig.fk_spine_rig.fk_spine_rig_class()

fk_spine_rig_info = fk_spine_rig_var.fk_spine_rig_meth()

# parent top spine group under global control
mc.parent(fk_spine_rig_info, global_ctrl_info[1])

# parent joints to global control
character_rigger.ar_functions.sel_near_jnt.sel_near_jnt('spine_ROOT_selection_box')
spine_root = mc.ls(sl=True)

#mc.parent(spine_root, global_ctrl_info[1])



