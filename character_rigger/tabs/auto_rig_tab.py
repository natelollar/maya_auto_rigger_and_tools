import maya.cmds as mc

import random as rd

from ..ar_rig import leg_rig
from ..ar_functions import find_jnts

    #_________________Auto Rig Tab Options _______________________#
    #_____________________________________________________________#

class auto_rig_options():

    def auto_rig_options(self):
        # lowest jnts in y of upper face jnts
        midFace_jnt_amnt = mc.textField('midFace_jnt_amnt_text', query=True, text=True)
        
        control_size = mc.textField('global_ctrl_size_text', query=True, text=True)

        headJnts_checkbox = mc.checkBox( 'headJnts_checkbox', query=1, v=1 )

        twstJnts_checkbox = mc.checkBox( 'twstJnts_checkbox', query=1, v=1 )

        arm_soft_ik = mc.textField( 'arm_soft_ik_amount_text', query=1, tx=1 )

        leg_soft_ik = mc.textField( 'leg_soft_ik_amount_text', query=1, tx=1 )

        return midFace_jnt_amnt, control_size, headJnts_checkbox, twstJnts_checkbox, arm_soft_ik, leg_soft_ik

    # reverse foot locator distance adjusted with Control Size textfield
    def rev_foot_adj(self, direction):
        auto_rig_ui_info = self.auto_rig_options()
        control_size = auto_rig_ui_info[1]

        if direction == 'left':
            leg_rig.leg_rig().rev_foot_locators( direction = "left", ft_loc_dist = (10 * float(control_size) ) )
        if direction == 'right':
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






