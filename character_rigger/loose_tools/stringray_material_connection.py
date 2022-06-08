import maya.cmds as mc


mySel = mc.ls(sl=True)

shader_grp = mySel[0]

stingray_mat = mySel[1]

red_mat = mySel[2]

baseColor_tex = mySel[3]
normal_tex = mySel[4]
metal_tex = mySel[5]
rough_tex = mySel[6]
ao_tex = mySel[7]


mc.connectAttr(stingray_mat + '.outColor', shader_grp + '.surfaceShader', f=True)

mc.connectAttr(red_mat + '.outColor', shader_grp + '.rsSurfaceShader', f=True)


mc.connectAttr(baseColor_tex + '.outColor', stingray_mat + '.TEX_color_map', f=True)

mc.connectAttr(normal_tex + '.outColor', stingray_mat + '.TEX_normal_map', f=True)

mc.connectAttr(metal_tex + '.outColor', stingray_mat + '.TEX_metallic_map', f=True)

mc.connectAttr(rough_tex + '.outColor', stingray_mat + '.TEX_roughness_map', f=True)

mc.connectAttr(ao_tex + '.outColor', stingray_mat + '.TEX_ao_map', f=True)

mc.rename(stingray_mat, 'StingrayPBS_' + red_mat)





        