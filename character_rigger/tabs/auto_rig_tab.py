import maya.cmds as mc

import os

import random as rd

import pymel.core as pm

try:
    from itertools import izip as zip
except: # will be python 3.x series
    pass

from ..ar_rig import leg_rig
from ..ar_functions import find_jnts
from ..ar_functions import bb_nurbs_ctrl

    #_________________Auto Rig Tab Options _______________________#
    #_____________________________________________________________#

class auto_rig_options():

    def auto_rig_options(self):
        # lowest jnts in y of upper face jnts
        midFace_jnt_amnt = mc.textField('midFace_jnt_amnt_text', query=True, text=True)
        
        control_size = mc.textField('global_ctrl_size_text', query=True, text=True)

        headJnts_checkbox = mc.checkBox( 'headJnts_checkbox', query=1, v=1 )

        twstJnts_checkbox = mc.checkBox( 'twstJnts_checkbox', query=1, v=1 )

        elbow_pv_dist = mc.textField( 'elbow_pv_dist_text', query=1, tx=1 )

        knee_pv_dist = mc.textField( 'knee_pv_dist_text', query=1, tx=1 )

        return midFace_jnt_amnt, control_size, headJnts_checkbox, twstJnts_checkbox, elbow_pv_dist, knee_pv_dist

    # reverse foot locator distance adjusted with Control Size textfield
    def rev_foot_adj(self, direction):
        auto_rig_ui_info = self.auto_rig_options()
        control_size = auto_rig_ui_info[1]

        if direction == 'l' or direction == 'left':
            leg_rig.leg_rig().rev_foot_locators( direction = "left", ft_loc_dist = (10 * float(control_size) ) )
        if direction == 'r' or direction == 'right':
            leg_rig.leg_rig().rev_foot_locators( direction = "right", ft_loc_dist = (10 * float(control_size) ) )

    def show_orient_axis(self):
        mySel = mc.ls(sl=True)
        for i in mySel:
            mc.setAttr(i +  '.rotateOrder', cb=True)

            mc.setAttr(i +  '.rotateAxisX', cb=True)
            mc.setAttr(i +  '.rotateAxisY', cb=True)
            mc.setAttr(i +  '.rotateAxisZ', cb=True)

            mc.setAttr(i +  '.jointOrientX', cb=True)
            mc.setAttr(i +  '.jointOrientY', cb=True)
            mc.setAttr(i +  '.jointOrientZ', cb=True)

            mc.setAttr(i +  '.wireColorR', cb=True)
            mc.setAttr(i +  '.wireColorG', cb=True)
            mc.setAttr(i +  '.wireColorB', cb=True)

    def hide_orient_axis(self):
        mySel = mc.ls(sl=True)
        for i in mySel:
            mc.setAttr(i +  '.rotateOrder', cb=0)

            mc.setAttr(i +  '.rotateAxisX', cb=0)
            mc.setAttr(i +  '.rotateAxisY', cb=0)
            mc.setAttr(i +  '.rotateAxisZ', cb=0)

            mc.setAttr(i +  '.jointOrientX', cb=0)
            mc.setAttr(i +  '.jointOrientY', cb=0)
            mc.setAttr(i +  '.jointOrientZ', cb=0)


    def jnt_loc_axis(self):
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.spaceLocator()
            mc.setAttr(".localScaleX", 10)
            mc.setAttr(".localScaleY", 10)
            mc.setAttr(".localScaleZ", 10)
            mc.setAttr(".overrideEnabled",1)
            mc.setAttr(".overrideRGBColors",1)

            mc.setAttr(".overrideColorR", rd.uniform(0,1.0))
            mc.setAttr(".overrideColorG", rd.uniform(0,1.0))
            mc.setAttr(".overrideColorB", rd.uniform(0,1.0))
            
            myLoc = mc.rename("localAxis_" + i)
            
            mc.parent(myLoc, i, relative=True)

    def jnt_loc_axis_del(self):
        myShape = mc.ls('localAxis_*', type='locator')
        mySel = mc.listRelatives(myShape, p=1)

        for i in mySel:
            mc.delete(i)


    def disp_local_axis(self):
        #mc.select(hi=True)
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.setAttr(i + '.displayLocalAxis', 1)

    def disp_local_axis_off(self):
        #mc.select(hi=True)
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.setAttr(i + '.displayLocalAxis', 0)


    # create fresh scene from model, skeleton, and skin weights file (allow to adjust skeleton seperatly)
    def new_character_scene(self):
        dialog_result = mc.confirmDialog(   title='Confirm', 
                                            message='Create New \nCharacter Scene?', 
                                            button=['Yes','No'], 
                                            defaultButton='Yes', 
                                            cancelButton='No', 
                                            dismissString='No',
                                            icon='question',
                                            bgc=(.2,0,.2)
                                            )
        if dialog_result == 'Yes':
            # start new file
            print('New Scene!')
            mc.file(f=1, new=1)

            # import model
            model_browser_text = mc.textFieldButtonGrp('model_browser_text', query=True, text=True)
            print(model_browser_text)
            mc.file(model_browser_text, 
                    i=1,  #import
                    #type="FBX",
                    ignoreVersion=1, 
                    mergeNamespacesOnClash=0, 
                    #rpr="orc_body", 
                    #options="fbx",  
                    pr=1,
                    importFrameRate=0, 
                    importTimeRange="keep" 
                    )

            # import skeleton
            skele_browser_text = mc.textFieldButtonGrp('skele_browser_text', query=True, text=True)
            print(skele_browser_text)
            mc.file(skele_browser_text, 
                    i=1,  #import
                    ignoreVersion=1, 
                    mergeNamespacesOnClash=0, 
                    pr=1,
                    importFrameRate=0, 
                    importTimeRange="keep" 
                    )

            # get weights text field
            weights_text = mc.textFieldButtonGrp('skin_weights_browser_text', query=True, text=True)
            # split up skin weight import file to work with 'deformerWeights' function
            weights_text_split = weights_text.split('/')
            # get last value of split text which is file name
            weights_text_file = weights_text_split[-1]
            # remove file name from string for just path
            weights_text_path = weights_text.replace(weights_text_file, '')

            # get character mesh
            characterShape = mc.ls(type='mesh')
            characterTransform = mc.listRelatives(characterShape, p=1)
            # get root skeleton joint
            skele_root_jnt = find_jnts.find_jnts().find_spine_root()

            # create default bind skin betwenn root joint and character mesh
            new_skinCluster = mc.skinCluster( skele_root_jnt, characterTransform)
            # set all weights to root joint to simplify and avoid skin transfer glitches
            mc.skinPercent( new_skinCluster[0], characterTransform, transformValue=(skele_root_jnt,1) )
            # import and apply user pre-saved weights 
            mc.deformerWeights( weights_text_file,
                                im=1, 
                                method="index", 
                                deformer=new_skinCluster[0], 
                                path=weights_text_path 
                                ) 
            # default option of normalize weights (that is on for weight import)
            mc.skinCluster( new_skinCluster, e=1, forceNormalizeWeights=1 )

        else:
            print('Cancel!')
            pass


    def model_file_browse(self):
        model_path_dir = mc.fileDialog2(fileMode=1, #1 A single existing file.
                                        caption='Choose Location',
                                        dialogStyle=2,
                                        okCaption='Accept')

        if model_path_dir: mc.textFieldButtonGrp('model_browser_text', edit=True, text=model_path_dir[0]) 


    def skele_file_browse(self):
        skele_path_dir = mc.fileDialog2(fileMode=1, #1 A single existing file.
                                        caption='Choose Location',
                                        dialogStyle=2,
                                        okCaption='Accept'
                                        )

        if skele_path_dir: mc.textFieldButtonGrp('skele_browser_text', edit=True, text=skele_path_dir[0]) 

    def skin_weights_browse(self):
        weights_path_dir = mc.fileDialog2(  fileMode=1, #1 A single existing file.
                                            caption='Choose Location',
                                            dialogStyle=2,
                                            okCaption='Accept'
                                            )

        if weights_path_dir: mc.textFieldButtonGrp('skin_weights_browser_text', edit=True, text=weights_path_dir[0]) 

    
    def sel_hierarchy(self):
        mySel = mc.ls(sl=1)
        mc.select(mySel, hi=1)


    def import_wyvern_fbx(self):
        file_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "/" "wyvern_skele_skin.fbx" )
        print(file_path)
        mc.file(    str(file_path),
                    i=True
                    )


    def wyverm_bounding_boxes(self):
        #_________________#
        #______tail_______#
        #_________________#
        chest_ctrl_name = 'standin_obj_chest_root'
        chest_ctrl_grp = chest_ctrl_name + '_grp'

        spine_root_ctrl_name = 'standin_obj_spine_root'
        spine_root_ctrl_grp = spine_root_ctrl_name + '_grp'

        start_ctrl_name = 'standin_obj_tail_start'
        start_ctrl_grp = start_ctrl_name + '_grp'

        end_ctrl_name = 'standin_obj_tail_end'
        end_ctrl_grp = end_ctrl_name + '_grp'

        ikTailA_ctrl_name = 'standin_obj_ikSpline_A'
        ikTailA_ctrl_grp = ikTailA_ctrl_name + '_grp'

        ikTailB_ctrl_name = 'standin_obj_ikSpline_B'
        ikTailB_ctrl_grp = ikTailB_ctrl_name + '_grp'

        spine_root_curve_name = 'spine_root_tail_curve'

        start_curve_name = 'start_tail_curve'

        start_curve_nameA = 'start_tail_curveA'

        start_curve_nameB = 'start_tail_curveB'

        organize_grp_name = 'bb_slc_wyvern_grp'

        tail_grp_name = 'bb_slc_wyver_tail_grp'

        l_wing_grp_name = 'bb_slc_wyvern_l_wing_grp'

        #____________________#
        if mc.objExists(organize_grp_name) == False:
            organize_grp = mc.group(em=True, n='bb_slc_wyvern_grp')

        if mc.objExists(tail_grp_name) == False:
            tail_grp = mc.group(em=True, n='bb_slc_wyver_tail_grp')
            if mc.objExists(organize_grp_name):
                mc.parent(tail_grp, organize_grp)

        if mc.objExists(l_wing_grp_name) == False:
            l_wing_grp = mc.group(em=True, n='bb_slc_wyvern_l_wing_grp')
            if mc.objExists(organize_grp_name):
                mc.parent(l_wing_grp, organize_grp)

        
        #____________________#
        if mc.objExists(chest_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_chest_root', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=1, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_box_ctrl()
            mc.select(chest_ctrl_name)
            mc.Unparent()
            mc.delete(chest_ctrl_grp)

            mc.setAttr(chest_ctrl_name + '.translate', 0.0, 174.427, 40.123)

            #mc.delete('standin_obj_chest_root1')

            mc.parent(  chest_ctrl_name, 
                        organize_grp)
        
        #____________________#
        if mc.objExists(spine_root_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_spine_root', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=1, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_box_ctrl()
            mc.select(spine_root_ctrl_name)
            mc.Unparent()
            mc.delete(spine_root_ctrl_grp)

            mc.setAttr(spine_root_ctrl_name + '.translate', 0.0, 140.38, 1.278)

            mc.parent(  spine_root_ctrl_name, 
                        tail_grp)

        
        #____________________#
        if mc.objExists(start_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_tail_start', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=1, 
                                        color1B=0, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_box_ctrl()
            mc.select(start_ctrl_name)
            mc.Unparent()
            mc.delete(start_ctrl_grp)

            mc.setAttr(start_ctrl_name + '.translate', 0.0, 133.91, -22.863)

            mc.parent(
                        start_ctrl_name, 
                        tail_grp
                        )

        #____________________#
        if mc.objExists(end_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_tail_end', 
                                        size=5, 
                                        color1R=1, 
                                        color1G=0, 
                                        color1B=0, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_box_ctrl()
            mc.select(end_ctrl_name)
            mc.Unparent(end_ctrl_name)
            mc.delete(end_ctrl_grp)

            mc.setAttr(end_ctrl_name + '.translate', 0.0, 100.497, -283.462)

            mc.parent(
                        end_ctrl_name,
                        tail_grp
                        )


        #____________________#
        if mc.objExists(ikTailA_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_ikSpline_A', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=.3, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_sphere_ctrl()
            ikTailA_ctrl_name = 'standin_obj_ikSpline_A1'
            ikTailA_ctrl_grp = ikTailA_ctrl_name + '_grp'
            mc.select(ikTailA_ctrl_name)
            mc.Unparent(ikTailA_ctrl_name)
            mc.delete(ikTailA_ctrl_grp)

            mc.setAttr(ikTailA_ctrl_name + '.translate', 0.0, 105.52, -131.872)

            mc.parent(
                        ikTailA_ctrl_name,
                        tail_grp
                        )
            ikTailA_ctrl_name = mc.rename(ikTailA_ctrl_name, ikTailA_ctrl_name[:-1])

        #____________________#
        if mc.objExists(ikTailB_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_ikSpline_B', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=.3, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_sphere_ctrl()
            ikTailB_ctrl_name = 'standin_obj_ikSpline_B1'
            ikTailB_ctrl_grp = ikTailB_ctrl_name + '_grp'
            mc.select(ikTailB_ctrl_name)
            mc.Unparent(ikTailB_ctrl_name)
            mc.delete(ikTailB_ctrl_grp)

            mc.setAttr(ikTailB_ctrl_name + '.translate', 0.0, 100.497, -283.462)

            mc.parent(
                        ikTailB_ctrl_name,
                        tail_grp
                        )
            ikTailB_ctrl_name = mc.rename(ikTailB_ctrl_name, ikTailB_ctrl_name[:-1])
        

        # ______________ connect curves _______________#
        #_____________
        if mc.objExists(spine_root_curve_name) == False:
            spine_root_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='spine_root_tail_curve')
            spine_root_curve_shp = mc.listRelatives(spine_root_curve, type='shape')
            mc.setAttr(spine_root_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(spine_root_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(spine_root_curve_shp[0] + '.overrideColorRGB', 0, 1, 1)
            mc.setAttr(spine_root_curve_shp[0] + '.lineWidth', 2)

            mc.connectAttr( spine_root_ctrl_name + '.translate', 
                            spine_root_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( start_ctrl_name + '.translate', 
                            spine_root_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        spine_root_curve,
                        tail_grp
                        )

        #_____________
        if mc.objExists(start_curve_name) == False:
            start_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='start_tail_curve')
            start_curve_shp = mc.listRelatives(start_curve, type='shape')
            mc.setAttr(start_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(start_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(start_curve_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(start_curve_shp[0] + '.lineWidth', 4)

            mc.connectAttr( start_ctrl_name + '.translate', 
                            start_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( end_ctrl_name + '.translate', 
                            start_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        start_curve,
                        tail_grp
                        )

        #_____________
        if mc.objExists(start_curve_nameA) == False:
            start_curveA = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='start_tail_curveA')
            start_curveA_shp = mc.listRelatives(start_curveA, type='shape')
            mc.setAttr(start_curveA_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(start_curveA_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(start_curveA_shp[0] + '.overrideColorRGB', 0, 1, 1)
            mc.setAttr(start_curveA_shp[0] + '.lineWidth', 2)

            mc.connectAttr( start_ctrl_name + '.translate', 
                            start_curveA_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( ikTailA_ctrl_name + '.translate', 
                            start_curveA_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        start_curveA,
                        tail_grp
                        )

        #_____________
        if mc.objExists(start_curve_nameB) == False:
            start_curveB = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='start_tail_curveB')
            start_curveB_shp = mc.listRelatives(start_curveB, type='shape')
            mc.setAttr(start_curveB_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(start_curveB_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(start_curveB_shp[0] + '.overrideColorRGB', 0, 1, 1)
            mc.setAttr(start_curveB_shp[0] + '.lineWidth', 2)

            mc.connectAttr( start_ctrl_name + '.translate', 
                            start_curveB_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( ikTailB_ctrl_name + '.translate', 
                            start_curveB_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        start_curveB,
                        tail_grp
                        )


        


        #_________________#
        #_____l_wing______#
        #_________________#

        l_chest_root_curve_name = 'l_chest_root_curve'

        l_clavicle_curve_name = 'l_clavicle_curve'

        l_arm_start_curve_name = 'l_arm_start_curve'

        l_elbow_curve_name = 'l_elbow_curve'
        l_elbow_curveA_name = 'l_elbowA_curve'

        l_arm_end_curveA_name = 'l_arm_end_curveA'
        l_arm_end_curveB_name = 'l_arm_end_curveB'
        l_arm_end_curveC_name = 'l_arm_end_curveC'
        l_arm_end_curveD_name = 'l_arm_end_curveD'
        l_arm_end_curveE_name = 'l_arm_end_curveE'


        l_wing_bb_lst = [
                            'standin_obj_l_clavicle', 
                            'standin_obj_l_arm_start',
                            'standin_obj_l_elbow',
                            'standin_fkObj_l_wingA',
                            'standin_obj_l_arm_end',
                            'standin_fkObj_l_wingB',
                            'standin_fkObj_l_wingC',
                            'standin_fkObj_l_wingD',
                            'standin_fkObj_l_wingF',
                            'standin_fkObj_l_wingE',
                        ]

        l_wing_bb_grp_lst = [
                            'standin_obj_l_clavicle_grp', 
                            'standin_obj_l_arm_start_grp',
                            'standin_obj_l_elbow_grp',
                            'standin_fkObj_l_wingA_grp',
                            'standin_obj_l_arm_end_grp',
                            'standin_fkObj_l_wingB_grp',
                            'standin_fkObj_l_wingC_grp',
                            'standin_fkObj_l_wingD_grp',
                            'standin_fkObj_l_wingF_grp',
                            'standin_fkObj_l_wingE_grp',
                        ]

        l_wing_bb_pos_lst = [   
                            (3.35, 171.894, 85.449), 
                            (20.417, 198.92, 53.718),
                            (86.027, 201.213, 26.698),
                            (86.708, 197.721, 20.523),
                            (173.696, 256.659, 81.309),
                            (183.624, 257.845, 79.356),
                            (196.932, 264.209, 84.819),
                            (206.782, 270.019, 95.036),
                            (199.161, 274.51, 101.963),
                            (180.16, 264.177, 92.352)
                        ]


        for i_bb, i_bb_grp, i_bb_pos in zip(l_wing_bb_lst, l_wing_bb_grp_lst, l_wing_bb_pos_lst):
             #____________________#
            if mc.objExists(i_bb) == False:
                bb_nurbs_ctrl.bb_nurbs_ctrl(name=i_bb, 
                                            size=5, 
                                            color1R=0, 
                                            color1G=0, 
                                            color1B=1, 
                                            color2R=1, 
                                            color2G=1, 
                                            color2B=0).sel_box_ctrl()
                mc.select(i_bb)
                mc.Unparent()
                mc.delete(i_bb_grp)

                mc.setAttr(i_bb + '.translate', i_bb_pos[0], i_bb_pos[1], i_bb_pos[2] )
                mc.setAttr(i_bb + '.scale', 0.5, 0.5, 0.5 )

                mc.parent(  i_bb, 
                            l_wing_grp)
        


        #_________________ connection curves ______________________#


        #_____________
        if mc.objExists(l_chest_root_curve_name) == False:
            l_chest_root_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_chest_root_curve')
            l_chest_root_curve_shp = mc.listRelatives(l_chest_root_curve, type='shape')
            mc.setAttr(l_chest_root_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_chest_root_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_chest_root_curve_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_chest_root_curve_shp[0] + '.lineWidth', 2)

            mc.connectAttr( chest_ctrl_name + '.translate', 
                            l_chest_root_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[0] + '.translate', 
                            l_chest_root_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_chest_root_curve,
                        l_wing_grp
                        )

        #_____________
        if mc.objExists(l_clavicle_curve_name) == False:
            l_clavicle_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_clavicle_curve')
            l_clavicle_curve_shp = mc.listRelatives(l_clavicle_curve, type='shape')
            mc.setAttr(l_clavicle_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_clavicle_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_clavicle_curve_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_clavicle_curve_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[0] + '.translate', 
                            l_clavicle_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[1] + '.translate', 
                            l_clavicle_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_clavicle_curve,
                        l_wing_grp
                        )
        
        #_____________
        if mc.objExists(l_arm_start_curve_name) == False:
            l_arm_start_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_start_curve')
            l_arm_start_curve_shp = mc.listRelatives(l_arm_start_curve, type='shape')
            mc.setAttr(l_arm_start_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_start_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_start_curve_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_start_curve_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[1] + '.translate', 
                            l_arm_start_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[2] + '.translate', 
                            l_arm_start_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_start_curve,
                        l_wing_grp
                        )

        #_____________
        if mc.objExists(l_elbow_curve_name) == False:
            l_elbow_curve = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_elbow_curve')
            l_elbow_curve_shp = mc.listRelatives(l_elbow_curve, type='shape')
            mc.setAttr(l_elbow_curve_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_elbow_curve_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_elbow_curve_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_elbow_curve_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[2] + '.translate', 
                            l_elbow_curve_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[3] + '.translate', 
                            l_elbow_curve_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_elbow_curve,
                        l_wing_grp
                        )


        #_____________
        if mc.objExists(l_elbow_curveA_name) == False:
            l_elbow_curveA = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_elbow_curveA')
            l_elbow_curveA_shp = mc.listRelatives(l_elbow_curveA, type='shape')
            mc.setAttr(l_elbow_curveA_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_elbow_curveA_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_elbow_curveA_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_elbow_curveA_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[2] + '.translate', 
                            l_elbow_curveA_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_elbow_curveA_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_elbow_curveA,
                        l_wing_grp
                        )


        #_____________**
        if mc.objExists(l_arm_end_curveA_name) == False:
            l_arm_end_curveA = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_end_curveA')
            l_arm_end_curveA_shp = mc.listRelatives(l_arm_end_curveA, type='shape')
            mc.setAttr(l_arm_end_curveA_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_end_curveA_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_end_curveA_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_end_curveA_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_arm_end_curveA_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[5] + '.translate', 
                            l_arm_end_curveA_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_end_curveA,
                        l_wing_grp
                        )

        #_____________**
        if mc.objExists(l_arm_end_curveB_name) == False:
            l_arm_end_curveB = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_end_curveB')
            l_arm_end_curveB_shp = mc.listRelatives(l_arm_end_curveB, type='shape')
            mc.setAttr(l_arm_end_curveB_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_end_curveB_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_end_curveB_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_end_curveB_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_arm_end_curveB_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[6] + '.translate', 
                            l_arm_end_curveB_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_end_curveB,
                        l_wing_grp
                        )

        #_____________**
        if mc.objExists(l_arm_end_curveC_name) == False:
            l_arm_end_curveC = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_end_curveC')
            l_arm_end_curveC_shp = mc.listRelatives(l_arm_end_curveC, type='shape')
            mc.setAttr(l_arm_end_curveC_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_end_curveC_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_end_curveC_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_end_curveC_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_arm_end_curveC_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[7] + '.translate', 
                            l_arm_end_curveC_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_end_curveC,
                        l_wing_grp
                        )

        #_____________**
        if mc.objExists(l_arm_end_curveD_name) == False:
            l_arm_end_curveD = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_end_curveD')
            l_arm_end_curveD_shp = mc.listRelatives(l_arm_end_curveD, type='shape')
            mc.setAttr(l_arm_end_curveD_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_end_curveD_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_end_curveD_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_end_curveD_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_arm_end_curveD_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[9] + '.translate', 
                            l_arm_end_curveD_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_end_curveD,
                        l_wing_grp
                        )

        #_____________**
        if mc.objExists(l_arm_end_curveE_name) == False:
            l_arm_end_curveE = mc.curve(degree=1, p=[(0,0,0),(0,0,-100)], n='l_arm_end_curveE')
            l_arm_end_curveE_shp = mc.listRelatives(l_arm_end_curveE, type='shape')
            mc.setAttr(l_arm_end_curveE_shp[0] + '.overrideEnabled', 1)
            mc.setAttr(l_arm_end_curveE_shp[0] + '.overrideRGBColors', 1)
            mc.setAttr(l_arm_end_curveE_shp[0] + '.overrideColorRGB', 0, 1, 0)
            mc.setAttr(l_arm_end_curveE_shp[0] + '.lineWidth', 2)

            mc.connectAttr( l_wing_bb_lst[4] + '.translate', 
                            l_arm_end_curveE_shp[0] + '.controlPoints[0]', f=True )

            mc.connectAttr( l_wing_bb_lst[8] + '.translate', 
                            l_arm_end_curveE_shp[0] + '.controlPoints[1]', f=True )

            mc.parent(  
                        l_arm_end_curveE,
                        l_wing_grp
                        )


        #_________________#
        #_____r_wing______#
        #_________________#
        
        r_wing_grp0 = mc.duplicate(l_wing_grp, rr=True, un=True)

        r_wing_grp1 = mc.rename(r_wing_grp0, 'bb_slc_wyvern_r_wing_grp' )
        # take away 1 at end of name
        r_wing_grp2 = r_wing_grp1[:-1]

        mc.select('bb_slc_wyvern_r_wing_grp', hi=True)

        r_wing_grp0_lst = mc.ls(sl=True)

        for i in pm.selected():
            i.rename(i.name().replace('l_', 'r_'))

        # -x flip to other side
        mc.setAttr(r_wing_grp1 + '.scaleX', -1 )

        # rename again to name curve shapes different
        mc.select('bb_slc_wyvern_r_wing_grp', hi=True)

        r_wing_grp0_lst = mc.ls(sl=True)

        for i in r_wing_grp0_lst:
            mc.rename(i, i)

        # delete extra duplicated chest node
        mc.delete('standin_obj_chest_root1')

        #attach curve to middle chest
        r_chest_root_curve_shp = mc.listRelatives('r_chest_root_curve', type='shape')
        mc.connectAttr( chest_ctrl_name + '.translate', 
                        r_chest_root_curve_shp[0] + '.controlPoints[0]', f=True )

        #____________________#
        #_____elbows PV______#
        #____________________#

        l_elbowPV_ctrl_name = 'standin_obj_l_elbow_pv'
        l_elbowPV_ctrl_grp = l_elbowPV_ctrl_name + '_grp'

        r_elbowPV_ctrl_name = 'standin_obj_r_elbow_pv'
        r_elbowPV_ctrl_grp = r_elbowPV_ctrl_name + '_grp'

        #__________l__________#
        if mc.objExists(l_elbowPV_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_l_elbow_pv', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=0, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_pyramid_ctrl()
            l_elbowPV_ctrl_name = 'standin_obj_l_elbow_pv1'
            l_elbowPV_ctrl_grp = l_elbowPV_ctrl_name + '_grp'
            mc.select(l_elbowPV_ctrl_name)
            mc.Unparent(l_elbowPV_ctrl_name)
            mc.delete(l_elbowPV_ctrl_grp)

            mc.setAttr(l_elbowPV_ctrl_name + '.translate', 106.07, 127.39, -110.583 )
            mc.setAttr(l_elbowPV_ctrl_name + '.rotate', -29.127, 0.017, 15.22 )


            mc.parent(
                        l_elbowPV_ctrl_name,
                        organize_grp
                        )
            l_elbowPV_ctrl_name = mc.rename(l_elbowPV_ctrl_name, l_elbowPV_ctrl_name[:-1])

        #__________r__________#
        if mc.objExists(r_elbowPV_ctrl_name) == False:
            bb_nurbs_ctrl.bb_nurbs_ctrl(name='standin_obj_r_elbow_pv', 
                                        size=5, 
                                        color1R=0, 
                                        color1G=0, 
                                        color1B=1, 
                                        color2R=1, 
                                        color2G=1, 
                                        color2B=0).sel_pyramid_ctrl()
            r_elbowPV_ctrl_name = 'standin_obj_r_elbow_pv1'
            r_elbowPV_ctrl_grp = r_elbowPV_ctrl_name + '_grp'
            mc.select(r_elbowPV_ctrl_name)
            mc.Unparent(r_elbowPV_ctrl_name)
            mc.delete(r_elbowPV_ctrl_grp)

            mc.setAttr(r_elbowPV_ctrl_name + '.translate', -106.07, 127.39, -110.583 )
            mc.setAttr(r_elbowPV_ctrl_name + '.rotate', -29.127, -0.017, -15.22 )


            mc.parent(
                        r_elbowPV_ctrl_name,
                        organize_grp
                        )
            r_elbowPV_ctrl_name = mc.rename(r_elbowPV_ctrl_name, r_elbowPV_ctrl_name[:-1])


        #hide grp
        #mc.hide(organize_grp)


    def wyvern_rev_foot_locators(self):
        l_direction = 'l'
        r_direction = 'r'

        l_loc_grp = mc.group(em=True, n=l_direction + '_ft_loc_grp')
        r_loc_grp = mc.group(em=True, n=r_direction + '_ft_loc_grp')

        # __________l locators ________#
        if mc.objExists(l_direction + '_loc_ankle') == False:
            loc_ankle = mc.spaceLocator(n = l_direction + '_loc_ankle')
            mc.setAttr((loc_ankle[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_ankle[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_ankle[0] + '.translate'), 28.478, 9.607, 7.831)
            mc.setAttr((loc_ankle[0] + '.rotate'), 0.0, -86.004, 0.0)
            mc.parent(loc_ankle, l_loc_grp)
        else:
            print(l_direction + '_loc_ankle' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(l_direction + '_loc_toe') == False:
            loc_toe = mc.spaceLocator(n = l_direction + '_loc_toe')
            mc.setAttr((loc_toe[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe[0] + '.translate'), 29.078, 4.778, 16.419)
            mc.setAttr((loc_toe[0] + '.rotate'), 0.0, -86.004, 0.0)
            mc.parent(loc_toe, l_loc_grp)
        else:
            print(l_direction + '_loc_toe' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(l_direction + '_loc_toe_end') == False:
            loc_toe_end = mc.spaceLocator(n = l_direction + '_loc_toe_end')
            mc.setAttr((loc_toe_end[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe_end[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe_end[0] + '.translate'), 30.123, 0.0, 31.383)
            mc.setAttr((loc_toe_end[0] + '.rotate'), 0.0, -86.004, 0.0)
            mc.parent(loc_toe_end, l_loc_grp)
        else:
            print(l_direction + '_loc_toe_end' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(l_direction + '_loc_heel') == False:
            loc_heel = mc.spaceLocator(n = l_direction + '_loc_heel')
            mc.setAttr((loc_heel[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_heel[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_heel[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_heel[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_heel[0] + '.translate'), 28.439, 0.0, 7.273)
            mc.setAttr((loc_heel[0] + '.rotate'), 0.0, -86.004, 0.0)
            mc.parent(loc_heel, l_loc_grp)
        else:
            print(l_direction + '_loc_heel' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(l_direction + '_loc_outer_foot') == False:
            loc_outer_foot = mc.spaceLocator(n = l_direction + '_loc_outer_foot')
            mc.setAttr((loc_outer_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_outer_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_outer_foot[0] + '.translate'), 40.142, 0.0, 15.063)
            mc.setAttr((loc_outer_foot[0] + '.rotate'), 0.0, -63.306, 0.0)
            mc.parent(loc_outer_foot, l_loc_grp)
        else:
            print(l_direction + '_loc_outer_foot' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(l_direction + '_loc_inner_foot') == False:
            loc_inner_foot = mc.spaceLocator(n = l_direction + '_loc_inner_foot')
            mc.setAttr((loc_inner_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_inner_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_inner_foot[0] + '.translate'), 17.481, 0.0, 17.846)
            mc.setAttr((loc_inner_foot[0] + '.rotate'), -0.0, -104.943, 0.0)
            mc.parent(loc_inner_foot, l_loc_grp)
        else:
            print(l_direction + '_loc_inner_foot' + ' Already Exists!')
            mc.select(cl=True)


    
        # __________r locators ________#
        if mc.objExists(r_direction + '_loc_ankle') == False:
            loc_ankle = mc.spaceLocator(n = r_direction + '_loc_ankle')
            mc.setAttr((loc_ankle[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_ankle[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_ankle[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_ankle[0] + '.translate'), -28.478, 9.607, 7.831)
            mc.setAttr((loc_ankle[0] + '.rotate'), 0.0, 266.004, 0.0)
            mc.parent(loc_ankle, r_loc_grp)
        else:
            print(r_direction + '_loc_ankle' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(r_direction + '_loc_toe') == False:
            loc_toe = mc.spaceLocator(n = r_direction + '_loc_toe')
            mc.setAttr((loc_toe[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe[0] + '.translate'), -29.078, 4.778, 16.419)
            mc.setAttr((loc_toe[0] + '.rotate'), 180.0, -86.004, 180.0)
            mc.parent(loc_toe, r_loc_grp)
        else:
            print(r_direction + '_loc_toe' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(r_direction + '_loc_toe_end') == False:
            loc_toe_end = mc.spaceLocator(n = r_direction + '_loc_toe_end')
            mc.setAttr((loc_toe_end[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_toe_end[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_toe_end[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_toe_end[0] + '.translate'), -30.123, 0.0, 31.383)
            mc.setAttr((loc_toe_end[0] + '.rotate'), 180.0, -86.004, 180.0)
            mc.parent(loc_toe_end, r_loc_grp)
        else:
            print(r_direction + '_loc_toe_end' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(r_direction + '_loc_heel') == False:
            loc_heel = mc.spaceLocator(n = r_direction + '_loc_heel')
            mc.setAttr((loc_heel[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_heel[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_heel[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_heel[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_heel[0] + '.translate'), -28.439, 0.0, 7.273)
            mc.setAttr((loc_heel[0] + '.rotate'), 0.0, 266.004, 0.0)
            mc.parent(loc_heel, r_loc_grp)
        else:
            print(r_direction + '_loc_heel' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(r_direction + '_loc_outer_foot') == False:
            loc_outer_foot = mc.spaceLocator(n = r_direction + '_loc_outer_foot')
            mc.setAttr((loc_outer_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_outer_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_outer_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_outer_foot[0] + '.translate'), -40.142, 0.0, 15.063)
            mc.setAttr((loc_outer_foot[0] + '.rotate'), 180.0, -63.306, 180.0)
            mc.parent(loc_outer_foot, r_loc_grp)
        else:
            print(r_direction + '_loc_outer_foot' + ' Already Exists!')
            mc.select(cl=True)


        if mc.objExists(r_direction + '_loc_inner_foot') == False:
            loc_inner_foot = mc.spaceLocator(n = r_direction + '_loc_inner_foot')
            mc.setAttr((loc_inner_foot[0] + '.overrideEnabled'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideRGBColors'), 1)
            mc.setAttr((loc_inner_foot[0] + '.overrideColorRGB'), .1, 1, 0)
            mc.setAttr((loc_inner_foot[0] + '.localScale'), 5, 5, 5)
            mc.setAttr((loc_inner_foot[0] + '.translate'), -17.481, 0.0, 17.846)
            mc.setAttr((loc_inner_foot[0] + '.rotate'), 0.0, -75.057, -0.0)
            mc.parent(loc_inner_foot, r_loc_grp)
        else:
            print(r_direction + '_loc_inner_foot' + ' Already Exists!')
            mc.select(cl=True)


        # hide grps
        #mc.hide(l_loc_grp)
        #mc.hide(r_loc_grp)

