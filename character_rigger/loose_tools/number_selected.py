# prints number of selected items
import maya.cmds as mc

mySel = mc.ls(sl=True)

print ( len(mySel) )


    
    