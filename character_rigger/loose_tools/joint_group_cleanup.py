import maya.cmds as cmds

def select_constraints_in_group(group_name):
    all_descendants = cmds.listRelatives(group_name, allDescendents=True, type='transform')
    
    constraint_nodes = []

    constraint_types = ['aimConstraint', 'parentConstraint', 'pointConstraint', 'orientConstraint', 'scaleConstraint', 'ikEffector']
    
    for node in all_descendants:
        node_type = cmds.nodeType(node)
        if node_type in constraint_types:
            constraint_nodes.append(node)
    
    if constraint_nodes:
        cmds.select(constraint_nodes)

group_name = cmds.ls(sl=True)
select_constraints_in_group(group_name)