# main rig

import maya.cmds as mc

from ..tabs import auto_rig_tab
from ..ar_functions import find_jnts
from ..ar_functions import nurbs_ctrl
from . import fk_spine_rig
from . import extra_rig
from . import face_rig
from . import quadruped_leg_rig
from . import tail_tentacle_rig
from . import arm_wing_rig
from . import fk_chains_rig

def character_rig():
    #________________________________________________________________________#
    # return auto_rig ui tab info
    auto_rig_tab_info = auto_rig_tab.auto_rig_options().auto_rig_options()
    # generally lip corners and maybe mid cheek joints
    mid_jnt_amount = auto_rig_tab_info[0]
    # general scaling for physical size of controls
    control_size = auto_rig_tab_info[1]
    # get boolean value of headJnt checkbox
    headJnts_checkbox = auto_rig_tab_info[2]
    # get boolean value of twstJnt checkbox
    twstJnts_checkbox = auto_rig_tab_info[3]
    # get arm soft ik amount from textfield
    elbow_pv_dist = auto_rig_tab_info[4]
    # get leg soft ik amount from textfield
    knee_pv_dist = auto_rig_tab_info[5]
    
    #________________________________________________________________________#
    #create grp for item organization
    character_misc_grp = mc.group(em=1, n='character_misc_grp')

    #________________________________________________________________________#

    # global control
    global_ctrl_var = nurbs_ctrl.nurbs_ctrl(name='character_global_ctrl', 
                                            size= (1 * float(control_size) ), 
                                            colorR=1, 
                                            colorG=1, 
                                            colorB=0 )

    global_ctrl_info = global_ctrl_var.global_ctrl()

    #________________________________________________________________________#

    # fk spine controls, including fk neck controls 
    fk_spine_rig_var = fk_spine_rig.fk_spine_rig_class()
    fk_spine_rig_info = fk_spine_rig_var.fk_spine_rig_meth (ctrl_size = (4.5 * float(control_size) ) )

    # parent first spine ctrl grp under global control
    mc.parent(fk_spine_rig_info[0], global_ctrl_info[1])

    #________________________________________________________________________#

    # find spine root joint and parent to global ctrl
    # therefore parent ALL joints to global control for global scaling and organization
    spine_root_temp = find_jnts.find_jnts()
    spine_root = spine_root_temp.find_spine_root()

    mc.parent(spine_root, global_ctrl_info[1])

    #________________________________________________________________________#

    # create offset joints for blend color legs
    # parent constrain to spine root fk control
    spine_blend_offset = extra_rig.extra_rig ()
    spine_blend_offset_info =  spine_blend_offset.blend_jnt_offset( parent='spine_root_pos', 
                                                                    parentTo=fk_spine_rig_info[1], 
                                                                    size =5, 
                                                                    colorR=1, 
                                                                    colorG=0, 
                                                                    colorB=0)

    # parent spine offset JOINT under global control (for organization and global scale)
    mc.parent(spine_blend_offset_info, global_ctrl_info[1])
    # hide blend joint and blend leg joints as result
    mc.setAttr(spine_blend_offset_info + '.visibility', 0)

    
    #________________________________________________________________________#
    # head joints on/ off
    if headJnts_checkbox == True:
    #________________________________________________________________________#
        # fk jaw ctrl
        #parent to spine top (head) control
        jaw_ctrl_var = face_rig.face_rig()
        jaw_ctrl_var_info = jaw_ctrl_var.jaw_ctrl(  parent_to = fk_spine_rig_info[3], 
                                                    ctrl_size = (2.5 * float(control_size) ) 
                                                    )

        #________________________________________________________________________#

        # bot face ctrls
        # parent to jaw control
        bot_ctrls_var = face_rig.face_rig()
        bot_ctrls_var.bot_face_ctrls(   ctrl_size = (1 * float(control_size) ) , 
                                        parent_to = jaw_ctrl_var_info[1])
        
        #________________________________________________________________________#

        # top face ctrls/ mid face ctrls
        #parent to spine top (head) control
        top_ctrls_var = face_rig.face_rig()
        top_ctrls_info = top_ctrls_var.top_face_ctrls(  ctrl_size = (1 * float(control_size) ),
                                                        parent_to_head = fk_spine_rig_info[3], 
                                                        parent_to_jaw = jaw_ctrl_var_info[1], 
                                                        mid_ctrls = int(mid_jnt_amount) )
        # create extra grp for mid face ctrls
        face_grp = mc.group(em=1, n='face_grp')
        #if mid face ctrls exist
        if top_ctrls_info[2]:
            mc.parent(top_ctrls_info[2], face_grp)
        #parent top face ctrls to top head
        mc.parent(face_grp, character_misc_grp)

        #________________________________________________________________________#

        # ear ctrls (top face jnts w/ children jnt/s)
        #parent to spine top (head) control
        top_ctrls_var = face_rig.face_rig()
        top_ctrls_var.ear_ctrls(ctrl_size = (3 * float( control_size ) ), 
                                parent_to = fk_spine_rig_info[3])

        #________________________________________________________________________#

        # tongue ctrls
        # parent to jaw controls
        top_ctrls_var = face_rig.face_rig()
        top_ctrls_var.tongue_ctrls( ctrl_size = (3 * float( control_size ) ), 
                                    parent_to=jaw_ctrl_var_info[1] )
    elif headJnts_checkbox == False:
        pass
    
    #________________________________________________________________________#
    
    # left leg ctrls
    # parent to spine root control (global_ctrl for scale offset)
    left_leg_rig_info = quadruped_leg_rig.leg_rig().create_fk_ik_leg(  
                        direction='l',
                        ft_loc_dist = (15 * float(control_size) ),
                        offset_parent_jnt=spine_blend_offset_info,
                        swch_ctrl_dist = (40 * float(control_size) ),
                        toe_wiggle_size = (2 * float(control_size) ),
                        rev_foot_size = (3 * float(control_size) ),
                        fk_ctrl_size = (12 * float(control_size) ),
                        ik_ctrl_size = (12 * float(control_size) ),
                        pv_ctrl_size = (1 * float(control_size) ),
                        knee_dist_mult =  3.5, #(float(knee_pv_dist) * float(control_size) ),
                        spine_root_ctrl=fk_spine_rig_info[1],
                        global_ctrl=global_ctrl_info[1] 
                        )

    # parent fk and ik hip controls under spine root control
    # ik hip to spine root ctrl
    mc.parent(left_leg_rig_info[0], fk_spine_rig_info[1])
    # fk hip to spine root ctrl
    mc.parent(left_leg_rig_info[1], fk_spine_rig_info[1])
    # parent other grps to global misc grp
    mc.parent(left_leg_rig_info[2], character_misc_grp)
    
    
    #________________________________________________________________________#
    
    # right leg ctrls
    # parent to spine root control (global_ctrl for scale offset)
    right_leg_rig_info = quadruped_leg_rig.leg_rig().create_fk_ik_leg(  
                        direction='r',
                        ft_loc_dist = (15 * float(control_size) ),
                        offset_parent_jnt=spine_blend_offset_info,
                        swch_ctrl_dist = (40 * float(control_size) ),
                        toe_wiggle_size = (2 * float(control_size) ),
                        rev_foot_size = (3 * float(control_size) ),
                        fk_ctrl_size = (12 * float(control_size) ),
                        ik_ctrl_size = (12 * float(control_size) ),
                        pv_ctrl_size = (1 * float(control_size) ),
                        knee_dist_mult =  3.5, #(float(knee_pv_dist) * float(control_size) ),
                        spine_root_ctrl=fk_spine_rig_info[1],
                        global_ctrl=global_ctrl_info[1] 
                        )

    # parent fk and ik hip controls under spine root control
    # ik hip to spine root ctrl
    mc.parent(right_leg_rig_info[0], fk_spine_rig_info[1])
    # fk hip to spine root ctrl
    mc.parent(right_leg_rig_info[1], fk_spine_rig_info[1])
    # parent other grps to global misc grp
    mc.parent(right_leg_rig_info[2], character_misc_grp)


    #________________________________________________________________________#
    
    # tail ctrls

    tail_rig_info = tail_tentacle_rig.tail_tentacle_rig(    defaultJnt_prefix = 'sknJnt_',
                                                            fkJnt_prefix = 'fkJnt_',
                                                            ikJnt_prefix = 'ikJnt_',
                                                            offs_prntJnt = spine_blend_offset_info,
                                                            spine_root_ctrl = fk_spine_rig_info[1],
                                                            global_ctrl = global_ctrl_info[1],
                                                            global_misc_grp = character_misc_grp,
                                                            fk_ctrl_size = ( 10 * float(control_size) ) )


    
    #________________________________________________________________________#
    # create offset joints for blend color arms
    
    # find chest jnt index
    chest_index = find_jnts.find_jnts().find_chest_jnt_index()

    # fk spine joints up to chest control
    to_chest_ctrl  = extra_rig.extra_rig ().to_chest_ctrl(fk_spine_rig_info[4])

    # create offset jnt
    # parent constrain offset jnt to fk chest ctrl
    chest_blend_offset = extra_rig.extra_rig ()
    chest_blend_offset_info =  chest_blend_offset.blend_jnt_offset( parent='chest_pos', 
                                                                    parentTo=to_chest_ctrl[chest_index], 
                                                                    size=5, 
                                                                    colorR=1, 
                                                                    colorG=0, 
                                                                    colorB=0)

    # parent chest offset joint under global control (for organization and global scale)
    mc.parent(chest_blend_offset_info, global_ctrl_info[1])
    # hide blend joint and blend arm joints as result
    mc.setAttr(chest_blend_offset_info + '.visibility', 0)
    


    #________________________________________________________________________#
    # create l arm wing ctrls
    l_arm_wing_rig = arm_wing_rig.arm_wing_rig( direction = 'l',
                                                offset_parent_jnt = chest_blend_offset_info,
                                                swch_ctrl_size = (3 * float(control_size) ),
                                                swch_ctrl_dist = (35 * float(control_size) ),
                                                fk_ctrl_size = (10 * float(control_size) ),
                                                ik_ctrl_size = (10 * float(control_size) ),
                                                pv_ctrl_size = (20 * float(control_size) ), 
                                                chest_ctrl = to_chest_ctrl[chest_index],
                                                global_ctrl = global_ctrl_info[1],
                                                global_misc_grp=character_misc_grp )

            

    # create l arm wing fin ctrls
    l_arm_wing_fins = fk_chains_rig.fk_chains_rig(  direction = 'l',
                                                    jnt_prefix = 'sknJnt_',
                                                    standin_name = 'fkObj_',
                                                    fk_ctrl_size = 10,
                                                    aim_at_PV_ctrl = l_arm_wing_rig[3],
                                                    swch_ctrl = l_arm_wing_rig[4] )
    print ('||||||______________||||||')
    print (l_arm_wing_fins)


    #________________________________________________________________________#
    # create r arm wing ctrls
    r_arm_wing_rig = arm_wing_rig.arm_wing_rig( direction = 'r',
                                                offset_parent_jnt = chest_blend_offset_info,
                                                swch_ctrl_size = (3 * float(control_size) ),
                                                swch_ctrl_dist = (35 * float(control_size) ),
                                                fk_ctrl_size = (10 * float(control_size) ),
                                                ik_ctrl_size = (10 * float(control_size) ),
                                                pv_ctrl_size = (20 * float(control_size) ), 
                                                chest_ctrl = to_chest_ctrl[chest_index],
                                                global_ctrl = global_ctrl_info[1],
                                                global_misc_grp=character_misc_grp )

            
    '''
    # create r arm wing fin ctrls
    r_arm_wing_fins = fk_chains_rig.fk_chains_rig(  direction = 'r',
                                                    jnt_prefix = 'sknJnt_',
                                                    standin_name = 'fkObj_',
                                                    fk_ctrl_size = 10,
                                                    aim_at_PV_ctrl = r_arm_wing_rig[3],
                                                    swch_ctrl = r_arm_wing_rig[4] )


    
    #________________________________________________________________________#
    # create r arm ctrls
    r_arm_rig_class = arm_rig.arm_rig()

    r_arm_rig_return = r_arm_rig_class.arm_rig( direction='right', 
                                            offset_parent_jnt=chest_blend_offset_info, 
                                            finger_size = (0.4 * float(control_size) ),
                                            swch_ctrl_size = (3 * float(control_size) ),
                                            swch_ctrl_dist = (35 * float(control_size) ),
                                            fk_ctrl_size = (12 * float(control_size) ),
                                            ik_ctrl_size = (10 * float(control_size) ),
                                            pv_ctrl_size = (1 * float(control_size) ), 
                                            elbow_dist_mult = (float(elbow_pv_dist) * float(control_size) ), 
                                            to_chest_ctrl=to_chest_ctrl,
                                            global_ctrl=global_ctrl_info[1],
                                            global_misc_grp=character_misc_grp,
                                            twstJnts_checkbox=twstJnts_checkbox )
    '''
    
    #________________________________________________________________________#
    # grp misc and global ctrl grp in final grp
    final_grp = mc.group(em=1, n='character_all_grp')
    mc.parent( global_ctrl_info[0], character_misc_grp, final_grp )

    
    #______________________________________________________________________________#
    # select all nurbs curves to tag as controls
    allNurbsCtrls = mc.listRelatives(final_grp, ad=True, type='nurbsCurve')
    allNurbsCtrls_parent = mc.listRelatives(allNurbsCtrls, p=True)
    mc.select(allNurbsCtrls_parent)
    
    # # remove arm twist splines from tag selection # FIX, l_arm_rig_return, not correct
    # if l_arm_rig_return:
    #     mc.select(l_arm_rig_return, d=True)
    # if r_arm_rig_return:
    #     mc.select(r_arm_rig_return, d=True)
    
    mc.select(tail_rig_info, d=True) # remove tail spline curve from controller selection

    # tag most all ctrls as Controller (for parallel evaluation)
    mc.TagAsController()

    #__________________________________#
    #deselect all, back to main screen
    mc.select(cl=True)
    mc.setFocus("MayaWindow")
    
    

