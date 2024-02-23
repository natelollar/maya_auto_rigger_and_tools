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
import character_rigger.ar_rig.character_rig_quadruped
import character_rigger.ar_rig.clavicle_rig
import character_rigger.ar_rig.extra_rig
import character_rigger.ar_rig.face_rig
import character_rigger.ar_rig.fk_spine_rig
import character_rigger.ar_rig.leg_rig
import character_rigger.ar_rig.quadruped_leg_rig
import character_rigger.ar_rig.tail_tentacle_rig
import character_rigger.ar_rig.tentacle_rig
import character_rigger.ar_rig.tentacle_rigA
import character_rigger.ar_rig.arm_wing_rig
import character_rigger.ar_rig.fk_chains_rig

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
import character_rigger.tabs.shading_tab

import character_rigger.samples
import character_rigger.samples.soft_ik_native

import character_rigger.loose_tools
import character_rigger.loose_tools.arrow_twist_ctrl
import character_rigger.loose_tools.add_custom_attr
import character_rigger.loose_tools.add_space_switch_multi_1
import character_rigger.loose_tools.add_space_switch_multi_rot
import character_rigger.loose_tools.outliner_reorder
import character_rigger.loose_tools.assign_blinn_mat
import character_rigger.loose_tools.copy_attribute
import character_rigger.loose_tools.four_arrow_ctrl_simple
import character_rigger.loose_tools.vs_code_port_connect
import character_rigger.loose_tools.random_scatter_tools
import character_rigger.loose_tools.cylinder_ctrl
import character_rigger.loose_tools.joint_scale_compensate_toggle
import character_rigger.loose_tools.copy_vertex_weights
import character_rigger.loose_tools.mirror_jnt_same_orient

import character_rigger.loose_tools.arnold
import character_rigger.loose_tools.arnold.arnold_basic_character

import character_rigger.loose_tools.json_scripts
import character_rigger.loose_tools.json_scripts.save_curve_attributes

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
imp.reload( character_rigger.ar_rig.character_rig_quadruped)
imp.reload( character_rigger.ar_rig.clavicle_rig)
imp.reload( character_rigger.ar_rig.extra_rig)
imp.reload( character_rigger.ar_rig.face_rig)
imp.reload( character_rigger.ar_rig.fk_spine_rig)
imp.reload( character_rigger.ar_rig.leg_rig)
imp.reload( character_rigger.ar_rig.quadruped_leg_rig)
imp.reload( character_rigger.ar_rig.tail_tentacle_rig)
imp.reload( character_rigger.ar_rig.tentacle_rig)
imp.reload( character_rigger.ar_rig.tentacle_rigA)
imp.reload( character_rigger.ar_rig.arm_wing_rig )
imp.reload( character_rigger.ar_rig.fk_chains_rig )

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
imp.reload( character_rigger.tabs.shading_tab)

imp.reload( character_rigger.samples)
imp.reload( character_rigger.samples.soft_ik_native)

imp.reload( character_rigger.loose_tools )
imp.reload( character_rigger.loose_tools.arrow_twist_ctrl )
imp.reload( character_rigger.loose_tools.add_custom_attr )
imp.reload( character_rigger.loose_tools.add_space_switch_multi_1 )
imp.reload( character_rigger.loose_tools.add_space_switch_multi_rot )
imp.reload( character_rigger.loose_tools.outliner_reorder )
imp.reload( character_rigger.loose_tools.assign_blinn_mat )
imp.reload( character_rigger.loose_tools.copy_attribute )
imp.reload( character_rigger.loose_tools.four_arrow_ctrl_simple )
imp.reload( character_rigger.loose_tools.vs_code_port_connect )
imp.reload( character_rigger.loose_tools.random_scatter_tools )
imp.reload( character_rigger.loose_tools.cylinder_ctrl )
imp.reload( character_rigger.loose_tools.joint_scale_compensate_toggle )
imp.reload( character_rigger.loose_tools.copy_vertex_weights )
imp.reload( character_rigger.loose_tools.mirror_jnt_same_orient )

imp.reload( character_rigger.loose_tools.arnold )
imp.reload( character_rigger.loose_tools.arnold.arnold_basic_character )

imp.reload(  character_rigger.loose_tools.json_scripts )
imp.reload(  character_rigger.loose_tools.json_scripts.save_curve_attributes )

#_______________________________________________#

# relaunch UI
character_rigger.ar_ui.rigger_ui.rigger_ui_class().rigger_ui_method()