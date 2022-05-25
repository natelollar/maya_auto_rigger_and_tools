#______________________# auto create multi space switch
import maya.cmds as mc


#______________________# apply constraints for space switch
mySel = mc.ls(sl=True)

# first objects selected are constraints
constraints = mySel[:-1]
# constrained object is last selected
constrained_object = mySel[-1]

for i in mySel:
    if i != mySel[-1]:
        prnt_const = mc.parentConstraint(i, mySel[-1], mo=True)
        scl_const = mc.scaleConstraint(i, mySel[-1], mo=True)



#______________________# add unneeded seperation attribute
mc.addAttr(mySel[-1], ln='__________', nn='__________', at='enum', enumName = '__________')

mc.setAttr(mySel[-1] + '.__________', e=1, channelBox=1)



#______________________# add Space Switch attribute
# get list of constraint object names
const_name_lst = ''

for i in mySel[:-1]:
    const_name_lst += i + ':'



# add space switch attr
mc.addAttr( mySel[-1], 
            ln='Space_Switch', 
            nn='Space_Switch', 
            at='enum', 
            k=1, 
            enumName = const_name_lst ) # add first selected constraint



#______________________# set driven key constraints to Space Switch Attribute

space_swtch_attr = mySel[-1] + '.Space_Switch'



# list constraint weight names
prnt_cnst_attr_lst = []
scl_cnst_attr_lst = []
current_ind = 0
for i in mySel[:-1]:
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