import maya.cmds as mc

mySel = mc.ls(sl=1)


mc.connectAttr( mySel[0] + '.worldSpace[0]', 
                mySel[1] + '.inputTarget[0].inputTargetGroup[0].inputTargetItem[6000].inputGeomTarget', 
                f=1)

