# copy vert skin weight
# copy first selected vertices to second group of vertices
# select second set in same order as first
import maya.cmds as mc
import maya.mel as mel

import os

try: # for python 2.7
    from itertools import izip as zip
except: # for python 3.x
    pass

def copy_vertex_weights():
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
        skinA_amnt = mc.skinPercent( 'skinCluster1', vertA, query=True, value=True )
        print('skinA_amnt: ' +str( skinA_amnt))
        #mel.eval('CopyVertexWeights')
        mel.eval('artAttrSkinWeightCopy')

        mc.select(vertB)
        skinB_amnt = mc.skinPercent( 'skinCluster1', vertB, query=True, value=True )
        print('skinB_amnt: ' + str(skinB_amnt))
        #mel.eval('PasteVertexWeights')
        mel.eval('artAttrSkinWeightPaste')

        skinB_amnt_new = mc.skinPercent( 'skinCluster1', vertB, query=True, value=True )
        print('skinB_amnt_new: ' + str(skinB_amnt_new))


def copy_vertex_weights_test():
    file_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "/" "vert_weight_test.fbx" )
    print(file_path)
    mc.file(    str(file_path),
                i=True
                )