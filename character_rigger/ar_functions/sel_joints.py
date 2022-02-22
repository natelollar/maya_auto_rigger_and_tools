import maya.cmds as mc

class sel_joints():

    def __init__(self, firstJoint, lastJoint):
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


    def sel_jnt_chain(self):
        pass






