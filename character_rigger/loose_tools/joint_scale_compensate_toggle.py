import maya.cmds as mc

def scale_compensate_off():
    mySel = mc.ls(sl=True)

    for i in mySel:
        mc.setAttr( i + '.segmentScaleCompensate', 0)

def scale_compensate_on():
    mySel = mc.ls(sl=True)

    for i in mySel:
        mc.setAttr( i + '.segmentScaleCompensate', 1)
