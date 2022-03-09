import maya.cmds as mc

from ..ar_rig import leg_rig

    #_________________Auto Rig Tab Options _______________________#
    #_____________________________________________________________#

class auto_rig_options():

    def auto_rig_options(self):
        # lowest jnts in y of upper face jnts
        midFace_jnt_amnt = mc.textField('midFace_jnt_amnt_text', query=True, text=True)
        
        control_size = mc.textField('global_ctrl_size_text', query=True, text=True)

        headJnts_checkbox = mc.checkBox( 'headJnts_checkbox', query=1, v=1 )

        return midFace_jnt_amnt, control_size, headJnts_checkbox

    # reverse foot locator distance adjusted with Control Size textfield
    def rev_foot_adj(self, direction):
        auto_rig_ui_info = self.auto_rig_options()
        control_size = auto_rig_ui_info[1]

        if direction == 'left':
            leg_rig.leg_rig().rev_foot_locators( direction = "left", ft_loc_dist = (10 * float(control_size) ) )
        if direction == 'right':
            leg_rig.leg_rig().rev_foot_locators( direction = "right", ft_loc_dist = (10 * float(control_size) ) )

