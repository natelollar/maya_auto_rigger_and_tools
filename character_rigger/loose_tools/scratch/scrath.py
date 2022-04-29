import maya.cmds as mc
direction = 'l'

# make nodes for stretchy limb
leg_dist_ratio = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_leg_dist_ratio' )
# set mulDiv node to Divide
mc.setAttr(leg_dist_ratio + '.operation', 2)
# global scale offset multDiv node
globalScale_off = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_leg_globalScale_off' )
# operation to divide
mc.setAttr(globalScale_off + '.operation', 2)
# create mult/div nodes for ratio * length
ratio_knee_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_knee_mult' )
ratio_ankle_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_ankle_mult' )
ratio_foot_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_ratio_foot_mult' )
#create condition nodes for if greater than length, to prevent negative stretching
knee_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_knee_len_con' )
ankle_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_ankle_len_con' )
foot_len_con = mc.shadingNode('condition', asUtility=True, n=direction + '_ankle_foot_con' )
#set operation to 'greater than'
if direction == 'l':
    mc.setAttr(knee_len_con + '.operation', 2)
    mc.setAttr(ankle_len_con + '.operation', 2)
    mc.setAttr(foot_len_con + '.operation', 2)
#set operation to 'less than'
elif direction == 'r':
    mc.setAttr(knee_len_con + '.operation', 4)
    mc.setAttr(ankle_len_con + '.operation', 4)
    mc.setAttr(foot_len_con + '.operation', 4)

# connect leg distance to global scale offset
mc.connectAttr( (ik_jnt_ruler + '.distance'), (globalScale_off + '.input1X'), f=True )
# connect global ctrl scale X to global scale offset
mc.connectAttr( (global_ctrl + '.scaleX'), (globalScale_off + '.input2X'), f=True )

# connect ruler distance over total distance of joints
if direction == 'l':
    mc.connectAttr( (globalScale_off + '.outputX'), (leg_dist_ratio + '.input1X'), f=True )
elif direction == 'r':
    # (right) invert to negative translate X (since x is up the chain instead of down the chain)
    invert_value = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_leg_invert_value' )
    mc.setAttr( (invert_value + '.input2X'), -1 )
    mc.connectAttr( (globalScale_off + '.outputX'), (invert_value + '.input1X'), f=True )
    mc.connectAttr( (invert_value + '.outputX'), (leg_dist_ratio + '.input1X'), f=True )

#__________#
# Stretch alteration Expression

# soft ik, a little less than total length to keep some bend in knee joint
#mc.expression ( s = leg_dist_ratio + '.input2X = ' + str(to_knee_len + to_ankle_len + to_foot_len) + ' * ' + ik_ctrl_list[0] + '.stretch_AT_length' )

# create nodes instead of expression (which causes visual glitch at startup)
total_jnt_len = mc.shadingNode('multiplyDivide', asUtility=True, n=direction + '_leg_jnt_len_sum' )
#set mult 1x to sum of all leg jnt length
mc.setAttr( (total_jnt_len + '.input1X'), (to_knee_len + to_ankle_len + to_foot_len) )

# divide with leg_dist_ratio (global scale mult offset)
mc.connectAttr( (total_jnt_len + '.outputX'), (leg_dist_ratio + '.input2X'), f=True )

# multiply stretch at with jnt length sum
mc.connectAttr( (ik_ctrl_list[0] + '.stretch_AT_length'), (total_jnt_len + '.input2X'), f=True )

#_____________#


# connect length ratio to apply to x length of knee and ankle (fraction * distance)
mc.connectAttr( (leg_dist_ratio + '.outputX'), (ratio_knee_mult + '.input2X'), f=True )
mc.connectAttr( (leg_dist_ratio + '.outputX'), (ratio_ankle_mult + '.input2X'), f=True )
mc.connectAttr( (leg_dist_ratio + '.outputX'), (ratio_foot_mult + '.input2X'), f=True )
# joint length to input 1X
mc.setAttr( (ratio_knee_mult + '.input1X'), to_knee_len )
mc.setAttr( (ratio_ankle_mult + '.input1X'), to_ankle_len )
mc.setAttr( (ratio_foot_mult + '.input1X'), to_foot_len )

# connect mult ratio nodes to condition node (if length greater, then stretch)
mc.connectAttr( (ratio_knee_mult + '.outputX'), (knee_len_con + '.colorIfTrueR'), f=True )
mc.connectAttr( (ratio_knee_mult + '.outputX'), (knee_len_con + '.firstTerm'), f=True )

mc.connectAttr( (ratio_ankle_mult + '.outputX'), (ankle_len_con + '.colorIfTrueR'), f=True )
mc.connectAttr( (ratio_ankle_mult + '.outputX'), (ankle_len_con + '.firstTerm'), f=True )

mc.connectAttr( (ratio_foot_mult + '.outputX'), (foot_len_con + '.colorIfTrueR'), f=True )
mc.connectAttr( (ratio_foot_mult + '.outputX'), (foot_len_con + '.firstTerm'), f=True )

# add joint lengths to base value, if false
mc.setAttr( (knee_len_con + '.colorIfFalseR'), to_knee_len )
mc.setAttr( (knee_len_con + '.secondTerm'), to_knee_len )

mc.setAttr( (ankle_len_con + '.colorIfFalseR'), to_ankle_len )
mc.setAttr( (ankle_len_con + '.secondTerm'), to_ankle_len )

mc.setAttr( (foot_len_con + '.colorIfFalseR'), to_foot_len )
mc.setAttr( (foot_len_con + '.secondTerm'), to_foot_len )

#connect stretch lengths to joint translate x
mc.connectAttr( (knee_len_con + '.outColorR'), (ikJoint_list[1] + '.tx'), f=True )
mc.connectAttr( (ankle_len_con + '.outColorR'), (ikJoint_list[2] + '.tx'), f=True )
mc.connectAttr( (foot_len_con + '.outColorR'), (ikJoint_list[3] + '.tx'), f=True )

#and to translate x of driver joints
mc.connectAttr( (knee_len_con + '.outColorR'), (ikDriverJoint_list[1] + '.tx'), f=True )
mc.connectAttr( (ankle_len_con + '.outColorR'), (ikDriverJoint_list[2] + '.tx'), f=True )
mc.connectAttr( (foot_len_con + '.outColorR'), (ikDriverJoint_list[3] + '.tx'), f=True )
