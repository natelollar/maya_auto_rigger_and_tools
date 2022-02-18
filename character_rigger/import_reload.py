import maya.cmds as mc
import imp
import character_rigger
import character_rigger.ar_functions
import character_rigger.ar_other
import character_rigger.ar_rig
import character_rigger.ar_rig.fk_spine_rig
import character_rigger.ar_rig.global_ctrl_setup
import character_rigger.ar_ui

imp.reload(character_rigger.ar_functions.sel_near_jnt)
imp.reload(character_rigger.ar_functions.sel_joints)
imp.reload(character_rigger.ar_functions.nurbs_ctrl)

imp.reload( character_rigger.ar_rig.character_rig )
imp.reload( character_rigger.ar_rig.fk_spine_rig )
imp.reload( character_rigger.ar_rig.global_ctrl_setup )
