# instructions
# select constraint objects first
# second to last select parent constrained object
# lastly select object to have custom space switch attribute
#______________________# auto create multi space switch
#______________________# apply constraints for space switch
import maya.cmds as cmds


def add_space_switch_multi_rot():

    mySel = cmds.ls(sl=True)

    # first objects selected are constraints
    constraining_objs = mySel[:-2]
    # constrained object is second to last selected
    constrained_obj = mySel[-2]
    # final attribute object (to control space switch from)
    attribute_object = mySel[-1]

    #______________________# create parent constraint between objects.  skip translation.  basically an orient constraint.
    #w=0, so don't have to set weight in for loop (to avoid flipping on creation)
    rot_prnt_const_nm = constrained_obj + "_rot" + "_parentConstraint1"
    rot_prnt_const = cmds.parentConstraint( constraining_objs, constrained_obj, n=rot_prnt_const_nm, st=("x", "y", "z"), mo=True, w=0 ) 

    #______________________# add unneeded seperation attribute
    sep_attr_nm = "______"
    sep_enum_nm = "______"
    cmds.addAttr(constrained_obj, ln=sep_attr_nm, nn=sep_attr_nm, at='enum', enumName = sep_enum_nm)
    cmds.setAttr(constrained_obj + '.' + sep_attr_nm, e=1, channelBox=1)

    cmds.addAttr(attribute_object, ln=sep_attr_nm, nn=sep_attr_nm, at='enum', enumName = sep_enum_nm)
    cmds.setAttr(attribute_object + '.' + sep_attr_nm, e=1, channelBox=1)


    #______________________# add Space Switch attribute
    # get list of constraint object names
    const_name_lst = ''

    for object in constraining_objs:
        const_name_lst += object + ':'

    # add space switch attr to parented object
    cmds.addAttr( constrained_obj, 
                ln='rot_Space_Switch', 
                nn='rot_Space_Switch', 
                at='enum', 
                k=1, 
                enumName = const_name_lst ) # add first selected constraint

    # add space switch attr to ctrl object
    cmds.addAttr( attribute_object, 
                ln='rot_Space_Switch', 
                nn='rot_Space_Switch', 
                at='enum', 
                k=1, 
                enumName = const_name_lst ) # add first selected constraint


    #______________________# set driven key constraints to Space Switch Attribute

    space_swtch_attr = constrained_obj + '.rot_Space_Switch'



    # list constraint weight names
    prnt_cnst_attr_lst = []
    current_ind = 0
    for objects in constraining_objs:
        prnt_cnst_attr = rot_prnt_const[0] + '.' + objects + 'W' + str(current_ind)

        prnt_cnst_attr_lst.append(prnt_cnst_attr)

        current_ind += 1


    # parent constraint set driven keys
    current_ind = 0
    for i in prnt_cnst_attr_lst:
        # set current attribute to on
        cmds.setAttr( space_swtch_attr, current_ind )
        cmds.setAttr( i,  1 )

        # set other attribute to off
        for x in prnt_cnst_attr_lst:
            if x != prnt_cnst_attr_lst[current_ind]:
                cmds.setAttr( x,  0 )
                cmds.setDrivenKeyframe( x, currentDriver = space_swtch_attr )

        # set key
        cmds.setDrivenKeyframe( i, currentDriver = space_swtch_attr )

        # go to next parent weight index in loop
        current_ind += 1



    #______________________#

    # connect ctrl object to parented object attributes
    cmds.connectAttr(attribute_object + '.rot_Space_Switch', constrained_obj + '.rot_Space_Switch', force=True)


