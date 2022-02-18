#import maya commands
import maya.cmds as mc
#import python random functions
import random

import itertools

import maya.api.OpenMaya as om

#close UI if already open
if mc.window("nate_tools_ui", ex=True):
    mc.deleteUI("nate_tools_ui", window=True)

mc.window("nate_tools_ui", t="Nate Tools!", rtf=True, s=True, menuBar=True, bgc = (0.2,0,0.2))

#________________________layout Begin______________________________________#
#__________________________________________________________________________#
#main layout creation
myForm = mc.formLayout()

myColumn = mc.columnLayout(bgc=(0.1,0,0.1))

#_______Beginning Title_______#
#to create border around edge
mc.formLayout(myForm, edit=True, attachForm=[(myColumn, 'top', 10),(myColumn, 'bottom', 10),(myColumn, 'left', 10),(myColumn, 'right', 10)])

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#'Nate Tools!'
mc.rowLayout( numberOfColumns=1)
mc.text(label = 'Nate Tools!', height=20, width=454, align='center', bgc=(0.4,.5,0), font='boldLabelFont', statusBarMessage='Nate Tools!')
mc.setParent("..")

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#_________________________declare Tabs____________________________________#
#Insert Tabs
myTabs = mc.tabLayout()



#________________________________Rigging Tab @mkr _______________________________#
#__________________________________________________________________________#
#tab Rigging
myColumnB = mc.columnLayout()

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

# Button Row 1
mc.rowLayout(numberOfColumns = 5)
mc.button(label='FK Chain \n ~~~~~~~~ \n Select Joints', h=75, w=142, command = 'create_fk_chain()', bgc = (.5,0,0), statusBarMessage='Select Joints in Order')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='IK Limb \n ~~~~~~~~ \n Select 3 Joints', h=75, w=142, command = 'create_ik_limb()', bgc = (0,0.4,0), statusBarMessage='Select Joints in Order, Oriented for Main Axis X')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='FK/ IK Limb Blended \n ~~~~~~~~ \n Select 3+ Joints', h=75, w=142, command = 'create_fk_ik_limb()', bgc = (0,0.2,0.45), statusBarMessage='Select 3 or More Joints in Order, Oriented for Main Axis X')
mc.setParent('..')

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

# Button Row 2
mc.rowLayout(numberOfColumns = 6)
mc.button(label='Simple Blend Joints \n ~~~~~~~~ \n Select FK, IK, then Bind Jnt', h=75, w=142, command = 'simple_blend_joints()', bgc = (.5,0.1,0), statusBarMessage='Auto Sets Up Blend Color Node Between 3 Joints')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='Blended Joint Chain \n ~~~~~~~~ \n Select Joints in Order', h=75, w=142, command = 'blend_joint_chain()', bgc = (0,0.4,0.2), statusBarMessage='FK(A) and IK(B) chains will be created automatically')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='Reverse \n Foot \n Locators', h=75, w=71, command = 'rev_foot_locators()', bgc = (0.8,0.8,0), statusBarMessage='Create Locators for Positions of Reverse Foot Controls')
mc.button(label='Reverse \n Foot', h=75, w=71, command = 'reverse_foot_setup()', bgc = (0.2,0,0.45), statusBarMessage='Create Reverse Foot Setup/ Based on Locator Positions/ CREATE MORE! Locators for Each Reverse Foot')
mc.setParent('..')

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

# Button Row 3
mc.rowLayout(numberOfColumns = 5)
mc.button(label='Nurbs Curve Cube', h=75, w=142, command = 'nurbs_curve_cube()', bgc = (.5,0,0.1), statusBarMessage='Create nurbs cube with groups.')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='Nurbs Curve Sphere', h=75, w=142, command = 'nurbs_curve_sphere()', bgc = (0.2,0.4,0), statusBarMessage='Create nurbs sphere with groups.')
mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
mc.button(label='Nurbs Curve Arrow', h=75, w=142, command = 'nurbs_curve_arrow()', bgc = (0.1,.1,.45), statusBarMessage='Create nurbs arrow with groups.')
mc.setParent('..')

# Red Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
mc.setParent("..")

#parent column to tab
mc.setParent('..')


#______________________________Animation Tab @mkp _______________________________#
#__________________________________________________________________________#
myColumnC = mc.columnLayout()

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
mc.setParent("..")

# Buttons Row
mc.rowLayout(numberOfColumns = 5)
mc.button(label='create LOCATOR', h=75, w=142, command = 'create_locator()', bgc = (0.8,0.8,0), statusBarMessage='Create large locator')
mc.separator(style='none', w=10, h=75, bgc=(0,0.5,0.25))
mc.button(label='Multi-Parent Const \n ~~~~~~~~ \n Parent Ctrls to Locator \n To Move In Worldspace', h=75, w=142, command = 'multi_parent_const()', bgc = (0.5,0.1,0.1), statusBarMessage='Select Locator Last/ Exectute/ Key Ctrls/ then delete Locator (constraints will auto delete with locator)')
mc.separator(style='none', w=10, h=75, bgc=(0,0.5,0.25))
mc.button(label='RESET Ctrls', h=75, w=142, command = 'reset_ctrls()', bgc = (0.1,0.1,0.5), statusBarMessage='Reset Translation, Rotation, and Scale to ZERO')
mc.setParent('..')

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
mc.setParent("..")

# Buttons Row
mc.rowLayout(numberOfColumns = 5)
mc.separator(style='none', w=142, h=2)
mc.separator(style='none', w=10, h=2, bgc=(0,0.5,0.25))
mc.separator(style='none', w=142, h=2)
mc.separator(style='none', w=10, h=2, bgc=(0,0.5,0.25))
mc.setParent('..')

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = 'Mirror Controls or Objects:', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
mc.setParent("..")

# Text Label Row
mc.rowLayout(numberOfColumns = 15)
mc.text(label = 'Prefix', w=82, h=24, align='center', font = 'boldLabelFont', bgc=(0.2,0,0.2), statusBarMessage='Prefix to Mirror')
mc.text(label = '\/', w=104, h=23, align='center', bgc=(0.2,0,0.2), font = 'boldLabelFont', statusBarMessage='Select LEFT Controls/ Objects to Mirror, Or Mirror Selected if No Opposite Conrols/ Objects Exist')
mc.text(label = 'tran X*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Translate X Multiplier')
mc.text(label = 'tran Y*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Translate Y Multiplier')
mc.text(label = 'tran Z*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Translate Z Multiplier')
mc.separator(style='none', w=10, h=23, bgc=(0.2,0,0.2))
mc.text(label = 'rot X*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Rotate X Multiplier')
mc.text(label = 'rot Y*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Rotate Y Multiplier')
mc.text(label = 'rot Z*', width=40, height=24, bgc=(0.2,0,0.2), align='center', font = 'boldLabelFont', statusBarMessage='Rotate Z Multiplier')
mc.setParent('..')


# Text Input Row
mc.rowLayout(numberOfColumns = 15)
mc.textField('l_hip_text', width=40, h=24, text='L_')
mc.textField('r_hip_text', width=40, h=24, text='R_')
mc.separator(style='none', w=10, h=23, bgc=(0,0.5,0.25))
mc.button(label='Mirror Ctrls', w=80, command = 'mirror_ctrls()', bgc = (0.1,0.5,0.1), statusBarMessage='Select LEFT Controls/ Objects to Mirror, Or Mirror Selected if No Opposite Conrols/ Objects Exist')
mc.separator(style='none', w=10, h=23, bgc=(0,0.5,0.25))
mc.textField('translateX_text', width=40, h=24, text='-1')
mc.textField('translateY_text', width=40, h=24, text='1')
mc.textField('translateZ_text', width=40, h=24, text='1')
mc.separator(style='none', w=10, h=23, bgc=(0,0.5,0.25))
mc.textField('rotateX_text', width=40, h=24, text='1')
mc.textField('rotateY_text', width=40, h=24, text='-1')
mc.textField('rotateZ_text', width=40, h=24, text='-1')
mc.setParent('..')

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
mc.setParent("..")

#parent column to tab
mc.setParent('..')


#________________________________Modeling Tab @mkg ________________________________#
#____________________________________________________________________________#


