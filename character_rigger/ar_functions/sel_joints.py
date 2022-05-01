import maya.cmds as mc

class sel_joints():

    def __init__(self, firstJoint='', lastJoint=''):
        self.firstJoint = firstJoint
        self.lastJoint = lastJoint

    # reverse select joint chain (from last joint)
    def rev_sel_jnt_chain(self):
        chain_list = []
        jointSel = [self.lastJoint]
        chain_list.append(jointSel)
        for i in range(1,25):
            if jointSel != self.firstJoint:
                if jointSel != None:
                    jointSel = mc.listRelatives( jointSel, type = 'joint', ap = True )
                    chain_list.append(jointSel)
        
        # delete "None" value from last append before repeating if statement
        chain_list.pop(-1)
        # reverse list as it was selected in reverse
        chain_list.reverse()
        
        #get rid of list: list structure
        chain_list_new = []
        for i in chain_list:
            i = i[0]
            chain_list_new.append(i)

        # return clean list
        return chain_list_new

    #fixed from above
    def rev_sel_jnt_chainA(self):
        chain_list = []
        firstJnt = [self.firstJoint]
        jointSel = [self.lastJoint]
        chain_list.append(jointSel)
        for i in range(1,25):
            if jointSel != firstJnt:
                if jointSel != None:
                    jointSel = mc.listRelatives( jointSel, type = 'joint', ap = True )
                    chain_list.append(jointSel)
        
        # delete "None" value from last append before repeating if statement
        if chain_list[-1] == None:
            chain_list.pop(-1)
        # reverse list as it was selected in reverse
        chain_list.reverse()
        
        #get rid of list: list structure
        chain_list_new = []
        for i in chain_list:
            i = i[0]
            chain_list_new.append(i)

        # return clean list
        return chain_list_new



    # select basic chain with no fork (finger, tongue, tentacle)
    def sel_jnt_chain(self):
        jnt_desc = mc.listRelatives(self.firstJoint, type='joint', ad=True)

        jnt_desc.append(self.firstJoint)

        jnt_desc.reverse()

        mc.select(jnt_desc)
        return jnt_desc





