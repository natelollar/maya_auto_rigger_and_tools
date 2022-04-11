# copy vert skin weight
# copy first selected vertices to second group of vertices
# select second set in same order as first
import maya.cmds as mc
import maya.mel as mel

try: # for python 2.7
    from itertools import izip as zip
except: # for python 3.x
    pass


mySel = mc.ls(sl=True, flatten=True)  #flatten to get verts individually

mySel_half = len(mySel)/2

listA = mySel[:mySel_half]

listB = mySel[mySel_half:]

print(listA)

print(listB)


for vertA, vertB in zip(listA, listB):
    print(vertA)
    print(vertB)
     
    mc.select(vertA)
    #mel.eval('CopyVertexWeights')
    mel.eval('artAttrSkinWeightCopy')

    mc.select(vertB)
    #mel.eval('PasteVertexWeights')
    mel.eval('artAttrSkinWeightPaste')

    