import maya.cmds as mc

mySel = mc.ls(sl=True)

for i in mySel:
    mc.select(i, cl=True)
    jnt_name = i
    jnt_pos = mc.getAttr(i + ".translate")
    jnt_rot = mc.getAttr(i + ".rotate")
    rot_order = mc.getAttr(i + ".rotateOrder")
    jnt_rot_axis = mc.getAttr(i + ".rotateAxis")
    jnt_orient = mc.getAttr(i + ".jointOrient")
    
    mc.delete(i)
    new_jnt = mc.joint( n=jnt_name, #name
                        position=jnt_pos[0], #translation
                        orientation=jnt_orient[0], #joint orient
                        radius=1,  #radius
                        angleX=0, #rotation
                        angleY=0, 
                        angleZ=0,
                        scaleOrientation=(0,0,0),#rotation axis
                        rotationOrder="XYZ"  #rotation order
                        )
    mc.setAttr(new_jnt + ".displayLocalAxis", 1)
    mc.setAttr(new_jnt + ".jointOrientX", cb=True)
    mc.setAttr(new_jnt + ".jointOrientY", cb=True)
    mc.setAttr(new_jnt + ".jointOrientZ", cb=True)
    mc.setAttr(new_jnt + ".rotateAxisX", cb=True)
    mc.setAttr(new_jnt + ".rotateAxisY", cb=True)
    mc.setAttr(new_jnt + ".rotateAxisZ", cb=True)
    mc.setAttr(new_jnt + ".rotateOrder", cb=True)

    
    
