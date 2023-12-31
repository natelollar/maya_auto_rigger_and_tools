import maya.cmds as cmds

def delete_space_switch():
    parentConstraint_lst0 = cmds.ls(type='parentConstraint')
    parentConstraint_lst1 = []
    for p_cnst in parentConstraint_lst0:
        if '_ps' in p_cnst:
            parentConstraint_lst1.append(p_cnst)
    print (parentConstraint_lst1)
    
    scaleConstraint_lst0 = cmds.ls(type='scaleConstraint')
    scaleConstraint_lst1 = []
    for p_cnst in scaleConstraint_lst0:
        if '_ps' in p_cnst:
            scaleConstraint_lst1.append(p_cnst)
    print (scaleConstraint_lst1)

    transform_lst0 = cmds.ls(type='transform')
    transform_lst1 = []
    for trns in transform_lst0:
        if '_ps' in trns\
        and '_parentConstraint' not in trns\
        and '_scaleConstraint' not in trns:
                transform_lst1.append(trns)
    print (transform_lst1)

    #delete elements
    cmds.delete(parentConstraint_lst1)
    cmds.delete(scaleConstraint_lst1)

    #for group in transform_lst1:
    for group in transform_lst1:
        cmds.deleteAttr(group + ".Space_Switch")
        cmds.deleteAttr(group + ".__________")
     
    #delete space switch attribute on control
    ctrl_lst0 = []
    for trns in transform_lst1: #pickwalk down 2 from _ps group
        cmds.select(trns)
        cmds.pickWalk(direction='down')
        cmds.pickWalk(direction='down')
        ctrl = cmds.ls(sl=True)
        print(ctrl)
        try:
            cmds.deleteAttr(ctrl[0] + ".Space_Switch")
            cmds.deleteAttr(ctrl[0] + ".__________")
        except:
            pass
