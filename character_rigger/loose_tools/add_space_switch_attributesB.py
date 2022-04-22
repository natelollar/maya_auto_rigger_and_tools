#______________________#
#multi parent constraint
import maya.cmds as mc

mySel = mc.ls(sl=1)

# last object is constrained
mc.parentConstraint(mySel[0], mySel[1], mySel[2], mo=True)
mc.scaleConstraint(mySel[0], mySel[1], mySel[2], mo=True)

#______________________#
# unneeded divider attribute, for organization/ look
import maya.cmds as mc

mySel = mc.ls(sl=1)

mc.addAttr(mySel, ln='Space', nn='Space', at='enum', enumName = 'Attr')

mc.setAttr(mySel[0] + '.Space', e=1, channelBox=1)

#______________________#
#create space switch enum attributes
import maya.cmds as mc

mySel = mc.ls(sl=1)


mc.addAttr(mySel, ln='Space_Switch', nn='Space_Switch', at='enum', k=1, enumName = 'Global_Ctrl:Foot_Ctrl')


#________________________#
import maya.cmds as mc

mySel = mc.ls(sl=1)

attr_obj = mySel[0]

parent_const = mySel[1]

scale_const = mySel[2]


control_1_name = 'character_global_ctrl'


control_2_name = 'right_ikFoot_ctrl'


space_swtch_attr = attr_obj + '.Space_Switch'
#attr_obj + '.Space_Switch', 0  #Global_Ctrl
#attr_obj + '.Space_Switch', 1  #Foot_Ctrl

prnt_cnst_attrA = parent_const + '.' + control_1_name + 'W0'  #Parent Constrain First Value
prnt_cnst_attrB = parent_const + '.' + control_2_name + 'W1'  #Parent Constrain Second Value

scl_cnst_attrA = scale_const + '.' + control_1_name + 'W0'  #Scale Constrain First Value
scl_cnst_attrB = scale_const + '.' + control_2_name + 'W1'  #Scale Constrain Second Value


# set attributes first
mc.setAttr( space_swtch_attr, 0 ) #space switch set to global ctrl
mc.setAttr( prnt_cnst_attrA,  1 ) #global ctrl to on
mc.setAttr( prnt_cnst_attrB,  0 ) #waist ctrl to off
mc.setAttr( scl_cnst_attrA,  1 ) #global ctrl to on
mc.setAttr( scl_cnst_attrB,  0 ) #waist ctrl to off

#set key on attributes
mc.setDrivenKeyframe( prnt_cnst_attrA, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( prnt_cnst_attrB, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( scl_cnst_attrA, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( scl_cnst_attrB, currentDriver = space_swtch_attr )

# flip attributes
mc.setAttr( space_swtch_attr, 1 ) #space switch set to global ctrl
mc.setAttr( prnt_cnst_attrA,  0 ) #global ctrl to off
mc.setAttr( prnt_cnst_attrB,  1 ) #waist ctrl to on
mc.setAttr( scl_cnst_attrA,  0 ) #global ctrl to off
mc.setAttr( scl_cnst_attrB,  1 ) #waist ctrl to on

#set key on attributes
mc.setDrivenKeyframe( prnt_cnst_attrA, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( prnt_cnst_attrB, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( scl_cnst_attrA, currentDriver = space_swtch_attr )
mc.setDrivenKeyframe( scl_cnst_attrB, currentDriver = space_swtch_attr )







            

