import maya.cmds as mc

from ..ar_functions import find_jnts
    
#__________________________________________________________#
#______________________ Clavicle___________________________#
#__________________________________________________________#



def clavicle_rig(direction):
    # find clavicle/ scapula joint
    clav_jnt_temp = find_jnts.find_jnts()
    clav_jnt = clav_jnt_temp.l_r_clavicle_jnt(direction)

    # find shoulder joint
    shoulder_jnt = mc.listConnections(clav_jnt, s=0, d=1, type='joint') 

    print( clav_jnt )
    
    print( shoulder_jnt )

    mc.select(shoulder_jnt)



    '''
    #create single chain ikHandle for clavicle________
    l_clavicle_ikHandle = mc.ikHandle(n='ikHandle_l_clavicle',sj=l_clavicle_var_list[0], ee=l_upperArm1_var_list[0], sol='ikSCsolver')

    mc.setAttr((l_clavicle_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((l_clavicle_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((l_clavicle_ikHandle[0] + '.poleVectorZ'), 0)
    #rename ik effector
    l_clavicle_ikHandle_effector = mc.listConnections(l_clavicle_ikHandle, s=True, type='ikEffector')
    mc.rename(l_clavicle_ikHandle_effector, 'effector_l_arm')
    #group ik handle
    lClvGrp = mc.group(em=True)
    lClvGrp = mc.rename(lClvGrp, l_clavicle_ikHandle[0] + '_grp')
    lClvGrp_const = mc.parentConstraint(l_clavicle_ikHandle[0], lClvGrp)
    mc.delete(lClvGrp_const)
    mc.parent(l_clavicle_ikHandle[0], lClvGrp)

    
    l_arm_clavicle_ctrl_list = []
    l_arm_clavicle_ctrl_grp_list = []
    #create ctrl for l clavicle
    for items in range(0,1):
        #create pyramid curve
        myCurve = mc.curve(d=1, p=[ (-1, 1, 1), 
                                    (-1, 1, -1), 
                                    (1, 1, -1), 
                                    (1, 1, 1), 
                                    (-1, 1, 1), 
                                    (-1, -1, 1), 
                                    (-1, -1, -1), 
                                    (1, -1, -1), 
                                    (1, -1, 1), 
                                    (-1, -1, 1), 
                                    (-1, 1, 1), 
                                    (1, 1, 1), 
                                    (1, -1, 1), 
                                    (1, -1, -1), 
                                    (1, 1, -1), 
                                    (-1, 1, -1), 
                                    (-1, -1, -1)
                                    ])
        #curve size
        mc.setAttr((myCurve + ".translateX"), 3)
        mc.setAttr((myCurve + ".translateY"), 12)
        mc.setAttr((myCurve + ".translateZ"), 0)
        mc.setAttr((myCurve + ".scaleX"), 1)
        mc.setAttr((myCurve + ".scaleY"), 1)
        mc.setAttr((myCurve + ".scaleZ"), 1)
        #pivot to world origin
        mc.xform(myCurve, piv=(-3,-12,0))
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        mc.setAttr((curveShape[0] + '.lineWidth'), 2) 
        #hide uneeded attributes
        mc.setAttr((myCurve + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.rz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.sx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.sy'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.sz'), lock=True, keyable=False, channelBox=False)
        #rename curve
        myCurve = mc.rename('pvCtrl_l_clavicle')
        #group curve
        curveGrouped_offset = mc.group(em=True)
        mc.parent(myCurve, curveGrouped_offset)
        curveGrouped = mc.group(em=True)
        mc.parent(curveGrouped_offset, curveGrouped)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        
        #parent constrain and delete to get position
        tempConst = mc.parentConstraint(l_upperArm1_var_list, myGroup, sr=('x','y','z'))
        mc.delete(tempConst)

        #append list for later use
        l_arm_clavicle_ctrl_list.append(myCurve)
        l_arm_clavicle_ctrl_grp_list.append(myGroup)

    # parent ik handle to clavicle ctrl
    mc.parentConstraint(l_arm_clavicle_ctrl_list[0], lClvGrp, sr=('x','y','z'))

    #_____________________L Clavicle Stretch___________________________#
    l_clavicle_var_loc = mc.spaceLocator(n=l_clavicle_var_list[0] + '_locator')
    l_upperArm1_var_loc = mc.spaceLocator(n=l_upperArm1_var_list[0] + '_locator')
    mc.pointConstraint(l_clavicle_var_list[0], l_clavicle_var_loc)
    mc.pointConstraint(l_clavicle_ikHandle[0], l_upperArm1_var_loc)
    lClv_measerTool = mc.distanceDimension(l_clavicle_var_loc, l_upperArm1_var_loc)
    lClv_measerTool_parent = mc.listRelatives(lClv_measerTool, p=True)
    lClv_measerTool_parent = mc.rename(lClv_measerTool_parent, ('distanceDimension_' + l_clavicle_var_list[0]))
    mc.connectAttr(lClv_measerTool_parent + '.distance', l_upperArm1_var_list[0] + '.translateX')
    lClv_measerTool_grp = mc.group(em = True, n=lClv_measerTool_parent + '_grp')
    mc.parent(lClv_measerTool_parent, l_clavicle_var_loc, l_upperArm1_var_loc, lClv_measerTool_grp)
    #***was getting "cycle" glitch for parentConstraining clavicle locator instead of pointConstraining


    #__________________________________________________________#
    #_______________blendColor offset Joint____________________#
    #__________________________________________________________#
    #selection needed to be cleared (for some reason)
    mc.select(cl=True)

    l_arm_blend_offsetJnt = []
    for i in range(0,1):
        myJoint = mc.joint()
        myJoint = mc.rename(myJoint, (l_clavicle_var_list[0] + '_offset'))
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        pcA = mc.parentConstraint(l_clavicle_var_list[0], myJoint)
        mc.delete(pcA)
        mc.makeIdentity(myJoint, apply=True)
        pcB = mc.parentConstraint(l_clavicle_var_list[0], myJoint)
        l_arm_blend_offsetJnt.append(myJoint)
        '''