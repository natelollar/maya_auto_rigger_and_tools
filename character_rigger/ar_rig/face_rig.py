import maya.cmds as mc

from character_rigger.ar_functions import find_jnts
from character_rigger.ar_tools import fk_ctrl

# fk jaw ctrl
class face_rig():

    def jaw_ctrl(self, parent_to):
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
                                                        colorR=0, 
                                                        colorG=1, 
                                                        colorB=0)
        # return joint group and then control
        return jaw_ctrl_info[0], jaw_ctrl_info[1]

    def tongue_ctrls(self, parent_to):
        # find head joint
        head_jnt_temp = find_jnts.find_jnts()
        head_jnt = head_jnt_temp.find_head_jnt()
        # find jaw joint
        jaw_jnt_temp = find_jnts.find_jnts()
        jaw_jnt = jaw_jnt_temp.most_children_jnt(head_jnt)
        # find jaw joint
        tongue_jnt_temp = find_jnts.find_jnts()
        tongue_jnt = tongue_jnt_temp.most_descendants_jnt(jaw_jnt)

        mc.select(tongue_jnt)
        return tongue_jnt


    def bot_face_ctrls(self, parent_to):
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
            bot_face_ctrl.single_fk_sphere_ctrl(jnt=i, 
                                                parent_to=parent_to,
                                                size=1,
                                                colorR=0, 
                                                colorG=1, 
                                                colorB=0)
        


    def mid_face_ctrls(self, parent_to):
        pass


    def top_face_ctrls(self, parent_to):
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
        #list head joints without ear joitns
        top_face_jnts = []
        for i in top_head_jnts:
            i_descendats = mc.listRelatives(i, type='joint', ad=True)
            try:
                if len(i_descendats) >= 1:
                    pass
            except:
                top_face_jnts.append(i)
        
        for i in top_face_jnts:
            top_face_ctrl = fk_ctrl.fk_ctrl()
            top_face_ctrl.single_fk_sphere_ctrl(jnt=i, 
                                                parent_to=parent_to, 
                                                size=1,
                                                colorR=1, 
                                                colorG=0, 
                                                colorB=1)


    def ear_ctrls(self, parent_to):
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
        # return only ear joints
        mc.select(ear_jnts)
        return ear_jnts
