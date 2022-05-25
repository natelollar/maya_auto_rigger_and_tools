# copy attribute to another object

import maya.cmds as mc

mySel = mc.ls(sl=True)

# copy first selected object attribute to second selected object
mc.copyAttr(mySel[0], 
            mySel[1], 
            values = True, 
            attribute = ['tx'] )