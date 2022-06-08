try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass

# ___________________ #
import maya.cmds as mc

from character_rigger.ar_functions import sel_joints


fkJoint_list = sel_joints.sel_joints('fkJnt_hair1', 'fkJnt_hair9').rev_sel_jnt_chainA()
ikJoint_list = sel_joints.sel_joints('ikJnt_hair1', 'ikJnt_hair9').rev_sel_jnt_chainA()
jnt_chain = sel_joints.sel_joints('sknJnt_hair1', 'sknJnt_hair9').rev_sel_jnt_chainA()

switch_ctrl_list = 'hair_swch_ctrl'


print(fkJoint_list)
print(ikJoint_list)
print(jnt_chain)


# ______ add blend scale _____ #

'''
for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, jnt_chain):
        mc.scaleConstraint(i_FK, i_IK, i)
'''


# scale constraint switch
for jnt_FK, jnt_IK, jnt in zip(fkJoint_list, ikJoint_list, jnt_chain):
    # 1 is fk, 0 is ik
    mc.setAttr((switch_ctrl_list + '.fk_ik_blend'), 0)
    # alternative is to disconnect/ unlock and use '.target[0].targetWeight'
    mc.setAttr( (jnt + '_scaleConstraint1.' + jnt_FK + 'W0'),  0)
    mc.setAttr( (jnt + '_scaleConstraint1.' + jnt_IK + 'W1'),  1)

    mc.setDrivenKeyframe((jnt + '_scaleConstraint1.' + jnt_FK + 'W0'), currentDriver = (switch_ctrl_list + '.fk_ik_blend'))
    mc.setDrivenKeyframe((jnt + '_scaleConstraint1.' + jnt_IK + 'W1'), currentDriver = (switch_ctrl_list + '.fk_ik_blend'))

    mc.setAttr((switch_ctrl_list + '.fk_ik_blend'), 1)
    mc.setAttr( (jnt + '_scaleConstraint1.' + jnt_FK + 'W0'),  1)
    mc.setAttr( (jnt + '_scaleConstraint1.' + jnt_IK + 'W1'),  0)

    mc.setDrivenKeyframe((jnt + '_scaleConstraint1.' + jnt_FK + 'W0'), currentDriver = (switch_ctrl_list + '.fk_ik_blend'))
    mc.setDrivenKeyframe((jnt + '_scaleConstraint1.' + jnt_IK + 'W1'), currentDriver = (switch_ctrl_list + '.fk_ik_blend'))










'''
# ______ add blend scale _____ #


for i_FK, i_IK, i in zip(fkJoint_list, ikJoint_list, jnt_chain):
        #create blend color nodes
        blendColorsScl = mc.createNode('blendColors', n= i + '_blendColorsScl')

        #translate
        mc.connectAttr((i_FK + '.scale'), (blendColorsTran + '.color1'), f=True)
        mc.connectAttr((i_IK + '.scale'), (blendColorsTran + '.color2'), f=True)
        mc.connectAttr((blendColorsScl + '.output'), (i + '.scale'), f=True)

        #append lists for outside loop use
        blendColorsTran_list.append(blendColorsTran)
'''





















