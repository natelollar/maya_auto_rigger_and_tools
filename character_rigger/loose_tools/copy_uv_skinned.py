# works with delete non-deformer history on skinned meshes
# transfer between objects, select source first
import maya.cmds as mc
mySel = mc.ls(sl=True)
source = mySel[0]
target = mySel[-1]
mc.polyTransfer( target, uv=1, ao=source)