import maya.cmds as mc

class sel_joints():

    def __init__(self, firstJoint, lastJoint):
        self.firstJoint = firstJoint
        self.lastJoint = lastJoint

    # reverse select joint chain (from last joint)
    def rev_sel_jnt_chain(self):
        chain_list = []
        jointSel = self.lastJoint
        chain_list.append(jointSel[0])
        for i in range(1,25):
            if jointSel != self.firstJoint:
                jointSel = mc.listRelatives( jointSel, type = 'joint', ap = True )
                chain_list.append(jointSel[0])

        chain_list.reverse()
        return chain_list






