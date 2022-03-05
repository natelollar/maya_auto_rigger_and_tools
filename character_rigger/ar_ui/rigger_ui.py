#import maya commands
import maya.cmds as mc
#import python random functions
import random

import itertools

import maya.api.OpenMaya as om


def rigger_ui():
    
    #close UI if already open
    if mc.window('character_rigger', ex=True):
        mc.deleteUI('character_rigger', window=True)

    mc.window('character_rigger', t='Character Rigger!', rtf=True, s=True, menuBar=True, bgc = (0.2,0,0.2))

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
    mc.setParent('..')

    #'CHARACTER RIGGER'
    mc.rowLayout( numberOfColumns=1)
    mc.text(label = 'CHARACTER RIGGER', height=20, width=454, align='center', bgc=(0,0.5,0.5), font='boldLabelFont', statusBarMessage='Nate Tools!')
    mc.setParent('..')

    # Red Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
    mc.setParent('..')

    #_________________________declare Tabs____________________________________#
    #Insert Tabs
    myTabs = mc.tabLayout()



    #______________________________Animation Tab @mkp _______________________________#
    #__________________________________________________________________________#
    myColumnC = mc.columnLayout()

    # Green Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.5,0.25))
    mc.setParent('..')

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
    mc.setParent('..')

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
    mc.setParent('..')

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
    mc.setParent('..')

    #parent column to tab
    mc.setParent('..')


    #______________________________Color Tab @mkp _______________________________#
    #__________________________________________________________________________#

    myColumnD = mc.columnLayout()

    # Blue Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = ' Change Color of Selection "Shapes"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(0,0.2,0.5))
    mc.setParent('..')

    #shape color slider
    mc.rowLayout(numberOfColumns = 2)
    mc.intSlider('slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='slider_move()')
    mc.iconTextButton('color', w=55, bgc=(0.5, 0.5, 0.5))
    mc.setParent('..')

    # Orange Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = ' Change Color of Selection "Transforms"', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.5,0.1,0))
    mc.setParent('..')

    #transform color slider
    mc.rowLayout(numberOfColumns = 2)
    mc.intSlider('transform_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='transform_slider_move()')
    mc.iconTextButton('transform_color', w=55, bgc=(0.5, 0.5, 0.5))
    mc.setParent('..')

    # Green Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = ' Change "WIRE" Color of Selection (Shapes)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
    mc.setParent('..')

    #wire color slider
    mc.rowLayout(numberOfColumns = 2)
    mc.intSlider('wire_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='wire_slider_move()')
    mc.iconTextButton('wire_color', w=55, bgc=(0.5, 0.5, 0.5))
    mc.setParent('..')

    # Green Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = ' Change "WIRE" Color of Selection (Transforms)', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.4,0))
    mc.setParent('..')

    #wire color slider
    mc.rowLayout(numberOfColumns = 2)
    mc.intSlider('wireT_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='wireT_slider_move()')
    mc.iconTextButton('wireT_color', w=55, bgc=(0.5, 0.5, 0.5))
    mc.setParent('..')

    # Grey Seperator
    mc.rowLayout(numberOfColumns = 1)
    mc.text(label = ' Change "Outliner" Color of Selection', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.1,0.1,0.1))
    mc.setParent('..')

    #wire color slider
    mc.rowLayout(numberOfColumns = 2)
    mc.intSlider('outliner_slider_value', w=200, minValue=0, max=5, value=0, step=1, dc='outliner_slider_move()')
    mc.iconTextButton('outliner_color', w=55, bgc=(0.5, 0.5, 0.5))
    mc.setParent('..')


    #parent column to tab
    mc.setParent('..')



    #_________________Tab Layout/ UI End___________________#

    #tabs layout
    mc.tabLayout(myTabs, edit=True, tabLabel=[ (myColumnC, 'Animation'), (myColumnD, 'Color')], bs='none')

    #Show UI Window
    mc.showWindow()
