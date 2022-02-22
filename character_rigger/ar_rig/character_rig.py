# main rig

import maya.cmds as mc

from character_rigger.ar_functions import find_jnts
from character_rigger.ar_functions import nurbs_ctrl
from character_rigger.ar_rig import fk_spine_rig
from character_rigger.ar_rig import extra_rig
from character_rigger.ar_rig import face_rig

#________________________________________________________________________#

# global control
global_ctrl_var = nurbs_ctrl.nurbs_ctrl(name='character_global_ctrl', 
                                        size=1, 
                                        colorR=1, 
                                        colorG=1, 
                                        colorB=0 )

global_ctrl_info = global_ctrl_var.global_ctrl()

#________________________________________________________________________#

# fk spine controls
fk_spine_rig_var = fk_spine_rig.fk_spine_rig_class()
fk_spine_rig_info = fk_spine_rig_var.fk_spine_rig_meth()

# parent top spine ctrl group under global control
mc.parent(fk_spine_rig_info[0], global_ctrl_info[1])

#________________________________________________________________________#

# parent joints to global control
spine_root_temp = find_jnts.find_jnts()
spine_root = spine_root_temp.find_spine_root()

mc.parent(spine_root, global_ctrl_info[1])

#________________________________________________________________________#

# create offset joints for blend color limbs
spine_blend_offset = extra_rig.extra_rig ()

spine_blend_offset_info =  spine_blend_offset.blend_jnt_offset('spine_root_pos', fk_spine_rig_info[1] , 5, 1, 0, 0)

# parent spine offset joint under global control
mc.parent(spine_blend_offset_info, global_ctrl_info[1])

#________________________________________________________________________#

# fk jaw ctrl
#parent to spine top (head) control
jaw_ctrl_var = face_rig.face_rig()
jaw_ctrl_var_info = jaw_ctrl_var.jaw_ctrl(fk_spine_rig_info[-1])

#________________________________________________________________________#

# bot face ctrls
# parent to jaw control
bot_ctrls_var = face_rig.face_rig()
bot_ctrls_var.bot_face_ctrls(jaw_ctrl_var_info[1])

#________________________________________________________________________#

# top face ctrls
#parent to spine top (head) control
top_ctrls_var = face_rig.face_rig()
top_ctrls_var.top_face_ctrls(fk_spine_rig_info[-1])