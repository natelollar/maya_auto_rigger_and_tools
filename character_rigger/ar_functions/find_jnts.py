import maya.cmds as mc

# find joints with boudning box object as starting point
class find_jnts():
    # find base root to start rigging and find all other joints from
    # finds joint in scene with most children joints
    def find_spine_root(self):
        #get all joints in scene
        scene_jnts = mc.ls(type='joint')
        #create list with each joints child joint mount
        jnt_relatives_amount = []
        for i in scene_jnts:
            jnt_relatives = mc.listRelatives(i, ad=True, type='joint')
            # joint with no child returns 'NoneType', cannot get len()
            try:
                jnt_relatives_amount.append(len(jnt_relatives))
            except:
                jnt_relatives_amount.append(0)
        # find joint index with most child joints
        max_child_amount_index = jnt_relatives_amount.index(max(jnt_relatives_amount))
        # get joints name with most child joints
        max_child_amount_jnt = scene_jnts[max_child_amount_index]
        # return and select joint with most child joints
        mc.select(max_child_amount_jnt)
        return max_child_amount_jnt


    #first spine joint with more than 1 child
    def find_chest_jnt(self):
        # select spine root
        myJoint = self.find_spine_root()
        mc.select(cl=True)
        # list immediate joint children
        jointSel = mc.listConnections(myJoint, d=True, type='joint')
        # make list of child world space positions
        y_pos_list = []
        for i in jointSel:
            pos = mc.xform(i, q=True , ws=True, t=True)
            y_pos = pos[1]
            y_pos_list.append(y_pos)
        # get index of joint with highest y value position (more Left)
        high_y_val_ind = y_pos_list.index(max(y_pos_list))
        # get joint name with highest y value
        high_y_val_jnt = [jointSel[high_y_val_ind]]
        # next spine joint is highest in y
        jointSelA = mc.listConnections(high_y_val_jnt, s=False, type='joint')
        # stop at first joint with more than one child
        # 25 in case of many spine joints
        for i in range(1,25):
            if len(jointSelA) == 1:
                jointSelA = mc.listConnections( jointSelA, s=False, type = 'joint' )
            else:
                jointSelB = mc.listConnections( jointSelA, d=False, type = 'joint')
        #select chest joint
        mc.select(jointSelB)
        chest_jnt = mc.ls(sl=True)
        return chest_jnt


    # get left or right most child joint (immediate child)
    def l_r_hip_jnt(self, direction):
        # select spine root
        myJoint = self.find_spine_root()
        # spine root children
        jointSel = mc.listConnections(myJoint, d=True, type='joint')
        # get world positions
        x_pos_list = []
        for i in jointSel:
            pos = mc.xform(i, q=True , ws=True, t=True)
            x_pos = pos[0]
            x_pos_list.append(x_pos)

        # get index of joint with highest x value position (more Left)
        high_x_val_ind = x_pos_list.index(max(x_pos_list))
        # get joint name with highest x value
        high_x_val_jnt = [jointSel[high_x_val_ind]]
        
        # get index of joint with lowest x value position (more Left)
        low_x_val_ind = x_pos_list.index(min(x_pos_list))
        # get joint name with lowest x value
        low_x_val_jnt = [jointSel[low_x_val_ind]]

        # if argument left or right str() choose appropriate joint
        if direction == 'left':
            mc.select(high_x_val_jnt)
            return high_x_val_jnt
        elif direction == 'right':
            mc.select(low_x_val_jnt)
            return low_x_val_jnt


    def l_r_clavicle_jnt(self, direction):
        chest_jnt = self.find_chest_jnt()
        # with chest found, now select right or left clavicle

        # get immediate children of chest
        jointSelC_temp = mc.listConnections(chest_jnt, type='joint', s=False )
        mc.select(jointSelC_temp)
        jointSelC = mc.ls(sl=True)

        # get world positions of joints
        x_pos_list = []
        for i in jointSelC:
            pos = mc.xform(i, q=True , ws=True, t=True)
            x_pos = pos[0]
            x_pos_list.append(x_pos)

        # get index of joint with highest x value position (more Left)
        high_x_val_ind = x_pos_list.index(max(x_pos_list))
        # get joint name with highest x value
        high_x_val_jnt = [jointSelC[high_x_val_ind]]

        # get index of joint with lowest x value position (more Left)
        low_x_val_ind = x_pos_list.index(min(x_pos_list))
        # get joint name with lowest x value
        low_x_val_jnt = [jointSelC[low_x_val_ind]]
    
        # select left or right most chest children
        if direction == 'left':
            mc.select(high_x_val_jnt)
            return high_x_val_jnt
        elif direction == 'right':
            mc.select(low_x_val_jnt)
            return low_x_val_jnt

    # find head/ top of neck joint
    def find_head_jnt(self):
        chest_jnt = self.find_chest_jnt()
        
        # get immediate children of chest
        chest_children_jnts = mc.listConnections(chest_jnt, type='joint', s=False )
        mc.select(chest_children_jnts)
        chest_children_jnts_sel = mc.ls(sl=True)
        print(chest_children_jnts_sel)
        
        # get l and r clavicle
        l_clav = self.l_r_clavicle_jnt('left')
        r_clav = self.l_r_clavicle_jnt('right')
        # if not l or r clavicle, must be neck
        for child_jnt in chest_children_jnts_sel:
            if child_jnt != l_clav[0] and child_jnt != r_clav[0]:
                neck_base_jnt = child_jnt
                
        # neck base # of children
        neck_jnt_children = mc.listConnections(neck_base_jnt, s=False, type='joint' )
        mc.select (neck_jnt_children)
        try:
            # joint with more than 1 child would be head/ top neck
            if len(neck_jnt_children) >= 2:
                # head = neck base joint
                mc.select(neck_base_jnt)
                return neck_base_jnt
            else:
                # if only 1 joint go up until more than 1 joint
                for i in range(1,25):
                    if len(neck_jnt_children) == 1:
                        neck_jnt_children = mc.listConnections( neck_jnt_children, s=False, type = 'joint' )
                    else:
                        head_jnt = mc.listConnections( neck_jnt_children, d=False, type = 'joint')
                        mc.select(head_jnt)
                        head_jnt_sel = mc.ls(sl=True)
                        return head_jnt_sel[0]
        except:
            # if len() is 0 children and returns 'NoneType' 
            # head = neck top joint
            mc.select(neck_base_jnt)
            return neck_base_jnt

    
    # find next fork in the joint road
    def find_next_fork(self, start_jnt):
        # get immediate child of start_jnt
        next_jnt = mc.listConnections( start_jnt, s=False, type='joint' )

        #get next joint until multiple children
        for i in range(1,25):
            if len(next_jnt) == 1:
                next_jnt = mc.listConnections( next_jnt, s=False, type = 'joint' )
            else:
                #go backward one step to fork in road
                next_fork = mc.listConnections( next_jnt, d=False, type = 'joint')
                mc.select(next_fork)
                return next_fork

    # out of all children joints, which one has most immediate children
    def most_children_jnt(self, start_jnt):
        # all children of start_jnt
        all_children = mc.listRelatives( start_jnt, ad=True, type='joint' )
        #create list with each joints number of children
        jnt_relatives_amount = []
        # find number of immediate children for all_children
        for i in all_children:
            jnt_relatives = mc.listConnections( i, s=False, type = 'joint' )
            # joint with no child returns 'NoneType', cannot get len()
            try:
                jnt_relatives_amount.append(len(jnt_relatives))
            except:
                jnt_relatives_amount.append(0)
        # find joint index with most child joints
        most_children_index = jnt_relatives_amount.index(max(jnt_relatives_amount))
        # get joints name with most child joints
        most_children_jnt = all_children[most_children_index]
        # return and select joint with most child joints
        mc.select(most_children_jnt)
        return most_children_jnt

    # out of all immediate children joints, which one has most total descendant
    def most_descendants_jnt(self, start_jnt):
        # all children of start_jnt
        all_children = mc.listRelatives( start_jnt, ad=True, type='joint' )
        #create list with each joints number of children
        jnt_relatives_amount = []
        # find number of immediate children for all_children
        for i in all_children:
            jnt_relatives = mc.listRelatives( i, ad=True, type = 'joint' )
            # joint with no child returns 'NoneType', cannot get len()
            try:
                jnt_relatives_amount.append(len(jnt_relatives))
            except:
                jnt_relatives_amount.append(0)
        # find joint index with most child joints
        most_children_index = jnt_relatives_amount.index(max(jnt_relatives_amount))
        # get joints name with most child joints
        most_children_jnt = all_children[most_children_index]
        # return and select joint with most child joints
        mc.select(most_children_jnt)
        return most_children_jnt

    def find_ankle_jnt(self, direction):
        clavicle_jnt = self.l_r_hip_jnt(direction)
        clavicle_jnt_rel = mc.listRelatives(clavicle_jnt, ad=True, type='joint')
        
        return clavicle_jnt_rel[-2]


    
    




