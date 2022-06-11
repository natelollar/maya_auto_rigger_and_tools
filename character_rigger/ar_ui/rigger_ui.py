# ui 
import maya.cmds as mc

import os

# main ui with tabs and everything
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

        myColumn = mc.columnLayout( bgc=(0.1,0,0.1), h=100, w=470 )

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

        #seperators
        auto_rig_s1 = mc.separator(style='none', w=454, h=10, bgc=(0,.448,1) )
        auto_rig_s2 = mc.separator(style='none', w=464, h=10, bgc=(0,.448,1) )
        auto_rig_s3 = mc.separator(style='none', h=265, w=10, bgc=(0,.448,1) )
        auto_rig_s4 = mc.separator(style='none', h=265, w=10, bgc=(0,.448,1) )
        # buttons
        auto_rig_b1 = mc.symbolButton(  image = os.path.abspath( os.path.join(__file__, "..", "..", "icons/", "RIG_ME.png") ),
                                        h=120, 
                                        w=220, 
                                        command = 'character_rigger.ar_rig.character_rig.character_rig()',
                                        statusBarMessage='Auto Rig Character.  No Joint Names Required. Must have tongue, bot face joints, and top face joints. Else uncheck "Head Jnts."',
                                        ann='Auto Rig Character.  No Joint Names Required. Must have tongue, bot face joints, and top face joints. Else uncheck "Head Jnts."'
                                    )
        auto_rig_b1a = mc.button(   label='Wyvern + Hind Legs \nAuto Rig! (Beta)',
                                    h=40, 
                                    w=110, 
                                    command = 'character_rigger.ar_rig.character_rig_quadruped.character_rig()',
                                    bgc = (0,.5,0), 
                                    statusBarMessage='Same as RIG ME! button, except quaruped legs (double knees), instead of normal biped legs. For something like a bipedal wyvern or dragon.',
                                    ann='Same as RIG ME! button, except quaruped legs (double knees), instead of normal biped legs. For something like a bipedal wyvern or dragon.',
                                )
        auto_rig_b1b = mc.button(   label='Import Wyvern \nModel + Skin', 
                                    h=30, 
                                    w=110, 
                                    command =   'character_rigger.tabs.auto_rig_tab.auto_rig_options().import_wyvern_fbx()',
                                    bgc = (.1,.1,.5), 
                                    statusBarMessage='Import Wyvern Model + Skin .FBX')
        auto_rig_b1c = mc.button(   label='Import Wyvern \nBounding Boxes', 
                                    h=30, 
                                    w=110, 
                                    command =   'character_rigger.tabs.auto_rig_tab.auto_rig_options().wyverm_bounding_boxes()',
                                    bgc = (.4,.1,.1), 
                                    statusBarMessage='Import Wyvern Bounding Boxes for the Auto Rigger to find the joints.')
        auto_rig_b1d = mc.button(   label='Import Wyvern \nRev Foot Locators', 
                                    h=30, 
                                    w=110, 
                                    command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().wyvern_rev_foot_locators()',
                                    bgc = (.1,.4,.1), 
                                    statusBarMessage='Import Wyvern Reverse Foot Locators.')
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
        auto_rig_b4 = mc.button(label='Jnt Ori/ Rot Axis', 
                                ann='Show Joint Orient & Rotate Axis & Rotate Order.',
                                h=25, 
                                w=100, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().show_orient_axis()',
                                bgc = (0,.1,.5), 
                                statusBarMessage='Reveal Rotate Axis, Joint Orient, & Rotate Order in channel box.  Rotate Axis should be 0. Regular rotation should be 0. Rotation values should be in Joint Orient.')
        auto_rig_b4a = mc.button(label='', 
                                ann='Hide Joint Orient & Rotate Axis & Rotate Order.',
                                h=25, 
                                w=15, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().hide_orient_axis()',
                                bgc = (.5,0,0), 
                                statusBarMessage='Hide Joint Orient & Rotate Axis & Rotate Order.')
        auto_rig_b5 = mc.button(label='Locator/s for Axis', 
                                ann='Create & parent locator under joint.',
                                h=25, 
                                w=100, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().jnt_loc_axis()',
                                bgc = (0,.2,.5), 
                                statusBarMessage='Creare locator parented under selected joint to help align axis.' )
        auto_rig_b5a = mc.button(label='', 
                                ann='Delete locator/s under joint.',
                                h=25, 
                                w=15, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().jnt_loc_axis_del()',
                                bgc = (.5,0,0), 
                                statusBarMessage='Delete locator/s under joint.' )
        auto_rig_b6 = mc.button(label='Show Local Axis', 
                                ann='Show local axis.',
                                h=25, 
                                w=100, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().disp_local_axis()',
                                bgc = (0,.3,.5), 
                                statusBarMessage='Show local axis.' )
        auto_rig_b6a = mc.button(label='', 
                                ann='Hide local axis.',
                                h=25, 
                                w=15, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().disp_local_axis_off()',
                                bgc = (.5,0,0), 
                                statusBarMessage='Hide local axis.' )
        auto_rig_b7 = mc.button(label='Select Hierarchy', 
                                ann='Select hierarchy of selection.',
                                h=15, 
                                w=100, 
                                command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().sel_hierarchy()',
                                bgc = (.6,.1,.1), 
                                statusBarMessage='Select hierarchy of selection.' )
        
        
        # text fields
        # corner lips
        auto_rig_text1 = mc.text(   label = 'Mid Face Jnts:', width=85, height=24, bgc=(0.4,0,0.4), align='center', font = 'boldLabelFont', 
                                    statusBarMessage='Amount of Mid Face Joints to be weighted between top face and bot face jnts. ' + 
                                    'First 2 mid joints might be the lip corners.  Then the next 2 lowest top face joints, might be the cheeks.',
                                    ann='Lowest top face jnts. Parent between upper and lower face.' )
        auto_rig_textF1 = mc.textField( 'midFace_jnt_amnt_text', width=40, h=24, text='2', bgc=(.2,0,.2), 
                                        statusBarMessage='Amount of Mid Face Joints to be weighted between top face and bot face jnts. ' +  
                                        'First 2 mid joints might be the lip corners.  Then the next lowest top face joints, might be the cheeks.',
                                        ann='Lowest top face jnts. Parent between upper and lower face.' )
        auto_rig_text2 = mc.text(   label = 'Control Size:', width=85, height=24, bgc=(0.4,0,0.4), align='center', font = 'boldLabelFont', 
                                    statusBarMessage='Global size of ctrls.')
        auto_rig_textF2 = mc.textField( 'global_ctrl_size_text', width=40, h=24, text='1', bgc=(.2,0,.2), 
                                        statusBarMessage='' )
        auto_rig_text3 = mc.text(   label = 'Elbow PV Dist', width=76, height=24, bgc=(0.3,0,0.5), align='center', font = 'boldLabelFont', 
                                    ann='Elbow Polve Vector Ctrl Start Distance.',
                                    statusBarMessage='Elbow Polve Vector Ctrl Start Distance.' )
        auto_rig_textF3 = mc.textField( 'elbow_pv_dist_text', width=28, h=24, text='20', bgc=(.2,0,.2), 
                                        ann='Elbow Polve Vector Ctrl Start Distance.',
                                        statusBarMessage='Elbow Polve Vector Ctrl Start Distance.' )
        auto_rig_text4 = mc.text(   label = 'Knee PV Dist', width=76, height=24, bgc=(0.3,0,0.5), align='center', font = 'boldLabelFont', 
                                    ann='Knee Polve Vector Ctrl Start Distance.',
                                    statusBarMessage='' )
        auto_rig_textF4 = mc.textField( 'knee_pv_dist_text', width=28, h=24, text='20', bgc=(.2,0,.2), 
                                        ann='Knee Polve Vector Ctrl Start Distance.',
                                        statusBarMessage='Knee Polve Vector Ctrl Start Distance.' )


        # check boxes
        headJnts_checkbox = mc.checkBox('headJnts_checkbox', 
                                        label='Head Jnts', 
                                        value=False, 
                                        bgc=(.4,0,.4), 
                                        width=115, 
                                        height=24,
                                        statusBarMessage='If unchecked, will not look for face joints.' +  
                                        ' For instance, uncheck if mocap skeleton with only top head joint and no face joints, ear joints, or tongue joints.' )
        twstJnts_checkbox = mc.checkBox('twstJnts_checkbox', 
                                        label='ForeArm Twst Jnts', 
                                        value=False, 
                                        bgc=(.4,0,.4), 
                                        width=115, 
                                        height=24,
                                        statusBarMessage='Uncheck if no forearm twist jnts.  Also, wrist jnt should be parented to elbow, not twist jnt end (a current rig limitation.)')
        

        # browser
        skin_weight_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "\orc_skinWeights.xml" )
        find_weights_browser = mc.textFieldButtonGrp( 'skin_weights_browser_text',
                                                    label = '  Skin Weights :', # title
                                                    cl3 = ['right', 'left', 'left'], # alignment of 3 columns (title, text, button)
                                                    height=20, 
                                                    width=437, 
                                                    text= skin_weight_path,
                                                    cw3 = [75,305,20], # width of the 3 columns 
                                                    buttonLabel='Browse', # button label
                                                    buttonCommand= 'character_rigger.tabs.auto_rig_tab.auto_rig_options().skin_weights_browse()',
                                                    statusBarMessage= 'Set skin weights import path.  Export XML weights using "Deform<Export Weights".  Disconnect from NG Skin tools (if exist), before weights export.',
                                                    ann='Set skin weights import path. Export XML weights using "Deform<Export Weights"'
                                                    ) 
        skele_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "\orc_skele.fbx" )
        find_skele_browser = mc.textFieldButtonGrp( 'skele_browser_text',
                                                    label = '  Skeleton :', # title
                                                    cl3 = ['right', 'left', 'left'], # alignment of 3 columns (title, text, button)
                                                    height=20, 
                                                    width=437, 
                                                    text= skele_path,
                                                    cw3 = [75,305,20], # width of the 3 columns 
                                                    buttonLabel='Browse', # button label
                                                    buttonCommand= 'character_rigger.tabs.auto_rig_tab.auto_rig_options().skele_file_browse()',
                                                    statusBarMessage= 'Set skeleton import path.  .ma or fbx. will work.',
                                                    ann='Set skeleton import path.  .ma or fbx. will work.'
                                                     ) 
        model_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "\orc_body.obj" )
        find_model_browser = mc.textFieldButtonGrp( 'model_browser_text',
                                                    label = '  Model :', # title
                                                    cl3 = ['right', 'left', 'left'], # alignment of 3 columns (title, text, button)
                                                    height=20, 
                                                    width=437, 
                                                    text= model_path,
                                                    cw3 = [75,305,20], # width of the 3 columns 
                                                    buttonLabel='Browse', # button label
                                                    buttonCommand= 'character_rigger.tabs.auto_rig_tab.auto_rig_options().model_file_browse()',
                                                    statusBarMessage= 'Set character model import path.  .ma or fbx. will work.',
                                                    ann='Set character model import path.  .ma or fbx. will work.'
                                                     ) 
        new_scene_button = mc.button(label='New Skinned \n Character Scene', 
                                            h=60, 
                                            w=95, 
                                            command = 'character_rigger.tabs.auto_rig_tab.auto_rig_options().new_character_scene()',
                                            bgc = (0,.3,.5), 
                                            statusBarMessage='Create a new scene that automatically skins the skeleton to the model with premade skin weights.  Makes it easy to adjust skeleton in seperate file.',
                                            ann='Create a new scene that automatically skins the chosen skeleton to the model with premade weights.' 
                                            )
        

        # rigger tab ui layout
        mc.formLayout(  auto_rig_form,
                        edit=True,  # seperators
                        attachForm=[(auto_rig_s1 , 'top', 0),(auto_rig_s1 , 'left', 0),
                                    (auto_rig_s2 , 'top', 265),(auto_rig_s2 , 'left', 0),
                                    (auto_rig_s3 , 'top', 0),(auto_rig_s3 , 'left', 0),
                                    (auto_rig_s4 , 'top', 0),(auto_rig_s4 , 'left', 454),
                                    # buttons
                                    (auto_rig_b1 , 'top', 77),(auto_rig_b1 , 'left', 130),
                                    (auto_rig_b1b , 'top', 280),(auto_rig_b1b , 'left', 0),
                                    (auto_rig_b1c , 'top', 280),(auto_rig_b1c , 'left',115),
                                    (auto_rig_b1d , 'top', 280),(auto_rig_b1d , 'left',230),
                                    (auto_rig_b1a , 'top', 280),(auto_rig_b1a , 'left', 345),
                                    (auto_rig_b2 , 'top', 15),(auto_rig_b2 , 'left', 325),
                                    (auto_rig_b3 , 'top', 15),(auto_rig_b3 , 'left', 390),
                                    (auto_rig_b4 , 'top', 86),(auto_rig_b4 , 'left', 15),
                                    (auto_rig_b4a , 'top', 86),(auto_rig_b4a , 'left', 116),
                                    (auto_rig_b5 , 'top', 116),(auto_rig_b5 , 'left', 15),
                                    (auto_rig_b5a , 'top', 116),(auto_rig_b5a , 'left', 116),
                                    (auto_rig_b6 , 'top', 146),(auto_rig_b6 , 'left', 15),
                                    (auto_rig_b6a , 'top', 146),(auto_rig_b6a , 'left', 116),
                                    (auto_rig_b7 , 'top', 176),(auto_rig_b7 , 'left', 15),
                                    # text fields
                                    (auto_rig_text1 , 'top', 20),(auto_rig_text1 , 'left', 20),
                                    (auto_rig_textF1 , 'top', 20),(auto_rig_textF1 , 'left', 110),
                                    (auto_rig_text2 , 'top', 50),(auto_rig_text2 , 'left', 20),
                                    (auto_rig_textF2 , 'top', 50),(auto_rig_textF2 , 'left', 110),
                                    (auto_rig_text3 , 'top', 73),(auto_rig_text3 , 'left', 375),
                                    (auto_rig_textF3 , 'top', 73),(auto_rig_textF3 , 'left', 346),
                                    (auto_rig_text4 , 'top', 101),(auto_rig_text4 , 'left', 375),
                                    (auto_rig_textF4 , 'top', 101),(auto_rig_textF4 , 'left', 346),
                                    # checkboxes
                                    (headJnts_checkbox , 'top', 50),(headJnts_checkbox , 'left', 180),
                                    (twstJnts_checkbox , 'top', 20),(twstJnts_checkbox , 'left', 180),
                                    #browser
                                    (new_scene_button , 'top', 132),(new_scene_button , 'left', 353),
                                    (find_weights_browser , 'top', 195),(find_weights_browser , 'left', 15),
                                    (find_skele_browser , 'top', 218),(find_skele_browser , 'left', 15),
                                    (find_model_browser , 'top', 241),(find_model_browser , 'left', 15)
                                    ]
                        )
        # parent for layout to column
        mc.setParent("..")

        # parent column to tab
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
        # column parented to row
        mc.columnLayout()
        mc.button(  label='Nurbs Curve Cube', 
                    h=38, 
                    w=140, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_cube()', 
                    bgc = (.5,0,0.1), 
                    statusBarMessage='Create nurbs cube with groups.')

        mc.button(  label='Tri Circle Ctrl', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.ar_functions.bb_nurbs_ctrl.bb_nurbs_ctrl( name="tri_circle_ctrl",' + 
                                                                                            'size=1,'+ 
                                                                                            'color1R=0,'+ 
                                                                                            'color1G=0,'+ 
                                                                                            'color1B=1,'+ 
                                                                                            'color2R=1,'+ 
                                                                                            'color2G=1,'+ 
                                                                                            'color2B=0 ).sel_tri_circle_ctrl()',
                    bgc = (.5,.2,.1), 
                    statusBarMessage='Create 3 nurb circles with locator in middle.')

        mc.button(  label='Arrow Twist Ctrl', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.loose_tools.arrow_twist_ctrl.arrow_twist_ctrl()',
                    bgc = (.4,.1,.1), 
                    ann='',
                    statusBarMessage='')
        # column parented to row
        mc.setParent("..")
        mc.separator(style='none', w=10, h=112, bgc=(0.4,0,0))

        # column parented to row
        mc.columnLayout()
        mc.button(  label='Nurbs Curve Sphere', 
                    h=38, 
                    w=140, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_sphere()', 
                    bgc = (0.2,0.4,0), 
                    statusBarMessage='Create nurbs sphere with groups.')
        
        mc.button(  label='Sphere Circle Ctrl', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.ar_functions.bb_nurbs_ctrl.bb_nurbs_ctrl( name="sphere_circle_ctrl",' + 
                                                                                            'size=1,'+ 
                                                                                            'color1R=0,'+ 
                                                                                            'color1G=0,'+ 
                                                                                            'color1B=1,'+ 
                                                                                            'color2R=1,'+ 
                                                                                            'color2G=1,'+ 
                                                                                            'color2B=0 ).sel_sphere_ctrl()',
                    bgc = (.1,.5,.1), 
                    statusBarMessage='Create nurb curve sphere with locator shape in middle.')
        mc.button(  label='Four Arrow Ctrl', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.loose_tools.four_arrow_ctrl_simple.four_arrow_ctrl()',
                    bgc = (.1,.3,.1), 
                    statusBarMessage='')
        # column parented to row
        mc.setParent("..")
        mc.separator(style='none', w=10, h=112, bgc=(0.4,0,0))


        # column parented to row
        mc.columnLayout()
        mc.button(  label='Nurbs Curve Arrow', 
                    h=38, 
                    w=140, 
                    command = 'character_rigger.tabs.rigging.rigging_class().nurbs_curve_arrow()', 
                    bgc = (0.1,.1,.45), 
                    statusBarMessage='Create nurbs arrow with groups.')

        mc.button(  label='Pyramid Ctrl', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.ar_functions.bb_nurbs_ctrl.bb_nurbs_ctrl( name="tri_circle_ctrl",' + 
                                                                                            'size=1,'+ 
                                                                                            'color1R=0,'+ 
                                                                                            'color1G=0,'+ 
                                                                                            'color1B=1,'+ 
                                                                                            'color2R=1,'+ 
                                                                                            'color2G=1,'+ 
                                                                                            'color2B=0 ).sel_pyramid_ctrl()',
                    bgc = (.1,.2,.5), 
                    statusBarMessage='Create nurb curve sphere with locator shape in middle.')
        mc.button(  label='Cylinder Ctrl Hard', 
                    h=37, 
                    w=140, 
                    command =   'character_rigger.loose_tools.cylinder_ctrl.cylinder_ctrl().cylinder_ctrl_hard()',
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Create nurb curve sphere with locator shape in middle.')
        '''
        mc.button(  label='Cylinder Ctrl Smooth', 
                    h=18, 
                    w=140, 
                    command =   'character_rigger.loose_tools.cylinder_ctrl.cylinder_ctrl().cylinder_ctrl_smooth()',
                    bgc = (.1,.3,.5), 
                    statusBarMessage='Create nurb curve sphere with locator shape in middle.')
        '''

        # column parented to row
        mc.setParent("..")

        mc.setParent('..')


        # red seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='  Create New Bind Pose : \n ~~~~~~~~ \n Select Any Joint', 
                    h=60, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().new_bindpose()', 
                    bgc = (0.4,0,0.4), 
                    ann='Delete old bind pose, create new one. Select any joint in skeleton.',
                    statusBarMessage='Delete old bind pose, create new one. Select any joint in skeleton.')
        mc.separator(style='none', w=10, h=60, bgc=(0.4,0,0))
        mc.textField( 'bindpose_name_text', width=142, h=60, text='newBindPose_name', 
                        statusBarMessage='Delete old bind pose, create new one. Select any joint in skeleton.')
        mc.separator(style='none', w=10, h=60, bgc=(0.4,0,0))
        mc.button(  label=  'Print \n Object Type', 
                    h=60, 
                    w=142, 
                    command = 'character_rigger.tabs.rigging.rigging_class().object_type()', 
                    bgc = (.1,.2,.4), 
                    ann='Print selected object "type."',
                    statusBarMessage='Print selected object "type."')

        mc.setParent('..')

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 15)

        mc.textField('left_prefix_text', width=40, h=24, text='l_')
        mc.textField('right_prefix_text', width=40, h=24, text='r_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.button(  label='MIRROR Ctrl Shape/s', 
                    w=113, 
                    command = 'character_rigger.tabs.rigging.rigging_class().mirror_ctrl_shape()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage = 'Mirror Ctrl Shape to Opposite side Ctrl (across X Axis).  Select LEFT Controls to Mirror. ' +
                                        'Useful for autrigger when controls need to be aligned, but dont want to do both sides.',
                    ann = 'Mirror Ctrl Shape to Opposite side Ctrl (across X Axis).  Select LEFT Controls to Mirror.' )
        mc.separator( style='none', w=10, h=23, bgc=(0,0.7,0.25) )

        mc.textField('left_prefix_textA', width=36, h=24, text='l_')
        mc.textField('right_prefix_textA', width=36, h=24, text='r_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.button(  label='MIRROR Jnt Same Orient', 
                    h=23,
                    w=130, 
                    command = 'character_rigger.loose_tools.mirror_jnt_same_orient.mirror_jnt_same_orient()', 
                    bgc = (0.1,0.3,0.5), 
                    statusBarMessage = 'Similar to mirror joint (Currently just for individual joint/s, not chains.). Keeps equivilent orient. Different than "Behavior" or "Orientation" Mirror function.' +
                                        ' For instance, to mirror leg.  Seperete joints, parent to middle joint, then mirror.  Then reconnect if needed.  Mirrors, then rotates X 180 Degrees, and freezes rotation.')
        mc.separator( style='none', w=10, h=23, bgc=(0,0.7,0.25) )
        mc.setParent("..")

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 15)
        mc.textField('offs_grp_suffix_text', width=82, h=24, text='_grp_offset')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.button(  label='Shape to Offset Grp', 
                    w=113, 
                    command = 'character_rigger.tabs.rigging.rigging_class().add_shape_to_offset_grp()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage = 'Add Shape to Similar Named Offset Grp With Suffix (ex. _offset_grp).' +
                    'Good for adding shape to empty grp for set driven key animation.',
                    ann = 'Add Shape to Similar Named Offset Grp With Suffix (ex. _offset_grp).' +
                    'Good for adding shape to empty grp for set driven key animation.' )
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.radioButtonGrp(  'axis_button',
                            label='  MIRROR Jnt Axis Flip:', 
                            labelArray3=['X', 'Y', 'Z'], 
                            numberOfRadioButtons=3,
                            cl4 = ['left', 'left', 'left', 'left'],
                            cw4 = [130, 25, 25, 25],
                            h=23,
                            w=230,
                            bgc = (0.1,0.3,0.5),
                            sl=1,
                            statusBarMessage ='Flips this jnt AXIS 180*, then freezes rotation on joint. After mirroring.'
                            )
        mc.setParent("..")


        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")


        # Text Input Row
        mc.rowLayout(numberOfColumns = 15)
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.button(  label='Replace 2nd Object Shape', 
                    w=197, 
                    command = 'character_rigger.tabs.rigging.rigging_class().shape_to_selected()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage = 'Select 2 Curves. Replace 2nd Object Shape with First Object Shape',
                    ann = 'Select 2 Curves. Replace 2nd Object Shape with First Object Shape' )
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))
        mc.button(  label='Shape Vis Off', 
                    w=102, 
                    command = 'character_rigger.tabs.rigging.rigging_class().shape_vis_off()', 
                    bgc = (0.5,0.2,0), 
                    statusBarMessage = 'Select Transforms. Shape/s Visibility Off',
                    ann = 'Select Transforms. Shape/s Visibility Off' )
        mc.separator(style='none', w=10, h=23, bgc=(0.25,0.7,0))
        mc.button(  label='Shape Vis On', 
                    w=102, 
                    command = 'character_rigger.tabs.rigging.rigging_class().shape_vis_on()', 
                    bgc = (0.2,0.5,0), 
                    statusBarMessage = 'Select Transforms. Shape/s Visibility On',
                    ann = 'Select Transforms. Shape/s Visibility On' )
        mc.separator(style='none', w=10, h=23, bgc=(0.25,0.7,0))
        mc.setParent("..")


        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0.2,0,0.2))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Soft IK Sample', 
            h=30, 
            w=110, 
            command =   'character_rigger.samples.soft_ik_native.soft_ik_native()',
            bgc = (.5,.3,.1), 
            statusBarMessage="Create a sample joint setup.  Don't select anything.")
        mc.separator(style='none', w=15, h=30, bgc=(0.4,0,0.4))
        mc.button(  label='Sample \n Tentacle Jnts', 
                    h=30, 
                    w=75, 
                    command = 'character_rigger.ar_rig.tentacle_rigA.sample_tentacle_joints()', 
                    bgc = (0.4,0.1,0.2), 
                    statusBarMessage= 'Create sample tentacle joints.'
                    )
        mc.button(  label='Bounding Boxes', 
                    h=30, 
                    w=90, 
                    command = 'character_rigger.ar_rig.tentacle_rigA.tentacle_rig_bounding_boxes()', 
                    bgc = (0.5,0.1,0.1), 
                    statusBarMessage= 'Place around parent joint, start joint and end joint of tentacle.  Parent joint not required.'
                    )
        mc.textField(   'defaultJnt_prefix_text', width=65, h=30, text='baseJnt_', bgc=(.2,0,.2), 
                        statusBarMessage='Prefix of tentacle joints. Used for ikJnt_ and fkJnt_ names.')
        mc.button(  label='Tentacle Rig', 
                    h=30, 
                    w=90, 
                    command = 'character_rigger.ar_rig.tentacle_rigA.tentacle_rig()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage= 'Requires joints and bounding boxes.  Click next button to create boudning boxes.'
                    )
        
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0.2,0,0.2))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Copy Vertex \nWeights', 
            h=30, 
            w=110, 
            command =   'character_rigger.loose_tools.copy_vertex_weights.copy_vertex_weights()',
            bgc = (.1,.1,.5), 
            statusBarMessage=   'Copy 1st selected vert skin weights to second selected vert.' +
                                'Or select multiple verts, then corresponding verts in same order.')
        mc.separator( style='none', w=15, h=30, bgc=(0.4,0,0.4) )
        mc.button(  label='Import Vertex \nWeights Test', 
            h=30, 
            w=90, 
            command =   'character_rigger.loose_tools.copy_vertex_weights.copy_vertex_weights_test()',
            bgc = (.1,.1,.4), 
            statusBarMessage='Import Maya scene to test out Copy Vert Weights tool.')
        mc.separator( style='none', w=15, h=30, bgc=(0.4,0,0.4) )
        mc.button(  label='Multi Space Switch', 
                    h=30, 
                    w=110, 
                    command = 'character_rigger.loose_tools.add_space_switch_multi_1.multi_space_switch()', 
                    bgc = (0.5,0.2,0.2), 
                    statusBarMessage=   'Select constraint objects first.   ' +
                                        'Second to last select parent constrained object.   ' +
                                        'Lastly select object to have custom space switch attribute.   ',
                    ann=                'Select constraint objects first.   ' +
                                        'Second to last select parent constrained object.   ' +
                                        'Lastly select object to have custom space switch attribute.   ')
        
        mc.separator( style='none', w=15, h=30, bgc=(0.4,0,0.4) )
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
        mc.text(label = '', height=15, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        # Text Input Row
        mc.rowLayout(numberOfColumns = 15)
        mc.textField('l_ctrlObject_text', width=40, h=24, text='l_')
        mc.textField('r_ctrlObject_text', width=40, h=24, text='r_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.button(  label='M I R R O R', 
                    w=80, 
                    command = 'character_rigger.tabs.animation.animation_class().mirror_ctrls(row=1)', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage=   'Select LEFT Controls/ Objects to Mirror. ' +
                                        'Or Mirror Selected if No Opposite Conrols/ Objects Exist. ' +
                                        'Possibly Add "-=180" to channel box Rotate X afterwards if wanting to immitate "mirror behavior" from skeleton mirror.')
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

        #____repeat mirror controls incase some oriented differently___#
        # Text Input Row
        mc.rowLayout(numberOfColumns = 15)
        mc.textField('l_ctrlObject_textA', width=40, h=24, text='l_')
        mc.textField('r_ctrlObject_textA', width=40, h=24, text='r_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.button(  label='M I R R O R', 
                    w=80, 
                    command = 'character_rigger.tabs.animation.animation_class().mirror_ctrls(row=2)', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage=   'Select LEFT Controls/ Objects to Mirror. ' +
                                        'Or Mirror Selected if No Opposite Conrols/ Objects Exist. ' +
                                        'Possibly Add "-=180" to channel box Rotate X afterwards if wanting to immitate "mirror behavior" from skeleton mirror.')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('translateX_textA', width=40, h=24, text='-1')
        mc.textField('translateY_textA', width=40, h=24, text='-1')
        mc.textField('translateZ_textA', width=40, h=24, text='-1')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('rotateX_textA', width=40, h=24, text='1')
        mc.textField('rotateY_textA', width=40, h=24, text='1')
        mc.textField('rotateZ_textA', width=40, h=24, text='1')
        mc.setParent('..')

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        #____repeat mirror controls incase some oriented differently___#
        # Text Input Row
        mc.rowLayout(numberOfColumns = 15)
        mc.textField('l_ctrlObject_textB', width=40, h=24, text='left_')
        mc.textField('r_ctrlObject_textB', width=40, h=24, text='right_')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.button(  label='M I R R O R', 
                    w=80, 
                    command = 'character_rigger.tabs.animation.animation_class().mirror_ctrls(row=3)', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage=   'Select LEFT Controls/ Objects to Mirror. ' +
                                        'Or Mirror Selected if No Opposite Conrols/ Objects Exist. ' +
                                        'Possibly Add "-=180" to channel box Rotate X afterwards if wanting to immitate "mirror behavior" from skeleton mirror.')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('translateX_textB', width=40, h=24, text='-1')
        mc.textField('translateY_textB', width=40, h=24, text='-1')
        mc.textField('translateZ_textB', width=40, h=24, text='-1')
        mc.separator(style='none', w=10, h=23, bgc=(0,0.7,0.25))

        mc.textField('rotateX_textB', width=40, h=24, text='1')
        mc.textField('rotateY_textB', width=40, h=24, text='1')
        mc.textField('rotateZ_textB', width=40, h=24, text='1')
        mc.setParent('..')

        # green seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=15, width=454, align='center', font = 'boldLabelFont', bgc=(0,0.7,0.25))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 4)
        mc.button(  label='Reference \nCtrl Shapes', 
                    h=30, 
                    w=100, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().reference_curve_shape()', 
                    bgc = (0.4,0.2,0.2), 
                    statusBarMessage='Make Ctrl Unselectable. Good for referenceing global ctrl when animating.',
                    ann='Make Ctrl Unselectable.')
        mc.button(  label='Unreference \nCtrl Shapes', 
                    h=30, 
                    w=100, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().unreference_curve_shape()', 
                    bgc = (0.2,0.4,0.2), 
                    statusBarMessage='Make Ctrl Selectable.  Must find and select first (outliner, select by name, etc).'
                    )
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
        mc.rowLayout(numberOfColumns = 6)
        mc.button(  label='Multi OBJECT Export \n \      / \n \   / \n \/', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().mult_obj_exp()', 
                    bgc = (.5,0,.5), 
                    statusBarMessage='Select multiple objects to export.')
        
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.button(  label='Make Polygon ARCH \n (No Undo)', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().make_poly_arch()', 
                    bgc = (.5,.2,0), 
                    statusBarMessage='Create Basic Polygonal Arch (1st One Created Does Not Support Undo Currently)')
        mc.separator(style='none', w=10, h=75, bgc=(0,0.2,0.4))
        mc.button(  label='create HUMAN model', 
                    h=75, 
                    w=142, 
                    command = 'character_rigger.tabs.modeling.modeling_class().create_human()', 
                    bgc = (.25,.2,.2), 
                    statusBarMessage='Imports Default Human Sculpting Base' )
        mc.setParent('..')


        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=10, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.2,0.4))
        mc.setParent("..")

        # obj export text field
        def_text_var = os.path.abspath( os.path.join(__file__, "..", "..", "..", "..", "..", "..", "..", "downloads") )
        mc.rowLayout(numberOfColumns = 1)
        mc.textFieldButtonGrp(  'obj_exp_text',
                                label = '   Export Path:', # title
                                cl3 = ['left', 'left', 'left'], # alignment of 3 columns (title, text, button)
                                height=30, 
                                width=454, 
                                text= def_text_var + '/',
                                #bgc=(.5,0,.5), #background color
                                cw3 = [75,315,60], # width of the 3 columns 
                                buttonLabel='Browse', # button label
                                buttonCommand= 'character_rigger.tabs.modeling.modeling_class().browse_files()' ) 
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.radioButtonGrp(  'obj_radio_button',
                            label='   Export Type:', 
                            labelArray3=['.obj', '.fbx', '.ma'], 
                            numberOfRadioButtons=3,
                            cl4 = ['left', 'left', 'left', 'left'],
                            cw4 = [85, 75, 65, 65],
                            height=20, 
                            width=454,
                            bgc = (0,0.2,0.4),
                            sl=1
                            )
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = 'Random Scatter Tools', height=30, width=454, align='center', font = 'fixedWidthFont', bgc=(0,0.4,0.2))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Scatter \nto Verts', 
                    h=30, 
                    w=72, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().scatter_to_vert_pos_and_norm()', 
                    bgc = (.5,.1,.1), 
                    statusBarMessage='Scatter to last selected objects verts. Not for too many objects. Creates rivet then deletes for placement.' )
        mc.text(    label = 'Up \n Down:', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='Move Up Down, Normal Orient Only',
                    ann='Click Me!' )
        mc.textField( 'move_up_down_text', width=30, h=30, text='0', bgc=(.2,0,.2), 
                        statusBarMessage='Move Up Down, Normal Orient Only',
                        ann='' )
        mc.checkBox(    'normal_orient_checkbox', 
                        label='Normal \nOrient', 
                        value=True, 
                        bgc=(.2,.7,.2), 
                        width=60, 
                        height=30,
                        statusBarMessage='' )
        mc.checkBox(    'normal_orient_random_checkbox', 
                        label='Normal \nOrient Rand', 
                        #align = 'center',
                        value=True, 
                        bgc=(.2,.7,.2), 
                        width=90, 
                        height=30,
                        statusBarMessage='' )
        mc.checkBox(    'rand_rot_checkbox', 
                        label='Rand \nRotate', 
                        value=False, 
                        bgc=(.2,.7,.5), 
                        width=60, 
                        height=30,
                        statusBarMessage='' )
        mc.checkBox(    'super_rand_rot_checkbox', 
                        label=' Super \n Rand Rotate', 
                        value=False, 
                        bgc=(.2,.7,.5), 
                        width=90, 
                        height=30,
                        statusBarMessage='' )
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Simple \nScatter', 
                    h=30, 
                    w=72, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().simple_scatter()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Scatter to last selected object.  A more random scatter with geometry constraints and normal constraints, instead of verts and rivets.' )
        mc.checkBox(    'normal_orient_checkbox1', 
                        label='Normal \nOrient', 
                        value=True, 
                        bgc=(.2,.7,.2), 
                        width=60, 
                        height=30,
                        statusBarMessage=   'A more random scatter with geometry constraints and normal constraints, instead of verts and rivets.'  +
                                            'Scatters to bounding box. Then geo constrains.' )
        
        mc.text(label = '', height=30, width=20, align='center', font = 'fixedWidthFont', bgc=(0.4,0,0.4))
        mc.button(  label='Reset \nRotate', 
                    h=30, 
                    w=55, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().reset_rotation()', 
                    bgc = (.1,.5,.1), 
                    statusBarMessage='Zero out rotation. Will skip locked attributes.' )
        mc.button(  label='Reset \nScale', 
                    h=30, 
                    w=55, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().reset_scale()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Reset scale. Will skip locked attributes.' )
        mc.button(  label='Reset \nTranslate', 
                    h=30, 
                    w=55, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().reset_translation()', 
                    bgc = (.5,.1,.1), 
                    statusBarMessage='Zero out translation. Will skip locked attributes.' )
        
        
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=5, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Random \n Rotate', 
                    h=30, 
                    w=72, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().random_rotate()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Randomly rotate selected objects.' )
        mc.text(    label = 'X \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'x_rot_low_text',  width=30, h=30, text='-360', bgc=(.2,0,.2))
        mc.textField( 'x_rot_high_text',  width=30, h=30, text='360', bgc=(.2,0,.2))
        mc.text(    label = 'Y \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'y_rot_low_text', width=30, h=30, text='-360', bgc=(.2,0,.2))
        mc.textField( 'y_rot_high_text', width=30, h=30, text='360', bgc=(.2,0,.2))
        mc.text(    label = 'Z \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'z_rot_low_text', width=30, h=30, text='-360', bgc=(.2,0,.2))
        mc.textField( 'z_rot_high_text', width=30, h=30, text='360', bgc=(.2,0,.2))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Random \n Scale', 
                    h=30, 
                    w=72, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().random_scale()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Randomly rotate selected objects.' )
        mc.text(    label = 'Scale \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'scl_low_text',  width=30, h=30, text='0.5', bgc=(.2,0,.2))
        mc.textField( 'scl_high_text',  width=30, h=30, text='2', bgc=(.2,0,.2))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Simple \n Translate', 
                    h=30, 
                    w=72, 
                    command = 'character_rigger.loose_tools.random_scatter_tools.random_scatter_tools().simple_move()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage='Simple translation in relative direction.' )
        mc.text(    label = 'X \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'x_trans_amnt_text',  width=30, h=30, text='0', bgc=(.2,0,.2))
        mc.text(    label = 'Y \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'y_trans_amnt_text', width=30, h=30, text='-5', bgc=(.2,0,.2))
        mc.text(    label = 'Z \n -+', width=40, height=30, bgc=(.2,.7,.2), align='center',
                    statusBarMessage='')
        mc.textField( 'z_trans_amnt_text', width=30, h=30, text='0', bgc=(.2,0,.2))
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
        max=14, 
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
        max=11, 
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
        max=11, 
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
        max=11, 
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
        max=11, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().outliner_slider_move()')
        mc.iconTextButton('outliner_color', w=55, bgc=(0.5, 0.5, 0.5))
        mc.setParent('..')

        # Seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = ' Change "WIDTH" of Curve Selection', height=20, width=454, align='left', font = 'fixedWidthFont', bgc=(.5,0.5,0))
        mc.setParent("..")

        # outliner color slider
        mc.rowLayout(numberOfColumns = 2)
        mc.intSlider('curve_width_value', 
        w=200, 
        minValue=0, 
        max=11, 
        value=0, 
        step=1, 
        dc='character_rigger.tabs.color_slider.color_class().curve_width()')
        mc.iconTextButton('curve_width', w=55, bgc=(0, 0, 0))
        mc.setParent('..')

        #parent column to tab
        mc.setParent('..')


        #______________________________Shading Tab @mkp _______________________________#
        #__________________________________________________________________________#

        shading_tab = mc.columnLayout()

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Redshift \n Displacement Off', 
                    h=30, 
                    w=100, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().redshift_displacement_off()', 
                    bgc = (.5,.1,.1), 
                    statusBarMessage='Turn off Redshift render displacement and tessalation for selected.' )
        mc.button(  label='', 
                    h=30, 
                    w=15, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().redshift_displacement_on()', 
                    bgc = (.1,.6,.1), 
                    statusBarMessage='Turn on Redshift render displacement and tessalation for selected.' )
        mc.text(label = '', height=30, width=20, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.button(  label='Assign Random Blinn/s', 
                    h=30, 
                    w=150, 
                    command = 'character_rigger.loose_tools.assign_blinn_mat.assign_blinn()', 
                    bgc = (0.1,0.1,0.4), 
                    statusBarMessage='Assign blinn materials to selected objects named after object with random color.',
                    ann='Assign blinn materials to selected objects named after object with random color.')
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Create Redshift Materials \n & Connect Textures', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().connect_redshift_mat_all()', 
                    bgc = (.1,.5,.1), 
                    statusBarMessage='Select models with correct names. Will auto connect textures in scene.' +
                                    ' Object name should match texture without the texture suffix.' +
                                    '  _BaseColor, _Metallic, _Roughness, _Gloss, _Normal, _Opacity' +
                                    ' Opacity will create Sprite.'  +
                                    ' There will be a "_1" on the end of the texture name when u drag and drop it in.  This is accounted for.' )
        mc.checkBox(    'fip_normal_y_checkbox', 
                        label='Flip Y\nNormal', 
                        value=True, 
                        bgc=(.2,.6,.4), 
                        width=60, 
                        height=40,
                        statusBarMessage='Flips Y/G Normal.  As in the middle value of XYZ or RGB.' )
        mc.text(label = '', height=30, width=20, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        
        mc.button(  label='+ Stingray \nMaterial', 
                    h=40, 
                    w=100, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().stingray_mat_add()', 
                    bgc = (.0,.3,.0), 
                    statusBarMessage='Select object/s. Adds stingray material after youve added redshift material first.' +
                                    ' Y/G Normal Channel still must be flipped manually in the ShaderFX graph.' +
                                    '  Warning!  Stingray material and ShaderFX graph is very unstable.'  +
                                    '  Should work fine though after setup and saved.  (Maya 2020)'
                    )
        

        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=20, width=454, align='center', font = 'fixedWidthFont', bgc=(0.1,0,0.1))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 10)
        mc.button(  label='Connect\nMaterial', 
                    h=40, 
                    w=70, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().connect_mat()', 
                    bgc = (.1,.1,.5), 
                    statusBarMessage=' assign = object + "_mat" ' 
                    )
        mc.button(  label='Connect\nMat Sprite', 
                    h=40, 
                    w=70, 
                    command = 'character_rigger.tabs.shading_tab.shader_utility().connect_mat_sprite()', 
                    bgc = (.1,.3,.5), 
                    statusBarMessage=' assign = object + "_mat_sprite" ' 
                    )
        
        mc.setParent("..")



        #parent column to tab
        mc.setParent('..')


        #______________________________Misc Tab @mkp _______________________________#
        #__________________________________________________________________________#

        misc_tab = mc.columnLayout()

        # blue seperator
        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=3, width=454, align='left', font='boldLabelFont', bgc=(0.5,0.5,0.9))
        mc.setParent("..")

        # new row
        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Maya, API, Python, QtCore, \n PySide2, OS Version', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().python_maya_info()', 
                    bgc = (0.4,0.4,0.4), 
                    statusBarMessage='')
        mc.button(  label='Test Function', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().function_test()', 
                    bgc = (0.5,0.3,0.3), 
                    statusBarMessage='')
        mc.button(  label='Curve/s Vertex Positions', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().curve_vert_pos()', 
                    bgc = (0.2,0.2,0.5), 
                    statusBarMessage='Select curve. Or shape if multiple shapes in curve.  Print Curve Vertex Positions.  Good for pasting into cmds.curve().',
                    ann='Print Curve Vertex Positions')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 1)
        mc.text(label = '', height=3, width=454, align='left', font='boldLabelFont', bgc=(0.5,0.5,0.9))
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='VS Code \n Port Connect', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.loose_tools.vs_code_port_connect.vs_code_port_connect()', 
                    bgc = (0.2,0.2,0.2), 
                    statusBarMessage='',
                    ann='')
        mc.button(  label='RENAME First Occurrence', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().rename_first()', 
                    bgc = (0.4,0.2,0.2), 
                    statusBarMessage='Rename first occurrence.',
                    ann='Rename first occurrence.')
        mc.textField(   'current_part_text', width=75, h=40, text='l',
                        statusBarMessage='Text to be replaced.',
                        ann='Text to be replaced.' )
        mc.textField(   'replace_part_text', width=75, h=40, text='l_', 
                        statusBarMessage='Replace text with...',
                        ann='Replace text with...' )
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Constrain between Last 2', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().parent_scale_multi()', 
                    bgc = (0.1,0.1,0.1), 
                    statusBarMessage='Parent and Scale Constrain to Last 2 Selected.',
                    ann='Parent and Scale Constrain to Last 2 Selected.')
        mc.button(  label='Multi Set DrivenKey', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().multi_set_driven_key()', 
                    bgc = (0.4,0.2,0.2), 
                    statusBarMessage='Select objects with contraints, except last selected has switch attribute.  Currently only works with 1 const per object. ' +
                    'Enter 0 for W0 = 0 when swch is 0, and W0=1, when swch is 1. W1 is opposite.',
                    ann='Select objects with contraints, except LAST selected has switch attribute. Currently only works with 1 const per object. ' +
                    'Enter 0 value for W0 to match swch. Or 1 for W1 to match switch.')
        mc.textField(   'swch_attr_name', width=75, h=40, text='.fk_ik_blend',
                        statusBarMessage='Name of Swch Ctrl Attribute.',
                        ann='Name of Swch Ctrl Attribute.' )
        mc.textField(   'W0_text', width=75, h=40, text='0', 
                        statusBarMessage='Enter 0 value for W0 to match swch. Or 1 for W1 to match switch.  (ex. W0 = 0, swch 0, W0 = 1, swch 1, W1 Opposite.. For value 0)',
                        ann='Enter 0 value for W0 to match swch. Or 1 for W1 to match switch.' )
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Cnst btwn Lst 2 (Parnt Only)', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().parent_multi()', 
                    bgc = (0.05,0.05,0.05), 
                    statusBarMessage='Parent Constrain to Last 2 Selected.',
                    ann='Parent and Scale Constrain to Last 2 Selected.')
        mc.button(  label='Multi Attr Set', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().set_multi_attr()', 
                    bgc = (0.5,0.2,0.2), 
                    statusBarMessage='Select multiple objects. Enter attribute name.  Enter attribute value.',
                    ann='Select multiple objects. Enter attribute name.  Enter attribute value.')
        mc.textField(   'attr_name_text', width=75, h=40, text='.scale',
                        statusBarMessage='Enter Attribute Name',
                        ann='Enter Attribute Name' )
        mc.textField(   'attr_value_text', width=75, h=40, text='1, 1, 1', 
                        statusBarMessage='Enter Attribute Value',
                        ann='Enter Attribute Value' )
        mc.setParent("..")



        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Multi Scale Cnst to Last', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().scale_multi_const()', 
                    bgc = (0.2,0.2,0.2), 
                    statusBarMessage='Scale constrain multiple to LAST selected object.',
                    ann='Scale constrain multiple to LAST selected object.')
        mc.button(  label='Add Separator Attribute', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.loose_tools.add_custom_attr.add_enum_attr()', 
                    bgc = (0.3,0.2,0.2), 
                    statusBarMessage='Add Separator Enum Attribute to Selected Ctrl/ Object',
                    ann='Add Separator Enum Attribute to Selected Ctrl/ Object')
        mc.button(  label='Jnt Scale \n Comp Off', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.joint_scale_compensate_toggle.scale_compensate_off()', 
                    bgc = (0.5,0.1,0.1), 
                    statusBarMessage=''
                    )
        mc.button(  label='Jnt Scale \n Comp On', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.joint_scale_compensate_toggle.scale_compensate_on()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage=''
                    )
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Outliner \n Move Up 1', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.outliner_reorder.outliner_move_up()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage='Outliner Selection Move Up 1',
                    ann='Outliner Selection Move Up 1')
        mc.button(  label='Outliner \n Move Down 1', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.outliner_reorder.outliner_move_down()', 
                    bgc = (0.5,0.1,0.1), 
                    statusBarMessage='Outliner Selection Move Down 1',
                    ann='Outliner Selection Move Down 1')
        mc.button(  label='Outliner \n Move Up 5', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.outliner_reorder.outliner_move_up_five()', 
                    bgc = (0.1,0.5,0.1), 
                    statusBarMessage='Outliner Selection Move Up 5',
                    ann='Outliner Selection Move Up 5')
        mc.button(  label='Outliner \n Move Down 5', 
                    h=40, 
                    w=74, 
                    command = 'character_rigger.loose_tools.outliner_reorder.outliner_move_down_five()', 
                    bgc = (0.5,0.1,0.1), 
                    statusBarMessage='Outliner Selection Move Down 5',
                    ann='Outliner Selection Move Down 5')
        
        mc.button(  label='Select \nHierarchy', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().sel_hierarchy()', 
                    bgc = (0.1,0.1,0.4), 
                    statusBarMessage='',
                    ann='')
        mc.setParent("..")


        mc.rowLayout(numberOfColumns = 5)
        mc.button(  label='Copy Attributes \n To 2nd Object', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.loose_tools.copy_attribute.copy_attribute()', 
                    bgc = (0.1,0.1,0.1), 
                    statusBarMessage='Copy First Selected Translate Rotate Scale to Second Selected',
                    ann='Copy First Selected Translate Rotate Scale to Second Selected')
        mc.button(  label='Print \nObject Info', 
                    h=40, 
                    w=150, 
                    command = 'character_rigger.tabs.misc_tab.misc_tab_class().object_info()', 
                    bgc = (0.3,0.0,0.1), 
                    statusBarMessage='Print basic object attributes (translation, rotation, name)'
                    )
        mc.setParent("..")



        #parent column to tab
        mc.setParent('..')



        

        

        #_________________Tab Layout/ UI End___________________#

        #tabs layout
        mc.tabLayout(myTabs, edit=True, tabLabel=[ (auto_rig_tab, 'Auto Rig'), (modeling_tab, 'Modeling'), (rigging_tab, 'Rigging'), (animation_tab, 'Animation'), (color_tab, 'Color'), (shading_tab, 'Shading'), (misc_tab, 'Misc')], bs='none')

        #Show UI Window
        mc.showWindow()




