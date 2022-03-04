#_________@mkg Start_________________________#
#_________ Auto Rigger__________________#

#____________________________________________#
#_________import modules_____________________#

import maya.cmds as mc

import maya.api.OpenMaya as om

import itertools

import ast

#____________________________________________#
#_________print start________________________#

print('\n')
print('__________Start__________')
print('Welcome to my Auto Rigger')
print('_________________________')



#___________initial prefix__________#

skel_pre_var_list = ['sknJnt_']

#___________initial Spine Neck variables__________#

spine1_var_list = [(skel_pre_var_list[0] + 'spine1')]
spine2_var_list = [(skel_pre_var_list[0] + 'spine2')]
spine3_var_list = [(skel_pre_var_list[0] + 'spine3')]
spine4_var_list = [(skel_pre_var_list[0] + 'spine4')]
spine5_var_list = [(skel_pre_var_list[0] + 'spine5')]
spine6_var_list = [(skel_pre_var_list[0] + 'spine6')]

neck1_var_list = [(skel_pre_var_list[0] + 'neck1')]
neck2_var_list = [(skel_pre_var_list[0] + 'neck2')]
neck3_var_list = [(skel_pre_var_list[0] + 'neck3')]
neck4_var_list = [(skel_pre_var_list[0] + 'neck4')]

#___________initial Leg variables__________#
#l
l_hip_var_list = [(skel_pre_var_list[0] + 'l_leg1')]
l_knee_var_list = [(skel_pre_var_list[0] + 'l_leg2')]
l_ankle_var_list = [(skel_pre_var_list[0] + 'l_foot1')]
l_toe_var_list = [(skel_pre_var_list[0] + 'l_foot2')]
#r
r_hip_var_list = [(skel_pre_var_list[0] + 'r_leg1')]
r_knee_var_list = [(skel_pre_var_list[0] + 'r_leg2')]
r_ankle_var_list = [(skel_pre_var_list[0] + 'r_foot1')]
r_toe_var_list = [(skel_pre_var_list[0] + 'r_foot2')]

#____________initial Arm variables__________#
#l
l_clavicle_var_list = [(skel_pre_var_list[0] + 'l_clavicle')]

l_upperArm1_var_list = [(skel_pre_var_list[0] + 'l_upperArm1')]

l_foreArm1_var_list = [(skel_pre_var_list[0] + 'l_foreArm1')]
l_foreArm2_var_list = [(skel_pre_var_list[0] + 'l_foreArm2')]
l_foreArm3_var_list = [(skel_pre_var_list[0] + 'l_foreArm3')]
l_foreArm4_var_list = [(skel_pre_var_list[0] + 'l_foreArm4')]
l_foreArm5_var_list = [(skel_pre_var_list[0] + 'l_foreArm5')]

#r
r_clavicle_var_list = [(skel_pre_var_list[0] + 'r_clavicle')]

r_upperArm1_var_list = [(skel_pre_var_list[0] + 'r_upperArm1')]

r_foreArm1_var_list = [(skel_pre_var_list[0] + 'r_foreArm1')]
r_foreArm2_var_list = [(skel_pre_var_list[0] + 'r_foreArm2')]
r_foreArm3_var_list = [(skel_pre_var_list[0] + 'r_foreArm3')]
r_foreArm4_var_list = [(skel_pre_var_list[0] + 'r_foreArm4')]
r_foreArm5_var_list = [(skel_pre_var_list[0] + 'r_foreArm5')]


#___________ initial Finger variables__________#
#l
l_thumb1 = skel_pre_var_list[0] + 'l_thumb1'
l_thumb2 = skel_pre_var_list[0] + 'l_thumb2'
l_thumb3 = skel_pre_var_list[0] + 'l_thumb3'

l_pointerFinger1 = skel_pre_var_list[0] + 'l_pointerFinger1'
l_pointerFinger2 = skel_pre_var_list[0] + 'l_pointerFinger2'
l_pointerFinger3 = skel_pre_var_list[0] + 'l_pointerFinger3'
l_pointerFinger4 = skel_pre_var_list[0] + 'l_pointerFinger4'

l_middleFinger1 = skel_pre_var_list[0] + 'l_middleFinger1'
l_middleFinger2 = skel_pre_var_list[0] + 'l_middleFinger2'
l_middleFinger3 = skel_pre_var_list[0] + 'l_middleFinger3'
l_middleFinger4 = skel_pre_var_list[0] + 'l_middleFinger4'

l_ringFinger1 = skel_pre_var_list[0] + 'l_ringFinger1'
l_ringFinger2 = skel_pre_var_list[0] + 'l_ringFinger2'
l_ringFinger3 = skel_pre_var_list[0] + 'l_ringFinger3'
l_ringFinger4 = skel_pre_var_list[0] + 'l_ringFinger4'

l_pinkyFinger1 = skel_pre_var_list[0] + 'l_pinkyFinger1'
l_pinkyFinger2 = skel_pre_var_list[0] + 'l_pinkyFinger2'
l_pinkyFinger3 = skel_pre_var_list[0] + 'l_pinkyFinger3'
l_pinkyFinger4 = skel_pre_var_list[0] + 'l_pinkyFinger4'

#r
r_thumb1 = skel_pre_var_list[0] + 'r_thumb1'
r_thumb2 = skel_pre_var_list[0] + 'r_thumb2'
r_thumb3 = skel_pre_var_list[0] + 'r_thumb3'

r_pointerFinger1 = skel_pre_var_list[0] + 'r_pointerFinger1'
r_pointerFinger2 = skel_pre_var_list[0] + 'r_pointerFinger2'
r_pointerFinger3 = skel_pre_var_list[0] + 'r_pointerFinger3'
r_pointerFinger4 = skel_pre_var_list[0] + 'r_pointerFinger4'

r_middleFinger1 = skel_pre_var_list[0] + 'r_middleFinger1'
r_middleFinger2 = skel_pre_var_list[0] + 'r_middleFinger2'
r_middleFinger3 = skel_pre_var_list[0] + 'r_middleFinger3'
r_middleFinger4 = skel_pre_var_list[0] + 'r_middleFinger4'

r_ringFinger1 = skel_pre_var_list[0] + 'r_ringFinger1'
r_ringFinger2 = skel_pre_var_list[0] + 'r_ringFinger2'
r_ringFinger3 = skel_pre_var_list[0] + 'r_ringFinger3'
r_ringFinger4 = skel_pre_var_list[0] + 'r_ringFinger4'

r_pinkyFinger1 = skel_pre_var_list[0] + 'r_pinkyFinger1'
r_pinkyFinger2 = skel_pre_var_list[0] + 'r_pinkyFinger2'
r_pinkyFinger3 = skel_pre_var_list[0] + 'r_pinkyFinger3'
r_pinkyFinger4 = skel_pre_var_list[0] + 'r_pinkyFinger4'

#___finger joint lists______________________#
#l
l_thumb_list = [l_thumb1, l_thumb2, l_thumb3]

l_pointerFinger_list = [l_pointerFinger1, l_pointerFinger2, l_pointerFinger3, l_pointerFinger4]

l_middleFinger_list = [l_middleFinger1, l_middleFinger2, l_middleFinger3, l_middleFinger4]

l_ringFinger_list = [l_ringFinger1, l_ringFinger2, l_ringFinger3, l_ringFinger4]

l_pinkyFinger_list = [l_pinkyFinger1, l_pinkyFinger2, l_pinkyFinger3, l_pinkyFinger4]

#r
r_thumb_list = [r_thumb1, r_thumb2, r_thumb3]

r_pointerFinger_list = [r_pointerFinger1, r_pointerFinger2, r_pointerFinger3, r_pointerFinger4]

r_middleFinger_list = [r_middleFinger1, r_middleFinger2, r_middleFinger3, r_middleFinger4]

r_ringFinger_list = [r_ringFinger1, r_ringFinger2, r_ringFinger3, r_ringFinger4]

r_pinkyFinger_list = [r_pinkyFinger1, r_pinkyFinger2, r_pinkyFinger3, r_pinkyFinger4]

#___________initial Face/ Head variables__________#
#________face joints______________#
#__________________________________________________________#

nose_var = skel_pre_var_list[0] + 'nose'
l_nose_var = skel_pre_var_list[0] + 'l_nose'
r_nose_var = skel_pre_var_list[0] + 'r_nose'
nose_bridge_var = skel_pre_var_list[0] + 'nose_bridge'

brow_center_var = skel_pre_var_list[0] + 'brow_center'
l_brow1_var = skel_pre_var_list[0] + 'l_brow1'
r_brow1_var = skel_pre_var_list[0] + 'r_brow1'
l_brow2_var = skel_pre_var_list[0] + 'l_brow2'
r_brow2_var = skel_pre_var_list[0] + 'r_brow2'
l_brow3_var = skel_pre_var_list[0] + 'l_brow3'
r_brow3_var = skel_pre_var_list[0] + 'r_brow3'

lip_top_var = skel_pre_var_list[0] + 'lip_top'
lip_bot_var = skel_pre_var_list[0] + 'lip_bot'
l_lip_top_var = skel_pre_var_list[0] + 'l_lip_top'
r_lip_top_var = skel_pre_var_list[0] + 'r_lip_top'
l_lip_bot_var = skel_pre_var_list[0] + 'l_lip_bot'
r_lip_bot_var = skel_pre_var_list[0] + 'r_lip_bot'
l_lip_corner_var = skel_pre_var_list[0] + 'l_lip_corner'
r_lip_corner_var = skel_pre_var_list[0] + 'r_lip_corner'

l_lid_top_var = skel_pre_var_list[0] + 'l_lid_top'
r_lid_top_var = skel_pre_var_list[0] + 'r_lid_top'
l_lid_bot_var = skel_pre_var_list[0] + 'l_lid_bot'
r_lid_bot_var = skel_pre_var_list[0] + 'r_lid_bot'
l_lid1_var = skel_pre_var_list[0] + 'l_lid1'
r_lid1_var = skel_pre_var_list[0] + 'r_lid1'
l_lid3_var = skel_pre_var_list[0] + 'l_lid3'
r_lid3_var = skel_pre_var_list[0] + 'r_lid3'

l_cheek1_var = skel_pre_var_list[0] + 'l_cheek1'
r_cheek1_var = skel_pre_var_list[0] + 'r_cheek1'
l_cheek2_var = skel_pre_var_list[0] + 'l_cheek2'
r_cheek2_var = skel_pre_var_list[0] + 'r_cheek2'
r_cheek3_var = skel_pre_var_list[0] + 'r_cheek3'
l_cheek3_var = skel_pre_var_list[0] + 'l_cheek3'

chin_var = skel_pre_var_list[0] + 'chin'
l_chin1_var = skel_pre_var_list[0] + 'l_chin1'
r_chin1_var = skel_pre_var_list[0] + 'r_chin1'
l_chin2_var = skel_pre_var_list[0] + 'l_chin2'
r_chin2_var = skel_pre_var_list[0] + 'r_chin2'

#ear joints_____________________
l_ear1_var = skel_pre_var_list[0] + 'l_ear1'
l_ear2_var = skel_pre_var_list[0] + 'l_ear2'

r_ear1_var = skel_pre_var_list[0] + 'r_ear1'
r_ear2_var = skel_pre_var_list[0] + 'r_ear2'

#___jaw joint______________________#
jaw_var_list = [(skel_pre_var_list[0] + 'jaw')]

#_________________________________________#
#___Face/head joint lists______________________#
#_________________________________________#

topFaceJnt_var_list = [ nose_var,
                        l_nose_var,
                        r_nose_var,
                        nose_bridge_var,

                        brow_center_var,
                        l_brow1_var,
                        r_brow1_var,
                        l_brow2_var,
                        r_brow2_var,
                        l_brow3_var,
                        r_brow3_var,

                        lip_top_var,
                        l_lip_top_var,
                        r_lip_top_var,
                        
                        l_lid_top_var,
                        r_lid_top_var,
                        l_lid_bot_var,
                        r_lid_bot_var,
                        l_lid1_var,
                        r_lid1_var,
                        l_lid3_var,
                        r_lid3_var,

                        l_cheek1_var,
                        r_cheek1_var,
                        l_cheek2_var,
                        r_cheek2_var,
                        ]

midFaceJnt_var_list = [ l_lip_corner_var,
                        r_lip_corner_var,

                        r_cheek3_var,
                        l_cheek3_var,
                        ]

botFaceJnt_var_list = [ lip_bot_var,
                        l_lip_bot_var,
                        r_lip_bot_var,

                        chin_var,
                        l_chin1_var,
                        r_chin1_var,
                        l_chin2_var,
                        r_chin2_var,
                        ]

#ear lists
lEarJnt_var_list = [l_ear1_var, l_ear2_var]

rEarJnt_var_list = [r_ear1_var, r_ear2_var]





#____FUNCTIONS_____ (to replace joint name text field with selected joint)___#

#___________Spine_____________#
def spine1_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine1_text', edit=True, text=selString)
    textInput = mc.textField('spine1_text', q=True, text=True)
    del spine1_var_list [:]
    spine1_var_list.append(textInput)
    print (spine1_var_list[0])

def spine2_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine2_text', edit=True, text=selString)
    textInput = mc.textField('spine2_text', q=True, text=True)
    del spine2_var_list [:]
    spine2_var_list.append(textInput)
    print (spine2_var_list[0])

def spine3_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine3_text', edit=True, text=selString)
    textInput = mc.textField('spine3_text', q=True, text=True)
    del spine3_var_list [:]
    spine3_var_list.append(textInput)
    print (spine3_var_list[0])

def spine4_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine4_text', edit=True, text=selString)
    textInput = mc.textField('spine4_text', q=True, text=True)
    del spine4_var_list [:]
    spine4_var_list.append(textInput)
    print (spine4_var_list[0])

def spine5_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine5_text', edit=True, text=selString)
    textInput = mc.textField('spine5_text', q=True, text=True)
    del spine5_var_list [:]
    spine5_var_list.append(textInput)
    print (spine5_var_list[0])

def spine6_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('spine6_text', edit=True, text=selString)
    textInput = mc.textField('spine6_text', q=True, text=True)
    del spine6_var_list [:]
    spine6_var_list.append(textInput)
    print (spine6_var_list[0])
#___________Neck_____________#
def neck1_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('neck1_text', edit=True, text=selString)
    textInput = mc.textField('neck1_text', q=True, text=True)
    del neck1_var_list [:]
    neck1_var_list.append(textInput)
    print (neck1_var_list[0])

def neck2_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('neck2_text', edit=True, text=selString)
    textInput = mc.textField('neck2_text', q=True, text=True)
    del neck2_var_list [:]
    neck2_var_list.append(textInput)
    print (neck2_var_list[0])

def neck3_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('neck3_text', edit=True, text=selString)
    textInput = mc.textField('neck3_text', q=True, text=True)
    del neck3_var_list [:]
    neck3_var_list.append(textInput)
    print (neck3_var_list[0])

def neck4_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('neck4_text', edit=True, text=selString)
    textInput = mc.textField('neck4_text', q=True, text=True)
    del neck4_var_list [:]
    neck4_var_list.append(textInput)
    print (neck4_var_list[0])

#___________Face_____________#
#top face
def topFace_selection(items):
    #get selection
    mySel = mc.ls(selection=True)
    #get input list as text=string()
    mc.textFieldGrp('topFace_text', edit=True, text=str(mySel))
    #query text input
    textInput = mc.textFieldGrp('topFace_text', q=True, text=True)
    #turn string back into list
    mySel_list = ast.literal_eval(textInput)
    #delete default/prior list
    del topFaceJnt_var_list [:]
    #extend instead of append b/c it's list to list
    topFaceJnt_var_list.extend(mySel_list)
    #print test
    print (topFaceJnt_var_list)
#mid face
def midFace_selection(items):
    #get selection
    mySel = mc.ls(selection=True)
    #get input list as text=string()
    mc.textFieldGrp('midFace_text', edit=True, text=str(mySel))
    #query text input
    textInput = mc.textFieldGrp('midFace_text', q=True, text=True)
    #turn string back into list
    mySel_list = ast.literal_eval(textInput)
    #delete default/prior list
    del midFaceJnt_var_list [:]
    #extend instead of append b/c it's list to list
    midFaceJnt_var_list.extend(mySel_list)
    #print test
    print (midFaceJnt_var_list)
#bot face
def botFace_selection(items):
    #get selection
    mySel = mc.ls(selection=True)
    #get input list as text=string()
    mc.textFieldGrp('botFace_text', edit=True, text=str(mySel))
    #query text input
    textInput = mc.textFieldGrp('botFace_text', q=True, text=True)
    #turn string back into list
    mySel_list = ast.literal_eval(textInput)
    #delete default/prior list
    del botFaceJnt_var_list [:]
    #extend instead of append b/c it's list to list
    botFaceJnt_var_list.extend(mySel_list)
    #print test
    print (botFaceJnt_var_list)

#___________Ear_____________#
def lEar_selection(items):
    #get selection
    mySel = mc.ls(selection=True)
    #get input list as text=string()
    mc.textFieldGrp('lEar_text', edit=True, text=str(mySel))
    #query text input
    textInput = mc.textFieldGrp('lEar_text', q=True, text=True)
    #turn string back into list
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        #myItem = str(i).replace('l_','r_')
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    #delete default/prior list
    del lEarJnt_var_list [:]
    del rEarJnt_var_list [:]
    #extend instead of append b/c it's list to list
    lEarJnt_var_list.extend(mySel_list)
    rEarJnt_var_list.extend(mySel_listR)
    #print test
    print (lEarJnt_var_list)
    print (rEarJnt_var_list)

def jaw_selection(items):
    mySel = mc.ls(selection=True)
    selString = mySel[0]
    mc.textField('jaw_text', edit=True, text=selString)
    textInput = mc.textField('jaw_text', q=True, text=True)
    del jaw_var_list [:]
    jaw_var_list.append(textInput)
    print (jaw_var_list[0])


#________________L Leg funcions_________________#
#update l_hip jnt
def l_hip_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_hip_text', edit=True, text=selString)
    textInput = mc.textField('l_hip_text', q=True, text=True)
    del l_hip_var_list [:]
    del r_hip_var_list [:]
    l_hip_var_list.append(selString)
    r_hip_var_list.append(selStringR)
    print(l_hip_var_list[0])
    print(r_hip_var_list[0])

#update l knee jnt
def l_knee_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_knee_text', edit=True, text=selString)
    textInput = mc.textField('l_knee_text', q=True, text=True)
    del l_knee_var_list [:]
    del r_knee_var_list [:]
    l_knee_var_list.append(selString)
    r_knee_var_list.append(selStringR)
    print(l_knee_var_list[0])
    print(r_knee_var_list[0])

#update l ankle jnt
def l_ankle_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_ankle_text', edit=True, text=selString)
    textInput = mc.textField('l_ankle_text', q=True, text=True)
    del l_ankle_var_list [:]
    del r_ankle_var_list [:]
    l_ankle_var_list.append(selString)
    r_ankle_var_list.append(selStringR)
    print(l_ankle_var_list[0])
    print(r_ankle_var_list[0])

# update l toe jnt
def l_toe_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_toe_text', edit=True, text=selString)
    textInput = mc.textField('l_toe_text', q=True, text=True)
    del l_toe_var_list [:]
    del r_toe_var_list [:]
    l_toe_var_list.append(selString)
    r_toe_var_list.append(selStringR)
    print(l_toe_var_list[0])
    print(r_toe_var_list[0])

