# ui 
import maya.cmds as mc

import os

from ..tabs import modeling
from ..tabs import rigging
from ..tabs import animation
from ..tabs import color_slider

from ..ar_rig import character_rig


class rigger_ui_class():

    def rigger_ui_method(self):
    #close UI if already open
        if mc.window("nate_tools_ui", ex=True):
            mc.deleteUI("nate_tools_ui", window=True)

        mc.window("nate_tools_ui", t="Nate Tools!", rtf=True, s=True, menuBar=True, bgc = (0.2,0,0.2))

        #________________________layout Begin______________________________________#
        #__________________________________________________________________________#
        #main layout creation
        myForm = mc.formLayout()

        myColumn = mc.columnLayout( bgc=(0.1,0,0.1) )

        #_______Beginning Title_______#
        #to create border around edge
        mc.formLayout(myForm, edit=True, attachForm=[(myColumn, 'top', 10),(myColumn, 'bottom', 10),(myColumn, 'left', 10),(myColumn, 'right', 10)])

        #'Nate Tools!'
        mc.rowLayout( numberOfColumns=1)
        mc.text(label = 'Nate Tools!', height=20, width=454, align='center', bgc=(0.4,.7,0), font='boldLabelFont', statusBarMessage='Nate Tools!')
        mc.setParent("..")

        #_________________________declare Tabs____________________________________#
        #Insert Tabs
        myTabs = mc.tabLayout()

        #________________________________Auto Rig Tab @mkg _______________________________#
        #__________________________________________________________________________#
        # rigging tab column
       
        auto_rig_tab = mc.columnLayout()

        auto_rig_form = mc.formLayout(numberOfDivisions=100)


        auto_rig_s1 = mc.separator(style='none', w=454, h=10, bgc=(0,.448,1) )
        auto_rig_s2 = mc.separator(style='none', w=464, h=10, bgc=(0,.448,1) )
        auto_rig_s3 = mc.separator(style='none', h=265, w=10, bgc=(0,.448,1) )
        auto_rig_s4 = mc.separator(style='none', h=265, w=10, bgc=(0,.448,1) )

        auto_rig_b1 = mc.symbolButton(  image = os.path.abspath( os.path.join(__file__, "..", "..", "icons/", "RIG_ME.png") ),
                                        h=130, 
                                        w=230, 
                                        command = 'character_rigger.ar_rig.character_rig.character_rig()',
                                        statusBarMessage='Auto Rig Character.  No Joint Names Required. Must have tongue, bot face joints, and top face joints.'
                                    )
        auto_rig_b2 = mc.button(label='L \n Rev Foot \n Locators', 
                                h=50, 
                                w=60, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().rev_foot_adj("left")', 
                                bgc = (.2,.5,0), 
                                statusBarMessage='Only needed if want to adjust rev ft loc positions and not in scene yet.')
        auto_rig_b3 = mc.button(label='R \n Rev Foot \n Locators', 
                                h=50, 
                                w=60, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().rev_foot_adj("right")',
                                bgc = (0,.5,.2), 
                                statusBarMessage='Only needed if want to adjust rev ft loc positions and not in scene yet.')
        # corner lips
        auto_rig_text1 = mc.text(   label = 'Mid Face Jnts:', width=85, height=24, bgc=(0.4,0,0.4), align='center', font = 'boldLabelFont', 
                                    statusBarMessage='Amount of Mid Face Joints to be weighted between top face and bot face jnts. First 2 mid joints might be the lip corners.  Then the next 2 lowest top face joints, might be the cheeks.')
        auto_rig_textF1 = mc.textField( 'midFace_jnt_amnt_text', width=40, h=24, text='2', bgc=(.2,0,.2), 
                                        statusBarMessage='Amount of Mid Face Joints to be weighted between top face and bot face jnts.  First 2 mid joints might be the lip corners.  Then the next lowest top face joints, might be the cheeks.' )
        auto_rig_text2 = mc.text(   label = 'Control Size:', width=85, height=24, bgc=(0.4,0,0.4), align='center', font = 'boldLabelFont', 
                                    statusBarMessage='')
        auto_rig_textF2 = mc.textField( 'global_ctrl_size_text', width=40, h=24, text='0.5', bgc=(.2,0,.2), 
                                        statusBarMessage='' )
        headJnts_checkbox = mc.checkBox('headJnts_checkbox', 
                                        label='Head Jnts', 
                                        value=True, 
                                        bgc=(.4,0,.4), 
                                        width=115, 
                                        height=24,
                                        statusBarMessage='If unchecked, will not look for face joints.' +  
                                        ' For instance, uncheck if mocap skeleton with only top head joint and no face joints, ear joints, or tongue joints.' )
        twstJnts_checkbox = mc.checkBox('twstJnts_checkbox', 
                                        label='ForeArm Twst Jnts', 
                                        value=True, 
                                        bgc=(.4,0,.4), 
                                        width=115, 
                                        height=24,
                                        statusBarMessage='Uncheck if no forearm twist jnts.  Also, wrist jnt should be parented to elbow, not twist jnt end (a current rig limitation.)')
        
        mc.formLayout(  auto_rig_form,
                        edit=True, 
                        attachForm=[(auto_rig_s1 , 'top', 0),(auto_rig_s1 , 'left', 0),
                                    (auto_rig_s2 , 'top', 265),(auto_rig_s2 , 'left', 0),
                                    (auto_rig_s3 , 'top', 0),(auto_rig_s3 , 'left', 0),
                                    (auto_rig_s4 , 'top', 0),(auto_rig_s4 , 'left', 454),
                                    (auto_rig_b1 , 'top', 90),(auto_rig_b1 , 'left', 115),
                                    (auto_rig_b2 , 'top', 15),(auto_rig_b2 , 'left', 325),
                                    (auto_rig_b3 , 'top', 15),(auto_rig_b3 , 'left', 390),
                                    (auto_rig_text1 , 'top', 20),(auto_rig_text1 , 'left', 20),
                                    (auto_rig_textF1 , 'top', 20),(auto_rig_textF1 , 'left', 110),
                                    (auto_rig_text2 , 'top', 50),(auto_rig_text2 , 'left', 20),
                                    (auto_rig_textF2 , 'top', 50),(auto_rig_textF2 , 'left', 110),
                                    (headJnts_checkbox , 'top', 50),(headJnts_checkbox , 'left', 180),
                                    (twstJnts_checkbox , 'top', 20),(twstJnts_checkbox , 'left', 180)
                                    ]
                        )
        
        mc.setParent("..")


        #parent column to tab
        mc.setParent('..')

        #________________________________Rigging Tab @mkg _______________________________#
        #__________________________________________________________________________#
        # rigging tab column
        rigging_tab = mc.columnLayout()

        # Red Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
        mc.setParent("..")

        # create_fk_chain, create_ik_limb, create_fk_ik_limb
        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='FK Chain \n ~~~~~~~~ \n Select Joints', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().create_fk_chain()', 
                    bgc = (.5,0,0), 
                    statusBarMessage='Select Joints in Order')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='IK Limb \n ~~~~~~~~ \n Select 3 Joints', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().create_ik_limb()', 
                    bgc = (0,0.4,0), 
                    statusBarMessage='Select Joints in Order, Oriented for Main Axis X')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='FK/ IK Limb Blended \n ~~~~~~~~ \n Select 3+ Joints', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().create_fk_ik_limb()', 
                    bgc = (0,0.2,0.45), 
                    statusBarMessage='Select 3 or More Joints in Order, Oriented for Main Axis X')
        mc.setParent('..')

        # red seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
        mc.setParent("..")

        # simple_blend_joints, blend_joint_chain, rev_foot_locators
        mc.rowLayout(numberOfColumns = 8)
        mc.button(  label='Simple Blend Joints \n ~~~~~~~~ \n Select FK, IK, then Bind Jnt', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().simple_blend_joints()', 
                    bgc = (.5,0.1,0), 
                    statusBarMessage='Auto Sets Up Blend Color Node Between 3 Joints')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='Blended Joint Chain \n ~~~~~~~~ \n Select Single Chain \n Joints in Order', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().blend_joint_chain()', 
                    bgc = (0,0.4,0.2), 
                    statusBarMessage='FK(A) and IK(B) chains will be created automatically')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='"L" \n l \n o \n c', 
                    h=75, 
                    w=33, 
                    command = 'character_rigger.tabs.rigging.rigging_class().rev_foot_locators("l")', 
                    bgc = (0.8,0.8,0), 
                    statusBarMessage='Create "L" Locators for Positions of Reverse Foot Controls')
        mc.button(  label='Rev \n Foot', 
                    h=75, 
                    w=34, 
                    command = 'character_rigger.tabs.rigging.rigging_class().reverse_foot_setup("l")', 
                    bgc = (0.8,0.7,0), 
                    statusBarMessage='Create "L" Reverse Foot Setup/ Based on Locator Positions/ CREATE MORE! Locators for Each Reverse Foot')
        
        mc.button(  label='"R" \n l \n o \n c', 
                    h=75, 
                    w=34, 
                    command = 'character_rigger.tabs.rigging.rigging_class().rev_foot_locators("r")', 
                    bgc = (0.3,0,0.45), 
                    statusBarMessage='Create "R" Locators for Positions of Reverse Foot Controls')
        mc.button(  label='Rev \n Foot', 
                    h=75, 
                    w=33, 
                    command = 'character_rigger.tabs.rigging.rigging_class().reverse_foot_setup("r")', 
                    bgc = (0.25,0,0.45), 
                    statusBarMessage='Create "R" Reverse Foot Setup/ Based on Locator Positions/ CREATE MORE! Locators for Each Reverse Foot')
        
        mc.setParent('..')

        # red seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
        mc.setParent("..")

        # nurbs_curve_cube, nurbs_curve_sphere, nurbs_curve_arrow
        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Nurbs Curve Cube', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_cube()', 
                    bgc = (.5,0,0.1), 
                    statusBarMessage='Create nurbs cube with groups.')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='Nurbs Curve Sphere', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_sphere()', 
                    bgc = (0.2,0.4,0), 
                    statusBarMessage='Create nurbs sphere with groups.')
        mc.separator(style='none', w=10, h=75, bgc=(0.4,0,0))
        mc.button(  label='Nurbs Curve Arrow', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_arrow()', 
                    bgc = (0.1,.1,.45), 
                    statusBarMessage='Create nurbs arrow with groups.')
        mc.setParent('..')

        # red seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
        mc.setParent("..")

        #parent column to tab
        mc.setParent('..')


        #______________________________Animation Tab @mkp _______________________________#
        #__________________________________________________________________________#
        animation_tab = mc.columnLayout()

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
        mc.setParent("..")

        # create_locator, multi_parent_const, reset_ctrls
        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='create LOCATOR', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.animation.animation_class().create_locator()', 
                    bgc = (0.8,0.8,0), 
                    statusBarMessage='Create large locator')
        mc.separator(style='none', w=10, h=75, bgc=(0,0.5,0.25))
        mc.button(  label='Multi-Parent Const \n ~~~~~~~~ \n Parent Ctrls to Locator \n To Move In Worldspace', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.animation.animation_class().multi_parent_const()', 
                    bgc = (0.5,0.1,0.1), 
                    statusBarMessage='Select Locator Last/ Exectute/ Key Ctrls/ then delete Locator (constraints will auto delete with locator)')
        mc.separator(style='none', w=10, h=75, bgc=(0,0.5,0.25))
        mc.button(  label='RESET Ctrls', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.animation.animation_class().reset_ctrls()', 
                    bgc = (0.1,0.1,0.5), 
                    statusBarMessage='Reset Translation, Rotation, and Scale to ZERO')
        mc.setParent('..')


        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = 'M I R R O R  Controls', height=20, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
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

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        # Text Input Row
        mc.rowLayout(numberOfColumns = 15)
        mc.textField('l_hip_text', width=40, h=24, text='l_')
        mc.textField('r_hip_text', width=40, h=24, text='r_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.button(  label='M I R R O R', 
                    w=80, 
                    command = 'character_rigger.tabs.animation.animation_class().mirror_ctrls()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage=   'Select LEFT Controls/ Objects to Mirror, \
                                        Or Mirror Selected if No Opposite Conrols/ Objects Exist')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('translateX_text', width=40, h=24, text='-1')
        mc.textField('translateY_text', width=40, h=24, text='1')
        mc.textField('translateZ_text', width=40, h=24, text='1')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('rotateX_text', width=40, h=24, text='1')
        mc.textField('rotateY_text', width=40, h=24, text='-1')
        mc.textField('rotateZ_text', width=40, h=24, text='-1')
        mc.setParent('..')

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        #parent column to tab
        mc.setParent('..')


        #___________________________Modeling Tab @mkg _______________________________#
        #____________________________________________________________________________#
        # modeling column tab (below are rows stacked in column tab)
        modeling_tab = mc.columnLayout()

        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
        mc.setParent("..")

        # create random, scatter selected, scatter to vertices
        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='create RANDOM objects', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().create_random()', 
                    bgc = (.4,0,.1), 
                    statusBarMessage='Creates random polygonal objects for testing')
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.button(  label='SCATTER Selected', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().scatter_selected()' , 
                    bgc = (0,.4,.4), 
                    statusBarMessage='Scatter selected randomly' )
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.button(  label='SCATTER Selected \n ...to Object Verts', 
                    h=75, w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().scatter_to_vertices()', 
                    bgc = (.25,.5,0), 
                    statusBarMessage='First Select Objects to Scatter, Last Select Single Object to Scatter On' )
        mc.setParent('..')


        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
        mc.setParent("..")

        # create HUMAN model, Polygon ARCH 
        mc.rowLayout(numberOfColumns = 4)
        mc.button(  label='create HUMAN model', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().create_human()', 
                    bgc = (.25,.2,.2), 
                    statusBarMessage='Imports Default Human Sculpting Base' )
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.button(  label='Make Polygon ARCH \n (No Undo)', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().make_poly_arch()', 
                    bgc = (.5,.2,0), 
                    statusBarMessage='Create Basic Polygonal Arch (1st One Created Does Not Support Undo Currently)')
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.setParent('..')

        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=310, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
        mc.setParent("..")

        #parent column to tab
        mc.setParent('..')


        #______________________________Color Tab @mkp _______________________________#
        #__________________________________________________________________________#

        color_tab = mc.columnLayout()

        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change Color of Selection "Shapes"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(0,0.2,0.5))
        mc.setParent("..")

        # shape color slider
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('slider_value', 
        w=200, 
        minValue=0, 
        max=5, 
        value=0, 
        step=1, 
        dc = 'character_rigger.tabs.color_slider.color_class().slider_move()' )
        mc.iconTextButton('color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        # Orange Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change Color of Selection "Transforms"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.5,0.1,0))
        mc.setParent("..")

        #transform color slider
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('transform_slider_value', 
        w=200, 
        minValue=0, 
        max=5, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().transform_slider_move()')
        mc.iconTextButton('transform_color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        # Green Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change "WIRE" Color of Selection (Shapes)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
        mc.setParent("..")

        # wire color slider (shape)
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('wire_slider_value', 
        w=200, 
        minValue=0, 
        max=5, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().wire_slider_move()')
        mc.iconTextButton('wire_color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        # Green Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change "WIRE" Color of Selection (Transforms)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
        mc.setParent("..")

        # wire color slider (transform)
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('wireT_slider_value', 
        w=200, 
        minValue=0, 
        max=5, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().wireT_slider_move()')
        mc.iconTextButton('wireT_color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        # Grey Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change "Outliner" Color of Selection', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.1,0.1))
        mc.setParent("..")

        # outliner color slider
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('outliner_slider_value', 
        w=200, 
        minValue=0, 
        max=5, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().outliner_slider_move()')
        mc.iconTextButton('outliner_color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        #parent column to tab
        mc.setParent('..')


        #_________________Tab Layout/ UI End___________________#

        #tabs layout
        mc.tabLayout(myTabs, edit=True, tabLabel=[ (auto_rig_tab, 'Auto Rig'), (modeling_tab, 'Modeling'), (rigging_tab, 'Rigging'), (animation_tab, 'Animation'), (color_tab, 'Color')], bs='none')

        #Show UI Window
        mc.showWindow()



'''
    def test_method(self):
        import os
        print(__file__)
        print(os.path.join(os.path.dirname(__file__), '..'))
        print(os.path.dirname(os.path.realpath(__file__)))
        print(os.path.abspath(os.path.dirname(__file__)))
        print( os.path.abspath(os.path.join(__file__, "..", "icons/", "my_image.png") ) )
'''



