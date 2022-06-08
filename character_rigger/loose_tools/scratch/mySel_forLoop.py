
#___________________#

import maya.cmds as mc

mySel = mc.ls(sl=1)

for i in mySel:
    mc.setAttr( i + '.segmentScaleCompensate', 0 )


#___________________#

import maya.cmds as mc

mySel = mc.ls(sl=1)

mc.scaleConstraint(mySel[0], mySel[1])