#______________@mkp create reverse foot locators____________________#
def reverseFoot_loc(items):
    #____L______#
    #mc.delete(loc_l_foot_list)
    #mc.delete('l_foot_loc_grp')
    #loc_l_foot_ankle
    loc_l_foot_ankle = mc.spaceLocator(n='loc_l_foot_ankle')
    mc.setAttr((loc_l_foot_ankle[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_ankle[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_ankle[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_ankle[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_ankle[0] + ".translate"), 10.738,9.708,-3.181)
    mc.setAttr((loc_l_foot_ankle[0] + ".rotate"), 5.278, -82.31, -5.275)
    #loc_l_foot_toe
    loc_l_foot_toe = mc.spaceLocator(n='loc_l_foot_toe')
    mc.setAttr((loc_l_foot_toe[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_toe[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_toe[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_toe[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_toe[0] + ".translate"), 12.597,2.148,9.648)
    mc.setAttr((loc_l_foot_toe[0] + ".rotate"), 5.278, -82.31, -5.275)
    #loc_l_foot_toe_end
    loc_l_foot_toe_end = mc.spaceLocator(n='loc_l_foot_toe_end')
    mc.setAttr((loc_l_foot_toe_end[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_toe_end[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_toe_end[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_toe_end[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_toe_end[0] + ".translate"), 13.41,0.224,15.601)
    mc.setAttr((loc_l_foot_toe_end[0] + ".rotate"), 0.156, -82.539, 0.825)
    #loc_l_foot_heel
    loc_l_foot_heel = mc.spaceLocator(n='loc_l_foot_heel')
    mc.setAttr((loc_l_foot_heel[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_heel[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_heel[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_heel[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_heel[0] + ".translate"), 9.547,0.166,-6.787)
    mc.setAttr((loc_l_foot_heel[0] + ".rotate"), 0.156, -82.539, 0.825)
    #loc_l_foot_outer
    loc_l_foot_outer = mc.spaceLocator(n='loc_l_foot_outer')
    mc.setAttr((loc_l_foot_outer[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_outer[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_outer[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_outer[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_outer[0] + ".translate"), 17.04,0.289,7.031)
    mc.setAttr((loc_l_foot_outer[0] + ".rotate"), 0.076, -74.621, 0.906)
    #loc_l_foot_inner
    loc_l_foot_inner = mc.spaceLocator(n='loc_l_foot_inner')
    mc.setAttr((loc_l_foot_inner[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_l_foot_inner[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_l_foot_inner[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_l_foot_inner[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_l_foot_inner[0] + ".translate"), 7.205,0.119,10.571)
    mc.setAttr((loc_l_foot_inner[0] + ".rotate"), 0.782, -88.52, 0.198)
    #delete current locators if exist
    del loc_r_foot_list [:]
    #append back into list for rig
    loc_l_foot_list.extend((loc_l_foot_ankle[0], 
                            loc_l_foot_toe[0],
                            loc_l_foot_toe_end[0],
                            loc_l_foot_heel[0],
                            loc_l_foot_outer[0],
                            loc_l_foot_inner[0]))
    loc_l_foot_list_grp = mc.group(n='l_foot_loc_grp', em=True)
    mc.parent(loc_l_foot_list, loc_l_foot_list_grp)
    print(loc_l_foot_list)
    #____R______#
    #mc.delete(loc_r_foot_list)
    #mc.delete('r_foot_loc_grp')
    loc_r_foot_ankle = mc.spaceLocator(n='loc_r_foot_ankle')
    mc.setAttr((loc_r_foot_ankle[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_ankle[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_ankle[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_ankle[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_ankle[0] + ".translate"), -10.738,9.708,-3.181)
    mc.setAttr((loc_r_foot_ankle[0] + ".rotate"),174.722, -82.31, -174.725)
    #loc_r_foot_toe
    loc_r_foot_toe = mc.spaceLocator(n='loc_r_foot_toe')
    mc.setAttr((loc_r_foot_toe[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_toe[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_toe[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_toe[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_toe[0] + ".translate"), -12.597,2.148,9.648)
    mc.setAttr((loc_r_foot_toe[0] + ".rotate"), 179.844, -82.539, 179.175)
    #loc_r_foot_toe_end
    loc_r_foot_toe_end = mc.spaceLocator(n='loc_r_foot_toe_end')
    mc.setAttr((loc_r_foot_toe_end[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_toe_end[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_toe_end[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_toe_end[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_toe_end[0] + ".translate"), -13.41,0.224,15.601)
    mc.setAttr((loc_r_foot_toe_end[0] + ".rotate"), 179.844, -82.539, 179.175)
    #loc_r_foot_heel
    loc_r_foot_heel = mc.spaceLocator(n='loc_r_foot_heel')
    mc.setAttr((loc_r_foot_heel[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_heel[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_heel[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_heel[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_heel[0] + ".translate"), -9.547,0.166,-6.787)
    mc.setAttr((loc_r_foot_heel[0] + ".rotate"), 179.844, -82.539, 179.175)
    #loc_r_foot_outer
    loc_r_foot_outer = mc.spaceLocator(n='loc_r_foot_outer')
    mc.setAttr((loc_r_foot_outer[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_outer[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_outer[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_outer[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_outer[0] + ".translate"), -17.04,0.289,7.031)
    mc.setAttr((loc_r_foot_outer[0] + ".rotate"), 179.924, -74.621, 179.094)
    #loc_r_foot_inner
    loc_r_foot_inner = mc.spaceLocator(n='loc_r_foot_inner')
    mc.setAttr((loc_r_foot_inner[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_r_foot_inner[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_r_foot_inner[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_r_foot_inner[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_r_foot_inner[0] + ".translate"), -7.205,0.119,10.571)
    mc.setAttr((loc_r_foot_inner[0] + ".rotate"), 179.218, -88.52, 179.802)
    #delete current locators if exist
    del loc_r_foot_list [:]
    #append back into list for rig
    loc_r_foot_list.extend((loc_r_foot_ankle[0], 
                            loc_r_foot_toe[0],
                            loc_r_foot_toe_end[0],
                            loc_r_foot_heel[0],
                            loc_r_foot_outer[0],
                            loc_r_foot_inner[0]))
    loc_r_foot_list_grp = mc.group(n='r_foot_loc_grp', em=True)
    mc.parent(loc_r_foot_list, loc_r_foot_list_grp)
    print(loc_r_foot_list)

#________________ Arm funcions_________________#

def l_clavicle_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_clavicle_text', edit=True, text=selString)
    textInput = mc.textField('l_clavicle_text', q=True, text=True)
    del l_clavicle_var_list [:]
    del r_clavicle_var_list [:]
    l_clavicle_var_list.append(selString)
    r_clavicle_var_list.append(selStringR)
    print(l_clavicle_var_list[0])
    print(r_clavicle_var_list[0])

def l_shoulder_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_shoulder_text', edit=True, text=selString)
    textInput = mc.textField('l_shoulder_text', q=True, text=True)
    del l_upperArm1_var_list [:]
    del r_upperArm1_var_list [:]
    l_upperArm1_var_list.append(selString)
    r_upperArm1_var_list.append(selStringR)
    print(l_upperArm1_var_list[0])
    print(r_upperArm1_var_list[0])

def l_elbow_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_elbow_text', edit=True, text=selString)
    textInput = mc.textField('l_elbow_text', q=True, text=True)
    del l_foreArm1_var_list [:]
    del r_foreArm1_var_list [:]
    l_foreArm1_var_list.append(selString)
    r_foreArm1_var_list.append(selStringR)
    print(l_foreArm1_var_list[0])
    print(r_foreArm1_var_list[0])

def l_twist1_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_twist1_text', edit=True, text=selString)
    textInput = mc.textField('l_twist1_text', q=True, text=True)
    del l_foreArm2_var_list [:]
    del r_foreArm2_var_list [:]
    l_foreArm2_var_list.append(selString)
    r_foreArm2_var_list.append(selStringR)
    print(l_foreArm2_var_list[0])
    print(r_foreArm2_var_list[0])

def l_twist2_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_twist2_text', edit=True, text=selString)
    textInput = mc.textField('l_twist2_text', q=True, text=True)
    del l_foreArm3_var_list [:]
    del r_foreArm3_var_list [:]
    l_foreArm3_var_list.append(selString)
    r_foreArm3_var_list.append(selStringR)
    print(l_foreArm3_var_list[0])
    print(r_foreArm3_var_list[0])

def l_twist3_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_twist3_text', edit=True, text=selString)
    textInput = mc.textField('l_twist3_text', q=True, text=True)
    del l_foreArm4_var_list [:]
    del r_foreArm4_var_list [:]
    l_foreArm4_var_list.append(selString)
    r_foreArm4_var_list.append(selStringR)
    print(l_foreArm4_var_list[0])
    print(r_foreArm4_var_list[0])

def l_wrist_selection(items):
    mySel = mc.ls(selection=True)
    mySelR = []
    for i in mySel:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
            mySelR.append(myItem)
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
            mySelR.append(myItem)
    selString = mySel[0]
    selStringR = mySelR[0]
    mc.textField('l_wrist_text', edit=True, text=selString)
    textInput = mc.textField('l_wrist_text', q=True, text=True)
    del l_foreArm5_var_list [:]
    del r_foreArm5_var_list [:]
    l_foreArm5_var_list.append(selString)
    r_foreArm5_var_list.append(selStringR)
    print(l_foreArm5_var_list[0])
    print(r_foreArm5_var_list[0])

#______________________________#
#___________Fingers____________#

def l_thumb_selection(items):
    mySel = mc.ls(selection=True)
    mc.textFieldGrp('l_thumb_text', edit=True, text=str(mySel))
    textInput = mc.textFieldGrp('l_thumb_text', q=True, text=True)
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    del l_thumb_list [:]
    del r_thumb_list [:]
    l_thumb_list.extend(mySel_list)
    r_thumb_list.extend(mySel_listR)
    print (l_thumb_list)
    print (r_thumb_list)

def l_pointerFinger_selection(items):
    mySel = mc.ls(selection=True)
    mc.textFieldGrp('l_pointerFinger_text', edit=True, text=str(mySel))
    textInput = mc.textFieldGrp('l_pointerFinger_text', q=True, text=True)
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    del l_pointerFinger_list [:]
    del r_pointerFinger_list [:]
    l_pointerFinger_list.extend(mySel_list)
    r_pointerFinger_list.extend(mySel_listR)
    print (l_pointerFinger_list)
    print (r_pointerFinger_list)

def l_middleFinger_selection(items):
    mySel = mc.ls(selection=True)
    mc.textFieldGrp('l_middleFinger_text', edit=True, text=str(mySel))
    textInput = mc.textFieldGrp('l_middleFinger_text', q=True, text=True)
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    del l_middleFinger_list [:]
    del r_middleFinger_list [:]
    l_middleFinger_list.extend(mySel_list)
    r_middleFinger_list.extend(mySel_listR)
    print (l_middleFinger_list)
    print (r_middleFinger_list)

def l_ringFinger_selection(items):
    mySel = mc.ls(selection=True)
    mc.textFieldGrp('l_ringFinger_text', edit=True, text=str(mySel))
    textInput = mc.textFieldGrp('l_ringFinger_text', q=True, text=True)
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    del l_ringFinger_list [:]
    del r_ringFinger_list [:]
    l_ringFinger_list.extend(mySel_list)
    r_ringFinger_list.extend(mySel_listR)
    print (l_ringFinger_list)
    print (r_ringFinger_list)

def l_pinkyFinger_selection(items):
    mySel = mc.ls(selection=True)
    mc.textFieldGrp('l_pinkyFinger_text', edit=True, text=str(mySel))
    textInput = mc.textFieldGrp('l_pinkyFinger_text', q=True, text=True)
    mySel_list = ast.literal_eval(textInput)
    mySel_listR = []
    for i in mySel_list:
        if 'l_' in i:
            myItem = str(i).replace('l_','r_')
        if 'L_' in i:
            myItem = str(i).replace('L_','R_')
        mySel_listR.append(myItem)
    del l_pinkyFinger_list [:]
    del r_pinkyFinger_list [:]
    l_pinkyFinger_list.extend(mySel_list)
    r_pinkyFinger_list.extend(mySel_listR)
    print (l_pinkyFinger_list)
    print (r_pinkyFinger_list)

#___________update base joint prefix____________#
def prefix_update(name):
    textInput = mc.textFieldGrp(skel_pre_var, q=True, text=True)
    del skel_pre_var_list [:]
    skel_pre_var_list.append(textInput)
    print(textInput)

#####______________print test_______________######
def print_test(items):
    for i in range(0,1):
        print("add test variable here")
        #print(l_pinkyFinger_list)
        


#_____________________________________#
#_____________UI______________________#
#_____________________________________#

if mc.window("riggerWindow", ex=True):
    mc.deleteUI("riggerWindow", window=True)

mc.window("riggerWindow", t="Nate Lollar: Auto Rigger!", rtf=True, s=True, menuBar=True, bgc = (0.2,0,0.2))

#layout Begin___
#main layout creation
form = mc.formLayout()
layout = mc.columnLayout(bgc=(0.1,0,0.1))
#to create border around edge
mc.formLayout(form, edit=True, attachForm=[(layout, 'top', 10),(layout, 'bottom', 10),(layout, 'left', 10),(layout, 'right', 10)])

#'Auto Rigger!'
mc.rowLayout( numberOfColumns=1)
mc.text(label = 'Auto Rigger!', height=30, width=450, align='center', bgc=(0.4,.5,0), font='boldLabelFont', statusBarMessage='Auto Rigger')
mc.setParent("..")

# (instructions) 'Prefix via Typing (Press "Add")'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Prefix via Typing (Press "Add")', height=19, width=450, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")


#'(Current) Prefix'  (Update Prefix Button, type in text)
mc.rowLayout(numberOfColumns = 4)
mc.separator(style='none', w=115)
mc.text(label='(Current) Prefix', font='boldLabelFont')
skel_pre_var = mc.textFieldGrp(width=100, editable = True, text=skel_pre_var_list[0])
mc.button(label='Add', command = prefix_update, bgc=(0.5,0,0))
mc.setParent('..')



#'Replace Joint with Selection'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Replace Joint with Selection', height=17, width=450, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#(instructions)  ' *Left will be mirrored to Right automatically'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' *Left will be mirrored to Right automatically', height=19, width=450, align='left', font='boldLabelFont')
mc.setParent("..")

#l_hip jnt, spine 1, l clavicle
mc.rowLayout(numberOfColumns=6)
mc.button(label='l_hip', command = l_hip_selection, width=50, bgc=(0.5,0,0))
mc.textField('l_hip_text', width=100, text=l_hip_var_list[0])
mc.button(label='spine1', width=50, command = spine1_selection, bgc=(0.5,0,0))
mc.textField('spine1_text', width=100, text=spine1_var_list[0])
mc.button(label='l_clavicle', width=50, command = l_clavicle_selection, bgc=(0.5,0,0))
mc.textField('l_clavicle_text', width=100, text=l_clavicle_var_list[0])
mc.setParent("..")

#l_knee jnt, spine 2, l shoulder
mc.rowLayout(numberOfColumns = 6)
mc.button(label='l_knee', command = l_knee_selection, width=50, bgc=(0.5,0,0))
mc.textField('l_knee_text', width=100, text=l_knee_var_list[0])
mc.button(label='spine2', width=50, command = spine2_selection, bgc=(0.5,0,0))
mc.textField('spine2_text', width=100, text=spine2_var_list[0])
mc.button(label='l_shlder', width=50, command=l_shoulder_selection, bgc=(0.5,0,0))
mc.textField('l_shoulder_text', width=100, text=l_upperArm1_var_list[0])
mc.setParent('..')

#l_ankle jnt, spine 3, l elbow
mc.rowLayout(numberOfColumns = 6)
mc.button(label='l_ankle', command = l_ankle_selection, width=50, bgc=(0.5,0,0))
mc.textField('l_ankle_text', width=100, text=l_ankle_var_list[0])
mc.button(label='spine3', width=50, command = spine3_selection, bgc=(0.5,0,0))
mc.textField('spine3_text', width=100, text=spine3_var_list[0])
mc.button(label='l_elbow', width=50, command=l_elbow_selection,  bgc=(0.5,0,0))
mc.textField('l_elbow_text', width=100, text=l_foreArm1_var_list[0])
mc.setParent('..')

#l_toe jnt, spin 4, twist1
mc.rowLayout(numberOfColumns = 6)
mc.button(label='l_toe', command = l_toe_selection, width=50, bgc=(0.5,0,0))
mc.textField('l_toe_text', width=100, text=l_toe_var_list[0])
mc.button(label='spine4', width=50, command = spine4_selection, bgc=(0.5,0,0))
mc.textField('spine4_text', width=100, text=spine4_var_list[0])
mc.button(label='l_twist1', width=50, command=l_twist1_selection, bgc=(0.5,0,.25))
mc.textField('l_twist1_text', width=100, text=l_foreArm2_var_list[0])
mc.setParent('..')

#spine 5, twist2
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='spine5', width=50, command = spine5_selection,  bgc=(0.5,0,0))
mc.textField('spine5_text', width=100, text=spine5_var_list[0])
mc.button(label='l_twist2', width=50, command=l_twist2_selection, bgc=(0.5,0,.25))
mc.textField('l_twist2_text', width=100, text=l_foreArm3_var_list[0])
mc.setParent('..')

#spine 6, twist3
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='spine6', width=50, command = spine6_selection, bgc=(0.5,0,0))
mc.textField('spine6_text', width=100, text=spine6_var_list[0])
mc.button(label='l_twist3', width=50, command=l_twist3_selection, bgc=(0.5,0,.25))
mc.textField('l_twist3_text', width=100, text=l_foreArm4_var_list[0])
mc.setParent('..')

#neck1, l wrist
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='neck1', width=50, command = neck1_selection, bgc=(0.5,0,.25))
mc.textField('neck1_text', width=100, text=neck1_var_list[0])
mc.button(label='l_wrist', width=50, command=l_wrist_selection, bgc=(0.5,0,0))
mc.textField('l_wrist_text', width=100, text=l_foreArm5_var_list[0])
mc.setParent('..')

# neck 2
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='neck2', width=50, command = neck2_selection, bgc=(0.5,0,.25))
mc.textField('neck2_text', width=100, text=neck2_var_list[0])
mc.setParent('..')

# neck 3
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='neck3', width=50, command = neck3_selection, bgc=(0.5,0,.25))
mc.textField('neck3_text', width=100, text=neck3_var_list[0])
mc.setParent('..')

# neck 4
mc.rowLayout(numberOfColumns = 6)
mc.separator(style='none', w=152)
mc.button(label='neck4', width=50, command = neck4_selection, bgc=(0.5,0,.25))
mc.textField('neck4_text', width=100, text=neck4_var_list[0])
mc.setParent('..')


#____FINGER ctrls______#
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Replace Joints with Selection (Fingers)', height=17, width=450, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#thumb
mc.rowLayout(numberOfColumns = 6)
mc.button(label='L Thumb Joints', command = l_thumb_selection, width=150, bgc=(0.4,0,0))
mc.textFieldGrp('l_thumb_text', width=300, text=str(l_thumb_list))
mc.setParent("..")

#pointerFinger
mc.rowLayout(numberOfColumns = 6)
mc.button(label='L Pointer Finger Joints', command = l_pointerFinger_selection, width=150, bgc=(0,0.1,0.4))
mc.textFieldGrp('l_pointerFinger_text', width=300, text=str(l_pointerFinger_list))
mc.setParent("..")

#middleFinger
mc.rowLayout(numberOfColumns = 6)
mc.button(label='L Middle Finger Joints', command = l_middleFinger_selection, width=150, bgc=(0.4,0,0))
mc.textFieldGrp('l_middleFinger_text', width=300, text=str(l_middleFinger_list))
mc.setParent("..")

#ringFinger
mc.rowLayout(numberOfColumns = 6)
mc.button(label='L Ring Finger Joints', command = l_ringFinger_selection, width=150, bgc=(0,0.1,0.4))
mc.textFieldGrp('l_ringFinger_text', width=300, text=str(l_ringFinger_list))
mc.setParent("..")

#pinkyFinger
mc.rowLayout(numberOfColumns = 6)
mc.button(label='L Pinky Finger Joints', command = l_pinkyFinger_selection, width=150, bgc=(0.4,0,0))
mc.textFieldGrp('l_pinkyFinger_text', width=300, text=str(l_pinkyFinger_list))
mc.setParent("..")

#____Face ctrls______#
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Replace Joints With Selection (Face)', height=17, width=450, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#(instructions)  ' *Top (to head), Mid (between head & jaw), Bot (to jaw)'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' *Top (to head), Mid (between head & jaw), Bot (to jaw)', height=19, width=450, align='left', font='boldLabelFont')
mc.setParent("..")

#_____topFace_____#
mc.rowLayout(numberOfColumns = 6)
mc.button(label='Top Face Joints', command = topFace_selection, width=150, bgc=(0.49,0.49,0))
mc.textFieldGrp('topFace_text', width=300, text=str(topFaceJnt_var_list))
mc.setParent("..")
#_____midFace_____#
mc.rowLayout(numberOfColumns = 6)
mc.button(label='Mid Face Joints', command = midFace_selection, width=150, bgc=(0.1,0.1,0.45))
mc.textFieldGrp('midFace_text', width=300, text=str(midFaceJnt_var_list))
mc.setParent("..")
#_____botFace_____#
mc.rowLayout(numberOfColumns = 6)
mc.button(label='Bot Face Joints', command = botFace_selection, width=150, bgc=(0.1,0.4,0))
mc.textFieldGrp('botFace_text', width=300, text=str(botFaceJnt_var_list))
mc.setParent("..")

#_____lEar_____#
mc.rowLayout(numberOfColumns = 6)
mc.button(label="L Ear Joint/s", command = lEar_selection, width=150, bgc=(0.4,0,.4))
mc.textFieldGrp('lEar_text', width=300, text=str(lEarJnt_var_list))
mc.setParent("..")
#_____jaw_____#
mc.rowLayout(numberOfColumns = 6)
mc.button(label='Jaw Jnt', command = jaw_selection, width=150, bgc=(0.1,0.4,0))
mc.textField('jaw_text', width=300, text=jaw_var_list[0])
mc.setParent("..")

#'Reverse Foot Ctrl Locations'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Reverse Foot Ctrl Locations (If Needed)', height=17, width=450, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

mc.rowLayout(numberOfColumns = 6)
mc.button(label='Create Rev Foot Locators', command = reverseFoot_loc, width=152, bgc=(0.5,0.1,0))
mc.text(label = ' *Align to ankle, toe, toeEnd, heel, and feet sides', font='boldLabelFont')
mc.setParent("..")

#(instructions) 'Click to Build Rig'
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Click to Build Rig', height=19, width=450, align='center', font='boldLabelFont', bgc=(0.2,0,.4))
mc.setParent("..")

# FINAL BUTTON (Build Rig Button)
mc.rowLayout(numberOfColumns = 2)
mc.separator(style='none', w=174)
mc.button(label='"Execute" RIG ALL', h=30, command = 'auto_rig_all()', bgc = (.25,.5,0))
mc.setParent('..')

#Show UI Window
mc.showWindow()


#___________________________#
#_______Variables___________#
#___________________________#


#_______skeletal prefix___________#

skel_pre_betterName = str(skel_pre_var_list[0])

#___________main variable prefixs______________#

fkSkelPrefix = 'fkJnt_'

ikSkelPrefix = 'ikJnt_'

fkCtrlPrefix = 'fkCtrl_'

ikFootCtrlPrefix = 'ikFootCtrl_'

pvCurvePrefix = 'pvCtrl_'

reverseFootCtrlPrefix = 'ftCtrl_'

trans_blendColorsPrefix = 'trans_blndClr_'

rot_BlendColorsPrefix = 'rot_blndClr_'

scale_BlendColorsPrefix = 'scale_blndClr_'

twistSkelPrefix = 'twistJnt_'

trans_blendColorsPrefix = 'trans_blndClr_'

rot_BlendColorsPrefix = 'rot_blndClr_'

scale_BlendColorsPrefix = 'scale_blndClr_'

#___________________________________________________________________________________#
#_____________________________Spine_Neck_Face Variables_____________________________#
#___________________________________________________________________________________#

spine_var_list = [  spine1_var_list, 
                    spine2_var_list, 
                    spine3_var_list, 
                    spine4_var_list, 
                    spine5_var_list, 
                    spine6_var_list]

neck_var_list = [   neck1_var_list, 
                    neck2_var_list, 
                    neck3_var_list, 
                    neck4_var_list]

#_Spine Neck variables (better names)_#

spine1_var_list_betterName = str(spine1_var_list[0])
spine2_var_list_betterName = str(spine2_var_list[0])
spine3_var_list_betterName = str(spine3_var_list[0])
spine4_var_list_betterName = str(spine4_var_list[0])
spine5_var_list_betterName = str(spine5_var_list[0])
spine6_var_list_betterName = str(spine6_var_list[0])

neck1_var_list_betterName = str(neck1_var_list[0])
neck2_var_list_betterName = str(neck2_var_list[0])
neck3_var_list_betterName = str(neck3_var_list[0])
neck4_var_list_betterName = str(neck4_var_list[0])


#_____________________________Face/ Head Variables_____________________________#

#______Prefixes_____#
faceCtrl_prefix = 'faceCtrl_'
botFaceCtrl_prefix = 'botFaceCtrl_'
midFaceCtrl_prefix = 'midFaceCtrl_'
earCtrl_prefix = 'earCtrl_'

#_____Face/ Head Jnts List______#

jawJnt_var_list = [jaw_var_list]

#_________________________________________________________________________#
#_____________________________L Leg Variables_____________________________#
#_________________________________________________________________________#

#_____leg joint list_____#

l_leg_var_list = [l_hip_var_list, l_knee_var_list, l_ankle_var_list, l_toe_var_list]

r_leg_var_list = [r_hip_var_list, r_knee_var_list, r_ankle_var_list, r_toe_var_list]

#_L Leg IK variables (better names)_#
#****Currently these better names do not queue input****# (Since they are pre input action???)
#l
l_hip_var_betterName = str(l_hip_var_list[0])
l_knee_var_betterName = str(l_knee_var_list[0])
l_ankle_var_betterName = str(l_ankle_var_list[0])
l_toe_var_betterName = str(l_toe_var_list[0])
#r
r_hip_var_betterName = str(r_hip_var_list[0])
r_knee_var_betterName = str(r_knee_var_list[0])
r_ankle_var_betterName = str(r_ankle_var_list[0])
r_toe_var_betterName = str(r_toe_var_list[0])

#_ik jnt better names_#
#l
ik_l_leg_hip = l_hip_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_l_leg_knee = l_knee_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_l_leg_ankle = l_ankle_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_l_leg_toes = l_toe_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)
#r
ik_r_leg_hip = r_hip_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_r_leg_knee = r_knee_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_r_leg_ankle = r_ankle_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

ik_r_leg_toes = r_toe_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

#____leg IK ctrl variables_____#
#l
ikFootCtrl_l = l_ankle_var_betterName.replace(skel_pre_betterName, ikFootCtrlPrefix)

pvCtrl_l_leg = l_knee_var_betterName.replace(skel_pre_betterName, pvCurvePrefix)

pvCtrl_l_leg_grp = pvCtrl_l_leg + '_grp'
#r
ikFootCtrl_r = r_ankle_var_betterName.replace(skel_pre_betterName, ikFootCtrlPrefix)

pvCtrl_r_leg = r_knee_var_betterName.replace(skel_pre_betterName, pvCurvePrefix)

pvCtrl_r_leg_grp = pvCtrl_r_leg + '_grp'

#______other misc l leg variables________#
#l
switchCtrl_l_leg = 'switchCtrl_l_leg'

switchCtrl_l_leg_grp = 'switchCtrl_l_leg_grp'

ikHandkle_l_leg = 'ikHandkle_l_leg'

ikFootCtrl_l_foot1_grp = l_ankle_var_betterName.replace(skel_pre_betterName, ikFootCtrlPrefix) + '_grp'

fkJnt_l_hip =  l_hip_var_betterName.replace(skel_pre_betterName, fkSkelPrefix)

fkCtrl_l_hip_grp = l_hip_var_betterName.replace(skel_pre_betterName, fkCtrlPrefix) + '_grp'

ikJnt_l_hip = l_hip_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)
#r
switchCtrl_r_leg = 'switchCtrl_r_leg'

switchCtrl_r_leg_grp = 'switchCtrl_r_leg_grp'

ikHandkle_r_leg = 'ikHandkle_r_leg'

ikFootCtrl_r_foot1_grp = r_ankle_var_betterName.replace(skel_pre_betterName, ikFootCtrlPrefix) + '_grp'

fkJnt_r_hip =  r_hip_var_betterName.replace(skel_pre_betterName, fkSkelPrefix)

fkCtrl_r_hip_grp = r_hip_var_betterName.replace(skel_pre_betterName, fkCtrlPrefix) + '_grp'

ikJnt_r_hip = r_hip_var_betterName.replace(skel_pre_betterName, ikSkelPrefix)

#______reverse foot ctrls_______#
#l
ftCtrl_l_foot_ankle = reverseFootCtrlPrefix + 'l_foot_ankle'

ftCtrl_l_foot_toe =  reverseFootCtrlPrefix + 'l_foot_toe'

ftCtrl_l_foot_toe_end =  reverseFootCtrlPrefix + 'l_foot_toe_end'

ftCtrl_l_foot_heel =  reverseFootCtrlPrefix + 'l_foot_heel'

ftCtrl_l_foot_outer =  reverseFootCtrlPrefix + 'l_foot_outer'

ftCtrl_l_foot_inner =  reverseFootCtrlPrefix + 'l_foot_inner'

ftCtrl_l_foot_inner_grp =  reverseFootCtrlPrefix + 'l_foot_inner_grp'

ftCtrl_l_foot_toe_toeWiggle =  reverseFootCtrlPrefix + 'l_foot_toe_toeWiggle'
#r
ftCtrl_r_foot_ankle = reverseFootCtrlPrefix + 'r_foot_ankle'

ftCtrl_r_foot_toe =  reverseFootCtrlPrefix + 'r_foot_toe'

ftCtrl_r_foot_toe_end =  reverseFootCtrlPrefix + 'r_foot_toe_end'

ftCtrl_r_foot_heel =  reverseFootCtrlPrefix + 'r_foot_heel'

ftCtrl_r_foot_outer =  reverseFootCtrlPrefix + 'r_foot_outer'

ftCtrl_r_foot_inner =  reverseFootCtrlPrefix + 'r_foot_inner'

ftCtrl_r_foot_inner_grp =  reverseFootCtrlPrefix + 'r_foot_inner_grp'

ftCtrl_r_foot_toe_toeWiggle =  reverseFootCtrlPrefix + 'r_foot_toe_toeWiggle'


#___l reverse foot locator variables____________________#
#l_
loc_l_foot_ankle = 'loc_l_foot_ankle'

loc_l_foot_toe = 'loc_l_foot_toe'

loc_l_foot_toe_end = 'loc_l_foot_toe_end'

loc_l_foot_heel = 'loc_l_foot_heel'

loc_l_foot_outer = 'loc_l_foot_outer'

loc_l_foot_inner = 'loc_l_foot_inner'
#r_
loc_r_foot_ankle = 'loc_r_foot_ankle'

loc_r_foot_toe = 'loc_r_foot_toe'

loc_r_foot_toe_end = 'loc_r_foot_toe_end'

loc_r_foot_heel = 'loc_r_foot_heel'

loc_r_foot_outer = 'loc_r_foot_outer'

loc_r_foot_inner = 'loc_r_foot_inner'


#_____other lists_______#
#reverse foot loc list
#l
loc_l_foot_list = [ loc_l_foot_ankle, 
                    loc_l_foot_toe, 
                    loc_l_foot_toe_end, 
                    loc_l_foot_heel, 
                    loc_l_foot_outer, 
                    loc_l_foot_inner]
#r
loc_r_foot_list = [ loc_r_foot_ankle, 
                    loc_r_foot_toe, 
                    loc_r_foot_toe_end, 
                    loc_r_foot_heel, 
                    loc_r_foot_outer, 
                    loc_r_foot_inner]


#_______________________________________________________________________#
#_____________________________Arm Variables_____________________________#
#_______________________________________________________________________#
#l
l_arm_var_list = [l_upperArm1_var_list, l_foreArm1_var_list, l_foreArm5_var_list]

l_arm_twist_var_list = [l_foreArm1_var_list, l_foreArm2_var_list, l_foreArm3_var_list, l_foreArm4_var_list, l_foreArm5_var_list]

#r
r_arm_var_list = [r_upperArm1_var_list, r_foreArm1_var_list, r_foreArm5_var_list]

r_arm_twist_var_list = [r_foreArm1_var_list, r_foreArm2_var_list, r_foreArm3_var_list, r_foreArm4_var_list, r_foreArm5_var_list]



##################################################################
##################################################################
##################################################################

#_________________________AUTO RIG START_________________________#

def auto_rig_all():
    
    #_____________________________________________________________________________#
    #_____________________________________________________________________________#
    #_____________________________@mkg Spine_Neck_Face_____________________________#
    #_____________________________________________________________________________#
    #_____________________________________________________________________________#


    #create SPINE ctrls_______________________
    spine_ctrl_list = []
    spine_ctrl_grp_list = []

    for items in spine_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items_betterName.replace(prefix_betterName, fkCtrlPrefix)
        circleCurve = mc.circle(n=(itemsName), ch=False, r=3, nr=(1,0,0))
        #curve size
        mc.setAttr(".scaleX", 7)
        mc.setAttr(".scaleY", 6)
        mc.setAttr(".scaleZ", 7)
        #freeze transforms
        mc.makeIdentity(apply=True)

        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        #rename curve
        myCurve = items_betterName.replace(prefix_betterName, fkCtrlPrefix)

        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the ctrls
        spine_ctrl_list.append(myCurve)
        #create a list of the grps
        spine_ctrl_grp_list.append(myGroup)

    #parent ctrl grps together
    mc.parent(spine_ctrl_grp_list[1], spine_ctrl_list[0])
    mc.parent(spine_ctrl_grp_list[2], spine_ctrl_list[1])
    mc.parent(spine_ctrl_grp_list[3], spine_ctrl_list[2])
    mc.parent(spine_ctrl_grp_list[4], spine_ctrl_list[3])
    mc.parent(spine_ctrl_grp_list[5], spine_ctrl_list[4])

    #parent constrain ctrls to jnts
    mc.parentConstraint(spine_ctrl_list[0], spine_var_list[0])
    mc.parentConstraint(spine_ctrl_list[1], spine_var_list[1])
    mc.parentConstraint(spine_ctrl_list[2], spine_var_list[2])
    mc.parentConstraint(spine_ctrl_list[3], spine_var_list[3])
    mc.parentConstraint(spine_ctrl_list[4], spine_var_list[4])
    mc.parentConstraint(spine_ctrl_list[5], spine_var_list[5])

    #__________create Root Spine0 jnt for leg Blend Color Offset_________#
    #____________________________________________________________________#
    spine1_colorBlendJnt = []
    for i in spine_var_list[0]:
        myJoint = mc.joint()
        mc.Unparent(myJoint)
        myJoint = mc.rename(myJoint, (i + '_blendOffset'))
        #size and color
        mc.setAttr(".radius", 4)
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        mc.parentConstraint(i, myJoint)
        spine1_colorBlendJnt.append(myJoint)
        

    #create NECK ctrls_______________________
    neck_ctrl_list = []
    neck_ctrl_grp_list = []

    for items in neck_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items_betterName.replace(prefix_betterName, fkCtrlPrefix)
        circleCurve = mc.circle(n=(itemsName), ch=False, r=2, nr=(1,0,0))
        #curve size
        mc.setAttr(".scaleX", 7)
        mc.setAttr(".scaleY", 7)
        mc.setAttr(".scaleZ", 7)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        print(itemsShape[0])

        #color curve box's shape red
        mc.setAttr((itemsShape[0] + '.overrideEnabled'), 1)
        mc.setAttr((itemsShape[0] + '.overrideRGBColors'), 1)
        mc.setAttr((itemsShape[0] + '.overrideColorR'), 1)
        mc.setAttr((itemsShape[0] + '.overrideColorG'), 0)
        mc.setAttr((itemsShape[0] + '.overrideColorB'), 0)

        #rename curve
        myCurve = items_betterName.replace(prefix_betterName, fkCtrlPrefix)

        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the ctrls
        neck_ctrl_list.append(myCurve)
        #create a list of the grps
        neck_ctrl_grp_list.append(myGroup)

    #parent ctrl grps together
    mc.parent(neck_ctrl_grp_list[1], neck_ctrl_list[0])
    mc.parent(neck_ctrl_grp_list[2], neck_ctrl_list[1])
    mc.parent(neck_ctrl_grp_list[3], neck_ctrl_list[2])

    #parent constrain ctrls to jnts
    mc.parentConstraint(neck_ctrl_list[0], neck_var_list[0])
    mc.parentConstraint(neck_ctrl_list[1], neck_var_list[1])
    mc.parentConstraint(neck_ctrl_list[2], neck_var_list[2])
    mc.parentConstraint(neck_ctrl_list[3], neck_var_list[3])

    #parent NECK to CHEST___________________
    mc.parent(neck_ctrl_grp_list[0], spine_ctrl_list[5])
    

    ######################################################################
    ######################################################################
    ######################################################################
    #___________________________face/ head ctrls_________________________#
    ######################################################################
    ######################################################################
    ######################################################################


    #______________________________________________
    #create JAW ctrl_______________________________
    #______________________________________________

    jawCtrl_list = []
    jawCtrl_grp_list = []

    for items in jawJnt_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items_betterName.replace(prefix_betterName, faceCtrl_prefix)
        circleCurve = mc.circle(n=(itemsName), ch=False, r=7.7, nr=(1,0,0))
        #curve size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", -15)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 0.8)
        mc.setAttr(".scaleZ", 1)
        #curve visual thickness
        mc.setAttr(".lineWidth", 2)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        #rename curve
        myCurve = items_betterName.replace(prefix_betterName, faceCtrl_prefix)

        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items_betterName, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(myCurve, items)

        #create a list for the ctrls and grps
        jawCtrl_list.append(myCurve)
        jawCtrl_grp_list.append(myGroup)

    mc.parent(jawCtrl_grp_list[0], neck_ctrl_list[3])


    #______________________________________________
    #________ create topFace ctrls_________________________
    #______________________________________________

    topFaceCtrl_list = []
    topFaceCtrl_grp_list = []

    for items in topFaceJnt_var_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items.replace(prefix_betterName, faceCtrl_prefix)
        circleCurve = mc.sphere(n=(itemsName), ch=False, r=0.4,)
        #curve size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", 0)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 1)
        mc.setAttr(".scaleZ", 1)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        #rename curve
        mySphere = items.replace(prefix_betterName, faceCtrl_prefix)

        #group curve
        curveGrouped = mc.group(mySphere)
        curveGrouped_offset = mc.group(mySphere)
        #rename group
        myGroup = mc.rename(curveGrouped, (mySphere + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (mySphere + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(mySphere, items)

        #create a list for the ctrls and grps
        topFaceCtrl_list.append(mySphere)
        topFaceCtrl_grp_list.append(myGroup)


    #creat blinn
    topFaceCtrl_mat = mc.shadingNode('blinn', asShader=True, n=(faceCtrl_prefix + '_mat'))
    mc.setAttr((topFaceCtrl_mat + '.color'), 1.0, 1.0, 0, type='double3')

    for items in topFaceCtrl_list:
        mc.select(items)
        mc.hyperShade(assign = topFaceCtrl_mat)
    
    #parent to head ctrl (neck4)
    mc.parent(topFaceCtrl_grp_list, neck_ctrl_list[3])
    
    #______________________________________________
    #create bot face ctrls_________________________
    #______________________________________________
    botFaceCtrl_list = []
    botFaceCtrl_grp_list = []

    for items in botFaceJnt_var_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items.replace(prefix_betterName, faceCtrl_prefix)
        circleCurve = mc.sphere(n=(itemsName), ch=False, r=0.4,)
        #curve size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", 0)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 1)
        mc.setAttr(".scaleZ", 1)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        #rename curve
        mySphere = items.replace(prefix_betterName, faceCtrl_prefix)

        #group curve
        curveGrouped = mc.group(mySphere)
        curveGrouped_offset = mc.group(mySphere)
        #rename group
        myGroup = mc.rename(curveGrouped, (mySphere + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (mySphere + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(mySphere, items)

        #create a list for the ctrls and grps
        botFaceCtrl_list.append(mySphere)
        botFaceCtrl_grp_list.append(myGroup)


    #creat blinn
    botFaceCtrl_mat = mc.shadingNode('blinn', asShader=True, n=(botFaceCtrl_prefix + '_mat'))
    mc.setAttr((botFaceCtrl_mat + '.color'), 0, 1.0, 0, type='double3')

    #assign blinn
    for items in botFaceCtrl_list:
        mc.select(items)
        mc.hyperShade(assign = botFaceCtrl_mat)

    #parent to jaw ctrl
    mc.parent(botFaceCtrl_grp_list, jawCtrl_list[0])


    #______________________________________________
    #create mid face ctrls_________________________
    #______________________________________________
    midFaceCtrl_list = []
    midFaceCtrl_grp_list = []

    for items in midFaceJnt_var_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve
        itemsName = items.replace(prefix_betterName, faceCtrl_prefix)
        circleCurve = mc.sphere(n=(itemsName), ch=False, r=0.4,)
        #curve size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", 0)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 1)
        mc.setAttr(".scaleZ", 1)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)

        #rename curve
        mySphere = items.replace(prefix_betterName, faceCtrl_prefix)

        #group curve
        curveGrouped = mc.group(mySphere)
        curveGrouped_offset = mc.group(mySphere)
        #rename group
        myGroup = mc.rename(curveGrouped, (mySphere + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (mySphere + '_grp_offset'))

        #parent and zero curveGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(mySphere, items)

        #create a list for the ctrls and grps
        midFaceCtrl_list.append(mySphere)
        midFaceCtrl_grp_list.append(myGroup)


    #creat blinn
    midFaceCtrl_mat = mc.shadingNode('blinn', asShader=True, n=(midFaceCtrl_prefix + '_mat'))
    mc.setAttr((midFaceCtrl_mat + '.color'), 0, 0, 1.0, type='double3')
    #assign blinn to nurbSpheres
    for items in midFaceCtrl_list:
        mc.select(items)
        mc.hyperShade(assign = midFaceCtrl_mat)

    #create grp
    midFaceCtrl_grp_offset = mc.group(name=midFaceCtrl_prefix+'offset_grp', empty=True, parent=neck_ctrl_list[3], relative=True)
    midFaceCtrl_grp = mc.group(midFaceCtrl_grp_offset, name=midFaceCtrl_prefix+'grp')
    mc.Unparent(midFaceCtrl_grp)
    mc.makeIdentity(midFaceCtrl_grp, r=True)

    #parent mid ctrls under new grp
    mc.parent(midFaceCtrl_grp_list, midFaceCtrl_grp_offset)

    #parent constrain mid ctrls to head(neck4) and jaw, to be attracted to both, in the middle
    mc.parentConstraint(neck_ctrl_list[3], midFaceCtrl_grp, mo=True)
    mc.parentConstraint(jawCtrl_list[0], midFaceCtrl_grp, mo=True)

    #______________________________________________
    #create l ear ctrls____________________________
    #______________________________________________
    lEarCtrl_list = []
    lEarCtrl_grp_list = []

    for items in lEarJnt_var_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create sphere
        itemsName = items.replace(prefix_betterName, faceCtrl_prefix)
        nurbsSphere = mc.sphere(n=(itemsName), ch=False, r=0.6,)
        #sphere size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", 0)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 1)
        mc.setAttr(".scaleZ", 1)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select sphere's shape
        itemsShape = mc.listRelatives(s=True)
        #color sphere box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)

        #rename sphere
        mySphere = items.replace(prefix_betterName, faceCtrl_prefix)

        #group sphere
        curveGrouped = mc.group(mySphere)
        curveGrouped_offset = mc.group(mySphere)
        #rename group
        myGroup = mc.rename(curveGrouped, (mySphere + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (mySphere + '_grp_offset'))

        #parent and zero sphereGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(mySphere, items)

        #create a list for the ctrls and grps
        lEarCtrl_list.append(mySphere)
        lEarCtrl_grp_list.append(myGroup)


    #creat blinn
    earCtrl_mat = mc.shadingNode('blinn', asShader=True, n=(earCtrl_prefix + '_mat'))
    mc.setAttr((earCtrl_mat + '.color'), 1.0, 0, 1.0, type='double3')

    for items in lEarCtrl_list:
        mc.select(items)
        mc.hyperShade(assign = earCtrl_mat)

    #parent l ear ctls together
    if len(lEarCtrl_grp_list) > 1:
        mc.parent(lEarCtrl_grp_list[1], lEarCtrl_list[0])

    #parent to head ctrl (neck4)
    mc.parent(lEarCtrl_grp_list[0], neck_ctrl_list[3])

    #______________________________________________
    #create r ear ctrls____________________________
    #______________________________________________

    rEarCtrl_list = []
    rEarCtrl_grp_list = []

    for items in rEarJnt_var_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create sphere
        itemsName = items.replace(prefix_betterName, faceCtrl_prefix)
        nurbsSphere = mc.sphere(n=(itemsName), ch=False, r=0.6,)
        #sphere size
        mc.setAttr(".rotateX", 0)
        mc.setAttr(".rotateY", 0)
        mc.setAttr(".rotateZ", 90)
        mc.setAttr(".scaleX", 1)
        mc.setAttr(".scaleY", 1)
        mc.setAttr(".scaleZ", 1)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select sphere's shape
        itemsShape = mc.listRelatives(s=True)
        #color sphere box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)

        #rename sphere
        mySphere = items.replace(prefix_betterName, faceCtrl_prefix)

        #group sphere
        curveGrouped = mc.group(mySphere)
        curveGrouped_offset = mc.group(mySphere)
        #rename group
        myGroup = mc.rename(curveGrouped, (mySphere + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (mySphere + '_grp_offset'))

        #parent and zero sphereGrp to spine
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        mc.parentConstraint(mySphere, items)

        #create a list for the ctrls and grps
        rEarCtrl_list.append(mySphere)
        rEarCtrl_grp_list.append(myGroup)


    #assign ear blinn created with l ear
    for items in rEarCtrl_list:
        mc.select(items)
        mc.hyperShade(assign = earCtrl_mat)

    #parent r ear ctls together
    if len(rEarCtrl_grp_list) > 1:
        mc.parent(rEarCtrl_grp_list[1], rEarCtrl_list[0])

    #parent to head ctrl (neck4)
    mc.parent(rEarCtrl_grp_list[0], neck_ctrl_list[3])


    
    ###############################################################################
    #_____________________________________________________________________________#
    #_________________________________@mkg L Leg__________________________________#
    #_____________________________________________________________________________#
    ###############################################################################

    #_____________________________________________________________________________#
    #_________________________________L FK Leg____________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left leg fk list
    l_leg_fk_list = []

    for items in l_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        
        #create fk joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 2)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        
        newName = items_betterName.replace(prefix_betterName, fkSkelPrefix)
        
        myJnt = mc.rename(newName)
        
        #parent and zero joints to l_leg_list
        mc.parent(myJnt, items_betterName, relative=True)
        
        #parent joints to world space
        mc.Unparent(myJnt)
        l_leg_fk_list.append(myJnt)


    #reparent fk leg together
    mc.parent(l_leg_fk_list[1], l_leg_fk_list[0])
    mc.parent(l_leg_fk_list[2], l_leg_fk_list[1])
    mc.parent(l_leg_fk_list[3], l_leg_fk_list[2])

    #__________________________________________________________________#
    #_parent joint to original root spine0 to offset blend Color nodes_#
    #__________________________________________________________________#
    mc.parent(l_leg_fk_list[0], spine1_colorBlendJnt[0])

    #_____________CTRLS_________________#

    #create empty ctrl grp list to append too
    l_leg_fk_ctrl_list = []
    l_leg_fk_ctrl_grp_list = []

    #create box curves at l fk joints
    for items in l_leg_fk_list:
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 4)
        mc.setAttr(".scaleY", 4)
        mc.setAttr(".scaleZ", 4)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = items.replace(fkSkelPrefix, fkCtrlPrefix)
        
        myCurve = mc.rename(curveName_prefixChange)

        
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the groups (for parenting to one another)
        l_leg_fk_ctrl_grp_list.append(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_leg_fk_ctrl_list.append(myCurve)


    #parent ctrl grps together
    mc.parent(l_leg_fk_ctrl_grp_list[1], l_leg_fk_ctrl_list[0])
    mc.parent(l_leg_fk_ctrl_grp_list[2], l_leg_fk_ctrl_list[1])
    mc.parent(l_leg_fk_ctrl_grp_list[3], l_leg_fk_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_leg_fk_ctrl_list[0], l_leg_fk_list[0])
    mc.parentConstraint(l_leg_fk_ctrl_list[1], l_leg_fk_list[1])
    mc.parentConstraint(l_leg_fk_ctrl_list[2], l_leg_fk_list[2])
    mc.parentConstraint(l_leg_fk_ctrl_list[3], l_leg_fk_list[3])


    #_____________________________________________________________________________#
    #_________________________________L IK Leg____________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left leg fk list
    l_leg_ik_list = []

    for items in l_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 0)
        mc.setAttr(".overrideColorG", 1)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, ikSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to l_leg_list
        mc.parent(myJnt, items_betterName, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        l_leg_ik_list.append(myJnt)


    #reparent ik leg together
    mc.parent(l_leg_ik_list[1], l_leg_ik_list[0])
    mc.parent(l_leg_ik_list[2], l_leg_ik_list[1])
    mc.parent(l_leg_ik_list[3], l_leg_ik_list[2])

    #__________________________________________________________________#
    #_parent joint to original root spine0 to offset blend Color nodes_#
    #__________________________________________________________________#
    mc.parent(l_leg_ik_list[0], spine1_colorBlendJnt[0])

    #_____________________________________________________________________________#
    #_________________________________L Leg Blend (Colors)________________________#
    #_____________________________________________________________________________#

    #list for blend color nodes
    blendColorsNode_trans_list = []
    blendColorsNode_rot_list = []
    blendColorsNode_scale_list = []

    #create blend nodes based on base joints (trans, rot, scale/ blend nodes for each jnt)
    for items in l_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #created blend colors node, then named it after joint
        blendColorsNode_trans = mc.createNode('blendColors')
        blendColorsNode_trans = items_betterName.replace(prefix_betterName, trans_blendColorsPrefix)
        blendColorsNode_trans = mc.rename(blendColorsNode_trans)

        blendColorsNode_rot = mc.createNode('blendColors')
        blendColorsNode_rot = items_betterName.replace(prefix_betterName, rot_BlendColorsPrefix)
        blendColorsNode_rot = mc.rename(blendColorsNode_rot)

        blendColorsNode_scale = mc.createNode('blendColors')
        blendColorsNode_scale = items_betterName.replace(prefix_betterName, scale_BlendColorsPrefix)
        blendColorsNode_scale = mc.rename(blendColorsNode_scale)

        #connected blend colors trans node to translation value of base joints
        mc.connectAttr((blendColorsNode_trans + ".output"), (items_betterName + ".translate"), f=True)

        #connected blend colors trans node to rotation value of base joints
        mc.connectAttr((blendColorsNode_rot + ".output"), (items_betterName + ".rotate"), f=True)

        #connected blend colors trans node to rotation value of base joints
        mc.connectAttr((blendColorsNode_scale + ".output"), (items_betterName + ".scale"), f=True)

        #create/add blend color nodes to a list
        blendColorsNode_trans_list.append(blendColorsNode_trans)
        blendColorsNode_rot_list.append(blendColorsNode_rot)
        blendColorsNode_scale_list.append(blendColorsNode_scale)



    for items_fk, items_ik, items_blClr_trans, items_blClr_rot, items_blClr_scale in itertools.izip(    l_leg_fk_list,
                                                                                                        l_leg_ik_list, 
                                                                                                        blendColorsNode_trans_list, 
                                                                                                        blendColorsNode_rot_list, 
                                                                                                        blendColorsNode_scale_list):
        mc.connectAttr((items_fk + ".translate"), (items_blClr_trans + ".color1"), f=True)

        mc.connectAttr((items_fk + ".rotate"), (items_blClr_rot + ".color1"), f=True)

        mc.connectAttr((items_fk + ".scale"), (items_blClr_scale + ".color1"), f=True)


        mc.connectAttr((items_ik + ".translate"), (items_blClr_trans + ".color2"), f=True)

        mc.connectAttr((items_ik + ".rotate"), (items_blClr_rot + ".color2"), f=True)

        mc.connectAttr((items_ik + ".scale"), (items_blClr_scale + ".color2"), f=True)


    #_____________________________________________________________________________#
    #____________________________L Leg Switch Ctrl________________________________#
    #_____________________________________________________________________________#

    #name circle curves
    switchCurveA_l_name = 'switchCtrl_l_leg'
    switchCurveB_l_name = 'switchCtrl_l_leg0'
    switchCurveC_l_name = 'switchCtrl_l_leg1'

    #create nurbs circle
    switchCurveA_l = mc.circle(n=switchCurveA_l_name, ch=False, r=3, nr=(0,1,0))
    #create variable for nurbs circle shape
    switchCurveA_l_shape = mc.listRelatives(switchCurveA_l, s=True)
    #color nurbs circle shape
    mc.setAttr((switchCurveA_l_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveA_l_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveA_l_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveA_l_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveA_l_shape[0] + ".overrideColorB"), 1)

    #create 2nd nurbs circle
    switchCurveB_l = mc.circle(n=switchCurveB_l_name, ch=False, r=3, nr=(0,0,0))
    #create variable for 2nd nurbs circle shape
    switchCurveB_l_shape = mc.listRelatives(switchCurveB_l, s=True)
    #color 2nd nurbs circle shape
    mc.setAttr((switchCurveB_l_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveB_l_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveB_l_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveB_l_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveB_l_shape[0] + ".overrideColorB"), 1)
    #parent 2nd nurbs circle shape to first nurbs circle
    mc.parent(switchCurveB_l_shape, switchCurveA_l, r=True, shape=True)
    #delete 2nd nurbs circle transform
    mc.delete(switchCurveB_l)

    #create 3rd nurbs circle
    switchCurveC_l = mc.circle(n=switchCurveC_l_name, ch=False, r=3, nr=(1,0,0))
    #create variable for 3rd nurbs circle shape
    switchCurveC_l_shape = mc.listRelatives(switchCurveC_l, s=True)
    #color 3rd nurbs circle shape
    mc.setAttr((switchCurveC_l_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveC_l_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveC_l_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveC_l_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveC_l_shape[0] + ".overrideColorB"), 1)
    #parent 3rd nurbs circle shape to first nurbs circle
    mc.parent(switchCurveC_l_shape, switchCurveA_l, r=True, shape=True)
    #delete 3rd nurbs circle transform
    mc.delete(switchCurveC_l)

    #_______group switch ctrl_______#
    switchCurveA_l_grp = mc.group(switchCurveA_l, n = (switchCurveA_l_name + '_grp'))
    switchCurveA_l_grp_offset = mc.group(switchCurveA_l, n = (switchCurveA_l_name + '_grp_offset'))

    #_______move ctrl shapes in -z_______#
    mc.setAttr((switchCurveA_l[0] + ".translateZ"), -15)
    mc.xform (switchCurveA_l, ws=True, piv= (0, 0, 0))
    mc.makeIdentity(switchCurveA_l, apply=True)

    #_______move joint to ankle and parent_______#

    #parent and zero joints to l_leg_list
    mc.parent(switchCurveA_l_grp, l_ankle_var_list[0], relative=True)
    #parent joints to world space
    mc.Unparent(switchCurveA_l_grp)
    #zero switch ctrl grp rotation
    mc.setAttr((switchCurveA_l_grp + ".rotateX"), 0)
    mc.setAttr((switchCurveA_l_grp + ".rotateY"), 0)
    mc.setAttr((switchCurveA_l_grp + ".rotateZ"), 0)

    # parent constrain switch ctrl to ankle
    mc.parentConstraint(l_ankle_var_list[0], switchCurveA_l_grp, mo=True)



    #_______add IK FK Blend attr to switch ctrl_______#

    mc.addAttr(switchCurveA_l, ln = "fk_ik_blend", min=0, max=1, k=True)

    #lock and hide unneeded attributes for switch ctrl

    mc.setAttr((switchCurveA_l[0] + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.rz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.sx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.sy'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_l[0] + '.sz'), lock=True, keyable=False, channelBox=False)

    #_______connet Blend Color nodes to switch ctrl "Blend Attr"______#

    for items_trans, items_rot, items_scale in itertools.izip(  blendColorsNode_trans_list, 
                                                                blendColorsNode_rot_list, 
                                                                blendColorsNode_scale_list):
        mc.connectAttr((switchCurveA_l[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switchCurveA_l[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)
        mc.connectAttr((switchCurveA_l[0] + '.fk_ik_blend'), (items_scale + '.blender'), f=True)


    #_____________________________________________________________________________#
    #____________________________Build IK Leg Ctrls and Functions_________________#
    #_____________________________________________________________________________#

    #___________create l leg IK HANDLE____________#

    l_leg_ikHandle = mc.ikHandle(n='ikHandkle_l_leg', sj=ik_l_leg_hip, ee=ik_l_leg_ankle)

    mc.setAttr((l_leg_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((l_leg_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((l_leg_ikHandle[0] + '.poleVectorZ'), 0)

    l_leg_ikHandle_effector = mc.listConnections(l_leg_ikHandle, s=True, type='ikEffector')

    mc.rename(l_leg_ikHandle_effector, 'effector_l_leg')


    #___________create l leg ik handle CTRL____________#

    #create curve box
    for items in range(0,1):
        print(l_ankle_var_list[0])
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
        mc.setAttr((myCurve + ".scaleX"), 5)
        mc.setAttr((myCurve + ".scaleY"), 5)
        mc.setAttr((myCurve + ".scaleZ"), 5)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 0.1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename(ikFootCtrl_l)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, l_ankle_var_list[0], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #zero ik ctrl rotations
        mc.setAttr((myGroup + ".rotateX"), 0)
        mc.setAttr((myGroup + ".rotateY"), 0)
        mc.setAttr((myGroup + ".rotateZ"), 0)


    #_________________POLE VECTOR Start___________________#
    #_____________________________________________________#
    for items in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0, 5, -5), 
                                    (-5, 0, -5), 
                                    (0, -5, -5),
                                    (5, 0, -5),
                                    (0, 5, -5), 
                                    (0, 0, 5), 
                                    (5, 0, -5), 
                                    (0, -5, -5), 
                                    (0, 0, 5), 
                                    (-5, 0, -5), 
                                    ])
        #curve size
        mc.setAttr((myCurve + ".scaleX"), 0.7)
        mc.setAttr((myCurve + ".scaleY"), 0.7)
        mc.setAttr((myCurve + ".scaleZ"), 0.7)
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
        #rename curve
        myCurve = mc.rename(pvCtrl_l_leg)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            

        #___more accurate mid point (for "hip_to_ankle_scaled")___
        #add leg lengths together
        lKnee_plus_lAnkle_len = (mc.getAttr(ik_l_leg_knee + '.translateX') + mc.getAttr(ik_l_leg_ankle + '.translateX'))
        #length of hip
        lKnee_len = mc.getAttr(ik_l_leg_knee + '.translateX')
        #divide sum of leg lengths by hip length (for more accurate mid point)
        better_midPoint_var = (lKnee_plus_lAnkle_len / lKnee_len)

        #__vector math____#

        #vector positions of hip, knee, ankle
        hip_pos = om.MVector(mc.xform(ik_l_leg_hip, q=True, rp=True, ws=True))
        knee_pos = om.MVector(mc.xform(ik_l_leg_knee, q=True, rp=True, ws=True))
        ankle_pos = om.MVector(mc.xform(ik_l_leg_ankle, q=True, rp=True, ws=True))

        #finding vector point of pv knee (on plane of hip, knee, ankle)
        hip_to_ankle = ankle_pos - hip_pos
        hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
        mid_point = hip_pos + hip_to_ankle_scaled
        mid_point_to_knee_vec = knee_pos - mid_point
        mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 8
        mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

        #final polve vector point (to avoid knee changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, l_leg_ikHandle[0])


    #_________________Reverse Foot Rig___________________#
    #____________________________________________________#

    l_ftCtrl_list = []
    l_ftCtrl_grp_list = []

    for items in loc_l_foot_list:
        
        #name circle curves
        locCurveA_l_name = items.replace('loc_', reverseFootCtrlPrefix)
        locCurveB_l_name = items.replace('loc_', reverseFootCtrlPrefix) + '0'
        locCurveC_l_name = items.replace('loc_', reverseFootCtrlPrefix) + '1'

        #create nurbs circle
        locCurveA_l = mc.circle(n=locCurveA_l_name, ch=False, r=4, nr=(0,1,0))
        #create variable for nurbs circle shape
        locCurveA_l_shape = mc.listRelatives(locCurveA_l, s=True)
        #color nurbs circle shape
        mc.setAttr((locCurveA_l_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveA_l_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveA_l_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveA_l_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveA_l_shape[0] + ".overrideColorB"), 0)

        #create 2nd nurbs circle
        locCurveB_l = mc.circle(n=locCurveB_l_name, ch=False, r=4, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        locCurveB_l_shape = mc.listRelatives(locCurveB_l, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((locCurveB_l_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveB_l_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveB_l_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveB_l_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveB_l_shape[0] + ".overrideColorB"), 0)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(locCurveB_l_shape, locCurveA_l, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(locCurveB_l)

        #create 3rd nurbs circle
        locCurveC_l = mc.circle(n=locCurveC_l_name, ch=False, r=4, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        locCurveC_l_shape = mc.listRelatives(locCurveC_l, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((locCurveC_l_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveC_l_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveC_l_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveC_l_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveC_l_shape[0] + ".overrideColorB"), 0)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(locCurveC_l_shape, locCurveA_l, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(locCurveC_l)

        #_______group ctrl_______#
        locCurveA_l_grp = mc.group(locCurveA_l, n = (locCurveA_l_name + '_grp'))
        locCurveA_l_grp_offset = mc.group(locCurveA_l, n = (locCurveA_l_name + '_grp_offset'))


        #_______move ctrl grp to loc_______#

        #parent and zero joints to l_leg_list
        mc.parent(locCurveA_l_grp, items, relative=True)
        #parent joints to world space
        mc.Unparent(locCurveA_l_grp)
        #add/ create list for ftCtrl's
        l_ftCtrl_list.append(locCurveA_l)
        l_ftCtrl_grp_list.append(locCurveA_l_grp)

    #group reverse foot ctrls together
    mc.parent(l_ftCtrl_grp_list[4], l_ftCtrl_list[5])
    mc.parent(l_ftCtrl_grp_list[3], l_ftCtrl_list[4])
    mc.parent(l_ftCtrl_grp_list[2], l_ftCtrl_list[3])
    mc.parent(l_ftCtrl_grp_list[1], l_ftCtrl_list[2])
    mc.parent(l_ftCtrl_grp_list[0], l_ftCtrl_list[1])
    #group reverse foot ctrls under ankle ctrl
    mc.parent(ftCtrl_l_foot_inner_grp, ikFootCtrl_l)

    # create extra toe offset ctrl_______
    for items in range(0,1):
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
        mc.setAttr((myCurve + ".scaleX"), 4.5)
        mc.setAttr((myCurve + ".scaleY"), 3)
        mc.setAttr((myCurve + ".scaleZ"), 6)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 0)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 1)
        #rename curve
        myCurve = loc_l_foot_toe.replace('loc_', reverseFootCtrlPrefix)
        myCurve = mc.rename(myCurve + '_toeWiggle')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp
        mc.parent(myGroup, ftCtrl_l_foot_toe, relative=True)
        #unparent after getting position
        mc.Unparent(myGroup)
        #reparent to toe_end
        mc.parent(myGroup, ftCtrl_l_foot_toe_end, relative=False)


    #___________reverse foot joint parenting___________#

    #parent reverse foot ankle ctrl to ikHandle trans and ankle joint rotate
    mc.parentConstraint(ftCtrl_l_foot_ankle, l_leg_ikHandle[0], mo=True, sr=('x', 'y', 'z'))
    mc.parentConstraint(ftCtrl_l_foot_ankle, ik_l_leg_ankle, mo=True, st=('x', 'y', 'z'))
    #parent toe
    mc.parentConstraint(ftCtrl_l_foot_toe_toeWiggle, ik_l_leg_toes, mo=True)

    #___________________________________________#
    #____l leg cleanup____ visibility, etc______#
    #___________________________________________#

    #hide ankle ctrl (not needed)
    mc.setAttr((ftCtrl_l_foot_ankle + '_grp' + '.visibility'), 0)
    #set driven key to hide ctrls for blend
    mc.setAttr((switchCtrl_l_leg + '.fk_ik_blend'), 0)
    mc.setAttr((ikFootCtrl_l_foot1_grp + '.visibility'), 1)
    mc.setAttr((pvCtrl_l_leg_grp + '.visibility'), 1)
    mc.setAttr((fkCtrl_l_hip_grp + '.visibility'), 0)
    mc.setDrivenKeyframe((ikFootCtrl_l_foot1_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((pvCtrl_l_leg_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((fkCtrl_l_hip_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
    mc.setAttr((switchCtrl_l_leg + '.fk_ik_blend'), 1)
    mc.setAttr((ikFootCtrl_l_foot1_grp + '.visibility'), 0)
    mc.setAttr((pvCtrl_l_leg_grp + '.visibility'), 0)
    mc.setAttr((fkCtrl_l_hip_grp + '.visibility'), 1)
    mc.setDrivenKeyframe((ikFootCtrl_l_foot1_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((pvCtrl_l_leg_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((fkCtrl_l_hip_grp + '.visibility'), currentDriver = (switchCtrl_l_leg + '.fk_ik_blend'))



    ###############################################################################
    #_____________________________________________________________________________#
    #_________________________________@mkg R Leg__________________________________#
    #_____________________________________________________________________________#
    ###############################################################################

    #_____________________________________________________________________________#
    #_________________________________ R FK Leg___________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left leg fk list
    r_leg_fk_list = []

    for items in r_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        
        #create fk joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 2)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        
        newName = items_betterName.replace(prefix_betterName, fkSkelPrefix)
        
        myJnt = mc.rename(newName)
        
        #parent and zero joints to r_leg_list
        mc.parent(myJnt, items_betterName, relative=True)
        
        #parent joints to world space
        mc.Unparent(myJnt)
        r_leg_fk_list.append(myJnt)


    #reparent fk leg together
    mc.parent(r_leg_fk_list[1], r_leg_fk_list[0])
    mc.parent(r_leg_fk_list[2], r_leg_fk_list[1])
    mc.parent(r_leg_fk_list[3], r_leg_fk_list[2])

    #__________________________________________________________________#
    #_parent joint to original root spine0 to offset blend Color nodes_#
    #__________________________________________________________________#
    mc.parent(r_leg_fk_list[0], spine1_colorBlendJnt[0])

    #_____________CTRLS_________________#

    #create empty ctrl grp list to append too
    r_leg_fk_ctrl_list = []
    r_leg_fk_ctrl_grp_list = []

    #create box curves at l fk joints
    for items in r_leg_fk_list:
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 4)
        mc.setAttr(".scaleY", 4)
        mc.setAttr(".scaleZ", 4)
        #freeze transforms
        mc.makeIdentity(apply=True)
        
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)

        
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = items.replace(fkSkelPrefix, fkCtrlPrefix)
        
        myCurve = mc.rename(curveName_prefixChange)

        
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the groups (for parenting to one another)
        r_leg_fk_ctrl_grp_list.append(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_leg_fk_ctrl_list.append(myCurve)


    #parent ctrl grps together
    mc.parent(r_leg_fk_ctrl_grp_list[1], r_leg_fk_ctrl_list[0])
    mc.parent(r_leg_fk_ctrl_grp_list[2], r_leg_fk_ctrl_list[1])
    mc.parent(r_leg_fk_ctrl_grp_list[3], r_leg_fk_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_leg_fk_ctrl_list[0], r_leg_fk_list[0])
    mc.parentConstraint(r_leg_fk_ctrl_list[1], r_leg_fk_list[1])
    mc.parentConstraint(r_leg_fk_ctrl_list[2], r_leg_fk_list[2])
    mc.parentConstraint(r_leg_fk_ctrl_list[3], r_leg_fk_list[3])


    #_____________________________________________________________________________#
    #_________________________________R IK Leg____________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left leg fk list
    r_leg_ik_list = []

    for items in r_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 0)
        mc.setAttr(".overrideColorG", 1)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, ikSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to r_leg_list
        mc.parent(myJnt, items_betterName, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        r_leg_ik_list.append(myJnt)


    #reparent ik leg together
    mc.parent(r_leg_ik_list[1], r_leg_ik_list[0])
    mc.parent(r_leg_ik_list[2], r_leg_ik_list[1])
    mc.parent(r_leg_ik_list[3], r_leg_ik_list[2])

    #____________________#
    #_parent joint to orig spine0 to offset blend color node_#
    #____________________#
    mc.parent(r_leg_ik_list[0], spine1_colorBlendJnt[0])

    #_____________________________________________________________________________#
    #_________________________________R Leg Blend (Colors)________________________#
    #_____________________________________________________________________________#

    #list for blend color nodes
    blendColorsNode_trans_list = []
    blendColorsNode_rot_list = []
    blendColorsNode_scale_list = []

    #create blend nodes based on base joints (trans, rot, scale/ blend nodes for each jnt)
    for items in r_leg_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #created blend colors node, then named it after joint
        blendColorsNode_trans = mc.createNode('blendColors')
        blendColorsNode_trans = items_betterName.replace(prefix_betterName, trans_blendColorsPrefix)
        blendColorsNode_trans = mc.rename(blendColorsNode_trans)

        blendColorsNode_rot = mc.createNode('blendColors')
        blendColorsNode_rot = items_betterName.replace(prefix_betterName, rot_BlendColorsPrefix)
        blendColorsNode_rot = mc.rename(blendColorsNode_rot)

        blendColorsNode_scale = mc.createNode('blendColors')
        blendColorsNode_scale = items_betterName.replace(prefix_betterName, scale_BlendColorsPrefix)
        blendColorsNode_scale = mc.rename(blendColorsNode_scale)

        #connected blend colors trans node to translation value of base joints
        mc.connectAttr((blendColorsNode_trans + ".output"), (items_betterName + ".translate"), f=True)

        #connected blend colors trans node to rotation value of base joints
        mc.connectAttr((blendColorsNode_rot + ".output"), (items_betterName + ".rotate"), f=True)

        #connected blend colors trans node to rotation value of base joints
        mc.connectAttr((blendColorsNode_scale + ".output"), (items_betterName + ".scale"), f=True)

        #create/add blend color nodes to a list
        blendColorsNode_trans_list.append(blendColorsNode_trans)
        blendColorsNode_rot_list.append(blendColorsNode_rot)
        blendColorsNode_scale_list.append(blendColorsNode_scale)



    for items_fk, items_ik, items_blClr_trans, items_blClr_rot, items_blClr_scale in itertools.izip(    r_leg_fk_list,
                                                                                                        r_leg_ik_list, 
                                                                                                        blendColorsNode_trans_list, 
                                                                                                        blendColorsNode_rot_list, 
                                                                                                        blendColorsNode_scale_list):
        mc.connectAttr((items_fk + ".translate"), (items_blClr_trans + ".color1"), f=True)

        mc.connectAttr((items_fk + ".rotate"), (items_blClr_rot + ".color1"), f=True)

        mc.connectAttr((items_fk + ".scale"), (items_blClr_scale + ".color1"), f=True)


        mc.connectAttr((items_ik + ".translate"), (items_blClr_trans + ".color2"), f=True)

        mc.connectAttr((items_ik + ".rotate"), (items_blClr_rot + ".color2"), f=True)

        mc.connectAttr((items_ik + ".scale"), (items_blClr_scale + ".color2"), f=True)


    #_____________________________________________________________________________#
    #____________________________R Leg Switch Ctrl________________________________#
    #_____________________________________________________________________________#

    #name circle curves
    switchCurveA_r_name = 'switchCtrl_r_leg'
    switchCurveB_r_name = 'switchCtrl_r_leg0'
    switchCurveC_r_name = 'switchCtrl_r_leg1'

    #create nurbs circle
    switchCurveA_r = mc.circle(n=switchCurveA_r_name, ch=False, r=3, nr=(0,1,0))
    #create variable for nurbs circle shape
    switchCurveA_r_shape = mc.listRelatives(switchCurveA_r, s=True)
    #color nurbs circle shape
    mc.setAttr((switchCurveA_r_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveA_r_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveA_r_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveA_r_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveA_r_shape[0] + ".overrideColorB"), 1)

    #create 2nd nurbs circle
    switchCurveB_r = mc.circle(n=switchCurveB_r_name, ch=False, r=3, nr=(0,0,0))
    #create variable for 2nd nurbs circle shape
    switchCurveB_r_shape = mc.listRelatives(switchCurveB_r, s=True)
    #color 2nd nurbs circle shape
    mc.setAttr((switchCurveB_r_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveB_r_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveB_r_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveB_r_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveB_r_shape[0] + ".overrideColorB"), 1)
    #parent 2nd nurbs circle shape to first nurbs circle
    mc.parent(switchCurveB_r_shape, switchCurveA_r, r=True, shape=True)
    #delete 2nd nurbs circle transform
    mc.delete(switchCurveB_r)

    #create 3rd nurbs circle
    switchCurveC_r = mc.circle(n=switchCurveC_r_name, ch=False, r=3, nr=(1,0,0))
    #create variable for 3rd nurbs circle shape
    switchCurveC_r_shape = mc.listRelatives(switchCurveC_r, s=True)
    #color 3rd nurbs circle shape
    mc.setAttr((switchCurveC_r_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((switchCurveC_r_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((switchCurveC_r_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((switchCurveC_r_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((switchCurveC_r_shape[0] + ".overrideColorB"), 1)
    #parent 3rd nurbs circle shape to first nurbs circle
    mc.parent(switchCurveC_r_shape, switchCurveA_r, r=True, shape=True)
    #delete 3rd nurbs circle transform
    mc.delete(switchCurveC_r)

    #_______group switch ctrl_______#
    switchCurveA_r_grp = mc.group(switchCurveA_r, n = (switchCurveA_r_name + '_grp'))
    switchCurveA_r_grp_offset = mc.group(switchCurveA_r, n = (switchCurveA_r_name + '_grp_offset'))

    #_______move ctrl shapes in -z_______#
    mc.setAttr((switchCurveA_r[0] + ".translateZ"), -15)
    mc.xform (switchCurveA_r, ws=True, piv= (0, 0, 0))
    mc.makeIdentity(switchCurveA_r, apply=True)

    #_______move joint to ankle and parent_______#

    #parent and zero joints to r_leg_list
    mc.parent(switchCurveA_r_grp, r_ankle_var_list[0], relative=True)
    #parent joints to world space
    mc.Unparent(switchCurveA_r_grp)
    #zero switch ctrl grp rotation
    mc.setAttr((switchCurveA_r_grp + ".rotateX"), 0)
    mc.setAttr((switchCurveA_r_grp + ".rotateY"), 0)
    mc.setAttr((switchCurveA_r_grp + ".rotateZ"), 0)

    # parent constrain switch ctrl to ankle
    mc.parentConstraint(r_ankle_var_list[0], switchCurveA_r_grp, mo=True)



    #_______add IK FK Blend attr to switch ctrl_______#

    mc.addAttr(switchCurveA_r, ln = "fk_ik_blend", min=0, max=1, k=True)

    #lock and hide unneeded attributes for switch ctrl

    mc.setAttr((switchCurveA_r[0] + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.rz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.sx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.sy'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((switchCurveA_r[0] + '.sz'), lock=True, keyable=False, channelBox=False)

    #_______connet Blend Color nodes to switch ctrl "Blend Attr"______#

    for items_trans, items_rot, items_scale in itertools.izip(  blendColorsNode_trans_list, 
                                                                blendColorsNode_rot_list, 
                                                                blendColorsNode_scale_list):
        mc.connectAttr((switchCurveA_r[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switchCurveA_r[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)
        mc.connectAttr((switchCurveA_r[0] + '.fk_ik_blend'), (items_scale + '.blender'), f=True)

    
    #_____________________________________________________________________________#
    #____________________________Build IK Leg Ctrls and Functions_________________#
    #_____________________________________________________________________________#

    #___________create l leg IK HANDLE____________#

    r_leg_ikHandle = mc.ikHandle(n='ikHandkle_r_leg', sj=ik_r_leg_hip, ee=ik_r_leg_ankle)

    mc.setAttr((r_leg_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((r_leg_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((r_leg_ikHandle[0] + '.poleVectorZ'), 0)

    r_leg_ikHandle_effector = mc.listConnections(r_leg_ikHandle, s=True, type='ikEffector')

    mc.rename(r_leg_ikHandle_effector, 'effector_r_leg')


    #___________create R leg ik handle CTRL____________#

    #create curve box
    for items in range(0,1):
        print(r_ankle_var_list[0])
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
        mc.setAttr((myCurve + ".scaleX"), 5)
        mc.setAttr((myCurve + ".scaleY"), 5)
        mc.setAttr((myCurve + ".scaleZ"), 5)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 0.1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename(ikFootCtrl_r)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, r_ankle_var_list[0], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #zero ik ctrl rotations
        mc.setAttr((myGroup + ".rotateX"), 0)
        mc.setAttr((myGroup + ".rotateY"), 0)
        mc.setAttr((myGroup + ".rotateZ"), 0)


    #_________________POLE VECTOR Start___________________#
    #_____________________________________________________#
    for items in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0, 5, -5), 
                                    (-5, 0, -5), 
                                    (0, -5, -5),
                                    (5, 0, -5),
                                    (0, 5, -5), 
                                    (0, 0, 5), 
                                    (5, 0, -5), 
                                    (0, -5, -5), 
                                    (0, 0, 5), 
                                    (-5, 0, -5), 
                                    ])
        #curve size
        mc.setAttr((myCurve + ".scaleX"), 0.7)
        mc.setAttr((myCurve + ".scaleY"), 0.7)
        mc.setAttr((myCurve + ".scaleZ"), 0.7)
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
        #rename curve
        myCurve = mc.rename(pvCtrl_r_leg)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            

        #___more accurate mid point (for "hip_to_ankle_scaled")___
        #add leg lengths together
        lKnee_plus_lAnkle_len = (mc.getAttr(ik_r_leg_knee + '.translateX') + mc.getAttr(ik_r_leg_ankle + '.translateX'))
        #length of hip
        lKnee_len = mc.getAttr(ik_r_leg_knee + '.translateX')
        #divide sum of leg lengths by hip length (for more accurate mid point)
        better_midPoint_var = (lKnee_plus_lAnkle_len / lKnee_len)

        #__vector math____#

        #vector positions of hip, knee, ankle
        hip_pos = om.MVector(mc.xform(ik_r_leg_hip, q=True, rp=True, ws=True))
        knee_pos = om.MVector(mc.xform(ik_r_leg_knee, q=True, rp=True, ws=True))
        ankle_pos = om.MVector(mc.xform(ik_r_leg_ankle, q=True, rp=True, ws=True))

        #finding vector point of pv knee (on plane of hip, knee, ankle)
        hip_to_ankle = ankle_pos - hip_pos
        hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
        mid_point = hip_pos + hip_to_ankle_scaled
        mid_point_to_knee_vec = knee_pos - mid_point
        mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 8
        mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

        #final polve vector point (to avoid knee changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, r_leg_ikHandle[0])


    #_________________Reverse Foot Rig___________________#
    #____________________________________________________#

    r_ftCtrl_list = []
    r_ftCtrl_grp_list = []

    for items in loc_r_foot_list:
        
        #name circle curves
        locCurveA_r_name = items.replace('loc_', reverseFootCtrlPrefix)
        locCurveB_r_name = items.replace('loc_', reverseFootCtrlPrefix) + '0'
        locCurveC_r_name = items.replace('loc_', reverseFootCtrlPrefix) + '1'

        #create nurbs circle
        locCurveA_r = mc.circle(n=locCurveA_r_name, ch=False, r=4, nr=(0,1,0))
        #create variable for nurbs circle shape
        locCurveA_r_shape = mc.listRelatives(locCurveA_r, s=True)
        #color nurbs circle shape
        mc.setAttr((locCurveA_r_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveA_r_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveA_r_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveA_r_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveA_r_shape[0] + ".overrideColorB"), 0)

        #create 2nd nurbs circle
        locCurveB_r = mc.circle(n=locCurveB_r_name, ch=False, r=4, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        locCurveB_r_shape = mc.listRelatives(locCurveB_r, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((locCurveB_r_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveB_r_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveB_r_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveB_r_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveB_r_shape[0] + ".overrideColorB"), 0)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(locCurveB_r_shape, locCurveA_r, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(locCurveB_r)

        #create 3rd nurbs circle
        locCurveC_r = mc.circle(n=locCurveC_r_name, ch=False, r=4, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        locCurveC_r_shape = mc.listRelatives(locCurveC_r, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((locCurveC_r_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveC_r_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveC_r_shape[0] + ".overrideColorR"), .5)
        mc.setAttr((locCurveC_r_shape[0] + ".overrideColorG"), 1)
        mc.setAttr((locCurveC_r_shape[0] + ".overrideColorB"), 0)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(locCurveC_r_shape, locCurveA_r, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(locCurveC_r)

        #_______group ctrl_______#
        locCurveA_r_grp = mc.group(locCurveA_r, n = (locCurveA_r_name + '_grp'))
        locCurveA_r_grp_offset = mc.group(locCurveA_r, n = (locCurveA_r_name + '_grp_offset'))


        #_______move ctrl grp to loc_______#

        #parent and zero joints to r_leg_list
        mc.parent(locCurveA_r_grp, items, relative=True)
        #parent joints to world space
        mc.Unparent(locCurveA_r_grp)
        #add/ create list for ftCtrl's
        r_ftCtrl_list.append(locCurveA_r)
        r_ftCtrl_grp_list.append(locCurveA_r_grp)

    #group reverse foot ctrls together
    mc.parent(r_ftCtrl_grp_list[4], r_ftCtrl_list[5])
    mc.parent(r_ftCtrl_grp_list[3], r_ftCtrl_list[4])
    mc.parent(r_ftCtrl_grp_list[2], r_ftCtrl_list[3])
    mc.parent(r_ftCtrl_grp_list[1], r_ftCtrl_list[2])
    mc.parent(r_ftCtrl_grp_list[0], r_ftCtrl_list[1])
    #group reverse foot ctrls under ankle ctrl
    mc.parent(ftCtrl_r_foot_inner_grp, ikFootCtrl_r)

    # create extra toe offset ctrl_______
    for items in range(0,1):
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
        mc.setAttr((myCurve + ".scaleX"), 4.5)
        mc.setAttr((myCurve + ".scaleY"), 3)
        mc.setAttr((myCurve + ".scaleZ"), 6)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 0)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 1)
        #rename curve
        myCurve = loc_r_foot_toe.replace('loc_', reverseFootCtrlPrefix)
        myCurve = mc.rename(myCurve + '_toeWiggle')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp
        mc.parent(myGroup, ftCtrl_r_foot_toe, relative=True)
        #unparent after getting position
        mc.Unparent(myGroup)
        #reparent to toe_end
        mc.parent(myGroup, ftCtrl_r_foot_toe_end, relative=False)


    #___________reverse foot joint parenting___________#

    #parent reverse foot ankle ctrl to ikHandle trans and ankle joint rotate
    mc.parentConstraint(ftCtrl_r_foot_ankle, r_leg_ikHandle[0], mo=True, sr=('x', 'y', 'z'))
    mc.parentConstraint(ftCtrl_r_foot_ankle, ik_r_leg_ankle, mo=True, st=('x', 'y', 'z'))
    #parent toe
    mc.parentConstraint(ftCtrl_r_foot_toe_toeWiggle, ik_r_leg_toes, mo=True)

    #___________________________________________#
    #____R leg cleanup____ visibility, etc______#
    #___________________________________________#

    #hide ankle ctrl (not needed)
    mc.setAttr((ftCtrl_r_foot_ankle + '_grp' + '.visibility'), 0)
    #set driven key to hide ctrls for blend
    mc.setAttr((switchCtrl_r_leg + '.fk_ik_blend'), 0)
    mc.setAttr((ikFootCtrl_r_foot1_grp + '.visibility'), 1)
    mc.setAttr((pvCtrl_r_leg_grp + '.visibility'), 1)
    mc.setAttr((fkCtrl_r_hip_grp + '.visibility'), 0)
    mc.setDrivenKeyframe((ikFootCtrl_r_foot1_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((pvCtrl_r_leg_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((fkCtrl_r_hip_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))
    mc.setAttr((switchCtrl_r_leg + '.fk_ik_blend'), 1)
    mc.setAttr((ikFootCtrl_r_foot1_grp + '.visibility'), 0)
    mc.setAttr((pvCtrl_r_leg_grp + '.visibility'), 0)
    mc.setAttr((fkCtrl_r_hip_grp + '.visibility'), 1)
    mc.setDrivenKeyframe((ikFootCtrl_r_foot1_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((pvCtrl_r_leg_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))
    mc.setDrivenKeyframe((fkCtrl_r_hip_grp + '.visibility'), currentDriver = (switchCtrl_r_leg + '.fk_ik_blend'))

    
    ###############################################################################
    #_____________________________________________________________________________#
    #_____________________________Leg End_________________________________________#
    #_____________________________________________________________________________#
    ###############################################################################
    

    ###############################################################################
    #_____________________________________________________________________________#
    #_____________________________L Arm Begin_______________________________________#
    #_____________________________________________________________________________#
    ###############################################################################

    
    #__________________________________________________________#
    #_____________________@mkg L Clavicle___________________________#
    #__________________________________________________________#

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

    
    #__________________________________________________________#
    #_____________________L FK ARM_____________________________#
    #__________________________________________________________#

    #create l arm fk joints
    l_arm_fk_list = []

    for items in l_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create fk joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 2)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        
        #rename joint
        newName = items_betterName.replace(prefix_betterName, fkSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to l_arm_list
        mc.parent(myJnt, items_betterName, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        l_arm_fk_list.append(myJnt)
    
    #reparent fk arm together
    mc.parent(l_arm_fk_list[1], l_arm_fk_list[0])
    mc.parent(l_arm_fk_list[2], l_arm_fk_list[1])
    
    #____________________________________________________________#
    #_____parent fk shoulder to blend colors offset joint________#
    #____________________________________________________________#
    mc.parent(l_arm_fk_list[0], l_arm_blend_offsetJnt[0])


    #_____________l fk arm CTRLS_________________#

    #create empty ctrl grp list to append too
    l_arm_fk_ctrl_list = []
    l_arm_fk_ctrl_grp_list = []

    #create box curves at l fk joints
    for items in l_arm_fk_list:
        #create curve box
        mc.curve(d=1, p=[   (-1, 1, 1), 
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
        mc.setAttr(".scaleX", 5)
        mc.setAttr(".scaleY", 5)
        mc.setAttr(".scaleZ", 5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = items.replace(fkSkelPrefix, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)

        #_____LOCK and HIDE_ unneaded FK attributes_____#
        mc.setAttr((myCurve + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.tz'), lock=True, keyable=False, channelBox=False)

        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_arm_fk_list
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the groups (for parenting to one another)
        l_arm_fk_ctrl_grp_list.append(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_arm_fk_ctrl_list.append(myCurve)

    #parent ctrl grps together
    mc.parent(l_arm_fk_ctrl_grp_list[1], l_arm_fk_ctrl_list[0])
    mc.parent(l_arm_fk_ctrl_grp_list[2], l_arm_fk_ctrl_list[1])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_arm_fk_ctrl_list[0], l_arm_fk_list[0])
    mc.parentConstraint(l_arm_fk_ctrl_list[1], l_arm_fk_list[1])
    mc.parentConstraint(l_arm_fk_ctrl_list[2], l_arm_fk_list[2])

    #parent clavicle to fk grp top
    mc.parentConstraint(l_arm_clavicle_ctrl_list[0], l_arm_fk_ctrl_grp_list[0], mo=True, sr=('x','y','z'))


    #_____________________________________________________________________________#
    #_________________________________L IK arm____________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left arm fk list
    l_arm_ik_list = []

    for items in l_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 0)
        mc.setAttr(".overrideColorG", 1)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, ikSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to l_arm_list
        mc.parent(myJnt, items, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        l_arm_ik_list.append(myJnt)

    #reparent ik arm together
    mc.parent(l_arm_ik_list[1], l_arm_ik_list[0])
    mc.parent(l_arm_ik_list[2], l_arm_ik_list[1])

    #____________________________________________________________#
    #_____parent fk shoulder to blend colors offset joint________#
    #____________________________________________________________#
    mc.parent(l_arm_ik_list[0], l_arm_blend_offsetJnt[0])


    #_____________________________________________________________________________#
    #____________________________Build IK arm Ctrls and Functions_________________#
    #_____________________________________________________________________________#

    #___________create l arm IK HANDLE____________#

    l_arm_ikHandle = mc.ikHandle(n='ikHandkle_l_arm', sj=l_arm_ik_list[0], ee=l_arm_ik_list[2])

    mc.setAttr((l_arm_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((l_arm_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((l_arm_ikHandle[0] + '.poleVectorZ'), 0)

    l_arm_ikHandle_effector = mc.listConnections(l_arm_ikHandle, s=True, type='ikEffector')

    mc.rename(l_arm_ikHandle_effector, 'effector_l_arm')

    #___________create l arm ik handle CTRL____________#
    ikHandCtrl = []
    ikHandCtrl_grp = []

    #create curve box
    for items in range(0,1):
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
        mc.setAttr((myCurve + ".scaleX"), 5.5)
        mc.setAttr((myCurve + ".scaleY"), 5.5)
        mc.setAttr((myCurve + ".scaleZ"), 5.5)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 0.1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename('ikHandCtrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_arm_fk_list
        mc.parent(myGroup, l_arm_ik_list[2], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #parent l clavicle ik handle to ctrl
        mc.parentConstraint(myCurve, l_arm_ikHandle[0], sr=('x','y','z'))
        mc.parentConstraint(myCurve, l_arm_ik_list[2], st=('x','y','z'))
        #access ctrl outside of for loop
        ikHandCtrl.append(myCurve)
        ikHandCtrl_grp.append(myGroup)

    
    #_________________POLE VECTOR Start___________________#
    #_____________________________________________________#
    l_arm_pv_grp = []

    for items in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0, 5, -5), 
                                    (-5, 0, -5), 
                                    (0, -5, -5),
                                    (5, 0, -5),
                                    (0, 5, -5), 
                                    (0, 0, 5), 
                                    (5, 0, -5), 
                                    (0, -5, -5), 
                                    (0, 0, 5), 
                                    (-5, 0, -5), 
                                    ])
        #curve size
        mc.setAttr((myCurve + ".scaleX"), 0.7)
        mc.setAttr((myCurve + ".scaleY"), 0.7)
        mc.setAttr((myCurve + ".scaleZ"), 0.7)
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
        #rename curve
        myCurve = mc.rename('pvCtrl_l_arm')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
        
        #___more accurate mid point (for "shoulder_to_wrist_scaled")___
        #add arm lengths together
        lElbow_plus_lWrist_len = (mc.getAttr(l_arm_ik_list[1] + '.translateX') + mc.getAttr(l_arm_ik_list[2] + '.translateX'))
        #length of shoulder
        lElbow_len = mc.getAttr(l_arm_ik_list[1] + '.translateX')
        #divide sum of arm lengths by shoulder length (for more accurate mid point)
        better_midPoint_var = (lElbow_plus_lWrist_len / lElbow_len)
        
        #__vector math____#

        #vector positions of shoulder, Elbow, wrist
        shoulder_pos = om.MVector(mc.xform(l_arm_ik_list[0], q=True, rp=True, ws=True))
        elbow_pos = om.MVector(mc.xform(l_arm_ik_list[1], q=True, rp=True, ws=True))
        wrist_pos = om.MVector(mc.xform(l_arm_ik_list[2], q=True, rp=True, ws=True))

        #finding vector point of pv elbow (on plane of shoulder, elbow, wrist)
        shoulder_to_wrist = wrist_pos - shoulder_pos
        shoulder_to_wrist_scaled = shoulder_to_wrist / better_midPoint_var #/two-ish
        mid_point_l_arm = shoulder_pos + shoulder_to_wrist_scaled
        mid_point_to_elbow_vec = elbow_pos - mid_point_l_arm
        mid_point_to_elbow_vec_scaled = mid_point_to_elbow_vec * 8
        mid_point_to_elbow_point = mid_point_l_arm + mid_point_to_elbow_vec_scaled

        #final polve vector point (to avoid elbow changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_elbow_point)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, l_arm_ikHandle[0])

        #append for outside loop
        l_arm_pv_grp.append(myGroup)
        
    #parent clavicle to ik shoulder
    mc.parentConstraint(l_arm_clavicle_ctrl_list[0], l_arm_ik_list[0], mo=True, sr=('x','y','z'))
    
    #_____________________________________________________________________________#
    #____________________________@mk Twist Jnts_________________#
    #_____________________________________________________________________________#

    #_________L________#

    #_____l start twist joint_____

    #create joint at elbow
    l_arm_startTwist_jnt = mc.joint(l_arm_var_list[1], n='startTwistJnt_l_arm', rad=6)
    mc.Unparent(l_arm_startTwist_jnt)
    #color joint
    mc.setAttr(l_arm_startTwist_jnt + ".overrideEnabled", 1)
    mc.setAttr(l_arm_startTwist_jnt + ".overrideRGBColors", 1)
    mc.setAttr(l_arm_startTwist_jnt + ".overrideColorR", 1)
    mc.setAttr(l_arm_startTwist_jnt + ".overrideColorG", 1)
    mc.setAttr(l_arm_startTwist_jnt + ".overrideColorB", 0)
    #parent constrain to elbow
    mc.parentConstraint(l_arm_var_list[1], l_arm_startTwist_jnt)
    #create joint grps
    #l_arm_startTwist_jnt_grp_offset = mc.group(l_arm_startTwist_jnt, n=l_arm_startTwist_jnt+'_grp_offset')
    #l_arm_startTwist_jnt_grp = mc.group(l_arm_startTwist_jnt_grp_offset, n=l_arm_startTwist_jnt+'_grp')
    #unparent now that position and rotation are gotten
    #mc.Unparent(l_arm_startTwist_jnt)

    #_____l end twist joint_____
    #create joint at elbow
    l_arm_endTwist_jnt = mc.joint(l_arm_var_list[2], n='endTwistJnt_l_arm', rad=6)
    mc.Unparent(l_arm_endTwist_jnt)
    #color joint
    mc.setAttr(l_arm_endTwist_jnt + ".overrideEnabled", 1)
    mc.setAttr(l_arm_endTwist_jnt + ".overrideRGBColors", 1)
    mc.setAttr(l_arm_endTwist_jnt + ".overrideColorR", 1)
    mc.setAttr(l_arm_endTwist_jnt + ".overrideColorG", 1)
    mc.setAttr(l_arm_endTwist_jnt + ".overrideColorB", 0)
    #parent constrain to elbow
    mc.parentConstraint(ikHandCtrl, l_arm_fk_ctrl_list[2], l_arm_endTwist_jnt)
    #create joint grps
    #l_arm_endTwist_jnt_grp_offset = mc.group(l_arm_endTwist_jnt, n=l_arm_endTwist_jnt+'_grp_offset')
    #l_arm_endTwist_jnt_grp = mc.group(l_arm_endTwist_jnt_grp_offset, n=l_arm_endTwist_jnt+'_grp')
    #unparent now that position and rotation are gotten
    #mc.Unparent(l_arm_endTwist_jnt)

    
    #_______create l arm mid twist joints_______

    l_arm_twist_list = []

    for items in l_arm_twist_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create twist joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, twistSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to l_arm_list
        mc.parent(myJnt, items, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        l_arm_twist_list.append(myJnt)

    #reparent twist jnts together
    mc.parent(l_arm_twist_list[1], l_arm_twist_list[0])
    mc.parent(l_arm_twist_list[2], l_arm_twist_list[1])
    mc.parent(l_arm_twist_list[3], l_arm_twist_list[2])
    mc.parent(l_arm_twist_list[4], l_arm_twist_list[3])

    #_____midtwist jnt parent Const to sknJnt_____#
    mc.parentConstraint(l_arm_twist_list[1], l_arm_twist_var_list[1])
    mc.parentConstraint(l_arm_twist_list[2], l_arm_twist_var_list[2])
    mc.parentConstraint(l_arm_twist_list[3], l_arm_twist_var_list[3])

    
    #__________________create IK SPLINE for arm TWIST__________________
    #create simple curve
    l_twistStart_pos = mc.xform(l_arm_startTwist_jnt,q=1,ws=1,rp=1)
    l_twistEnd_pos = mc.xform(l_arm_endTwist_jnt,q=1,ws=1,rp=1)
    l_twistCurve = mc.curve(d=1, p=[l_twistStart_pos, l_twistEnd_pos])
    #create ik spline
    l_arm_twist_ikHandle = mc.ikHandle(n='ikHandle_l_arm_twist',sj=l_arm_twist_list[0],ee=l_arm_twist_list[4],sol='ikSplineSolver', ccv=False, c=l_twistCurve)
    #set pole vectors to 0 to be clean (probably unesaccary)
    mc.setAttr((l_arm_twist_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((l_arm_twist_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((l_arm_twist_ikHandle[0] + '.poleVectorZ'), 0)
    #rename ik spline effector and curve
    l_arm_ikHandle_effector = mc.listConnections(l_arm_twist_ikHandle, s=True, type='ikEffector')
    l_arm_ikHandle_curve = mc.listConnections(l_arm_twist_ikHandle, s=True, type='nurbsCurve')
    l_arm_ikHandle_effector_newName = mc.rename(l_arm_ikHandle_effector, 'effector_l_arm_twist')
    l_arm_ikHandle_curve_newName = mc.rename(l_arm_ikHandle_curve, 'curve_l_arm_twist')
    #set up advanced twist controls for ik spline 
    mc.setAttr(l_arm_twist_ikHandle[0] + '.dTwistControlEnable', 1)
    mc.setAttr(l_arm_twist_ikHandle[0] + '.dWorldUpType', 4)
    mc.setAttr(l_arm_twist_ikHandle[0] + '.dWorldUpAxis', 4)
    mc.setAttr(l_arm_twist_ikHandle[0] + '.dWorldUpVector', 0, 0, -1)
    mc.setAttr(l_arm_twist_ikHandle[0] + '.dWorldUpVectorEnd', 0, 0, -1)
    mc.connectAttr(l_arm_startTwist_jnt + '.worldMatrix[0]', l_arm_twist_ikHandle[0] + '.dWorldUpMatrix')
    mc.connectAttr(l_arm_endTwist_jnt + '.worldMatrix[0]', l_arm_twist_ikHandle[0] + '.dWorldUpMatrixEnd')
    #_____skin start and end joints to ik spline curve_____#
    mc.skinCluster(l_arm_startTwist_jnt, l_arm_endTwist_jnt, l_arm_ikHandle_curve_newName, n='skinCluster_l_arm_twist')
    #RENAME twist curve TWEAK node
    l_arm_ikHandle_curve_newName_shape = mc.listRelatives(l_arm_ikHandle_curve_newName, s=True)
    l_arm_twist_curve_tweak = mc.listConnections(l_arm_ikHandle_curve_newName_shape, s=True, type='tweak')
    mc.rename(l_arm_twist_curve_tweak, 'tweak_l_arm_twist')


    #_________________________________#mkp parent twist BIND jnts____________________________________________#
    #twistBind_grp = mc.group(p=l_foreArm1_var_list[0], em=True, n='twistBind_grp')
    #twistBind_grp_offset = mc.group(p=l_foreArm1_var_list[0], em=True, n='twistBind_grp_offset')
    #mc.parent(twistBind_grp_offset, twistBind_grp)
    #mc.parent(l_arm_startTwist_jnt_grp, l_arm_endTwist_jnt_grp, twistBind_grp_offset)
    
    #_____________________________________________________________________________#
    #_________________________________L arm Blend (Colors)________________________#
    #_____________________________________________________________________________#

    #list for blend color nodes
    l_arm_blendColorsNode_trans_list = []
    l_arm_blendColorsNode_rot_list = []

    #create blend nodes based on base joints (trans, rot, scale/ blend nodes for each jnt)
    for items in l_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create blend colors node, then name it after joint
        blendColorsNode_trans = mc.createNode('blendColors')
        blendColorsNode_trans = items_betterName.replace(prefix_betterName, trans_blendColorsPrefix)
        blendColorsNode_trans = mc.rename(blendColorsNode_trans)

        blendColorsNode_rot = mc.createNode('blendColors')
        blendColorsNode_rot = items_betterName.replace(prefix_betterName, rot_BlendColorsPrefix)
        blendColorsNode_rot = mc.rename(blendColorsNode_rot)

        #create/add blend color nodes to a list
        l_arm_blendColorsNode_trans_list.append(blendColorsNode_trans)
        l_arm_blendColorsNode_rot_list.append(blendColorsNode_rot)
    

    #trans____________(b/c not all output needed)
    for item in l_arm_var_list[1]:
        mc.connectAttr((l_arm_blendColorsNode_trans_list[1] + '.output'), (item + '.translate'), f=True)
    
    #rot___________(b/c not all output needed)
    for item in l_arm_var_list[0]:
        mc.connectAttr((l_arm_blendColorsNode_rot_list[0] + '.output'), (item + '.rotate'), f=True)
    for item in l_arm_var_list[1]:
        mc.connectAttr((l_arm_blendColorsNode_rot_list[1] + '.output'), (item + '.rotate'), f=True)
    
    #alternate to wrist rotate blend (b/c does not work with blend color, bleed through rotate constraint)
    l_wrist_rotateConst = mc.parentConstraint(l_arm_ik_list[2], l_arm_fk_list[2], l_arm_var_list[2], st=('x','y','z'))

    
    #connect fk and ik joint chains to blend color nodes
    for items_fk, items_ik, items_blClr_trans, items_blClr_rot in itertools.izip(    l_arm_fk_list,
                                                                                    l_arm_ik_list, 
                                                                                    l_arm_blendColorsNode_trans_list,
                                                                                    l_arm_blendColorsNode_rot_list, ):
        mc.connectAttr((items_fk + '.translate'), (items_blClr_trans + '.color1'), f=True)

        mc.connectAttr((items_fk + '.rotate'), (items_blClr_rot + '.color1'), f=True)

        mc.connectAttr((items_ik + '.translate'), (items_blClr_trans + '.color2'), f=True)

        mc.connectAttr((items_ik + '.rotate'), (items_blClr_rot + '.color2'), f=True)

    
    #_____________________________________________________________________________#
    #____________________________L arm Switch Ctrl________________________________#
    #_____________________________________________________________________________#
    l_arm_switch_ctrl = []
    l_arm_switch_ctrl_grp = []
    for i in range (0,1):
        #name circle curves
        l_ArmSwchCrvA_name = 'switchCtrl_l_arm'
        l_ArmSwchCrvB_name = 'switchCtrl_l_arm0'
        l_ArmSwchCrvC_name = 'switchCtrl_l_arm1'

        #create nurbs circle
        l_ArmSwchCrvA = mc.circle(n=l_ArmSwchCrvA_name, ch=False, r=2, nr=(0,1,0))
        #create variable for nurbs circle shape
        l_ArmSwchCrvA_shape = mc.listRelatives(l_ArmSwchCrvA, s=True)
        #color nurbs circle shape
        mc.setAttr((l_ArmSwchCrvA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((l_ArmSwchCrvA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((l_ArmSwchCrvA_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((l_ArmSwchCrvA_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((l_ArmSwchCrvA_shape[0] + ".overrideColorB"), 1)

        #create 2nd nurbs circle
        l_ArmSwchCrvB = mc.circle(n=l_ArmSwchCrvB_name, ch=False, r=2, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        l_ArmSwchCrvB_shape = mc.listRelatives(l_ArmSwchCrvB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((l_ArmSwchCrvB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((l_ArmSwchCrvB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((l_ArmSwchCrvB_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((l_ArmSwchCrvB_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((l_ArmSwchCrvB_shape[0] + ".overrideColorB"), 1)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(l_ArmSwchCrvB_shape, l_ArmSwchCrvA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(l_ArmSwchCrvB)

        #create 3rd nurbs circle
        l_ArmSwchCrvC = mc.circle(n=l_ArmSwchCrvC_name, ch=False, r=2, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        l_ArmSwchCrvC_shape = mc.listRelatives(l_ArmSwchCrvC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((l_ArmSwchCrvC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((l_ArmSwchCrvC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((l_ArmSwchCrvC_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((l_ArmSwchCrvC_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((l_ArmSwchCrvC_shape[0] + ".overrideColorB"), 1)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(l_ArmSwchCrvC_shape, l_ArmSwchCrvA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(l_ArmSwchCrvC)

        #_______group switch ctrl_______#
        l_ArmSwchCrvA_grp = mc.group(l_ArmSwchCrvA, n = (l_ArmSwchCrvA_name + '_grp'))
        l_ArmSwchCrvA_grp_offset = mc.group(l_ArmSwchCrvA, n = (l_ArmSwchCrvA_name + '_grp_offset'))
        
        #_______move ctrl shapes in -z_______#
        mc.setAttr((l_ArmSwchCrvA[0] + ".translateZ"), -20)
        mc.xform (l_ArmSwchCrvA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(l_ArmSwchCrvA, apply=True)
        
        #_______move ctrl to ankle and parent_______#

        #parent and zero ctl to l_arm_list
        mc.parent(l_ArmSwchCrvA_grp, l_foreArm5_var_list, relative=True)
        #parent ctrl to world space
        mc.Unparent(l_ArmSwchCrvA_grp)

        # parent constrain switch ctrl to wrist
        mc.parentConstraint(l_foreArm5_var_list, l_ArmSwchCrvA_grp, mo=True)

        #_______add IK FK Blend attr to switch ctrl_______#
        mc.addAttr(l_ArmSwchCrvA, ln = "fk_ik_blend", min=0, max=1, k=True)

        #lock and hide unneeded attributes for switch ctrl
        mc.setAttr((l_ArmSwchCrvA[0] + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.tz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.sx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.sy'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((l_ArmSwchCrvA[0] + '.sz'), lock=True, keyable=False, channelBox=False)
        #append list for outside loop
        l_arm_switch_ctrl.append(l_ArmSwchCrvA)
        l_arm_switch_ctrl_grp.append(l_ArmSwchCrvA_grp)
        
        
        #_______connet Blend Color nodes to switch ctrl "Blend Attr"______#
        #0=IK, 1=FK

        for items_trans, items_rot in itertools.izip(  l_arm_blendColorsNode_trans_list, 
                                                                    l_arm_blendColorsNode_rot_list, ):
            mc.connectAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
            mc.connectAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)


        #_______L Wrist X Twist Parent Constraint BLEND________#
        #_______arm twist constraint________#
        #mc.parentConstraint(ikHandCtrl[0], l_arm_fk_ctrl_list[2], l_arm_endTwist_jnt, sr=('y','z'), st=('x','y','z'))

        #IK___________
        mc.setAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)  

        mc.setAttr((l_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_l_foreArm5W1'), 0)
        mc.setAttr((l_arm_endTwist_jnt + '_parentConstraint1' + '.ikHandCtrlW0'), 1)

        mc.setDrivenKeyframe((l_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_l_foreArm5W1'), currentDriver = (l_ArmSwchCrvA[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_endTwist_jnt + '_parentConstraint1' + '.ikHandCtrlW0'), currentDriver = (l_ArmSwchCrvA[0] + '.fk_ik_blend'))
        
        #FK_________
        mc.setAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), 1)  

        mc.setAttr((l_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_l_foreArm5W1'), 1)
        mc.setAttr((l_arm_endTwist_jnt + '_parentConstraint1' + '.ikHandCtrlW0'), 0)

        mc.setDrivenKeyframe((l_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_l_foreArm5W1'), currentDriver = (l_ArmSwchCrvA[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_endTwist_jnt + '_parentConstraint1' + '.ikHandCtrlW0'), currentDriver = (l_ArmSwchCrvA[0] + '.fk_ik_blend'))


        #__________IK FK Blend Hide keys, +  Key Wrist oreint__________#
        mc.setAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)
        mc.setAttr((ikHandCtrl_grp[0] + '.visibility'), 1)
        mc.setAttr((l_arm_pv_grp[0] + '.visibility'), 1)
        mc.setAttr((l_arm_fk_ctrl_grp_list[0] + '.visibility'), 0)
        mc.setAttr(l_wrist_rotateConst[0] + '.ikJnt_l_foreArm5W0', 1)
        mc.setAttr(l_wrist_rotateConst[0] + '.fkJnt_l_foreArm5W1', 0)

        mc.setDrivenKeyframe((ikHandCtrl_grp[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_pv_grp[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_wrist_rotateConst[0] + '.ikJnt_l_foreArm5W0'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_wrist_rotateConst[0] + '.fkJnt_l_foreArm5W1'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))

        mc.setAttr((l_ArmSwchCrvA[0]  + '.fk_ik_blend'), 1)
        mc.setAttr((ikHandCtrl_grp[0] + '.visibility'), 0)
        mc.setAttr((l_arm_pv_grp[0] + '.visibility'), 0)
        mc.setAttr((l_arm_fk_ctrl_grp_list[0] + '.visibility'), 1)
        mc.setAttr(l_wrist_rotateConst[0] + '.ikJnt_l_foreArm5W0', 0)
        mc.setAttr(l_wrist_rotateConst[0] + '.fkJnt_l_foreArm5W1', 1)

        mc.setDrivenKeyframe((ikHandCtrl_grp[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_pv_grp[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_arm_fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_wrist_rotateConst[0] + '.ikJnt_l_foreArm5W0'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((l_wrist_rotateConst[0] + '.fkJnt_l_foreArm5W1'), currentDriver = (l_ArmSwchCrvA[0]  + '.fk_ik_blend'))

        
    #__________reset value to 0 for default IK__________#
    mc.setAttr((l_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)

    #___BREAK Unneaded blendColor Connections____#
    mc.delete(l_arm_blendColorsNode_trans_list[0])
    mc.delete(l_arm_blendColorsNode_trans_list[2])
    mc.delete(l_arm_blendColorsNode_rot_list[2])
    


    
    ###############################################################################
    #_____________________________________________________________________________#
    #_____________________________R Arm Begin_______________________________________#
    #_____________________________________________________________________________#
    ###############################################################################
    

    #__________________________________________________________#
    #_____________________@mkb R Clavicle___________________________#
    #__________________________________________________________#

    #create single chain ikHandle for clavicle________
    r_clavicle_ikHandle = mc.ikHandle(n='ikHandle_r_clavicle',sj=r_clavicle_var_list[0], ee=r_upperArm1_var_list[0], sol='ikSCsolver')
    
    mc.setAttr((r_clavicle_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((r_clavicle_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((r_clavicle_ikHandle[0] + '.poleVectorZ'), 0)
    #rename ik effector
    r_clavicle_ikHandle_effector = mc.listConnections(r_clavicle_ikHandle, s=True, type='ikEffector')
    mc.rename(r_clavicle_ikHandle_effector, 'effector_r_arm')
    #group ik handle
    rClvGrp = mc.group(em=True)
    rClvGrp = mc.rename(rClvGrp, r_clavicle_ikHandle[0] + '_grp')
    rClvGrp_const = mc.parentConstraint(r_clavicle_ikHandle[0], rClvGrp)
    mc.delete(rClvGrp_const)
    mc.parent(r_clavicle_ikHandle[0], rClvGrp)

    
    r_arm_clavicle_ctrl_list = []
    r_arm_clavicle_ctrl_grp_list = []
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
        mc.setAttr((myCurve + ".translateX"), -3)
        mc.setAttr((myCurve + ".translateY"), 12)
        mc.setAttr((myCurve + ".translateZ"), 0)
        mc.setAttr((myCurve + ".scaleX"), 1)
        mc.setAttr((myCurve + ".scaleY"), 1)
        mc.setAttr((myCurve + ".scaleZ"), 1)
        #pivot to world origin
        mc.xform(myCurve, piv=(3,-12,0))
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
        myCurve = mc.rename('pvCtrl_r_clavicle')
        #group curve
        curveGrouped_offset = mc.group(em=True)
        mc.parent(myCurve, curveGrouped_offset)
        curveGrouped = mc.group(em=True)
        mc.parent(curveGrouped_offset, curveGrouped)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        
        #parent constrain and delete to get position
        tempConst = mc.parentConstraint(r_upperArm1_var_list, myGroup, sr=('x','y','z'))
        mc.delete(tempConst)

        #append list for later use
        r_arm_clavicle_ctrl_list.append(myCurve)
        r_arm_clavicle_ctrl_grp_list.append(myGroup)
    
    # parent ik handle to clavicle ctrl
    mc.parentConstraint(r_arm_clavicle_ctrl_list[0], rClvGrp, sr=('x','y','z'))
    
    #_____________________L Clavicle Stretch___________________________#
    r_clavicle_var_loc = mc.spaceLocator(n=r_clavicle_var_list[0] + '_locator')
    r_upperArm1_var_loc = mc.spaceLocator(n=r_upperArm1_var_list[0] + '_locator')
    mc.pointConstraint(r_clavicle_var_list[0], r_clavicle_var_loc)
    mc.pointConstraint(r_clavicle_ikHandle[0], r_upperArm1_var_loc)
    rClv_measerTool = mc.distanceDimension(r_clavicle_var_loc, r_upperArm1_var_loc)
    rClv_measerTool_parent = mc.listRelatives(rClv_measerTool, p=True)
    rClv_measerTool_parent = mc.rename(rClv_measerTool_parent, ('distanceDimension_' + r_clavicle_var_list[0]))
    #_______
    MD_makeNegative = mc.shadingNode('multiplyDivide', asUtility=True, n='multiplyDivide_' + r_clavicle_var_list[0])
    mc.setAttr(MD_makeNegative + '.input2X', -1)
    mc.connectAttr(rClv_measerTool_parent + '.distance', MD_makeNegative + '.input1X')
    mc.connectAttr(MD_makeNegative + '.outputX', r_upperArm1_var_list[0] + '.translateX')
    #________
    rClv_measerTool_grp = mc.group(em = True, n=rClv_measerTool_parent + '_grp')
    mc.parent(rClv_measerTool_parent, r_clavicle_var_loc, r_upperArm1_var_loc, rClv_measerTool_grp)



    #__________________________________________________________#
    #_______________blendColor offset Joint____________________#
    #__________________________________________________________#
    #selection needed to be cleared (for some reason)
    mc.select(cl=True)

    r_arm_blend_offsetJnt = []
    for i in range(0,1):
        myJoint = mc.joint()
        myJoint = mc.rename(myJoint, (r_clavicle_var_list[0] + '_offset'))
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        pcA = mc.parentConstraint(r_clavicle_var_list[0], myJoint)
        mc.delete(pcA)
        mc.makeIdentity(myJoint, apply=True)
        pcB = mc.parentConstraint(r_clavicle_var_list[0], myJoint)
        r_arm_blend_offsetJnt.append(myJoint)

    
    #__________________________________________________________#
    #_____________________L FK ARM_____________________________#
    #__________________________________________________________#

    #create l arm fk joints
    r_arm_fk_list = []

    for items in r_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create fk joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 2)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        
        #rename joint
        newName = items_betterName.replace(prefix_betterName, fkSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to r_arm_list
        mc.parent(myJnt, items_betterName, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        r_arm_fk_list.append(myJnt)
    
    #reparent fk arm together
    mc.parent(r_arm_fk_list[1], r_arm_fk_list[0])
    mc.parent(r_arm_fk_list[2], r_arm_fk_list[1])
    
    #____________________________________________________________#
    #_____parent fk shoulder to blend colors offset joint________#
    #____________________________________________________________#
    mc.parent(r_arm_fk_list[0], r_arm_blend_offsetJnt[0])

    
    #_____________l fk arm CTRLS_________________#

    #create empty ctrl grp list to append too
    r_arm_fk_ctrl_list = []
    r_arm_fk_ctrl_grp_list = []

    #create box curves at l fk joints
    for items in r_arm_fk_list:
        #create curve box
        mc.curve(d=1, p=[   (-1, 1, 1), 
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
        mc.setAttr(".scaleX", 5)
        mc.setAttr(".scaleY", 5)
        mc.setAttr(".scaleZ", 5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = items.replace(fkSkelPrefix, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)

        #_____LOCK and HIDE_ unneaded FK attributes_____#
        mc.setAttr((myCurve + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((myCurve + '.tz'), lock=True, keyable=False, channelBox=False)

        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_arm_fk_list
        mc.parent(myGroup, items, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list for the groups (for parenting to one another)
        r_arm_fk_ctrl_grp_list.append(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_arm_fk_ctrl_list.append(myCurve)

    #parent ctrl grps together
    mc.parent(r_arm_fk_ctrl_grp_list[1], r_arm_fk_ctrl_list[0])
    mc.parent(r_arm_fk_ctrl_grp_list[2], r_arm_fk_ctrl_list[1])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_arm_fk_ctrl_list[0], r_arm_fk_list[0])
    mc.parentConstraint(r_arm_fk_ctrl_list[1], r_arm_fk_list[1])
    mc.parentConstraint(r_arm_fk_ctrl_list[2], r_arm_fk_list[2])

    #parent clavicle to fk grp top
    mc.parentConstraint(r_arm_clavicle_ctrl_list[0], r_arm_fk_ctrl_grp_list[0], mo=True, sr=('x','y','z'))


    #_____________________________________________________________________________#
    #_________________________________R IK arm____________________________________#
    #_____________________________________________________________________________#

    #_____________JOINTS_________________#

    #Left arm fk list
    r_arm_ik_list = []

    for items in r_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 0)
        mc.setAttr(".overrideColorG", 1)
        mc.setAttr(".overrideColorB", 0.1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, ikSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to r_arm_list
        mc.parent(myJnt, items, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        r_arm_ik_list.append(myJnt)

    #reparent ik arm together
    mc.parent(r_arm_ik_list[1], r_arm_ik_list[0])
    mc.parent(r_arm_ik_list[2], r_arm_ik_list[1])

    #____________________________________________________________#
    #_____parent fk shoulder to blend colors offset joint________#
    #____________________________________________________________#
    mc.parent(r_arm_ik_list[0], r_arm_blend_offsetJnt[0])


    #_____________________________________________________________________________#
    #____________________________Build IK arm Ctrls and Functions_________________#
    #_____________________________________________________________________________#

    #___________create R arm IK HANDLE____________#

    r_arm_ikHandle = mc.ikHandle(n='ikHandkle_r_arm', sj=r_arm_ik_list[0], ee=r_arm_ik_list[2])

    mc.setAttr((r_arm_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((r_arm_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((r_arm_ikHandle[0] + '.poleVectorZ'), 0)

    r_arm_ikHandle_effector = mc.listConnections(r_arm_ikHandle, s=True, type='ikEffector')

    mc.rename(r_arm_ikHandle_effector, 'effector_r_arm')

    #___________create l arm ik handle CTRL____________#
    r_ikHandCtrl = []
    r_ikHandCtrl_grp = []

    #create curve box
    for items in range(0,1):
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
        mc.setAttr((myCurve + ".scaleX"), 5.5)
        mc.setAttr((myCurve + ".scaleY"), 5.5)
        mc.setAttr((myCurve + ".scaleZ"), 5.5)
        #freeze transforms
        mc.makeIdentity(myCurve, apply=True)
        #select curve box's shape
        curveShape = mc.listRelatives(myCurve, s=True)
        #color curve box's shape red
        mc.setAttr((curveShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((curveShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorR"), 0.1)
        mc.setAttr((curveShape[0] + ".overrideColorG"), 1)
        mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
        #rename curve
        myCurve = mc.rename('r_ikHandCtrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_arm_fk_list
        mc.parent(myGroup, r_arm_ik_list[2], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #parent l clavicle ik handle to ctrl
        mc.parentConstraint(myCurve, r_arm_ikHandle[0], sr=('x','y','z'))
        mc.parentConstraint(myCurve, r_arm_ik_list[2], st=('x','y','z'))
        #access ctrl outside of for loop
        r_ikHandCtrl.append(myCurve)
        r_ikHandCtrl_grp.append(myGroup)

    
    #_________________POLE VECTOR Start___________________#
    #_____________________________________________________#
    r_arm_pv_grp = []

    for items in range(0,1):
        #create pyramid curve______
        myCurve = mc.curve(d=1, p=[ (0, 5, -5), 
                                    (-5, 0, -5), 
                                    (0, -5, -5),
                                    (5, 0, -5),
                                    (0, 5, -5), 
                                    (0, 0, 5), 
                                    (5, 0, -5), 
                                    (0, -5, -5), 
                                    (0, 0, 5), 
                                    (-5, 0, -5), 
                                    ])
        #curve size
        mc.setAttr((myCurve + ".scaleX"), 0.7)
        mc.setAttr((myCurve + ".scaleY"), 0.7)
        mc.setAttr((myCurve + ".scaleZ"), 0.7)
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
        #rename curve
        myCurve = mc.rename('pvCtrl_r_arm')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
            
        
        #___more accurate mid point (for "shoulder_to_wrist_scaled")___
        #add arm lengths together
        lElbow_plus_lWrist_len = (mc.getAttr(r_arm_ik_list[1] + '.translateX') + mc.getAttr(r_arm_ik_list[2] + '.translateX'))
        #length of shoulder
        lElbow_len = mc.getAttr(r_arm_ik_list[1] + '.translateX')
        #divide sum of arm lengths by shoulder length (for more accurate mid point)
        better_midPoint_var = (lElbow_plus_lWrist_len / lElbow_len)
        
        #__vector math____#

        #vector positions of shoulder, Elbow, wrist
        shoulder_pos = om.MVector(mc.xform(r_arm_ik_list[0], q=True, rp=True, ws=True))
        elbow_pos = om.MVector(mc.xform(r_arm_ik_list[1], q=True, rp=True, ws=True))
        wrist_pos = om.MVector(mc.xform(r_arm_ik_list[2], q=True, rp=True, ws=True))

        #finding vector point of pv elbow (on plane of shoulder, elbow, wrist)
        shoulder_to_wrist = wrist_pos - shoulder_pos
        shoulder_to_wrist_scaled = shoulder_to_wrist / better_midPoint_var #/two-ish
        mid_point_r_arm = shoulder_pos + shoulder_to_wrist_scaled
        mid_point_to_elbow_vec = elbow_pos - mid_point_r_arm
        mid_point_to_elbow_vec_scaled = mid_point_to_elbow_vec * 8
        mid_point_to_elbow_point = mid_point_r_arm + mid_point_to_elbow_vec_scaled

        #final polve vector point (to avoid elbow changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_elbow_point)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, r_arm_ikHandle[0])

        #append for outside loop
        r_arm_pv_grp.append(myGroup)
        
    #parent clavicle to ik shoulder
    mc.parentConstraint(r_arm_clavicle_ctrl_list[0], r_arm_ik_list[0], mo=True, sr=('x','y','z'))
    
    #_____________________________________________________________________________#
    #____________________________@mk Twist Jnts_________________#
    #_____________________________________________________________________________#

    #_________R________#

    #_____R start twist joint_____

    #create joint at elbow
    r_arm_startTwist_jnt = mc.joint(r_arm_var_list[1], n='startTwistJnt_r_arm', rad=6)
    mc.Unparent(r_arm_startTwist_jnt)
    #color joint
    mc.setAttr(r_arm_startTwist_jnt + ".overrideEnabled", 1)
    mc.setAttr(r_arm_startTwist_jnt + ".overrideRGBColors", 1)
    mc.setAttr(r_arm_startTwist_jnt + ".overrideColorR", 1)
    mc.setAttr(r_arm_startTwist_jnt + ".overrideColorG", 1)
    mc.setAttr(r_arm_startTwist_jnt + ".overrideColorB", 0)
    #parent constrain to elbow
    mc.parentConstraint(r_arm_var_list[1], r_arm_startTwist_jnt)
    #create joint grps
    #r_arm_startTwist_jnt_grp_offset = mc.group(r_arm_startTwist_jnt, n=r_arm_startTwist_jnt+'_grp_offset')
    #r_arm_startTwist_jnt_grp = mc.group(r_arm_startTwist_jnt_grp_offset, n=r_arm_startTwist_jnt+'_grp')
    #unparent now that position and rotation are gotten
    #mc.Unparent(r_arm_startTwist_jnt)

    #_____l end twist joint_____
    #create joint at elbow
    r_arm_endTwist_jnt = mc.joint(r_arm_var_list[2], n='endTwistJnt_r_arm', rad=6)
    mc.Unparent(r_arm_endTwist_jnt)
    #color joint
    mc.setAttr(r_arm_endTwist_jnt + ".overrideEnabled", 1)
    mc.setAttr(r_arm_endTwist_jnt + ".overrideRGBColors", 1)
    mc.setAttr(r_arm_endTwist_jnt + ".overrideColorR", 1)
    mc.setAttr(r_arm_endTwist_jnt + ".overrideColorG", 1)
    mc.setAttr(r_arm_endTwist_jnt + ".overrideColorB", 0)
    #parent constrain to elbow
    mc.parentConstraint(r_ikHandCtrl, r_arm_fk_ctrl_list[2], r_arm_endTwist_jnt)
    #create joint grps
    #r_arm_endTwist_jnt_grp_offset = mc.group(r_arm_endTwist_jnt, n=r_arm_endTwist_jnt+'_grp_offset')
    #r_arm_endTwist_jnt_grp = mc.group(r_arm_endTwist_jnt_grp_offset, n=r_arm_endTwist_jnt+'_grp')
    #unparent now that position and rotation are gotten
    #mc.Unparent(r_arm_endTwist_jnt)

    
    #_______create r arm mid twist joints_______

    r_arm_twist_list = []

    for items in r_arm_twist_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create twist joint
        mc.joint()
        #joint visual size
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 1)
        #rename joint
        newName = items_betterName.replace(prefix_betterName, twistSkelPrefix)
        myJnt = mc.rename(newName)
        #parent and zero joints to r_arm_list
        mc.parent(myJnt, items, relative=True)
        #parent joints to world space
        mc.Unparent(myJnt)
        r_arm_twist_list.append(myJnt)

    #reparent twist jnts together
    mc.parent(r_arm_twist_list[1], r_arm_twist_list[0])
    mc.parent(r_arm_twist_list[2], r_arm_twist_list[1])
    mc.parent(r_arm_twist_list[3], r_arm_twist_list[2])
    mc.parent(r_arm_twist_list[4], r_arm_twist_list[3])

    #_____midtwist jnt parent to sknJnt_____#
    mc.parentConstraint(r_arm_twist_list[1], r_arm_twist_var_list[1])
    mc.parentConstraint(r_arm_twist_list[2], r_arm_twist_var_list[2])
    mc.parentConstraint(r_arm_twist_list[3], r_arm_twist_var_list[3])

    
    #__________________create IK SPLINE for arm TWIST__________________
    #create simple curve
    r_twistStart_pos = mc.xform(r_arm_startTwist_jnt,q=1,ws=1,rp=1)
    r_twistEnd_pos = mc.xform(r_arm_endTwist_jnt,q=1,ws=1,rp=1)
    r_twistCurve = mc.curve(d=1, p=[r_twistStart_pos, r_twistEnd_pos])
    #create ik spline
    r_arm_twist_ikHandle = mc.ikHandle(n='ikHandle_r_arm_twist',sj=r_arm_twist_list[0],ee=r_arm_twist_list[4],sol='ikSplineSolver', ccv=False, c=r_twistCurve)
    #set pole vectors to 0 to be clean (probably unesaccary)
    mc.setAttr((r_arm_twist_ikHandle[0] + '.poleVectorX'), 0)
    mc.setAttr((r_arm_twist_ikHandle[0] + '.poleVectorY'), 0)
    mc.setAttr((r_arm_twist_ikHandle[0] + '.poleVectorZ'), 0)
    #rename ik spline effector and curve
    r_arm_ikHandle_effector = mc.listConnections(r_arm_twist_ikHandle, s=True, type='ikEffector')
    r_arm_ikHandle_curve = mc.listConnections(r_arm_twist_ikHandle, s=True, type='nurbsCurve')
    r_arm_ikHandle_effector_newName = mc.rename(r_arm_ikHandle_effector, 'effector_r_arm_twist')
    r_arm_ikHandle_curve_newName = mc.rename(r_arm_ikHandle_curve, 'curve_r_arm_twist')
    #set up advanced twist controls for ik spline 
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dTwistControlEnable', 1)
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dForwardAxis', 1)
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dWorldUpType', 4)
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dWorldUpAxis', 3)
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dWorldUpVector', 0, 0, 1)
    mc.setAttr(r_arm_twist_ikHandle[0] + '.dWorldUpVectorEnd', 0, 0, 1)
    mc.connectAttr(r_arm_startTwist_jnt + '.worldMatrix[0]', r_arm_twist_ikHandle[0] + '.dWorldUpMatrix')
    mc.connectAttr(r_arm_endTwist_jnt + '.worldMatrix[0]', r_arm_twist_ikHandle[0] + '.dWorldUpMatrixEnd')
    #_____skin start and end joints to ik spline curve_____#
    mc.skinCluster(r_arm_startTwist_jnt, r_arm_endTwist_jnt, r_arm_ikHandle_curve_newName, n='skinCluster_r_arm_twist')
    #RENAME twist curve TWEAK node
    r_arm_ikHandle_curve_newName_shape = mc.listRelatives(r_arm_ikHandle_curve_newName, s=True)
    r_arm_twist_curve_tweak = mc.listConnections(r_arm_ikHandle_curve_newName_shape, s=True, type='tweak')
    mc.rename(r_arm_twist_curve_tweak, 'tweak_r_arm_twist')


    #_________________________________parent twist BIND jnts____________________________________________#
    #r_twistBind_grp = mc.group(p=r_foreArm1_var_list[0], em=True, n='r_twistBind_grp')
    #r_twistBind_grp_offset = mc.group(p=r_foreArm1_var_list[0], em=True, n='r_twistBind_grp_offset')
    #mc.parent(r_twistBind_grp_offset, r_twistBind_grp)
    #mc.parent(r_arm_startTwist_jnt_grp, r_arm_endTwist_jnt_grp, r_twistBind_grp_offset)
    
    #_____________________________________________________________________________#
    #_________________________________L arm Blend (Colors)________________________#
    #_____________________________________________________________________________#

    #list for blend color nodes
    r_arm_blendColorsNode_trans_list = []
    r_arm_blendColorsNode_rot_list = []

    #create blend nodes based on base joints (trans, rot, scale/ blend nodes for each jnt)
    for items in r_arm_var_list:
        items_betterName = str(items[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create blend colors node, then name it after joint
        blendColorsNode_trans = mc.createNode('blendColors')
        blendColorsNode_trans = items_betterName.replace(prefix_betterName, trans_blendColorsPrefix)
        blendColorsNode_trans = mc.rename(blendColorsNode_trans)

        blendColorsNode_rot = mc.createNode('blendColors')
        blendColorsNode_rot = items_betterName.replace(prefix_betterName, rot_BlendColorsPrefix)
        blendColorsNode_rot = mc.rename(blendColorsNode_rot)

        #create/add blend color nodes to a list
        r_arm_blendColorsNode_trans_list.append(blendColorsNode_trans)
        r_arm_blendColorsNode_rot_list.append(blendColorsNode_rot)
    

    #trans____________(b/c not all output needed)
    for item in r_arm_var_list[1]:
        mc.connectAttr((r_arm_blendColorsNode_trans_list[1] + '.output'), (item + '.translate'), f=True)
    
    #rot___________(b/c not all output needed)
    for item in r_arm_var_list[0]:
        mc.connectAttr((r_arm_blendColorsNode_rot_list[0] + '.output'), (item + '.rotate'), f=True)
    for item in r_arm_var_list[1]:
        mc.connectAttr((r_arm_blendColorsNode_rot_list[1] + '.output'), (item + '.rotate'), f=True)
    
    #alternate to wrist rotate blend (b/c does not work with blend color, bleed through rotate constraint)
    r_wrist_rotateConst = mc.parentConstraint(r_arm_ik_list[2], r_arm_fk_list[2], r_arm_var_list[2], st=('x','y','z'))

    
    #connect fk and ik joint chains to blend color nodes
    for items_fk, items_ik, items_blClr_trans, items_blClr_rot in itertools.izip(    r_arm_fk_list,
                                                                                    r_arm_ik_list, 
                                                                                    r_arm_blendColorsNode_trans_list,
                                                                                    r_arm_blendColorsNode_rot_list, ):
        mc.connectAttr((items_fk + '.translate'), (items_blClr_trans + '.color1'), f=True)

        mc.connectAttr((items_fk + '.rotate'), (items_blClr_rot + '.color1'), f=True)

        mc.connectAttr((items_ik + '.translate'), (items_blClr_trans + '.color2'), f=True)

        mc.connectAttr((items_ik + '.rotate'), (items_blClr_rot + '.color2'), f=True)

    
    #_____________________________________________________________________________#
    #____________________________R arm Switch Ctrl________________________________#
    #_____________________________________________________________________________#
    r_arm_switch_ctrl = []
    r_arm_switch_ctrl_grp = []
    for i in range (0,1):
        #name circle curves
        r_ArmSwchCrvA_name = 'switchCtrl_r_arm'
        r_ArmSwchCrvB_name = 'switchCtrl_r_arm0'
        r_ArmSwchCrvC_name = 'switchCtrl_r_arm1'

        #create nurbs circle
        r_ArmSwchCrvA = mc.circle(n=r_ArmSwchCrvA_name, ch=False, r=2, nr=(0,1,0))
        #create variable for nurbs circle shape
        r_ArmSwchCrvA_shape = mc.listRelatives(r_ArmSwchCrvA, s=True)
        #color nurbs circle shape
        mc.setAttr((r_ArmSwchCrvA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((r_ArmSwchCrvA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((r_ArmSwchCrvA_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((r_ArmSwchCrvA_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((r_ArmSwchCrvA_shape[0] + ".overrideColorB"), 1)

        #create 2nd nurbs circle
        r_ArmSwchCrvB = mc.circle(n=r_ArmSwchCrvB_name, ch=False, r=2, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        r_ArmSwchCrvB_shape = mc.listRelatives(r_ArmSwchCrvB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((r_ArmSwchCrvB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((r_ArmSwchCrvB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((r_ArmSwchCrvB_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((r_ArmSwchCrvB_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((r_ArmSwchCrvB_shape[0] + ".overrideColorB"), 1)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(r_ArmSwchCrvB_shape, r_ArmSwchCrvA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(r_ArmSwchCrvB)

        #create 3rd nurbs circle
        r_ArmSwchCrvC = mc.circle(n=r_ArmSwchCrvC_name, ch=False, r=2, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        r_ArmSwchCrvC_shape = mc.listRelatives(r_ArmSwchCrvC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((r_ArmSwchCrvC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((r_ArmSwchCrvC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((r_ArmSwchCrvC_shape[0] + ".overrideColorR"), 0)
        mc.setAttr((r_ArmSwchCrvC_shape[0] + ".overrideColorG"), 0.5)
        mc.setAttr((r_ArmSwchCrvC_shape[0] + ".overrideColorB"), 1)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(r_ArmSwchCrvC_shape, r_ArmSwchCrvA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(r_ArmSwchCrvC)

        #_______group switch ctrl_______#
        r_ArmSwchCrvA_grp = mc.group(r_ArmSwchCrvA, n = (r_ArmSwchCrvA_name + '_grp'))
        r_ArmSwchCrvA_grp_offset = mc.group(r_ArmSwchCrvA, n = (r_ArmSwchCrvA_name + '_grp_offset'))
        
        #_______move ctrl shapes in -z_______#
        mc.setAttr((r_ArmSwchCrvA[0] + ".translateZ"), 20)
        mc.xform (r_ArmSwchCrvA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(r_ArmSwchCrvA, apply=True)
        
        #_______move ctrl to ankle and parent_______#

        #parent and zero ctl to r_arm_list
        mc.parent(r_ArmSwchCrvA_grp, r_foreArm5_var_list, relative=True)
        #parent ctrl to world space
        mc.Unparent(r_ArmSwchCrvA_grp)

        # parent constrain switch ctrl to wrist
        mc.parentConstraint(r_foreArm5_var_list, r_ArmSwchCrvA_grp, mo=True)

        #_______add IK FK Blend attr to switch ctrl_______#
        mc.addAttr(r_ArmSwchCrvA, ln = "fk_ik_blend", min=0, max=1, k=True)

        #lock and hide unneeded attributes for switch ctrl
        mc.setAttr((r_ArmSwchCrvA[0] + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.tz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.sx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.sy'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((r_ArmSwchCrvA[0] + '.sz'), lock=True, keyable=False, channelBox=False)
        #append list for outside loop
        r_arm_switch_ctrl.append(r_ArmSwchCrvA)
        r_arm_switch_ctrl_grp.append(r_ArmSwchCrvA_grp)
        
        
        #_______connet Blend Color nodes to switch ctrl "Blend Attr"______#
        #0=IK, 1=FK

        for items_trans, items_rot in itertools.izip(  r_arm_blendColorsNode_trans_list, 
                                                                    r_arm_blendColorsNode_rot_list, ):
            mc.connectAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
            mc.connectAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)


        #_______L Wrist X Twist Parent Constraint BLEND________#
        #_______arm twist constraint________#
        #mc.parentConstraint(r_ikHandCtrl[0], r_arm_fk_ctrl_list[2], r_arm_endTwist_jnt, sr=('y','z'), st=('x','y','z'))

        #IK___________
        mc.setAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)  

        mc.setAttr((r_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_r_foreArm5W1'), 0)
        mc.setAttr((r_arm_endTwist_jnt + '_parentConstraint1' + '.r_ikHandCtrlW0'), 1)

        mc.setDrivenKeyframe((r_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_r_foreArm5W1'), currentDriver = (r_ArmSwchCrvA[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_endTwist_jnt + '_parentConstraint1' + '.r_ikHandCtrlW0'), currentDriver = (r_ArmSwchCrvA[0] + '.fk_ik_blend'))
        
        #FK_________
        mc.setAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), 1)  

        mc.setAttr((r_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_r_foreArm5W1'), 1)
        mc.setAttr((r_arm_endTwist_jnt + '_parentConstraint1' + '.r_ikHandCtrlW0'), 0)

        mc.setDrivenKeyframe((r_arm_endTwist_jnt + '_parentConstraint1' + '.fkCtrl_r_foreArm5W1'), currentDriver = (r_ArmSwchCrvA[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_endTwist_jnt + '_parentConstraint1' + '.r_ikHandCtrlW0'), currentDriver = (r_ArmSwchCrvA[0] + '.fk_ik_blend'))


        #__________IK FK Blend Hide keys, +  Key Wrist oreint__________#
        mc.setAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)
        mc.setAttr((r_ikHandCtrl_grp[0] + '.visibility'), 1)
        mc.setAttr((r_arm_pv_grp[0] + '.visibility'), 1)
        mc.setAttr((r_arm_fk_ctrl_grp_list[0] + '.visibility'), 0)
        mc.setAttr(r_wrist_rotateConst[0] + '.ikJnt_r_foreArm5W0', 1)
        mc.setAttr(r_wrist_rotateConst[0] + '.fkJnt_r_foreArm5W1', 0)

        mc.setDrivenKeyframe((r_ikHandCtrl_grp[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_pv_grp[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_wrist_rotateConst[0] + '.ikJnt_r_foreArm5W0'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_wrist_rotateConst[0] + '.fkJnt_r_foreArm5W1'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))

        mc.setAttr((r_ArmSwchCrvA[0]  + '.fk_ik_blend'), 1)
        mc.setAttr((r_ikHandCtrl_grp[0] + '.visibility'), 0)
        mc.setAttr((r_arm_pv_grp[0] + '.visibility'), 0)
        mc.setAttr((r_arm_fk_ctrl_grp_list[0] + '.visibility'), 1)
        mc.setAttr(r_wrist_rotateConst[0] + '.ikJnt_r_foreArm5W0', 0)
        mc.setAttr(r_wrist_rotateConst[0] + '.fkJnt_r_foreArm5W1', 1)

        mc.setDrivenKeyframe((r_ikHandCtrl_grp[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_pv_grp[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_arm_fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_wrist_rotateConst[0] + '.ikJnt_r_foreArm5W0'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))
        mc.setDrivenKeyframe((r_wrist_rotateConst[0] + '.fkJnt_r_foreArm5W1'), currentDriver = (r_ArmSwchCrvA[0]  + '.fk_ik_blend'))

        
    #__________reset value to 0 for default IK__________#
    mc.setAttr((r_ArmSwchCrvA[0] + '.fk_ik_blend'), 0)

    #___BREAK Unneaded blendColor Connections____#
    mc.delete(r_arm_blendColorsNode_trans_list[0])
    mc.delete(r_arm_blendColorsNode_trans_list[2])
    mc.delete(r_arm_blendColorsNode_rot_list[2])

    
    #_________________________________________________________#
    #________________@mkg L FINGERs___________________________#
    #_________________________________________________________#

    #_____________L Hand_______________________#
    #__________________________________________#

    l_hand_grp_list = []
    l_hand_grp_offset_list = []

    for i in l_foreArm5_var_list:
        #group
        myGroup_offset = mc.group(em=True)
        myGroup = mc.group(myGroup_offset)
        #rename group
        myGroup = mc.rename(myGroup, (i + '_grp'))
        myGroup_offset = mc.rename(myGroup_offset, (i + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #add variable to list to access outside of loop
        l_hand_grp_list.append(myGroup)
        l_hand_grp_offset_list.append(myGroup_offset)

    # constrain hand group to hand jnt
    mc.parentConstraint(l_foreArm5_var_list, l_hand_grp_list[0])
    
    #________________________________________#
    #_____________l FK THUMB_________________#
    #________________________________________#

    #create empty ctrl grp list to append too
    l_thumb_ctrl_list = []
    l_thumb_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in l_thumb_list:
        #items_betterName = str(i[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #set curve width
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_thumb_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        l_thumb_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(l_thumb_ctrl_grp_list[1], l_thumb_ctrl_list[0])
    mc.parent(l_thumb_ctrl_grp_list[2], l_thumb_ctrl_list[1])
    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_thumb_ctrl_list[0], l_thumb_list[0])
    mc.parentConstraint(l_thumb_ctrl_list[1], l_thumb_list[1])
    mc.parentConstraint(l_thumb_ctrl_list[2], l_thumb_list[2])

    #parent thumb top group under hand grp
    mc.parent(l_thumb_ctrl_grp_list[0], l_hand_grp_offset_list[0])
    
    
    #________________________________________#
    #_____________l FK pointerFinger_________________#
    #________________________________________#

    #create empty ctrl grp list to append too
    l_pointerFinger_ctrl_list = []
    l_pointerFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in l_pointerFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_pointerFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        l_pointerFinger_ctrl_grp_list.append(myGroup)
    
    #parent ctrl grps together
    mc.parent(l_pointerFinger_ctrl_grp_list[1], l_pointerFinger_ctrl_list[0])
    mc.parent(l_pointerFinger_ctrl_grp_list[2], l_pointerFinger_ctrl_list[1])
    mc.parent(l_pointerFinger_ctrl_grp_list[3], l_pointerFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_pointerFinger_ctrl_list[0], l_pointerFinger_list[0])
    mc.parentConstraint(l_pointerFinger_ctrl_list[1], l_pointerFinger_list[1])
    mc.parentConstraint(l_pointerFinger_ctrl_list[2], l_pointerFinger_list[2])
    mc.parentConstraint(l_pointerFinger_ctrl_list[3], l_pointerFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(l_pointerFinger_ctrl_grp_list[0], l_hand_grp_offset_list[0])
    

    #________________________________________#
    #________l FK middleFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    l_middleFinger_ctrl_list = []
    l_middleFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in l_middleFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_middleFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        l_middleFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(l_middleFinger_ctrl_grp_list[1], l_middleFinger_ctrl_list[0])
    mc.parent(l_middleFinger_ctrl_grp_list[2], l_middleFinger_ctrl_list[1])
    mc.parent(l_middleFinger_ctrl_grp_list[3], l_middleFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_middleFinger_ctrl_list[0], l_middleFinger_list[0])
    mc.parentConstraint(l_middleFinger_ctrl_list[1], l_middleFinger_list[1])
    mc.parentConstraint(l_middleFinger_ctrl_list[2], l_middleFinger_list[2])
    mc.parentConstraint(l_middleFinger_ctrl_list[3], l_middleFinger_list[3])
    
    #parent thumb top group under hand grp
    mc.parent(l_middleFinger_ctrl_grp_list[0], l_hand_grp_offset_list[0])

    
    #________________________________________#
    #________l FK ringFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    l_ringFinger_ctrl_list = []
    l_ringFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in l_ringFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_ringFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        l_ringFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(l_ringFinger_ctrl_grp_list[1], l_ringFinger_ctrl_list[0])
    mc.parent(l_ringFinger_ctrl_grp_list[2], l_ringFinger_ctrl_list[1])
    mc.parent(l_ringFinger_ctrl_grp_list[3], l_ringFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_ringFinger_ctrl_list[0], l_ringFinger_list[0])
    mc.parentConstraint(l_ringFinger_ctrl_list[1], l_ringFinger_list[1])
    mc.parentConstraint(l_ringFinger_ctrl_list[2], l_ringFinger_list[2])
    mc.parentConstraint(l_ringFinger_ctrl_list[3], l_ringFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(l_ringFinger_ctrl_grp_list[0], l_hand_grp_offset_list[0])

    
    #________________________________________#
    #________l FK pinkyFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    l_pinkyFinger_ctrl_list = []
    l_pinkyFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in l_pinkyFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        l_pinkyFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        l_pinkyFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(l_pinkyFinger_ctrl_grp_list[1], l_pinkyFinger_ctrl_list[0])
    mc.parent(l_pinkyFinger_ctrl_grp_list[2], l_pinkyFinger_ctrl_list[1])
    mc.parent(l_pinkyFinger_ctrl_grp_list[3], l_pinkyFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(l_pinkyFinger_ctrl_list[0], l_pinkyFinger_list[0])
    mc.parentConstraint(l_pinkyFinger_ctrl_list[1], l_pinkyFinger_list[1])
    mc.parentConstraint(l_pinkyFinger_ctrl_list[2], l_pinkyFinger_list[2])
    mc.parentConstraint(l_pinkyFinger_ctrl_list[3], l_pinkyFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(l_pinkyFinger_ctrl_grp_list[0], l_hand_grp_offset_list[0])

    
    #_________________________________________________________#
    #________________@mkb R FINGERs___________________________#
    #_________________________________________________________#

    #_____________R Hand_______________________#
    #__________________________________________#

    r_hand_grp_list = []
    r_hand_grp_offset_list = []

    for i in r_foreArm5_var_list:
        #group
        myGroup_offset = mc.group(em=True)
        myGroup = mc.group(myGroup_offset)
        #rename group
        myGroup = mc.rename(myGroup, (i + '_grp'))
        myGroup_offset = mc.rename(myGroup_offset, (i + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #add variable to list to access outside of loop
        r_hand_grp_list.append(myGroup)
        r_hand_grp_offset_list.append(myGroup_offset)

    # constrain hand group to hand jnt
    mc.parentConstraint(r_foreArm5_var_list, r_hand_grp_list[0])
    #________________________________________#
    #_____________l FK THUMB_________________#
    #________________________________________#

    #create empty ctrl grp list to append too
    r_thumb_ctrl_list = []
    r_thumb_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in r_thumb_list:
        #items_betterName = str(i[0])
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #set curve width
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_thumb_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        r_thumb_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(r_thumb_ctrl_grp_list[1], r_thumb_ctrl_list[0])
    mc.parent(r_thumb_ctrl_grp_list[2], r_thumb_ctrl_list[1])
    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_thumb_ctrl_list[0], r_thumb_list[0])
    mc.parentConstraint(r_thumb_ctrl_list[1], r_thumb_list[1])
    mc.parentConstraint(r_thumb_ctrl_list[2], r_thumb_list[2])

    #parent thumb top group under hand grp
    mc.parent(r_thumb_ctrl_grp_list[0], r_hand_grp_offset_list[0])
    
    
    #________________________________________#
    #_____________l FK pointerFinger_________________#
    #________________________________________#

    #create empty ctrl grp list to append too
    r_pointerFinger_ctrl_list = []
    r_pointerFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in r_pointerFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_pointerFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        r_pointerFinger_ctrl_grp_list.append(myGroup)
    
    #parent ctrl grps together
    mc.parent(r_pointerFinger_ctrl_grp_list[1], r_pointerFinger_ctrl_list[0])
    mc.parent(r_pointerFinger_ctrl_grp_list[2], r_pointerFinger_ctrl_list[1])
    mc.parent(r_pointerFinger_ctrl_grp_list[3], r_pointerFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_pointerFinger_ctrl_list[0], r_pointerFinger_list[0])
    mc.parentConstraint(r_pointerFinger_ctrl_list[1], r_pointerFinger_list[1])
    mc.parentConstraint(r_pointerFinger_ctrl_list[2], r_pointerFinger_list[2])
    mc.parentConstraint(r_pointerFinger_ctrl_list[3], r_pointerFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(r_pointerFinger_ctrl_grp_list[0], r_hand_grp_offset_list[0])
    

    #________________________________________#
    #________l FK middleFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    r_middleFinger_ctrl_list = []
    r_middleFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in r_middleFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_middleFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        r_middleFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(r_middleFinger_ctrl_grp_list[1], r_middleFinger_ctrl_list[0])
    mc.parent(r_middleFinger_ctrl_grp_list[2], r_middleFinger_ctrl_list[1])
    mc.parent(r_middleFinger_ctrl_grp_list[3], r_middleFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_middleFinger_ctrl_list[0], r_middleFinger_list[0])
    mc.parentConstraint(r_middleFinger_ctrl_list[1], r_middleFinger_list[1])
    mc.parentConstraint(r_middleFinger_ctrl_list[2], r_middleFinger_list[2])
    mc.parentConstraint(r_middleFinger_ctrl_list[3], r_middleFinger_list[3])
    
    #parent thumb top group under hand grp
    mc.parent(r_middleFinger_ctrl_grp_list[0], r_hand_grp_offset_list[0])

    
    #________________________________________#
    #________l FK ringFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    r_ringFinger_ctrl_list = []
    r_ringFinger_ctrl_grp_list = []

    #create box curves at l fk joints
    for i in r_ringFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 1)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_ringFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        r_ringFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(r_ringFinger_ctrl_grp_list[1], r_ringFinger_ctrl_list[0])
    mc.parent(r_ringFinger_ctrl_grp_list[2], r_ringFinger_ctrl_list[1])
    mc.parent(r_ringFinger_ctrl_grp_list[3], r_ringFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_ringFinger_ctrl_list[0], r_ringFinger_list[0])
    mc.parentConstraint(r_ringFinger_ctrl_list[1], r_ringFinger_list[1])
    mc.parentConstraint(r_ringFinger_ctrl_list[2], r_ringFinger_list[2])
    mc.parentConstraint(r_ringFinger_ctrl_list[3], r_ringFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(r_ringFinger_ctrl_grp_list[0], r_hand_grp_offset_list[0])

    #________________________________________#
    #________l FK pinkyFinger_______________#
    #________________________________________#

    #create empty ctrl grp list to append too
    r_pinkyFinger_ctrl_list = []
    r_pinkyFinger_ctrl_grp_list = []

        #create box curves at l fk joints
    for i in r_pinkyFinger_list:
        prefix_betterName = str(skel_pre_var_list[0])
        #create curve box
        mc.curve(d=1, p=[(-1, 1, 1), 
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
        mc.setAttr(".scaleX", 1.5)
        mc.setAttr(".scaleY", 1.5)
        mc.setAttr(".scaleZ", 1.5)
        #freeze transforms
        mc.makeIdentity(apply=True)
        #select curve box's shape
        itemsShape = mc.listRelatives(s=True)
        #color curve box's shape red
        mc.setAttr((itemsShape[0] + ".overrideEnabled"), 1)
        mc.setAttr((itemsShape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorR"), 1)
        mc.setAttr((itemsShape[0] + ".overrideColorG"), 0)
        mc.setAttr((itemsShape[0] + ".overrideColorB"), 0)
        mc.setAttr((itemsShape[0] + '.lineWidth'), 2)
        #rename curve, with joint name, and then new prefix
        curveName_prefixChange = i.replace(prefix_betterName, fkCtrlPrefix)
        myCurve = mc.rename(curveName_prefixChange)
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to r_leg_fk_list
        mc.parent(myGroup, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #create a list of the ctrl curves (to parent constrain the joints to)
        r_pinkyFinger_ctrl_list.append(myCurve)
        #create a list for the groups (for parenting to one another)
        r_pinkyFinger_ctrl_grp_list.append(myGroup)
        
    #parent ctrl grps together
    mc.parent(r_pinkyFinger_ctrl_grp_list[1], r_pinkyFinger_ctrl_list[0])
    mc.parent(r_pinkyFinger_ctrl_grp_list[2], r_pinkyFinger_ctrl_list[1])
    mc.parent(r_pinkyFinger_ctrl_grp_list[3], r_pinkyFinger_ctrl_list[2])

    #parent constrain ctrls to fk jnts
    mc.parentConstraint(r_pinkyFinger_ctrl_list[0], r_pinkyFinger_list[0])
    mc.parentConstraint(r_pinkyFinger_ctrl_list[1], r_pinkyFinger_list[1])
    mc.parentConstraint(r_pinkyFinger_ctrl_list[2], r_pinkyFinger_list[2])
    mc.parentConstraint(r_pinkyFinger_ctrl_list[3], r_pinkyFinger_list[3])

    #parent thumb top group under hand grp
    mc.parent(r_pinkyFinger_ctrl_grp_list[0], r_hand_grp_offset_list[0])
    
    #_______________________________________________________________#
    #_______________Global Character Control________________________#
    #_______________________________________________________________#

    globalCtrl_curve = mc.circle(n='global_ctrl', ch=False, r=50, nr=(0,1,0))
    globalCtrl_curve_shape = mc.listRelatives(globalCtrl_curve, s=True)
    mc.setAttr((globalCtrl_curve_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((globalCtrl_curve_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((globalCtrl_curve_shape[0] + ".overrideColorR"), 0)
    mc.setAttr((globalCtrl_curve_shape[0] + ".overrideColorG"), 0.5)
    mc.setAttr((globalCtrl_curve_shape[0] + ".overrideColorB"), 1)
    mc.setAttr(globalCtrl_curve[0] + ".translateZ", 10)
    #pivot to world center
    mc.xform (globalCtrl_curve, ws=True, piv= (0, 0, 0))
    #freeze transforms
    mc.makeIdentity(globalCtrl_curve, apply=True)
    #grp curve
    globalCtrl_curve_grp_offset = mc.group(n = globalCtrl_curve[0] + '_grp_offset', em=True)
    mc.parent(globalCtrl_curve, globalCtrl_curve_grp_offset)
    globalCtrl_curve_grp = mc.group(n = globalCtrl_curve[0] + '_grp', em=True)
    mc.parent(globalCtrl_curve_grp_offset, globalCtrl_curve_grp)
    
    #_______________________________________________________________#
    #_______________________group things____________________________#
    #_______________________________________________________________#

    #hidden group_________________#
    hiddenGrp = mc.group(n = 'hidden_grp', w=True, em=True)
    #l leg
    mc.parent(ikHandkle_l_leg, hiddenGrp)
    #r leg
    mc.parent(ikHandkle_r_leg, hiddenGrp)
    #l arm
    mc.parent(lClv_measerTool_grp, hiddenGrp)
    mc.parent(l_arm_ikHandle[0], hiddenGrp)
    mc.parent(l_arm_twist_ikHandle[0], hiddenGrp)
    mc.parent(l_arm_ikHandle_curve_newName, hiddenGrp)
    #l arm
    mc.parent(rClv_measerTool_grp, hiddenGrp)
    mc.parent(r_arm_ikHandle[0], hiddenGrp)
    mc.parent(r_arm_twist_ikHandle[0], hiddenGrp)
    mc.parent(r_arm_ikHandle_curve_newName, hiddenGrp)
    #grp settings
    mc.setAttr((hiddenGrp + '.visibility'), 0)
    mc.setAttr((hiddenGrp + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.rz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((hiddenGrp + '.sx'), lock=True)
    mc.setAttr((hiddenGrp + '.sy'), lock=True)
    mc.setAttr((hiddenGrp + '.sz'), lock=True)


    #ctrls group_________________#
    ctrlsGrp = mc.group(n = 'ctrls_grp', w=True, em=True)
    #parent global ctrl
    mc.parent(globalCtrl_curve_grp, ctrlsGrp)
    #l leg
    mc.parent(pvCtrl_l_leg_grp, globalCtrl_curve)
    mc.parent(ikFootCtrl_l_foot1_grp, globalCtrl_curve)
    mc.parent(switchCtrl_l_leg_grp, globalCtrl_curve)
    mc.parent(fkCtrl_l_hip_grp, globalCtrl_curve)
    #r leg
    mc.parent(pvCtrl_r_leg_grp, globalCtrl_curve)
    mc.parent(ikFootCtrl_r_foot1_grp, globalCtrl_curve)
    mc.parent(switchCtrl_r_leg_grp, globalCtrl_curve)
    mc.parent(fkCtrl_r_hip_grp, globalCtrl_curve)
    #l arm
    mc.parent(l_arm_clavicle_ctrl_grp_list, globalCtrl_curve)
    mc.parent(ikHandCtrl_grp, globalCtrl_curve)
    mc.parent(l_arm_pv_grp, globalCtrl_curve)
    mc.parent(l_arm_fk_ctrl_grp_list[0], globalCtrl_curve)
    mc.parent(l_arm_switch_ctrl_grp, globalCtrl_curve)
    mc.parent(l_hand_grp_list, globalCtrl_curve)
    #l clavicle handle______
    mc.parent(lClvGrp, globalCtrl_curve)
    mc.setAttr((lClvGrp + '.visibility'), 0)
    #r arm
    mc.parent(r_arm_clavicle_ctrl_grp_list, globalCtrl_curve)
    mc.parent(r_ikHandCtrl_grp, globalCtrl_curve)
    mc.parent(r_arm_pv_grp, globalCtrl_curve)
    mc.parent(r_arm_fk_ctrl_grp_list[0], globalCtrl_curve)
    mc.parent(r_arm_switch_ctrl_grp, globalCtrl_curve)
    mc.parent(r_hand_grp_list, globalCtrl_curve)
    #l clavicle handle______
    mc.parent(rClvGrp, globalCtrl_curve)
    mc.setAttr((rClvGrp + '.visibility'), 0)
    #r arm
    #base spine grp
    mc.parent(spine_ctrl_grp_list[0], globalCtrl_curve)
    mc.parent(midFaceCtrl_grp, globalCtrl_curve)
    #grp settings
    mc.setAttr((ctrlsGrp + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.rz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((ctrlsGrp + '.sx'), lock=True)
    mc.setAttr((ctrlsGrp + '.sy'), lock=True)
    mc.setAttr((ctrlsGrp + '.sz'), lock=True)


    #joint group_________________#
    jointsGrp = mc.group(n = 'joints_grp', w=True, em=True)
    #MAIN JOINT ROOT
    #mc.parent(spine1_var_list, jointsGrp)
    #leg blend offset parent to joint grp for organization
    mc.parent(spine1_colorBlendJnt[0], jointsGrp)
    #l arm
    mc.parent(l_arm_blend_offsetJnt[0], jointsGrp)
    mc.parent(l_arm_twist_list[0], jointsGrp)
    mc.parent(l_arm_startTwist_jnt, jointsGrp)
    mc.parent(l_arm_endTwist_jnt, jointsGrp)
    #r arm
    mc.parent(r_arm_blend_offsetJnt[0], jointsGrp)
    mc.parent(r_arm_twist_list[0], jointsGrp)
    mc.parent(r_arm_startTwist_jnt, jointsGrp)
    mc.parent(r_arm_endTwist_jnt, jointsGrp)
    #grp settings
    mc.setAttr((jointsGrp + '.visibility'), 0)
    mc.setAttr((jointsGrp + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.rz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((jointsGrp + '.sx'), lock=True)
    mc.setAttr((jointsGrp + '.sy'), lock=True)
    mc.setAttr((jointsGrp + '.sz'), lock=True)

    #global group_________________#
    globalGrp = mc.group(n = 'global_character_grp', w=True, em=True)
    #______#
    mc.parent(hiddenGrp, globalGrp)
    mc.parent(ctrlsGrp, globalGrp)
    mc.parent(jointsGrp, globalGrp)

    #grp settings
    mc.setAttr((globalGrp + '.tx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((globalGrp + '.ty'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((globalGrp + '.tz'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((globalGrp + '.rx'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((globalGrp + '.ry'), lock=True, keyable=False, channelBox=False)
    mc.setAttr((globalGrp + '.rz'), lock=True, keyable=False, channelBox=False)

    
    #_______________________________________________________________#
    #____________________CONNECTing Rig PARTS_______________________#
    #_______________________________________________________________#
    
    #_parent fk leg group to spine1 (base) ctrl_#
    mc.parent(l_leg_fk_ctrl_grp_list[0], spine_ctrl_list[0])
    mc.parent(r_leg_fk_ctrl_grp_list[0], spine_ctrl_list[0])

    #l_arm to chest
    mc.parent(l_arm_clavicle_ctrl_grp_list, spine_ctrl_list[5])
    mc.parent(l_arm_fk_ctrl_grp_list[0], spine_ctrl_list[5])

    #r_arm to chest
    mc.parent(r_arm_clavicle_ctrl_grp_list, spine_ctrl_list[5])
    mc.parent(r_arm_fk_ctrl_grp_list[0], spine_ctrl_list[5])
    #_______________________________________________________________#
    #____________________Default Settings_______________________#
    #_______________________________________________________________#
    #IKFK Blend Ctrl set default to IK
    mc.setAttr((switchCurveA_l[0] + '.fk_ik_blend'), 0)
    mc.setAttr((switchCurveA_r[0] + '.fk_ik_blend'), 0)
    #make leg joints invisible
    mc.setAttr((spine1_colorBlendJnt[0] + '.visibility'), 0)

    #______________________________________________________________________________#
    #__________tag all ctrls as Controller (for parallel evaluation________________#
    #______________________________________________________________________________#
    allNurbsCtrls = mc.listRelatives(globalCtrl_curve_grp, ad=True, type='nurbsCurve')
    allNurbsCtrls_parent = mc.listRelatives(allNurbsCtrls, p=True)
    mc.select(allNurbsCtrls_parent)
    mc.TagAsController()
    allNurbsFaceCtrls = mc.listRelatives(globalCtrl_curve_grp, ad=True, type='nurbsSurface')
    allNurbsFaceCtrls_parent = mc.listRelatives(allNurbsFaceCtrls, p=True)
    mc.select(allNurbsFaceCtrls_parent)
    mc.TagAsController()


    #deselect all, back to main screen
    mc.select(cl=True)
    mc.setFocus("MayaWindow")
    
    

print('\n')
print('_________________________')
print('________Thank You________')
print('__________End____________')


#____________________@mkg End_______________________#


