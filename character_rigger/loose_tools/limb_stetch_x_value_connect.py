# setting up stretch limb/ tail
import maya.cmds as mc

mySel = mc.ls(sl=1)

length_ration = 'tail_length_ratio_div'

for i in mySel:
    # create node to multuply length ratio with joint x value
    x_val_mult = mc.shadingNode('multiplyDivide', asUtility=True, n=i + '_x_val_mult' )
    # get joint translate x
    joint_translate_x = mc.getAttr(i + '.translateX')
    # set mult node 2X to joint length (x val)
    mc.setAttr( x_val_mult + '.input2X', joint_translate_x )
    # multiply joint length by ratio
    mc.connectAttr( length_ration + '.outputX',  x_val_mult + '.input1X')
    # connect value to joint
    mc.connectAttr( x_val_mult + '.outputX',  i + '.translateX')
    
    
    