import maya.cmds as mc


def add_ft_attr(direction = 'l'):
    mySel = mc.ls(sl=True)

    # add seperator
    mc.addAttr(mySel, ln='_________', nn='_________', at='enum', enumName = '_________')
    mc.setAttr(mySel[0] + '._________', e=1, channelBox=1)

    #______

    mc.addAttr(ln='heel_rot', nn='heel_rot', at='double', dv=0, min=0, max=50, keyable=True)
    mc.addAttr(ln='toe_rot', nn='toe_rot', at='double', dv=0, min=-35, max=0, keyable=True)
    mc.addAttr(ln='toeEnd_rot', nn='toeEnd_rot', at='double', dv=0, min=-50, max=0, keyable=True)
    mc.addAttr(ln='outerToe_rot', nn='outerToe_rot', at='double', dv=0, min=0, max=50, keyable=True)
    mc.addAttr(ln='innerToe_rot', nn='innerToe_rot', at='double', dv=0, min=-50, max=0, keyable=True)

    #________

    mc.connectAttr(mySel[0] + '.heel_rot', direction + '_ftCtrl_heel' + '.rotateZ')
    mc.connectAttr(mySel[0] + '.toe_rot', direction + '_ftCtrl_toe' + '.rotateZ')
    mc.connectAttr(mySel[0] + '.toeEnd_rot', direction + '_ftCtrl_toe_end' + '.rotateZ')
    mc.connectAttr(mySel[0] + '.outerToe_rot', direction + '_ftCtrl_outer_foot' + '.rotateX')
    mc.connectAttr(mySel[0] + '.innerToe_rot', direction + '_ftCtrl_inner_foot' + '.rotateX')

    #__________


def add_ft_roll():
    mySel = mc.ls(sl=True)

    # add seperator
    mc.addAttr(mySel, ln='________', nn='________', at='enum', enumName = '________')
    mc.setAttr(mySel[0] + '.________', e=1, channelBox=1)

    mc.addAttr(ln='foot_roll', nn='foot_roll', at='double', dv=0, min=-50, max=50, keyable=True)
    mc.addAttr(ln='foot_side_roll', nn='foot_side_roll', at='double', dv=0, min=-50, max=50, keyable=True)
    mc.addAttr(ln='heel_twist', nn='heel_twist', at='double', dv=0, min=-50, max=50, keyable=True)
    mc.addAttr(ln='foot_twist', nn='foot_twist', at='double', dv=0, min=-50, max=50, keyable=True)

def set_visibility():
    mySel = mc.ls(sl=True)

    for i in mySel:
        selShape = mc.listRelatives(i, s=True)
        for x in selShape:
            mc.setAttr(x + '.visibility', 0)


#add_ft_attr(direction = 'r')
#add_ft_roll()
set_visibility()