#tab Modeling 
myColumnA = mc.columnLayout()

# Blue Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
mc.setParent("..")

# Modeling Button Row
mc.rowLayout(numberOfColumns = 5)
mc.button(label='create RANDOM objects', h=75, w=142, command = 'create_random()', bgc = (.4,0,.1), statusBarMessage='Creates random polygonal objects for testing')
mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
mc.button(label='SCATTER Selected', h=75, w=142, command = 'scatter_selected()', bgc = (0,.4,.4), statusBarMessage='Scatter selected randomly')
mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
mc.button(label='SCATTER Selected \n ...to Object Verts', h=75, w=142, command = 'scatter_to_vertices()', bgc = (.25,.5,0), statusBarMessage='First Select Objects to Scatter, Last Select Single Object to Scatter On')
mc.setParent('..')

# Blue Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
mc.setParent("..")

# Modeling Button Row
mc.rowLayout(numberOfColumns = 5)
mc.button(label='create HUMAN model', h=75, w=142, command = 'create_human()', bgc = (.25,.2,.2), statusBarMessage='Imports Default Human Sculpting Base')
mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
mc.button(label='Make Polygon ARCH \n (No Undo)', h=75, w=142, command = 'make_poly_arch()', bgc = (.5,.2,0), statusBarMessage='Create Basic Polygonal Arch (1st One Created Does Not Support Undo Currently)')
mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
mc.setParent('..')

# Blue Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = '', height=10, width=310, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
mc.setParent("..")

#parent column to tab
mc.setParent('..')


#______________________________Color Tab @mkp _______________________________#
#__________________________________________________________________________#

myColumnD = mc.columnLayout()

# Blue Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' Change Color of Selection "Shapes"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(0,0.2,0.5))
mc.setParent("..")

#shape color slider
mc.rowLayout(numberOfColumns = 2)
mc.intSlider('slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='slider_move()')
mc.iconTextButton('color', w=55, bgc=(0.5, 0.5, 0.5))
mc.setParent('..')

# Orange Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' Change Color of Selection "Transforms"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.5,0.1,0))
mc.setParent("..")

#transform color slider
mc.rowLayout(numberOfColumns = 2)
mc.intSlider('transform_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='transform_slider_move()')
mc.iconTextButton('transform_color', w=55, bgc=(0.5, 0.5, 0.5))
mc.setParent('..')

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' Change "WIRE" Color of Selection (Shapes)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
mc.setParent("..")

#wire color slider
mc.rowLayout(numberOfColumns = 2)
mc.intSlider('wire_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='wire_slider_move()')
mc.iconTextButton('wire_color', w=55, bgc=(0.5, 0.5, 0.5))
mc.setParent('..')

# Green Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' Change "WIRE" Color of Selection (Transforms)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
mc.setParent("..")

#wire color slider
mc.rowLayout(numberOfColumns = 2)
mc.intSlider('wireT_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='wireT_slider_move()')
mc.iconTextButton('wireT_color', w=55, bgc=(0.5, 0.5, 0.5))
mc.setParent('..')

# Grey Seperator
mc.rowLayout(numberOfColumns = 1)
mc.text(label = ' Change "Outliner" Color of Selection', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.1,0.1))
mc.setParent("..")

#wire color slider
mc.rowLayout(numberOfColumns = 2)
mc.intSlider('outliner_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='outliner_slider_move()')
mc.iconTextButton('outliner_color', w=55, bgc=(0.5, 0.5, 0.5))
mc.setParent('..')


#parent column to tab
mc.setParent('..')



#_________________Tab Layout/ UI End___________________#

#tabs layout
mc.tabLayout(myTabs, edit=True, tabLabel=[(myColumnA, 'Modeling'), (myColumnB, 'Rigging'), (myColumnC, 'Animation'), (myColumnD, 'Color')], bs='none')

#Show UI Window
mc.showWindow()

#____________________________________#
#____________FUNCTIONS_______________#
#____________________________________#

#_________________Modeling Functions_____________________#
#________________________________________________________#

#random_radius = random.randrange(0,100,1)

# create random polygon objects @mkg 
def create_random():
    for i in range(10):
        #random sphere
        mySphereRand = random.uniform(.5,3)
        mySphere = mc.polySphere(r=random.randrange(5,25,1), ch=0)
        mc.move(random.randrange(-200,200,1), random.randrange(-200,200,1), random.randrange(-200,200,1), mySphere, r=True, os=True)
        mc.scale(mySphereRand, mySphereRand, mySphereRand, mySphere, r=True, os=True)
        mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), mySphere, r=True, os=True)
        #random cube
        myCubeRand = random.uniform(5,25)
        myCubeRandA = random.uniform(.5,5)
        myCube = mc.polyCube(w=myCubeRand, h=random.uniform(5,50), d=myCubeRand, ch=0)
        mc.move(random.uniform(-200,200), random.uniform(-200,200), random.uniform(-200,200), myCube, r=True, os=True)
        mc.scale(myCubeRandA, random.uniform(.3,5), myCubeRandA, myCube, r=True, os=True)
        mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), myCube, r=True, os=True)
        #random cube
        myCylinderRand = random.uniform(.5,3)
        myCylinder = mc.polyCylinder(r=random.randrange(5,25,1), h=random.randrange(5,50,1), sc=1, ch=0)
        mc.move(random.randrange(-200,200,1), random.randrange(-200,200,1), random.randrange(-200,200,1), myCylinder, r=True, os=True)
        mc.scale(myCylinderRand, random.uniform(.5,5), myCylinderRand, myCylinder, r=True, os=True)
        mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), myCylinder, r=True, os=True)

    #deselect all, back to main screen
    mc.select(cl=True)
    mc.setFocus("MayaWindow")


#scatter selected randomly
def scatter_selected():
    mySel = mc.ls(sl=True)
    myTrans = 300
    myRot = 360
    myScale = 3
    
    for i in mySel:
        #translate
        mc.setAttr((i + ".tx"), random.uniform(-myTrans,myTrans))
        mc.setAttr((i + ".ty"), random.uniform(-myTrans,myTrans))
        mc.setAttr((i + ".tz"), random.uniform(-myTrans,myTrans))
        #rotate
        mc.setAttr((i + ".rx"), random.uniform(-myRot,myRot))
        mc.setAttr((i + ".ry"), random.uniform(-myRot,myRot))
        mc.setAttr((i + ".rz"), random.uniform(-myRot,myRot))
        #scale
        #for uniform scale
        myScale_rand = random.uniform(.3 , myScale)
        mc.setAttr((i + ".sx"), myScale_rand)
        mc.setAttr((i + ".sy"), myScale_rand)
        mc.setAttr((i + ".sz"), myScale_rand)

#scatter Objects to vertices of object
def scatter_to_vertices():
    #get selection
    mySel = mc.ls(sl=True)
    #selection without last object
    objList = mySel[0:-1]
    #get verts of last object
    vtxIndexList = mc.getAttr(mySel[-1] + '.vrts', multiIndices=True)
    #create empty variable to be filled with vertext positions
    vtxIndexList_positions = []
    #get vert positions of last object
    for i in vtxIndexList:
        vertLoc = mc.xform(mySel[-1] + '.pnts[' + str(i) + ']', query=True, translation=True, worldSpace=True)
        vtxIndexList_positions.append(vertLoc)
    #get number of verts in list
    vtxIndexList_positions_length = len(vtxIndexList_positions)-1
    #assign objects to random vertex position of last object
    for i in objList:
        vtxIndexList_positions_length_rand = random.randrange(0,vtxIndexList_positions_length, 1)
        randVertPos = vtxIndexList_positions[vtxIndexList_positions_length_rand]
        mc.setAttr((i + ".translate"), randVertPos[0], randVertPos[1], randVertPos[2])

#import default maya human sculpting base
def create_human():
    mc.file("C:/Program Files/Autodesk/Maya2020/Examples/Modeling/Sculpting_Base_Meshes/Bipeds/HumanBody.ma", i=True)

