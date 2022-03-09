import maya.cmds as mc

import random as rd

from ..ar_rig import leg_rig

    #_________________Auto Rig Tab Options _______________________#
    #_____________________________________________________________#

class auto_rig_options():

    def auto_rig_options(self):
        # lowest jnts in y of upper face jnts
        midFace_jnt_amnt = mc.textField('midFace_jnt_amnt_text', query=True, text=True)
        
        control_size = mc.textField('global_ctrl_size_text', query=True, text=True)

        headJnts_checkbox = mc.checkBox( 'headJnts_checkbox', query=1, v=1 )

        twstJnts_checkbox = mc.checkBox( 'twstJnts_checkbox', query=1, v=1 )

        return midFace_jnt_amnt, control_size, headJnts_checkbox, twstJnts_checkbox

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

        mc.setAttr(mySel[0] +  '.rotateOrder', cb=True)

        mc.setAttr(mySel[0] +  '.rotateAxisX', cb=True)
        mc.setAttr(mySel[0] +  '.rotateAxisY', cb=True)
        mc.setAttr(mySel[0] +  '.rotateAxisZ', cb=True)

        mc.setAttr(mySel[0] +  '.jointOrientX', cb=True)
        mc.setAttr(mySel[0] +  '.jointOrientY', cb=True)
        mc.setAttr(mySel[0] +  '.jointOrientZ', cb=True)


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


    def disp_local_axis(self):
        mc.select(hi=True)
        mySel = mc.ls(sl=True)

        for i in mySel:
            mc.setAttr(i + ".displayLocalAxis", 1)

