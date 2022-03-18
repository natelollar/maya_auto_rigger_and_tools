import maya.cmds as mc

try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass

from ..ar_functions import find_jnts
from ..ar_functions import sel_joints
from ..ar_tools import fk_ctrl


# fk jaw ctrl
class face_rig():

    def jaw_ctrl(self, parent_to, ctrl_size):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # create jaw fk ctrl
        jaw_ctrl_var = fk_ctrl.fk_ctrl()
        # parent jaw control under head ctrl
        jaw_ctrl_info = jaw_ctrl_var.single_fk_ctrl(   jnt=jaw_jnt, 
                                                        parent_to=parent_to, 
                                                        normal=[0,1,0], 
                                                        size = ctrl_size,
                                                        colorR=0, 
                                                        colorG=1, 
                                                        colorB=0)
        # return joint group and then control
        return jaw_ctrl_info[0], jaw_ctrl_info[1]


    def tongue_ctrls(self, ctrl_size, parent_to):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # find jaw joint
        tongue_jnt_temp = find_jnts.find_jnts()
        tongue_jnt = tongue_jnt_temp.most_descendants_jnt(jaw_jnt)

        # find tongue joint chain
        tongue_list_var = sel_joints.sel_joints(firstJoint=tongue_jnt)

        tongue_list_info = tongue_list_var.sel_jnt_chain()

        #create controls and groups for tongue
        tongue_grp_list = []
        tongue_ctrl_list = []
        for jnt in tongue_list_info:
            jnt_var = fk_ctrl.fk_ctrl()
            jnt_var_info = jnt_var.single_fk_curve_ctrl(jnt=jnt, 
                                                        parent_to='', 
                                                        version='box', 
                                                        size=ctrl_size, 
                                                        colorR=1, 
                                                        colorG=0, 
                                                        colorB=0)
            # make grp and ctrl list for tongue ctrls
            tongue_grp_list.append(jnt_var_info[0])
            tongue_ctrl_list.append(jnt_var_info[1])
        # varaiable for top grp to parent
        tongue_top_grp = tongue_grp_list[0]

        #remove first and last of lists to correctly parent ctrls and grps together in for loop
        tongue_grp_list.pop(0)
        tongue_ctrl_list.pop(-1)

        #parent ctrls and grps together
        for i_grp, i_ctrl in zip(tongue_grp_list, tongue_ctrl_list):
            mc.parent(i_grp, i_ctrl)
        # parent top grp to head ctrl
        mc.parent(tongue_top_grp, parent_to)
        #return tongue top grp (not needed)
        return tongue_top_grp


    def bot_face_ctrls(self, ctrl_size, parent_to):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # find jaw joint
        tongue_jnt_temp = find_jnts.find_jnts()
        tongue_jnt = tongue_jnt_temp.most_descendants_jnt(jaw_jnt)

        jaw_jnt_descendants = mc.listConnections(jaw_jnt, type='joint', d=True, s=False)

        bot_face_jnts = []
        for i in jaw_jnt_descendants:
            if i != tongue_jnt:
                bot_face_jnts.append(i)
        
        for i in bot_face_jnts:
            bot_face_ctrl = fk_ctrl.fk_ctrl()
            bot_face_ctrl.single_fk_curve_ctrl(jnt=i, 
                                                parent_to=parent_to,
                                                size=ctrl_size,
                                                version='box',
                                                colorR=.5, 
                                                colorG=1, 
                                                colorB=0)
        

    #________________________________________________#
    #________________________________________________#
    #top face controls w/ mid ctrls (parented to head)
    def top_face_ctrls(self, ctrl_size, parent_to_head='', parent_to_jaw='', mid_ctrls=0):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # get immediate descendants of head joint
        head_jnt_descendants = mc.listConnections(head_jnt, type='joint', d=True, s=False)
        # list head joint descendants without jaw joint
        top_head_jnts = []
        for i in head_jnt_descendants:
            if i != jaw_jnt:
                top_head_jnts.append(i)
        #list head joints without ear joints
        top_face_jnts = []
        for i in top_head_jnts:
            i_descendats = mc.listRelatives(i, type='joint', ad=True)
            try:
                if len(i_descendats) >= 1:
                    pass
            except:
                top_face_jnts.append(i)
        
        #get position of face jnts
        y_pos_list = []
        for i in top_face_jnts:
            pos = mc.xform(i, q=True , ws=True, t=True, a=True)
            # y pos to find lowest ws value 
            y_pos = pos[1]
            y_pos_list.append(y_pos)
        
        # combine y_pos and top face jnt lst
        zip_y_pos = zip(y_pos_list, top_face_jnts)
        #sort lists from smallest to greatest Y pos
        sort_zip_y_pos = sorted(zip_y_pos)
        # create sorted list with just face jnts
        sorted_top_face_jnts = [somVar for i, somVar in sort_zip_y_pos]
        # get just jnts with lowest y positions
        mid_jnt_list = sorted_top_face_jnts[:mid_ctrls]
        # new face jnt list without mid face jnts
        new_top_face_jnts = sorted_top_face_jnts[mid_ctrls:]

        
        # create nurbs ctrl for each top face jnt
        for i in new_top_face_jnts:
            top_face_ctrl = fk_ctrl.fk_ctrl()
            top_face_ctrl.single_fk_curve_ctrl(jnt=i, 
                                                parent_to=parent_to_head, 
                                                version='box',
                                                size=ctrl_size,
                                                colorR=1, 
                                                colorG=.5, 
                                                colorB=0)

        # mid face grp list
        mid_face_ctrl_grps = []
        # create ctrl for the mid face jnts
        for i in mid_jnt_list:
            mid_face_ctrl = fk_ctrl.fk_ctrl()
            mid_face_ctrl_info = mid_face_ctrl.single_fk_curve_ctrl(    jnt=i, 
                                                                        parent_to=parent_to_head, 
                                                                        version='box',
                                                                        size=ctrl_size,
                                                                        colorR=0, 
                                                                        colorG=.5, 
                                                                        colorB=1)
            # parent constrain mid face ctrl grp between head and jaw
            mc.parentConstraint(parent_to_head, parent_to_jaw, mid_face_ctrl_info[0], mo=1)
            mc.scaleConstraint(parent_to_head, parent_to_jaw, mid_face_ctrl_info[0], mo=1)
            # append grps to list
            mid_face_ctrl_grps.append(mid_face_ctrl_info[0])

        return top_face_jnts, mid_jnt_list, mid_face_ctrl_grps
        
                
    #________________________________________________#
    #________________________________________________#
    def ear_ctrls(self, ctrl_size, parent_to):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # get immediate descendants of head joint
        head_jnt_descendants = mc.listConnections(head_jnt, type='joint', d=True, s=False)
        # list head joint descendants without jaw joint
        top_head_jnts = []
        for i in head_jnt_descendants:
            if i != jaw_jnt:
                top_head_jnts.append(i)
        # list head joints without face joints
        ear_jnts = []
        for i in top_head_jnts:
            i_descendats = mc.listRelatives(i, type='joint', ad=True)
            try:
                if len(i_descendats) >= 1:
                    ear_jnts.append(i)
            except:
                pass

        # if ear jnts do exist rig them (top face jnts w/ child/s)
        try:
            # chain for first r ear (should just put For Loop incase more fk chains on head)
            r_ear_list_var = sel_joints.sel_joints(firstJoint=ear_jnts[0])

            r_ear_list_info = r_ear_list_var.sel_jnt_chain()

            # chain for first l ear
            l_ear_list_var = sel_joints.sel_joints(firstJoint=ear_jnts[1])

            l_ear_list_info = l_ear_list_var.sel_jnt_chain()

            #create controls and groups for R EAR ___________________________
            r_ear_grp_list = []
            r_ear_ctrl_list = []
            for jnt in r_ear_list_info:
                jnt_var = fk_ctrl.fk_ctrl()
                jnt_var_info = jnt_var.single_fk_curve_ctrl(jnt=jnt, 
                                                            parent_to='', 
                                                            version='box', 
                                                            size=ctrl_size, 
                                                            colorR=0, 
                                                            colorG=0.5, 
                                                            colorB=1)
                r_ear_grp_list.append(jnt_var_info[0])
                r_ear_ctrl_list.append(jnt_var_info[1])
            # varaiable for top grp before removed
            r_ear_top_grp = r_ear_grp_list[0]

            #remove first and last of lists to correctly parent ctrls and grps together in for loop
            r_ear_grp_list.pop(0)
            r_ear_ctrl_list.pop(-1)

            #parent ctrls and grps together
            for i_grp, i_ctrl in zip(r_ear_grp_list, r_ear_ctrl_list):
                mc.parent(i_grp, i_ctrl)
            # parent top grp to head ctrl
            mc.parent(r_ear_top_grp, parent_to)

            #create controls and groups for L EAR ___________________________
            l_ear_grp_list = []
            l_ear_ctrl_list = []
            for jnt in l_ear_list_info:
                jnt_var = fk_ctrl.fk_ctrl()
                jnt_var_info = jnt_var.single_fk_curve_ctrl(jnt=jnt, 
                                                            parent_to='', 
                                                            version='box', 
                                                            size=ctrl_size, 
                                                            colorR=0, 
                                                            colorG=0.5, 
                                                            colorB=1)
                l_ear_grp_list.append(jnt_var_info[0])
                l_ear_ctrl_list.append(jnt_var_info[1])
            # varaiable for top grp before removed
            l_ear_top_grp = l_ear_grp_list[0]

            #remove first and last of lists to correctly parent ctrls and grps together in for loop
            l_ear_grp_list.pop(0)
            l_ear_ctrl_list.pop(-1)

            #parent ctrls and grps together
            for i_grp, i_ctrl in zip(l_ear_grp_list, l_ear_ctrl_list):
                mc.parent(i_grp, i_ctrl)
            # parent top grp to head ctrl
            mc.parent(l_ear_top_grp, parent_to)

            return r_ear_top_grp, l_ear_top_grp
        except:
            pass
