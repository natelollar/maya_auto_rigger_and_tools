import maya.cmds as mc

import random

# assign blinn to selected objects named after object with random color
def assign_blinn():
    
    mySel = mc.ls(sl=True)

    for i in mySel:
        #_________________________________________#

        # create shader
        blinn_mat = mc.shadingNode ( 'blinn', n = i + '_mat', asShader=True)

        # create shader group
        blinn_mat_SG = mc.sets( renderable=True, noSurfaceShader=True, empty=True, name = blinn_mat + 'SG'  )
        
        # connect material to sprite
        mc.connectAttr(blinn_mat + '.outColor', blinn_mat_SG + '.surfaceShader', f=True)
        
        # assign redshift material to selected
        mc.select(i)
        mc.hyperShade(assign=blinn_mat)
        
        # create random colors
        colorR_rand = random.triangular( 0, 1 )
        colorG_rand = random.triangular( 0, 1 )
        colorB_rand = random.triangular( 0, 1 )

        # assign random colors
        mc.setAttr( blinn_mat + '.colorR', colorR_rand )
        mc.setAttr( blinn_mat + '.colorG', colorG_rand )
        mc.setAttr( blinn_mat + '.colorB', colorB_rand )
        #_________________________________________#

#assign_blinn()

