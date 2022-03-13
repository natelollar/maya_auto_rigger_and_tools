# make maya shelf button to make changes to the scripts and easily reload
# add to when creating new files

import maya.cmds as mc
import imp

#_______________________________________________#
# import all
import character_rigger

import character_rigger.ar_functions
import character_rigger.ar_functions.bb_nurbs_ctrl
import character_rigger.ar_functions.create_jnts
import character_rigger.ar_functions.find_jnts
import character_rigger.ar_functions.nurbs_ctrl
import character_rigger.ar_functions.sel_joints
import character_rigger.ar_functions.sel_near_jnt

import character_rigger.ar_rig
import character_rigger.ar_rig.arm_rig
import character_rigger.ar_rig.character_rig
import character_rigger.ar_rig.clavicle_rig
import character_rigger.ar_rig.extra_rig
import character_rigger.ar_rig.face_rig
import character_rigger.ar_rig.fk_spine_rig
import character_rigger.ar_rig.leg_rig

import character_rigger.ar_tools
import character_rigger.ar_tools.fk_chain
import character_rigger.ar_tools.fk_ctrl

import character_rigger.ar_ui
import character_rigger.ar_ui.rigger_ui

import character_rigger.tabs
import character_rigger.tabs.animation
import character_rigger.tabs.auto_rig_tab
import character_rigger.tabs.color_slider
import character_rigger.tabs.modeling
import character_rigger.tabs.rigging
import character_rigger.tabs.misc_tab


#_______________________________________________#
# reimport all
imp.reload( character_rigger )

imp.reload( character_rigger.ar_functions)
imp.reload( character_rigger.ar_functions.bb_nurbs_ctrl)
imp.reload( character_rigger.ar_functions.create_jnts)
imp.reload( character_rigger.ar_functions.find_jnts)
imp.reload( character_rigger.ar_functions.nurbs_ctrl)
imp.reload( character_rigger.ar_functions.sel_joints)
imp.reload( character_rigger.ar_functions.sel_near_jnt)

imp.reload( character_rigger.ar_rig)
imp.reload( character_rigger.ar_rig.arm_rig)
imp.reload( character_rigger.ar_rig.character_rig)
imp.reload( character_rigger.ar_rig.clavicle_rig)
imp.reload( character_rigger.ar_rig.extra_rig)
imp.reload( character_rigger.ar_rig.face_rig)
imp.reload( character_rigger.ar_rig.fk_spine_rig)
imp.reload( character_rigger.ar_rig.leg_rig)

imp.reload( character_rigger.ar_tools)
imp.reload( character_rigger.ar_tools.fk_chain)
imp.reload( character_rigger.ar_tools.fk_ctrl)

imp.reload( character_rigger.ar_ui)
imp.reload( character_rigger.ar_ui.rigger_ui)

imp.reload( character_rigger.tabs)
imp.reload( character_rigger.tabs.animation)
imp.reload( character_rigger.tabs.auto_rig_tab)
imp.reload( character_rigger.tabs.color_slider)
imp.reload( character_rigger.tabs.modeling)
imp.reload( character_rigger.tabs.rigging)
imp.reload( character_rigger.tabs.misc_tab)

#_______________________________________________#
# relaunch UI
character_rigger.ar_ui.rigger_ui.rigger_ui_class().rigger_ui_method()