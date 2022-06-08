# copy attribute to another object

import maya.cmds as mc

def copy_attribute():
    mySel = mc.ls(sl=True)

    mc.copyAttr(mySel[0], 
                mySel[1], 
                values = True, 
                attribute = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz'] )