#make polygon arch
def make_poly_arch():
    #create 2d arch plance polygon points
    mc.polyCreateFacet(ch=0, p=[(86.295876, -2.03746, 0), 
                                        (83.403091, 20.861275, 0), 
                                        (74.906509, 42.321198, 0), 
                                        (61.339996, 60.993904, 0), 
                                        (43.555984, 75.706116, 0), 
                                        (22.671909, 85.533417, 0), 
                                        (4.29153e-06, 88.37664, 0), 
                                        (-22.671909, 85.533417, 0), 
                                        (-43.555984, 75.706116, 0), 
                                        (-61.340004, 60.993904, 0), 
                                        (-74.906517, 42.321198, 0), 
                                        (-83.403099, 20.861275, 0), 
                                        (-86.295883, -2.03746, 0), 
                                        (-111.295883, -2.03746, 0), 
                                        (-107.617683, 27.078522, 0), 
                                        (-96.814186, 54.36504, 0), 
                                        (-79.564217, 78.107582, 0), 
                                        (-56.951653, 96.814316, 0), 
                                        (-30.397335, 109.30983, 0), 
                                        (4.29153e-06, 113.327309, 0), 
                                        (30.397335, 109.30983, 0), 
                                        (56.951653, 96.814316, 0), 
                                        (79.564209, 78.107582, 0), 
                                        (96.814178, 54.36504, 0), 
                                        (107.617676, 27.078522, 0), 
                                        (111.295876, -2.03746, 0)]
                                        )
    #triangulate
    mc.polyTriangulate(ch=0)
    #quadrangulate
    mc.polyQuad(ch=0)
    #extrude to make 3d
    mc.polyExtrudeFacet(tz=-30, ch=0)
    #rename arch
    myArch = mc.rename('poly_arch')
    #clear selection (b/c faces selected after extrude)
    mc.select(cl=True)
    #select edges for bevel
    mc.select((myArch + '.e' + '[0:11]'), add=True)
    mc.select((myArch + '.e' + '[13:24]'), add=True)
    mc.select((myArch + '.e' + '[41]',
                myArch + '.e' + '[46]',
                myArch + '.e' + '[51]',
                myArch + '.e' + '[56]',
                myArch + '.e' + '[61]',
                myArch + '.e' + '[66]',
                myArch + '.e' + '[71]',
                myArch + '.e' + '[76]',
                myArch + '.e' + '[81]',
                myArch + '.e' + '[86]',
                myArch + '.e' + '[91]',
                myArch + '.e' + '[96]'),
                add=True)
    mc.select((myArch + '.e' + '[44]',
                myArch + '.e' + '[49]',
                myArch + '.e' + '[54]',
                myArch + '.e' + '[59]',
                myArch + '.e' + '[64]',
                myArch + '.e' + '[69]',
                myArch + '.e' + '[74]',
                myArch + '.e' + '[79]',
                myArch + '.e' + '[84]',
                myArch + '.e' + '[89]',
                myArch + '.e' + '[94]',
                myArch + '.e' + '[99]'),
                add=True)
    #floor edges
    mc.select((myArch + '.e' + '[97]',
                myArch + '.e' + '[98]',
                myArch + '.e' + '[95]',
                myArch + '.e' + '[25]',
                myArch + '.e' + '[37]',
                myArch + '.e' + '[39]',
                myArch + '.e' + '[38]',
                myArch + '.e' + '[12]'),
                add=True)
    #bevel
    mc.polyBevel3(offset=3, segments=2, smoothingAngle=180, subdivideNgons=1, ch=0)
    #nonlinear flare deformer
    myFlare = mc.nonLinear(myArch, type='flare')
    mc.setAttr(myFlare[0] + '.startFlareZ', 3)
    mc.setAttr(myFlare[0] + '.endFlareZ', 0)
    #delete history and/ deformer
    mc.delete(myArch, ch=True)
    #enlarge arch
    mc.setAttr(myArch + '.scale', 2.5,2.5,2.5)
    #adjust position
    mc.setAttr(myArch + '.tz', 37.5)
    mc.setAttr(myArch + '.ty', -2.5)
    #center pivot
    mc.move(0, 0, 0, (myArch + '.scalePivot'), (myArch + '.rotatePivot'))
    #freeze transforms
    mc.makeIdentity(myArch, apply=True)
    #select arch
    mc.select(myArch)


#_________________Rigging Functions @mkr _____________________#
#______________________________________________________________#

