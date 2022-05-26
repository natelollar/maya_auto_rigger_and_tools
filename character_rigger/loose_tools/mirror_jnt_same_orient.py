# mirror joint to have similar orient (not same)

import maya.cmds as mc

mySel = mc.ls(sl=True)

for i in mySel:

    newJoint = mc.mirrorJoint(i, mirrorYZ=True, mirrorBehavior=True, searchReplace=('l_', 'r_') )

    mc.setAttr(newJoint[0] + '.rotateX', 180) # change axis to rotate based on original joint

    mc.makeIdentity(newJoint, apply=True)

    jntClrR = mc.getAttr(i + '.wireColorR')
    jntClrG = mc.getAttr(i + '.wireColorG')
    jntClrB = mc.getAttr(i + '.wireColorB')

    mc.setAttr( newJoint[0] + '.wireColorRGB', jntClrR, jntClrG, jntClrB )


