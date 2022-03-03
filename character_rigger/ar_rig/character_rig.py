# main rig

import maya.cmds as mc

from ..ar_functions import find_jnts
from ..ar_functions import nurbs_ctrl
from . import fk_spine_rig
from . import extra_rig
from . import face_rig
from . import leg_rig
from . import arm_rig

def character_rig():
    #________________________________________________________________________#

    # global control
    global_ctrl_var = nurbs_ctrl.nurbs_ctrl(name='character_global_ctrl', 
                                            size=1, 
                                            colorR=1, 
                                            colorG=1, 
                                            colorB=0 )

    global_ctrl_info = global_ctrl_var.global_ctrl()

    #________________________________________________________________________#

    # fk spine controls, including fk neck controls 
    fk_spine_rig_var = fk_spine_rig.fk_spine_rig_class()
    fk_spine_rig_info = fk_spine_rig_var.fk_spine_rig_meth()

    # parent top spine ctrl group under global control
    mc.parent(fk_spine_rig_info[0], global_ctrl_info[1])

    #________________________________________________________________________#

    # find spine root joint
    # parent joints to global control
    spine_root_temp = find_jnts.find_jnts()
    spine_root = spine_root_temp.find_spine_root()

    mc.parent(spine_root, global_ctrl_info[1])

    #________________________________________________________________________#

    # create offset joints for blend color legs
    # parent constrain to spine root fk control
    spine_blend_offset = extra_rig.extra_rig ()
    spine_blend_offset_info =  spine_blend_offset.blend_jnt_offset( parent='spine_root_pos', 
                                                                    parentTo=fk_spine_rig_info[1], 
                                                                    size=5, 
                                                                    colorR=1, 
                                                                    colorG=0, 
                                                                    colorB=0)

    # parent spine offset JOINT under global control (for organization and global scale)
    mc.parent(spine_blend_offset_info, global_ctrl_info[1])
    '''
    #________________________________________________________________________#

    # fk jaw ctrl
    #parent to spine top (head) control
    jaw_ctrl_var = face_rig.face_rig()
    jaw_ctrl_var_info = jaw_ctrl_var.jaw_ctrl(fk_spine_rig_info[3])

    #________________________________________________________________________#

    # bot face ctrls
    # parent to jaw control
    bot_ctrls_var = face_rig.face_rig()
    bot_ctrls_var.bot_face_ctrls(jaw_ctrl_var_info[1])
    
    #________________________________________________________________________#

    # top face ctrls
    #parent to spine top (head) control
    top_ctrls_var = face_rig.face_rig()
    top_ctrls_info = top_ctrls_var.top_face_ctrls(  parent_to_head = fk_spine_rig_info[3], 
                                                    parent_to_jaw = jaw_ctrl_var_info[1], 
                                                    mid_ctrls = 2)

    #________________________________________________________________________#

    # ear ctrls
    #parent to spine top (head) control
    top_ctrls_var = face_rig.face_rig()
    top_ctrls_var.ear_ctrls(fk_spine_rig_info[3])

    #________________________________________________________________________#

    # tongue ctrls
    # parent to jaw controls
    top_ctrls_var = face_rig.face_rig()
    top_ctrls_var.tongue_ctrls(jaw_ctrl_var_info[1])
    
    #________________________________________________________________________#
    
    # left leg ctrls
    # parent to spine root control (global_ctrl for scale offset)
    left_leg_rig = leg_rig.leg_rig()
    left_leg_rig_info = left_leg_rig.create_fk_ik_leg(  direction='left',
                                                        offset_parent_jnt=spine_blend_offset_info,
                                                        fk_ctrl_size=12,
                                                        ik_ctrl_size=12,
                                                        pv_ctrl_size=1,
                                                        knee_dist_mult=10,
                                                        spine_root_ctrl=fk_spine_rig_info[1],
                                                        global_ctrl=global_ctrl_info[1] )

    # parent fk and ik hip controls under spine root control
    # ik hip to spine root ctrl
    mc.parent(left_leg_rig_info[0], fk_spine_rig_info[1])
    # fk hip to spine root ctrl
    mc.parent(left_leg_rig_info[1], fk_spine_rig_info[1])

    
    #________________________________________________________________________#

    # right leg ctrls
    # parent to spine root control
    right_leg_rig = leg_rig.leg_rig()
    right_leg_rig_info = right_leg_rig.create_fk_ik_leg(direction='right',
                                                        offset_parent_jnt=spine_blend_offset_info,
                                                        fk_ctrl_size=12,
                                                        ik_ctrl_size=12,
                                                        pv_ctrl_size=1,
                                                        knee_dist_mult=10,
                                                        global_ctrl=global_ctrl_info[1])

    # parent fk and ik hip controls under spine root control
    # ik hip to spine root ctrl
    mc.parent(right_leg_rig_info[0], fk_spine_rig_info[1])
    # fk hip to spine root ctrl
    mc.parent(right_leg_rig_info[1], fk_spine_rig_info[1])
    
    '''
    #________________________________________________________________________#
    # create offset joints for blend color arms

    # find chest jnt index
    chest_index = find_jnts.find_jnts()
    chest_index_info = chest_index.find_chest_jnt_index()

    # fk spine joints up to chest control
    to_chest_ctrl_list = fk_spine_rig_info[4]

    # create offset jnt
    # parent constrain offset jnt to fk chest ctrl
    chest_blend_offset = extra_rig.extra_rig ()
    chest_blend_offset_info =  chest_blend_offset.blend_jnt_offset( parent='chest_pos', 
                                                                    parentTo=to_chest_ctrl_list[chest_index_info], 
                                                                    size=5, 
                                                                    colorR=1, 
                                                                    colorG=0, 
                                                                    colorB=0)

    # parent chest offset joint under global control (for organization and global scale)
    mc.parent(chest_blend_offset_info, global_ctrl_info[1])
    
    
    
    #________________________________________________________________________#
    # create l arm ctrls
    arm_rig_class = arm_rig.arm_rig()

    arm_rig_return = arm_rig_class.arm_rig( direction='left', 
                                            offset_parent_jnt=chest_blend_offset_info, 
                                            fk_ctrl_size=12, 
                                            ik_ctrl_size=10, 
                                            pv_ctrl_size=1, 
                                            elbow_dist_mult=13, 
                                            to_chest_ctrl=fk_spine_rig_info[4],
                                            global_ctrl=global_ctrl_info[1] )

    
    '''
    #________________________________________________________________________#
    # create r arm ctrls
    arm_rig_class = arm_rig.arm_rig()

    arm_rig_return = arm_rig_class.arm_rig( direction='right', 
                                            offset_parent_jnt=chest_blend_offset_info, 
                                            fk_ctrl_size=12, 
                                            ik_ctrl_size=10, 
                                            pv_ctrl_size=1, 
                                            elbow_dist_mult=13, 
                                            global_ctrl=global_ctrl_info[1])
    '''
    

