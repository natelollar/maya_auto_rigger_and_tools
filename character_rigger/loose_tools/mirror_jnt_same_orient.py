# mirror joint to have similar orient (not same)
import maya.cmds as mc

def mirror_jnt_same_orient():
    radio_button = mc.radioButtonGrp( 'axis_button', query=True, sl=True)
    if radio_button == 1:
        flip_axis = '.rotateX'
    elif radio_button == 2:
        flip_axis = '.rotateY'
    elif radio_button == 3:
        flip_axis = '.rotateZ'

    left_prefixA = mc.textField('left_prefix_textA', query=True, text=True)
    right_prefixA = mc.textField('right_prefix_textA', query=True, text=True)

    mySel = mc.ls(sl=True)

    for i in mySel:

        newJoint = mc.mirrorJoint(i, mirrorYZ=True, mirrorBehavior=True, searchReplace=(left_prefixA, right_prefixA) )

        mc.setAttr(newJoint[0] + flip_axis, 180) # change axis to rotate based on original joint

        mc.makeIdentity(newJoint, apply=True)

        jntClrR = mc.getAttr(i + '.wireColorR')
        jntClrG = mc.getAttr(i + '.wireColorG')
        jntClrB = mc.getAttr(i + '.wireColorB')

        mc.setAttr( newJoint[0] + '.wireColorRGB', jntClrR, jntClrG, jntClrB )


