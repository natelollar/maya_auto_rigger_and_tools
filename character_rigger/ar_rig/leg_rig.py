import maya.cmds as mc

from character_rigger.ar_functions import find_jnts

# find left hip joint
l_hip_var = find_jnts.find_jnts( 'spine_ROOT_select_object' )

l_hip_var_info = l_hip_var.l_r_child_jnt('left')