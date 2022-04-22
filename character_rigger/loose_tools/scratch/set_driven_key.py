#______________________#
#create space switch enum attributes
import maya.cmds as mc

mySel = mc.ls(sl=1)

#mc.addAttr(mySel, ln='Space_Switch', nn='Space_Switch', at='enum', k=1, enumName = 'UpperArm:UpperArm_ForeArm')
#mc.addAttr(mySel, ln='Space_Switch', nn='Space_Switch', at='enum', k=1, enumName = 'Wrist:Wrist_ForeArm')

mc.addAttr(mySel, ln='Wing_In_Out', nn='Wing_In_Out', min=-10, max=10, at='double', dv=0, k=1)
mc.addAttr(mySel, ln='Wing_Forward_Back', nn='Wing_Forward_Back', min=-10, max=10, at='double', dv=0, k=1)
mc.addAttr(mySel, ln='Wing_Up_Down', nn='Wing_Up_Down', min=-10, max=10, at='double', dv=0, k=1)

#addAttr -ln "test"  -at double  -min 0 -max 1 -dv 0 
#setAttr -e-keyable true

#______________________#
# unneeded divider attribute, for organization/ look
import maya.cmds as mc

mySel = mc.ls(sl=1)

mc.addAttr(mySel, ln='Pose', nn='Pose', at='enum', enumName = 'Attr')

mc.setAttr(mySel[0] + '.Pose', e=1, channelBox=1)




#________________________#

import maya.cmds as mc

offset_listR = [ 'sknJnt_r_wingA1_ctrl_grp_offset', 
                'sknJnt_r_wingC2_ctrl_grp_offset', 
                'sknJnt_r_wingB2_ctrl_grp_offset', 
                'sknJnt_r_wingB1_ctrl_grp_offset', 
                'sknJnt_r_wingC1_ctrl_grp_offset', 
                'sknJnt_r_pointerFinger1_ctrl_grp_offset', 
                'sknJnt_r_thumb1_ctrl_grp_offset', 
                'FK_sknJnt_r_foreArm1_ctrl_grp_offset', 
                'FK_sknJnt_r_clavicle_ctrl_grp_offset', 
                'FK_sknJnt_r_upperArm1_ctrl_grp_offset', 
                'FK_sknJnt_r_foreArm3_ctrl_grp_offset']


for i in offset_listR:
    mc.setDrivenKeyframe( i + '.rotate', currentDriver = 'FK_sknJnt_r_foreArm3_ctrl.Wing_In_Out' )
    mc.setDrivenKeyframe( i + '.translate', currentDriver = 'FK_sknJnt_r_foreArm3_ctrl.Wing_In_Out' )


#________________________#

import maya.cmds as mc

offset_listL = [ 'sknJnt_l_wingA1_ctrl_grp_offset', 
                'sknJnt_l_wingC2_ctrl_grp_offset', 
                'sknJnt_l_wingB2_ctrl_grp_offset', 
                'sknJnt_l_wingB1_ctrl_grp_offset', 
                'sknJnt_l_wingC1_ctrl_grp_offset', 
                'sknJnt_l_pointerFinger1_ctrl_grp_offset', 
                'sknJnt_l_thumb1_ctrl_grp_offset', 
                'FK_sknJnt_l_foreArm1_ctrl_grp_offset', 
                'FK_sknJnt_l_clavicle_ctrl_grp_offset', 
                'FK_sknJnt_l_upperArm1_ctrl_grp_offset', 
                'FK_sknJnt_l_foreArm3_ctrl_grp_offset']


for i in offset_listL:
    mc.setDrivenKeyframe( i + '.rotate', currentDriver = 'FK_sknJnt_l_foreArm3_ctrl.Wing_In_Out' )
    mc.setDrivenKeyframe( i + '.translate', currentDriver = 'FK_sknJnt_l_foreArm3_ctrl.Wing_In_Out' )
    
    


#________________________#

import maya.cmds as mc

mySel = mc.ls(sl=1)

for i in mySel: 
    if mc.objExists(i + '.Wing_In_Out'):
        mc.deleteAttr(i, attribute='Wing_In_Out' )
    else:
        print('ATTRIBUTE DOES NOT EXIST!')











