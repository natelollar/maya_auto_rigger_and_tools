# for material selection instead
import maya.cmds as mc

import random

mySel = mc.ls(sl=True)
        
# add stingray material for pbr viewport, but keep redshift material
for i in mySel:

    red_mat = i
    shader_grp = red_mat + 'SG'
  
    
    blinn_mat = mc.shadingNode ( 'blinn', n = red_mat  + '_blinn', asShader=True)
    
    # create random colors
    colorR_rand = random.triangular( 0, 1 )
    colorG_rand = random.triangular( 0, 1 )
    colorB_rand = random.triangular( 0, 1 )

    # assign random colors
    mc.setAttr( blinn_mat + '.colorR', colorR_rand )
    mc.setAttr( blinn_mat + '.colorG', colorG_rand )
    mc.setAttr( blinn_mat + '.colorB', colorB_rand )
   
    
    #connect materials
    mc.connectAttr(blinn_mat + '.outColor', shader_grp + '.surfaceShader', f=True)
    
    mc.connectAttr(red_mat + '.outColor', shader_grp + '.rsSurfaceShader', f=True)
    