def create_fk_chain():
    #create list for ctrl grp parenting to one another
    fk_ctrl_grp_list = []
    #create list for ctrl parenting to one another
    fk_ctrl_list = []

    #my selection
    mySel = mc.ls(sl=True)

    for i in mySel:
        #create curve box
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
        myCurve_name = mc.rename(i + '_ctrl')

        #group curve
        curveGroup = mc.group(myCurve_name)
        curveGroup_offset = mc.group(myCurve_name)
        #rename group
        curveGroup_name = mc.rename(curveGroup, (myCurve_name + '_grp'))
        curveGroup_offset_name = mc.rename(curveGroup_offset, (myCurve_name + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(curveGroup_name, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(curveGroup_name)
        #create a list for the groups (for parenting to one another)
        fk_ctrl_grp_list.append(curveGroup_name)
        #create a list of the ctrl curves (to parent constrain the joints to)
        fk_ctrl_list.append(myCurve_name)

        #parent constrain ctrls to fk jnts
        mc.parentConstraint(myCurve_name, i)

    #remove first and last of lists to correctly parent ctrls and grps together in for loop
    fk_ctrl_grp_list.pop(0)
    fk_ctrl_list.pop(-1)

    #parent ctrls and grps together
    for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list, fk_ctrl_list):
        mc.parent(i_grp, i_ctrl)


#___________create IK Limb____________#
def create_ik_limb():
    #my joint selection
    mySel = mc.ls(sl=True)
    #group for organization
    myIKGrp = mc.group(em=True, n=mySel[0] + '_ik_grp')
    
    #___________create IK HANDLE____________#

    ikHandle_var = mc.ikHandle(n=mySel[0] + '_ikHandkle', sj=mySel[0], ee=mySel[-1])

    mc.setAttr((ikHandle_var[0] + '.poleVectorX'), 0)
    mc.setAttr((ikHandle_var[0] + '.poleVectorY'), 0)
    mc.setAttr((ikHandle_var[0] + '.poleVectorZ'), 0)

    ikHandle_effector_var = mc.listConnections(ikHandle_var, s=True, type='ikEffector')

    mc.rename(ikHandle_effector_var, ikHandle_var[0] + '_effector')

    #hide ik handle
    mc.setAttr(ikHandle_var[0] + '.visibility', 0)

    #parent ik handle global grp to organize
    mc.parent(ikHandle_var[0], myIKGrp)


    #___________ik handle CTRL____________#
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
        myCurve = mc.rename(mySel[0] + '_ik_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to l_leg_fk_list
        mc.parent(myGroup, mySel[-1], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)
        #zero ik ctrl rotations
        # mc.setAttr((myGroup + ".rotateX"), 0)
        # mc.setAttr((myGroup + ".rotateY"), 0)
        # mc.setAttr((myGroup + ".rotateZ"), 0)

        mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
        mc.parentConstraint(myCurve, mySel[-1], st=('x','y','z'))

        #parent grp to global grp to organize
        mc.parent(myGroup, myIKGrp)


    
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
        myCurve = mc.rename(mySel[0] + '_poleVector_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        
        
        #___more accurate mid point (for "hip_to_ankle_scaled")___
        #length of knee to ankle
        shin_len = (mc.getAttr(mySel[1] + '.translateX') + mc.getAttr(mySel[-1] + '.translateX'))
        #length of hip to knee
        upperLeg_len = mc.getAttr(mySel[1] + '.translateX')
        #divide sum of leg lengths by hip length (for more accurate mid point)
        better_midPoint_var = (shin_len / upperLeg_len)

        
        #__vector math____#
        #vector positions of hip, knee, ankle
        hip_pos = om.MVector(mc.xform(mySel[0], q=True, rp=True, ws=True))
        knee_pos = om.MVector(mc.xform(mySel[1], q=True, rp=True, ws=True))
        ankle_pos = om.MVector(mc.xform(mySel[-1], q=True, rp=True, ws=True))

        #finding vector point of pv knee (on plane of hip, knee, ankle)
        hip_to_ankle = ankle_pos - hip_pos
        hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
        mid_point = hip_pos + hip_to_ankle_scaled
        mid_point_to_knee_vec = knee_pos - mid_point
        mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 4
        mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

        #final polve vector point (to avoid knee changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

        myAimConst = mc.aimConstraint(  mySel[1], myGroup, 
                                        offset=(0, 0, 0), 
                                        weight=1, 
                                        aimVector=(0, 0, -1), 
                                        upVector=(0, 1, 0), 
                                        worldUpType=('vector'), 
                                        worldUpVector=(0, 1, 0))
        mc.delete(myAimConst)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, ikHandle_var[0])

        #parent grp to global grp to organize
        mc.parent(myGroup, myIKGrp)



#______________________________________________________________#
#____________IK/FK Limb Blend @mkr ____________________________#
#______________________________________________________________#
def create_fk_ik_limb():
    #______________________________#
    #_____Blended Joint Chain______#
    #______________________________#
    mySel = mc.ls(sl=True)
    fkJoint_list = []
    ikJoint_list = []
    for i in mySel:
        #______________________#
        #____create FK chain___#
        fkJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        
        fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
        mc.Unparent(fkJoint)
        
        fkJoint_list.append(fkJoint)
        
        #______________________#
        #____create _IK chain___#
        ikJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", .1)
        mc.setAttr(".overrideColorG", .9)
        mc.setAttr(".overrideColorB", 0.1)
        
        ikJoint = mc.rename(ikJoint_orig, ('IK_' + i))
        mc.Unparent(ikJoint)
        
        ikJoint_list.append(ikJoint)
    
    #parent FK joints together based on current index
    currentIndex = -1
    for i in fkJoint_list:
        currentIndex += 1
        if i != fkJoint_list[0]:
            mc.parent(fkJoint_list[currentIndex], fkJoint_list[currentIndex-1])
    #parent IK joints together based on current index
    currentIndex = -1
    for i in ikJoint_list:
        currentIndex += 1
        print (currentIndex)
        if i != ikJoint_list[0]:
            mc.parent(ikJoint_list[currentIndex], ikJoint_list[currentIndex-1])
    
    #blend color node lists
    blendColorsTran_list = []
    blendColorsRot_list = []
    blendColorsScale_list = []
    #blend joints together
    for i_FK, i_IK, i in itertools.izip(fkJoint_list, ikJoint_list, mySel):
        #create blend color nodes
        blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
        blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
        blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')
        #translate
        mc.connectAttr((i_FK + ".translate"), (blendColorsTran + ".color1"), f=True)
        mc.connectAttr((i_IK + ".translate"), (blendColorsTran + ".color2"), f=True)
        mc.connectAttr((blendColorsTran + ".output"), (i + ".translate"), f=True)
        #rotate
        mc.connectAttr((i_FK + ".rotate"), (blendColorsRot + ".color1"), f=True)
        mc.connectAttr((i_IK + ".rotate"), (blendColorsRot + ".color2"), f=True)
        mc.connectAttr((blendColorsRot + ".output"), (i + ".rotate"), f=True)
        #scale
        mc.connectAttr((i_FK + ".scale"), (blendColorsScale + ".color1"), f=True)
        mc.connectAttr((i_IK + ".scale"), (blendColorsScale + ".color2"), f=True)
        mc.connectAttr((blendColorsScale + ".output"), (i + ".scale"), f=True)
        #append lists for outside loop use
        blendColorsTran_list.append(blendColorsTran)
        blendColorsRot_list.append(blendColorsRot)
        blendColorsScale_list.append(blendColorsScale)


    #______________________________#
    #_________FK Controls__________#
    #______________________________#
    #create list for ctrl grp parenting to one another
    fk_ctrl_grp_list = []
    #create list for ctrl parenting to one another
    fk_ctrl_list = []
    #create nurbs curve ctrls
    for i in fkJoint_list:
        #create curve box
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
        myCurve_name = mc.rename(i + '_ctrl')

        #group curve
        curveGroup = mc.group(myCurve_name)
        curveGroup_offset = mc.group(myCurve_name)
        #rename group
        curveGroup_name = mc.rename(curveGroup, (myCurve_name + '_grp'))
        curveGroup_offset_name = mc.rename(curveGroup_offset, (myCurve_name + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(curveGroup_name, i, relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(curveGroup_name)
        #create a list for the groups (for parenting to one another)
        fk_ctrl_grp_list.append(curveGroup_name)
        #create a list of the ctrl curves (to parent constrain the joints to)
        fk_ctrl_list.append(myCurve_name)

        #parent constrain ctrls to fk jnts
        mc.parentConstraint(myCurve_name, i)

    
    #remove first and last of lists to correctly parent ctrls and grps together in for loop
    fk_ctrl_grp_list_temp = fk_ctrl_grp_list[1:]
    print(fk_ctrl_grp_list_temp)
    fk_ctrl_list_temp = fk_ctrl_list[:-1]
    print(fk_ctrl_list_temp)

    #parent ctrls and grps together
    for i_grp, i_ctrl in itertools.izip(fk_ctrl_grp_list_temp, fk_ctrl_list_temp):
        mc.parent(i_grp, i_ctrl)


    #_____________________________________#
    #______________IK Ctrls_______________#
    #_____________________________________#
    #group for organization
    myIKGrp = mc.group(em=True, n=ikJoint_list[0] + '_ik_grp')
    
    #___________create IK HANDLE____________#

    ikHandle_var = mc.ikHandle(n=ikJoint_list[0] + '_ikHandkle', sj=ikJoint_list[0], ee=ikJoint_list[-1])

    mc.setAttr((ikHandle_var[0] + '.poleVectorX'), 0)
    mc.setAttr((ikHandle_var[0] + '.poleVectorY'), 0)
    mc.setAttr((ikHandle_var[0] + '.poleVectorZ'), 0)

    ikHandle_effector_var = mc.listConnections(ikHandle_var, s=True, type='ikEffector')

    mc.rename(ikHandle_effector_var, ikHandle_var[0] + '_effector')

    #hide ik handle
    mc.setAttr(ikHandle_var[0] + '.visibility', 0)

    #parent ik handle global grp to organize
    mc.parent(ikHandle_var[0], myIKGrp)


    #___________ik handle CTRL____________#
    ik_group_list = []
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
        myCurve = mc.rename(ikJoint_list[0] + '_ik_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp to joints
        mc.parent(myGroup, ikJoint_list[-1], relative=True)
        #unparent group (since it has correct position)
        mc.Unparent(myGroup)

        #translate contrain ik ctrl to ik handle
        mc.parentConstraint(myCurve, ikHandle_var[0], sr=('x','y','z'))
        #rotate constrain ik ctrl to ankle joint
        mc.parentConstraint(myCurve, ikJoint_list[-1], st=('x','y','z'))

        #parent grp to global grp to organize
        mc.parent(myGroup, myIKGrp)

        #append grp for outside use
        ik_group_list.append(myGroup)
    

    #_________________POLE VECTOR Start___________________#
    #_____________________________________________________#
    pv_group_list = []
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
        mc.setAttr((curveShape[0] + ".overrideColorRGB"), 1, 1, 0)
        #rename curve
        myCurve = mc.rename(ikJoint_list[0] + '_poleVector_ctrl')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        
        
        #middle index value of ik joints (middle joint)
        roughMedian = round(len(ikJoint_list)/2.0)

        #___more accurate mid point (for "hip_to_ankle_scaled")___
        #length of whole limb
        limb_lenA = 0
        for i in ikJoint_list:
            if i != ikJoint_list[0]:
                limb_lenA += mc.getAttr(i + '.translateX')
        #length of upper half of limb
        upperLimb_lenA = 0
        for i in ikJoint_list[:int(roughMedian)]:
            if i != ikJoint_list[0]:
                upperLimb_lenA += mc.getAttr(i + '.translateX')

        #divide sum of leg lengths by upper leg length (for more accurate mid point)
        better_midPoint_var = (limb_lenA / upperLimb_lenA)

        #__vector math____#
        #vector positions of hip, knee, ankle
        hip_pos = om.MVector(mc.xform(ikJoint_list[0], q=True, rp=True, ws=True))
        knee_pos = om.MVector(mc.xform(ikJoint_list[int(roughMedian-1.0)], q=True, rp=True, ws=True))
        ankle_pos = om.MVector(mc.xform(ikJoint_list[-1], q=True, rp=True, ws=True))

        #finding vector point of pv knee (on plane of hip, knee, ankle)
        hip_to_ankle = ankle_pos - hip_pos
        hip_to_ankle_scaled = hip_to_ankle / better_midPoint_var #/two-ish
        mid_point = hip_pos + hip_to_ankle_scaled
        mid_point_to_knee_vec = knee_pos - mid_point
        mid_point_to_knee_vec_scaled = mid_point_to_knee_vec * 3  #pv ctrl distance from knee multiplier
        mid_point_to_knee_point = mid_point + mid_point_to_knee_vec_scaled

        #final polve vector point (to avoid knee changing position on creation)
        final_PV_point = mc.xform(myGroup, t=mid_point_to_knee_point)

        myAimConst = mc.aimConstraint(  ikJoint_list[int(roughMedian-1.0)], myGroup, 
                                        offset=(0, 0, 0), 
                                        weight=1, 
                                        aimVector=(0, 0, -1), 
                                        upVector=(0, 1, 0), 
                                        worldUpType=('vector'), 
                                        worldUpVector=(0, 1, 0))
        mc.delete(myAimConst)

        #___connect pole vector
        mc.poleVectorConstraint(myCurve, ikHandle_var[0])

        #parent grp to global grp to organize
        mc.parent(myGroup, myIKGrp)

        pv_group_list.append(myGroup)


    #______________________________________________________________________________#
    #____________________________IK/ FK Switch Ctrl @mkr ________________________________#
    #______________________________________________________________________________#
    switch_ctrl_list = []
    switch_ctrl_grp_list = []
    for items in range(0,1):
        #name circle curves
        switchCurveA_name = 'switch_ctrlA#'
        switchCurveB_name = 'switch_ctrlB#'
        switchCurveC_name = 'switch_ctrlC#'

        #create nurbs circle
        switchCurveA = mc.circle(n=switchCurveA_name, ch=False, r=3, nr=(0,1,0))
        #create variable for nurbs circle shape
        switchCurveA_shape = mc.listRelatives(switchCurveA, s=True)
        #color nurbs circle shape
        mc.setAttr((switchCurveA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveA_shape[0] + ".overrideColorRGB"), 0, .5, 1)

        #create 2nd nurbs circle
        switchCurveB = mc.circle(n=switchCurveB_name, ch=False, r=3, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        switchCurveB_shape = mc.listRelatives(switchCurveB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((switchCurveB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveB_shape[0] + ".overrideColorRGB"), 0, .5, 1)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveB_shape, switchCurveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(switchCurveB)

        #create 3rd nurbs circle
        switchCurveC = mc.circle(n=switchCurveC_name, ch=False, r=3, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        switchCurveC_shape = mc.listRelatives(switchCurveC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((switchCurveC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((switchCurveC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((switchCurveC_shape[0] + ".overrideColorRGB"), 0, .5, 1)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(switchCurveC_shape, switchCurveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(switchCurveC)

        #_______group switch ctrl_______#
        switchCurveA_grp = mc.group(switchCurveA, n = (switchCurveA_name + '_grp'))
        switchCurveA_l_grp_offset = mc.group(switchCurveA, n = (switchCurveA_name + '_grp_offset'))

        #_______move ctrl shapes in -z_______#
        mc.setAttr((switchCurveA[0] + ".translateY"), 20)
        mc.xform (switchCurveA, ws=True, piv= (0, 0, 0))
        mc.makeIdentity(switchCurveA, apply=True)

        #_______move joint to ankle and parent_______#
        #parent and zero joints to last joint in selection
        mc.parent(switchCurveA_grp, mySel[-1], relative=True)
        #parent joints to world space
        mc.Unparent(switchCurveA_grp)

        # parent constrain switch ctrl to ankle
        mc.parentConstraint(mySel[-1], switchCurveA_grp, mo=True)

        #_______add IK FK Blend attr to switch ctrl_______#
        mc.addAttr(switchCurveA, ln = "fk_ik_blend", min=0, max=1, k=True)

        #lock and hide unneeded attributes for switch ctrl
        mc.setAttr((switchCurveA[0] + '.tx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.ty'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.tz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.rx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.ry'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.rz'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sx'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sy'), lock=True, keyable=False, channelBox=False)
        mc.setAttr((switchCurveA[0] + '.sz'), lock=True, keyable=False, channelBox=False)

        switch_ctrl_list.append(switchCurveA[0])
        switch_ctrl_grp_list.append(switchCurveA_grp)


    #_______connect switch control to blendNodes_______#
    for items_trans, items_rot, items_scale in itertools.izip(  blendColorsTran_list, 
                                                                blendColorsRot_list, 
                                                                blendColorsScale_list):
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_trans + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_rot + '.blender'), f=True)
        mc.connectAttr((switch_ctrl_list[0] + '.fk_ik_blend'), (items_scale + '.blender'), f=True)


    #_______connect switch control to visibility______#
    for i in range(0,1): 
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 0)
        mc.setAttr((ik_group_list[0] + '.visibility'), 1)
        mc.setAttr((pv_group_list[0] + '.visibility'), 1)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 0)
        mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setAttr((switch_ctrl_list[0] + '.fk_ik_blend'), 1)
        mc.setAttr((ik_group_list[0] + '.visibility'), 0)
        mc.setAttr((pv_group_list[0] + '.visibility'), 0)
        mc.setAttr((fk_ctrl_grp_list[0] + '.visibility'), 1)
        mc.setDrivenKeyframe((ik_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((pv_group_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))
        mc.setDrivenKeyframe((fk_ctrl_grp_list[0] + '.visibility'), currentDriver = (switch_ctrl_list[0] + '.fk_ik_blend'))


    #organize into final group
    ik_fk_blend_grp = mc.group(em=True, n='ik_fk_blend_grp')
    mc.parent(fk_ctrl_grp_list[0], ik_fk_blend_grp)
    mc.parent(switch_ctrl_grp_list[0], ik_fk_blend_grp)
    mc.parent(myIKGrp, ik_fk_blend_grp)
    #parent joints to final group too
    mc.parent(fkJoint_list[0], ik_fk_blend_grp)
    mc.parent(ikJoint_list[0], ik_fk_blend_grp)
    

#________________________END of FK/IK BLEND______________________________________#


def simple_blend_joints():
    # Select Fk, then IK, then Main
    # Set up Switch control seperatly

    #my selection
    mySel = mc.ls(sl=True)

    blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
    blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
    blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')

    ####
    mc.connectAttr((mySel[0] + ".translate"), (blendColorsTran + ".color1"), f=True)
    mc.connectAttr((mySel[1] + ".translate"), (blendColorsTran + ".color2"), f=True)
    mc.connectAttr((blendColorsTran + ".output"), (mySel[2] + ".translate"), f=True)

    ####
    mc.connectAttr((mySel[0] + ".rotate"), (blendColorsRot + ".color1"), f=True)
    mc.connectAttr((mySel[1] + ".rotate"), (blendColorsRot + ".color2"), f=True)
    mc.connectAttr((blendColorsRot + ".output"), (mySel[2] + ".rotate"), f=True)

    ####
    mc.connectAttr((mySel[0] + ".scale"), (blendColorsScale + ".color1"), f=True)
    mc.connectAttr((mySel[1] + ".scale"), (blendColorsScale + ".color2"), f=True)
    mc.connectAttr((blendColorsScale + ".output"), (mySel[2] + ".scale"), f=True)


def blend_joint_chain():
    mySel = mc.ls(sl=True)
    fkJoint_list = []
    ikJoint_list = []
    for i in mySel:
        #______________________#
        #____create FK chain___#
        fkJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr(".radius", 4)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", 1)
        mc.setAttr(".overrideColorG", 0)
        mc.setAttr(".overrideColorB", 0.1)
        
        fkJoint = mc.rename(fkJoint_orig, ('FK_' + i))
        mc.Unparent(fkJoint)
        
        fkJoint_list.append(fkJoint)
        
        #______________________#
        #____create _K chain___#
        ikJoint_orig = mc.joint(i)
        
        #joint visual size
        mc.setAttr(".radius", 3)
        #joint color
        mc.setAttr(".overrideEnabled", 1)
        mc.setAttr(".overrideRGBColors", 1)
        mc.setAttr(".overrideColorR", .1)
        mc.setAttr(".overrideColorG", .9)
        mc.setAttr(".overrideColorB", 0.1)
        
        ikJoint = mc.rename(ikJoint_orig, ('IK_' + i))
        mc.Unparent(ikJoint)
        
        ikJoint_list.append(ikJoint)
    
    currentIndex = -1
    for i in fkJoint_list:
        currentIndex += 1
        if i != fkJoint_list[0]:
            mc.parent(fkJoint_list[currentIndex], fkJoint_list[currentIndex-1])

    currentIndex = -1
    for i in ikJoint_list:
        currentIndex += 1
        print (currentIndex)
        if i != ikJoint_list[0]:
            mc.parent(ikJoint_list[currentIndex], ikJoint_list[currentIndex-1])
    
    for i_FK, i_IK, i in itertools.izip(fkJoint_list, ikJoint_list, mySel):
        blendColorsTran = mc.createNode('blendColors', n='blendColorsTran#')
        blendColorsRot = mc.createNode('blendColors', n='blendColorsRot#')
        blendColorsScale = mc.createNode('blendColors', n='blendColorsScale#')
        #translate
        mc.connectAttr((i_FK + ".translate"), (blendColorsTran + ".color1"), f=True)
        mc.connectAttr((i_IK + ".translate"), (blendColorsTran + ".color2"), f=True)
        mc.connectAttr((blendColorsTran + ".output"), (i + ".translate"), f=True)
        #rotate
        mc.connectAttr((i_FK + ".rotate"), (blendColorsRot + ".color1"), f=True)
        mc.connectAttr((i_IK + ".rotate"), (blendColorsRot + ".color2"), f=True)
        mc.connectAttr((blendColorsRot + ".output"), (i + ".rotate"), f=True)
        #scale
        mc.connectAttr((i_FK + ".scale"), (blendColorsScale + ".color1"), f=True)
        mc.connectAttr((i_IK + ".scale"), (blendColorsScale + ".color2"), f=True)
        mc.connectAttr((blendColorsScale + ".output"), (i + ".scale"), f=True)
        

#avaliable for reverse foot function
rvFoot_loc_list = []
def rev_foot_locators():
    del rvFoot_loc_list [:]
    #loc_ankle
    loc_ankle = mc.spaceLocator(n='loc_ankle#')
    mc.setAttr((loc_ankle[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_ankle[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_ankle[0] + ".overrideColorRGB"), .1, 1, 0)
    mc.setAttr((loc_ankle[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_ankle[0] + ".translate"), 10.738,9.708,-3.181)
    mc.setAttr((loc_ankle[0] + ".rotate"), 5.278, -82.31, -5.275)
    #loc_toe
    loc_toe = mc.spaceLocator(n='loc_toe#')
    mc.setAttr((loc_toe[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_toe[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_toe[0] + ".overrideColorRGB"), .1, 1, 0)
    mc.setAttr((loc_toe[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_toe[0] + ".translate"), 12.597,2.148,9.648)
    mc.setAttr((loc_toe[0] + ".rotate"), 5.278, -82.31, -5.275)
    #loc_toe_end
    loc_toe_end = mc.spaceLocator(n='loc_toe_end#')
    mc.setAttr((loc_toe_end[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_toe_end[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_toe_end[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_toe_end[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_toe_end[0] + ".translate"), 13.41,0.224,15.601)
    mc.setAttr((loc_toe_end[0] + ".rotate"), 0.156, -82.539, 0.825)
    #loc_heel
    loc_heel = mc.spaceLocator(n='loc_heel#')
    mc.setAttr((loc_heel[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_heel[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_heel[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((loc_heel[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_heel[0] + ".translate"), 9.547,0.166,-6.787)
    mc.setAttr((loc_heel[0] + ".rotate"), 0.156, -82.539, 0.825)
    #loc_outer_foot
    loc_outer_foot = mc.spaceLocator(n='loc_outer_foot#')
    mc.setAttr((loc_outer_foot[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_outer_foot[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_outer_foot[0] + ".overrideColorRGB"), 1, .1, 0)
    mc.setAttr((loc_outer_foot[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_outer_foot[0] + ".translate"), 17.04,0.289,7.031)
    mc.setAttr((loc_outer_foot[0] + ".rotate"), 0.076, -74.621, 0.906)
    #loc_inner_foot
    loc_inner_foot = mc.spaceLocator(n='loc_inner_foot#')
    mc.setAttr((loc_inner_foot[0] + ".overrideEnabled"), 1)
    mc.setAttr((loc_inner_foot[0] + ".overrideRGBColors"), 1)
    mc.setAttr((loc_inner_foot[0] + ".overrideColorRGB"), 1, .1, 0)
    mc.setAttr((loc_inner_foot[0] + ".localScale"), 5, 5, 5)
    mc.setAttr((loc_inner_foot[0] + ".translate"), 7.205,0.119,10.571)
    mc.setAttr((loc_inner_foot[0] + ".rotate"), 0.782, -88.52, 0.198)

    #append back into list for rig
    rvFoot_loc_list.extend((loc_ankle[0], 
                            loc_toe[0],
                            loc_toe_end[0],
                            loc_heel[0],
                            loc_outer_foot[0],
                            loc_inner_foot[0]))
    loc_list_grp = mc.group(n='rvFoot_loc_grp#', em=True)
    mc.parent(rvFoot_loc_list, loc_list_grp)


#___________Reverse Foot Rig_____________#
def reverse_foot_setup():
    ftCtrl_list = []
    ftCtrl_grp_list = []

    for i in rvFoot_loc_list:
        
        #name circle curves
        locCurveA_name = i.replace('loc_', 'ftCtrl_')
        locCurveB_name = i.replace('loc_', 'ftCtrl_') + 'A'
        locCurveC_name = i.replace('loc_', 'ftCtrl_') + 'B'

        #create nurbs circle
        locCurveA = mc.circle(n=locCurveA_name, ch=False, r=3, nr=(0,1,0))
        #create variable for nurbs circle shape
        locCurveA_shape = mc.listRelatives(locCurveA, s=True)
        #color nurbs circle shape
        mc.setAttr((locCurveA_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveA_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveA_shape[0] + ".overrideColorRGB"), .5, 1, 0)

        #create 2nd nurbs circle
        locCurveB = mc.circle(n=locCurveB_name, ch=False, r=3, nr=(0,0,0))
        #create variable for 2nd nurbs circle shape
        locCurveB_shape = mc.listRelatives(locCurveB, s=True)
        #color 2nd nurbs circle shape
        mc.setAttr((locCurveB_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveB_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveB_shape[0] + ".overrideColorRGB"), .5, 1, 0)
        #parent 2nd nurbs circle shape to first nurbs circle
        mc.parent(locCurveB_shape, locCurveA, r=True, shape=True)
        #delete 2nd nurbs circle transform
        mc.delete(locCurveB)

        #create 3rd nurbs circle
        locCurveC = mc.circle(n=locCurveC_name, ch=False, r=3, nr=(1,0,0))
        #create variable for 3rd nurbs circle shape
        locCurveC_shape = mc.listRelatives(locCurveC, s=True)
        #color 3rd nurbs circle shape
        mc.setAttr((locCurveC_shape[0] + ".overrideEnabled"), 1)
        mc.setAttr((locCurveC_shape[0] + ".overrideRGBColors"), 1)
        mc.setAttr((locCurveC_shape[0] + ".overrideColorRGB"), .5, 1, 0)
        #parent 3rd nurbs circle shape to first nurbs circle
        mc.parent(locCurveC_shape, locCurveA, r=True, shape=True)
        #delete 3rd nurbs circle transform
        mc.delete(locCurveC)

        #_______group ctrl_______#
        locCurveA_grp = mc.group(locCurveA, n = (locCurveA[0] + '_grp'))
        locCurveA_grp_offset = mc.group(locCurveA, n = (locCurveA[0] + '_grp_offset'))
        
        #_______move ctrl grp to loc_______#
        mc.parent(locCurveA_grp, i, relative=True)
        mc.Unparent(locCurveA_grp)
        #add/ create list for ftCtrl's
        ftCtrl_list.append(locCurveA)
        ftCtrl_grp_list.append(locCurveA_grp)
    
    #group reverse foot ctrls together
    mc.parent(ftCtrl_grp_list[4], ftCtrl_list[5])
    mc.parent(ftCtrl_grp_list[3], ftCtrl_list[4])
    mc.parent(ftCtrl_grp_list[2], ftCtrl_list[3])
    mc.parent(ftCtrl_grp_list[1], ftCtrl_list[2])
    mc.parent(ftCtrl_grp_list[0], ftCtrl_list[1])


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
        myCurve = mc.rename('ftCtrl_toe_toeWiggle#')
        #group curve
        curveGrouped = mc.group(myCurve)
        curveGrouped_offset = mc.group(myCurve)
        #rename group
        myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
        myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))
        #parent and zero curveGrp
        mc.parent(myGroup, ftCtrl_list[1], relative=True)
        #unparent after getting position
        mc.Unparent(myGroup)
        #reparent to toe_end
        mc.parent(myGroup, ftCtrl_list[2], relative=False)

    #clear selection
    mc.select(cl=True)


def nurbs_curve_cube():
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
    mc.setAttr((curveShape[0] + ".overrideColorR"), 1)
    mc.setAttr((curveShape[0] + ".overrideColorG"), .1)
    mc.setAttr((curveShape[0] + ".overrideColorB"), 0)
    #rename curve
    myCurve = mc.rename('cubeCurve_ctrl#')
    #group curve
    curveGrouped = mc.group(myCurve)
    curveGrouped_offset = mc.group(myCurve)
    #rename group
    myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
    myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))


def nurbs_curve_sphere():
    #name circle curves
    curveA_name = 'circleCurveA_ctrl#'
    curveB_name = 'circleCurveB_ctrl#'
    curveC_name = 'circleCurveC_ctrl#'

    #create nurbs circle
    curveA = mc.circle(n=curveA_name, ch=False, r=3, nr=(0,1,0))
    #create variable for nurbs circle shape
    curveA_shape = mc.listRelatives(curveA, s=True)
    #color nurbs circle shape
    mc.setAttr((curveA_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((curveA_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((curveA_shape[0] + ".overrideColorR"), .8)
    mc.setAttr((curveA_shape[0] + ".overrideColorG"), .8)
    mc.setAttr((curveA_shape[0] + ".overrideColorB"), 0)

    #create 2nd nurbs circle
    curveB = mc.circle(n=curveB_name, ch=False, r=3, nr=(0,0,0))
    #create variable for 2nd nurbs circle shape
    curveB_shape = mc.listRelatives(curveB, s=True)
    #color 2nd nurbs circle shape
    mc.setAttr((curveB_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((curveB_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((curveB_shape[0] + ".overrideColorR"), .8)
    mc.setAttr((curveB_shape[0] + ".overrideColorG"), .8)
    mc.setAttr((curveB_shape[0] + ".overrideColorB"), 0)
    #parent 2nd nurbs circle shape to first nurbs circle
    mc.parent(curveB_shape, curveA, r=True, shape=True)
    #delete 2nd nurbs circle transform
    mc.delete(curveB)

    #create 3rd nurbs circle
    curveC = mc.circle(n=curveC_name, ch=False, r=3, nr=(1,0,0))
    #create variable for 3rd nurbs circle shape
    curveC_shape = mc.listRelatives(curveC, s=True)
    #color 3rd nurbs circle shape
    mc.setAttr((curveC_shape[0] + ".overrideEnabled"), 1)
    mc.setAttr((curveC_shape[0] + ".overrideRGBColors"), 1)
    mc.setAttr((curveC_shape[0] + ".overrideColorR"), .8)
    mc.setAttr((curveC_shape[0] + ".overrideColorG"), .8)
    mc.setAttr((curveC_shape[0] + ".overrideColorB"), 0)
    #parent 3rd nurbs circle shape to first nurbs circle
    mc.parent(curveC_shape, curveA, r=True, shape=True)
    #delete 3rd nurbs circle transform
    mc.delete(curveC)

    #_______group switch ctrl_______#
    curveA_grp = mc.group(curveA, n = (curveA[0] + '_grp'))
    curveA_grp_offset = mc.group(curveA, n = (curveA[0] + '_grp_offset'))

    
def nurbs_curve_arrow():
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
    mc.setAttr((curveShape[0] + ".overrideColorG"), .1)
    mc.setAttr((curveShape[0] + ".overrideColorB"), 1)
    #rename curve
    myCurve = mc.rename('arrowCurve_ctrl#')
    #group curve
    curveGrouped = mc.group(myCurve)
    curveGrouped_offset = mc.group(myCurve)
    #rename group
    myGroup = mc.rename(curveGrouped, (myCurve + '_grp'))
    myGroup_offset = mc.rename(curveGrouped_offset, (myCurve + '_grp_offset'))



#_________________Animation Functions @mkp ______________________#
#__________________________________________________________#

def multi_parent_const():
    mySel = mc.ls(sl=True)
    for i in mySel:
        if i != mySel[-1]:
            mc.parentConstraint(mySel[-1], i, mo=True, weight=True)

def reset_ctrls():
    mySel = mc.ls(sl=True)
    for i in mySel:
        mc.setAttr((i + ".translate"), 0,0,0)
        mc.setAttr((i + ".rotate"), 0,0,0)
        mc.setAttr((i + ".scale"), 1,1,1)
    
def create_locator():
    myLoc = mc.spaceLocator()
    mc.setAttr((myLoc[0] + ".overrideEnabled"), 1)
    mc.setAttr((myLoc[0] + ".overrideRGBColors"), 1)
    mc.setAttr((myLoc[0] + ".overrideColorRGB"), 1, 1, 0)
    mc.setAttr((myLoc[0] + ".localScale"), 15, 15, 15)
    mc.rename('temp_loc')

def mirror_ctrls():
    #selection
    mySel = mc.ls(sl=True)
    #prefix text
    left_prefix = mc.textField('l_hip_text', query=True, text=True)
    right_prefix = mc.textField('r_hip_text', query=True, text=True)
    #multiplier text
    tranX_mult = mc.textField('translateX_text', query=True, text=True)
    tranY_mult = mc.textField('translateY_text', query=True, text=True)
    tranZ_mult = mc.textField('translateZ_text', query=True, text=True)
    rotX_mult = mc.textField('rotateX_text', query=True, text=True)
    rotY_mult = mc.textField('rotateY_text', query=True, text=True)
    rotZ_mult = mc.textField('rotateZ_text', query=True, text=True)

    #mirrioring values of ctrls with correct prefix
    for i in mySel:
        #switching L_R_ prefix
        subVar = i.replace(left_prefix, right_prefix)
        mc.copyAttr(i, subVar, values=True, attribute=('translate', 'rotate', 'scale'))

        #get values of right side to multiply offset
        subVarTX = mc.getAttr(subVar + '.translateX')
        subVarTY = mc.getAttr(subVar + '.translateY')
        subVarTZ = mc.getAttr(subVar + '.translateZ')
        subVarRX = mc.getAttr(subVar + '.rotateX')
        subVarRY = mc.getAttr(subVar + '.rotateY')
        subVarRZ = mc.getAttr(subVar + '.rotateZ')
        # multiply trans, and rotation, by text fields to reverse etc
        mc.setAttr((subVar + '.translateX'), (subVarTX * float(tranX_mult)))
        mc.setAttr((subVar + '.translateY'), (subVarTY * float(tranY_mult)))
        mc.setAttr((subVar + '.translateZ'), (subVarTZ * float(tranZ_mult)))
        mc.setAttr((subVar + '.rotateX'), (subVarRX * float(rotX_mult)))
        mc.setAttr((subVar + '.rotateY'), (subVarRY * float(rotY_mult)))
        mc.setAttr((subVar + '.rotateZ'), (subVarRZ * float(rotZ_mult)))

    #set focus back to maya
    mc.setFocus('MayaWindow')



#_________________Other Functions @mkp ______________________#
#____________________________________________________________#

#_______________________________#
#change color of selection "SHAPE"
#_______________________________#

def slider_move():
    #query current slider value
    color1 = mc.intSlider('slider_value', q=True, value=True)
    #my selection
    mySel = mc.ls(sl=True)
    #apply color to selection shapes
    if color1 == 0: 
        mc.iconTextButton('color', e=True, bgc=(0.5, .5, 0.5))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 0)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 0)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), 0.5, 0.5, 0.5)
    if color1 == 1: 
        mc.iconTextButton('color', e=True, bgc=(.8, 0, .9))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), .8, 0, .9)
    if color1 == 2: 
        mc.iconTextButton('color', e=True, bgc=(1, .2, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), 1, .2, 0)
    if color1 == 3: 
        mc.iconTextButton('color', e=True, bgc=(1, 1, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), 1, 1, 0)
    if color1 == 4: 
        mc.iconTextButton('color', e=True, bgc=(0.6, 0, 0.15))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), 0.6, 0, 0.15)
    if color1 == 5: 
        mc.iconTextButton('color', e=True, bgc=(0, 0.9, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr((selShape[0] + ".overrideEnabled"), 1)
            mc.setAttr((selShape[0] + ".overrideRGBColors"), 1)
            mc.setAttr((selShape[0] + ".overrideColorRGB"), 0, .9, 0)

#_______________________________#
#change color of selection "TRANSFORM"
#_______________________________#

def transform_slider_move():
    #query current slider value
    color1 = mc.intSlider('transform_slider_value', q=True, value=True)
    #my selection
    mySel = mc.ls(sl=True)
    #apply color to selection shapes
    if color1 == 0: 
        mc.iconTextButton('transform_color', e=True, bgc=(0.5, .5, 0.5))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 0)
            mc.setAttr((i + ".overrideRGBColors"), 0)
            mc.setAttr((i + ".overrideColorRGB"), 0.5, 0.5, 0.5)
    if color1 == 1: 
        mc.iconTextButton('transform_color', e=True, bgc=(.8, 0, .9))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 1)
            mc.setAttr((i + ".overrideRGBColors"), 1)
            mc.setAttr((i + ".overrideColorRGB"), .8, 0, .9)
    if color1 == 2: 
        mc.iconTextButton('transform_color', e=True, bgc=(1, .2, 0))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 1)
            mc.setAttr((i + ".overrideRGBColors"), 1)
            mc.setAttr((i + ".overrideColorRGB"), 1, .2, 0)
    if color1 == 3: 
        mc.iconTextButton('transform_color', e=True, bgc=(1, 1, 0))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 1)
            mc.setAttr((i + ".overrideRGBColors"), 1)
            mc.setAttr((i + ".overrideColorRGB"), 1, 1, 0)
    if color1 == 4: 
        mc.iconTextButton('transform_color', e=True, bgc=(0.6, 0, 0.15))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 1)
            mc.setAttr((i + ".overrideRGBColors"), 1)
            mc.setAttr((i + ".overrideColorRGB"), 0.6, 0, 0.15)
    if color1 == 5: 
        mc.iconTextButton('transform_color', e=True, bgc=(0, 0.9, 0))
        for i in mySel:
            mc.setAttr((i + ".overrideEnabled"), 1)
            mc.setAttr((i + ".overrideRGBColors"), 1)
            mc.setAttr((i + ".overrideColorRGB"), 0, .9, 0)


#_______________________________#
#change color of selection "WIRE" (Shape)
#_______________________________#

def wire_slider_move():
    #query current slider value
    color1 = mc.intSlider('wire_slider_value', q=True, value=True)
    #my selection
    mySel = mc.ls(sl=True)
    #apply color to selection shapes
    if color1 == 0: 
        mc.iconTextButton('wire_color', e=True, bgc=(0.5, .5, 0.5))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 0)
            mc.setAttr(selShape[0] + ".wireColorRGB", 0, 0, 0)
    if color1 == 1: 
        mc.iconTextButton('wire_color', e=True, bgc=(.8, 0, .9))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 2)
            mc.setAttr(selShape[0] + ".wireColorRGB", .8, 0, .9)
    if color1 == 2: 
        mc.iconTextButton('wire_color', e=True, bgc=(1, .2, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 2)
            mc.setAttr(selShape[0] + ".wireColorRGB", 1, .2, 0)
    if color1 == 3: 
        mc.iconTextButton('wire_color', e=True, bgc=(1, 1, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 2)
            mc.setAttr(selShape[0] + ".wireColorRGB", 1, 1, 0)
    if color1 == 4: 
        mc.iconTextButton('wire_color', e=True, bgc=(0.6, 0, 0.15))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 2)
            mc.setAttr(selShape[0] + ".wireColorRGB", 0.6, 0, 0.15)
    if color1 == 5: 
        mc.iconTextButton('wire_color', e=True, bgc=(0, 0.9, 0))
        for i in mySel:
            selShape = mc.listRelatives(i, s=True)
            mc.setAttr(selShape[0] + ".useObjectColor", 2)
            mc.setAttr(selShape[0] + ".wireColorRGB", 0, 0.9, 0)


#_______________________________#
#change color of selection "WIRE" (Transform)
#_______________________________#

def wireT_slider_move():
    #query current slider value
    color1 = mc.intSlider('wireT_slider_value', q=True, value=True)
    #my selection
    mySel = mc.ls(sl=True)
    #apply color to selection shapes
    if color1 == 0: 
        mc.iconTextButton('wireT_color', e=True, bgc=(0.5, .5, 0.5))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 0)
            mc.setAttr(i + ".wireColorRGB", 0, 0, 0)
    if color1 == 1: 
        mc.iconTextButton('wireT_color', e=True, bgc=(.8, 0, .9))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 2)
            mc.setAttr(i + ".wireColorRGB", .8, 0, .9)
    if color1 == 2: 
        mc.iconTextButton('wireT_color', e=True, bgc=(1, .2, 0))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 2)
            mc.setAttr(i + ".wireColorRGB", 1, .2, 0)
    if color1 == 3: 
        mc.iconTextButton('wireT_color', e=True, bgc=(1, 1, 0))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 2)
            mc.setAttr(i + ".wireColorRGB", 1, 1, 0)
    if color1 == 4: 
        mc.iconTextButton('wireT_color', e=True, bgc=(0.6, 0, 0.15))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 2)
            mc.setAttr(i + ".wireColorRGB", 0.6, 0, 0.15)
    if color1 == 5: 
        mc.iconTextButton('wireT_color', e=True, bgc=(0, 0.9, 0))
        for i in mySel:
            mc.setAttr(i + ".useObjectColor", 2)
            mc.setAttr(i + ".wireColorRGB", 0, 0.9, 0)


#_______________________________#
#Change Outliner color
#_______________________________#

def outliner_slider_move():
    #query current slider value
    color1 = mc.intSlider('outliner_slider_value', q=True, value=True)
    #my selection
    mySel = mc.ls(sl=True)
    #apply color to selection shapes
    if color1 == 0: 
        mc.iconTextButton('outliner_color', e=True, bgc=(0.5, .5, 0.5))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 0)
            mc.setAttr(i + ".outlinerColor", 0, 0, 0)
    if color1 == 1: 
        mc.iconTextButton('outliner_color', e=True, bgc=(.8, 0, .9))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 1)
            mc.setAttr(i + ".outlinerColor", .8, 0, .9)
    if color1 == 2: 
        mc.iconTextButton('outliner_color', e=True, bgc=(1, .2, 0))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 1)
            mc.setAttr(i + ".outlinerColor", 1, .2, 0)
    if color1 == 3: 
        mc.iconTextButton('outliner_color', e=True, bgc=(1, 1, 0))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 1)
            mc.setAttr(i + ".outlinerColor", 1, 1, 0)
    if color1 == 4: 
        mc.iconTextButton('outliner_color', e=True, bgc=(0.6, 0, 0.15))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 1)
            mc.setAttr(i + ".outlinerColor", 0.6, 0, 0.15)
    if color1 == 5: 
        mc.iconTextButton('outliner_color', e=True, bgc=(0, 0.9, 0))
        for i in mySel:
            mc.setAttr(i + ".useOutlinerColor", 1)
            mc.setAttr(i + ".outlinerColor", 0, 0.9, 0)

        
