import maya.cmds as mc

def single_jnt():
    myJoint = mc.joint()
    mc.Unparent(myJoint)
    myJoint = mc.rename(myJoint, (i + '_blendOffset'))
    #size and color
    mc.setAttr(".radius", 4)
    mc.setAttr(".overrideEnabled", 1)
    mc.setAttr(".overrideRGBColors", 1)
    mc.setAttr(".overrideColorRGB", 1, 0, 0)
    mc.parentConstraint(i, myJoint)
    spine1_colorBlendJnt.append(myJoint)