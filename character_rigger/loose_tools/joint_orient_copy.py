import maya.cmds as mc

my_sel = mc.ls(sl=True)

jnt_1_ori = mc.joint(my_sel[0], orientation=True, query=True)
print(jnt_1_ori)
mc.joint(my_sel[1], orientation=jnt_1_ori, edit=True)

#jnt_1 = mc.getAttr(my_sel[0] + ".jointOrient")
#mc.setAttr(my_sel[1] + ".jointOrient", jnt_1[0])

    
