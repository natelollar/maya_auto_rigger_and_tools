import maya.cmds as mc

from ..ar_functions import find_jnts

# find left hip joint
l_hip_var = find_jnts.find_jnts()

l_hip_var_info = l_hip_var.l_r_hip_jnt('left')