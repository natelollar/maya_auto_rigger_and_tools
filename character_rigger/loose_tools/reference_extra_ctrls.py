#________________________#
import maya.cmds as mc

mySel = mc.ls(sl=1)

ctrl_attr = 'sknJnt_spine1_Root_ctrl.Reference_Extra_Ctrls'

for i in mySel:
    shape = mc.listRelatives(i, s=True)
    for i in shape:
        mc.setAttr(ctrl_attr, 0) # set 'Reference_Extra_Ctrls' to 'Normal'
        mc.setAttr(i + '.overrideDisplayType', 0) # set shape display type to 'Normal'
        mc.setDrivenKeyframe( i + '.overrideDisplayType', currentDriver = ctrl_attr )#set driven key above two attr
        
        mc.setAttr(ctrl_attr, 1) # set 'Reference_Extra_Ctrls' to 'Reference'
        mc.setAttr(i + '.overrideDisplayType', 2) # set shape display type to 'Reference'
        mc.setDrivenKeyframe( i + '.overrideDisplayType', currentDriver = ctrl_attr )#set driven key above two attr

        










            

