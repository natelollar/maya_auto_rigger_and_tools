
def multi_space_switch():

    # instructions
    # select constraint objects first
    # second to last select parent constrained object
    # lastly select object to have custom space switch attribute

    #______________________# auto create multi space switch
    import maya.cmds as mc

    #______________________# apply constraints for space switch
    mySel = mc.ls(sl=True)

    # first objects selected are constraints
    constraints = mySel[:-2]
    # constrained object is second to last selected
    constrained_object = mySel[-2]
    # final attribute object (to control space switch from)
    attribute_object = mySel[-1]

    current_ind = 0
    for i in mySel:
        if i != mySel[-2] and i != mySel[-1]:
            prnt_const = mc.parentConstraint(i, mySel[-2], mo=True)
            scl_const = mc.scaleConstraint(i, mySel[-2], mo=True)

            # set to zero to avoid constraining while flipping (caused by multiple on at once)
            # incase two weights on at once cause glitch, don't want to constrain third during glitch
            prnt_cnst_attr = prnt_const[0] + '.' + i + 'W' + str(current_ind)
            scl_cnst_attr = scl_const[0] + '.' + i + 'W' + str(current_ind)
            mc.setAttr( prnt_cnst_attr,  0 )
            mc.setAttr( scl_cnst_attr,  1 )

            current_ind += 1


    #______________________# add unneeded seperation attribute
    mc.addAttr(mySel[-2], ln='__________', nn='__________', at='enum', enumName = '__________')
    mc.setAttr(mySel[-2] + '.__________', e=1, channelBox=1)

    mc.addAttr(mySel[-1], ln='__________', nn='__________', at='enum', enumName = '__________')
    mc.setAttr(mySel[-1] + '.__________', e=1, channelBox=1)



    #______________________# add Space Switch attribute
    # get list of constraint object names
    const_name_lst = ''

    for i in mySel[:-2]:
        const_name_lst += i + ':'

    # add space switch attr to parented object
    mc.addAttr( mySel[-2], 
                ln='Space_Switch', 
                nn='Space_Switch', 
                at='enum', 
                k=1, 
                enumName = const_name_lst ) # add first selected constraint

    # add space switch attr to ctrl object
    mc.addAttr( mySel[-1], 
                ln='Space_Switch', 
                nn='Space_Switch', 
                at='enum', 
                k=1, 
                enumName = const_name_lst ) # add first selected constraint


    #______________________# set driven key constraints to Space Switch Attribute

    space_swtch_attr = mySel[-2] + '.Space_Switch'



    # list constraint weight names
    prnt_cnst_attr_lst = []
    scl_cnst_attr_lst = []
    current_ind = 0
    for i in mySel[:-2]:
        prnt_cnst_attr = prnt_const[0] + '.' + i + 'W' + str(current_ind)
        scl_cnst_attr = scl_const[0] + '.' + i + 'W' + str(current_ind)

        prnt_cnst_attr_lst.append(prnt_cnst_attr)
        scl_cnst_attr_lst.append(scl_cnst_attr)

        current_ind += 1


    # parent constraint set driven keys
    current_ind = 0
    for i in prnt_cnst_attr_lst:
        # set current attribute to on
        mc.setAttr( space_swtch_attr, current_ind )
        mc.setAttr( i,  1 )

        # set other attribute to off
        for x in prnt_cnst_attr_lst:
            if x != prnt_cnst_attr_lst[current_ind]:
                mc.setAttr( x,  0 )
                mc.setDrivenKeyframe( x, currentDriver = space_swtch_attr )

        # set key
        mc.setDrivenKeyframe( i, currentDriver = space_swtch_attr )

        # go to next parent weight index in loop
        current_ind += 1


    # parent constraint set driven keys
    current_ind = 0
    for i in scl_cnst_attr_lst:
        # set current attribute to on
        mc.setAttr( space_swtch_attr, current_ind )
        mc.setAttr( i,  1 )

        # set other attribute to off
        for x in scl_cnst_attr_lst:
            if x != scl_cnst_attr_lst[current_ind]:
                mc.setAttr( x,  0 )
                mc.setDrivenKeyframe( x, currentDriver = space_swtch_attr )

        # set key
        mc.setDrivenKeyframe( i, currentDriver = space_swtch_attr )
        
        # go to next parent weight index in loop
        current_ind += 1



    #______________________#

    # connect ctrl object to parented object attributes
    mc.connectAttr(mySel[-1] + '.Space_Switch', mySel[-2] + '.Space_Switch', force=True)
