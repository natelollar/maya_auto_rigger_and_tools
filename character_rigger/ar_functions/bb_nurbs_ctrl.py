import maya.cmds as mc

from . import nurbs_ctrl

class bb_nurbs_ctrl():

    def __init__(self, name, size, color1R, color1G, color1B, color2R, color2G, color2B):
        self.name = name
        self.size = size
        self.color1R = color1R
        self.color1G = color1G
        self.color1B = color1B
        self.color2R = color2R
        self.color2G = color2G
        self.color2B = color2B


    def sel_box_ctrl(self):
        box_ctrl_var = nurbs_ctrl.nurbs_ctrl( self.name, 5, self.color1R, self.color1G, self.color1B )
        box_ctrl_info = box_ctrl_var.box_ctrl()
        box_ctrl_grp = box_ctrl_info[0]
        box_ctrl = box_ctrl_info[1]
        locator_ctrl_var = nurbs_ctrl.nurbs_ctrl( box_ctrl + 'A', 1, self.color2R, self.color2G, self.color2B )
        locator_ctrl_info = locator_ctrl_var.locator_ctrl()
        locator_ctrl_grp = locator_ctrl_info[0]
        locator_ctrl = locator_ctrl_info[1]

        mc.parent(locator_ctrl, w=True)

        mc.delete(locator_ctrl_grp)

        locator_ctrl_shape = mc.listRelatives(locator_ctrl, s=True)
        
        mc.parent(locator_ctrl_shape, box_ctrl, r=True, shape=True)
        
        mc.delete(locator_ctrl)


    def sel_sphere_ctrl(self):
        sphere_ctrl_var = nurbs_ctrl.nurbs_ctrl( self.name, 1.7, self.color1R, self.color1G, self.color1B )
        sphere_ctrl_info = sphere_ctrl_var.sphere_ctrl()
        sphere_ctrl_grp = sphere_ctrl_info[0]
        sphere_ctrl = sphere_ctrl_info[1]
        locator_ctrl_var = nurbs_ctrl.nurbs_ctrl( sphere_ctrl + 'C', 1, self.color2R, self.color2G, self.color2B )
        locator_ctrl_info = locator_ctrl_var.locator_ctrl()
        locator_ctrl_grp = locator_ctrl_info[0]
        locator_ctrl = locator_ctrl_info[1]

        mc.parent(locator_ctrl, w=True)

        mc.delete(locator_ctrl_grp)

        locator_ctrl_shape = mc.listRelatives(locator_ctrl, s=True)
        
        mc.parent(locator_ctrl_shape, sphere_ctrl, r=True, shape=True)
        
        mc.delete(locator_ctrl)


    def sel_tri_circle_ctrl(self):
        tri_circle_ctrl_var = nurbs_ctrl.nurbs_ctrl( self.name, 1, self.color1R, self.color1G, self.color1B )
        tri_circle_ctrl_info = tri_circle_ctrl_var.tri_circle_ctrl()
        tri_circle_ctrl_grp = tri_circle_ctrl_info[0]
        tri_circle_ctrl = tri_circle_ctrl_info[1]
        locator_ctrl_var = nurbs_ctrl.nurbs_ctrl( tri_circle_ctrl + 'C', 1, self.color2R, self.color2G, self.color2B )
        locator_ctrl_info = locator_ctrl_var.locator_ctrl()
        locator_ctrl_grp = locator_ctrl_info[0]
        locator_ctrl = locator_ctrl_info[1]

        mc.parent(locator_ctrl, w=True)

        mc.delete(locator_ctrl_grp)

        locator_ctrl_shape = mc.listRelatives(locator_ctrl, s=True)
        
        mc.parent(locator_ctrl_shape, tri_circle_ctrl, r=True, shape=True)
        
        mc.delete(locator_ctrl)


    def sel_pyramid_ctrl(self):
        pyramid_ctrl_var = nurbs_ctrl.nurbs_ctrl( self.name, 1, self.color1R, self.color1G, self.color1B )
        pyramid_ctrl_info = pyramid_ctrl_var.pyramid_ctrl()
        pyramid_ctrl_grp = pyramid_ctrl_info[0]
        pyramid_ctrl = pyramid_ctrl_info[1]
        locator_ctrl_var = nurbs_ctrl.nurbs_ctrl( pyramid_ctrl + 'A', .5, self.color2R, self.color2G, self.color2B )
        locator_ctrl_info = locator_ctrl_var.locator_ctrl()
        locator_ctrl_grp = locator_ctrl_info[0]
        locator_ctrl = locator_ctrl_info[1]

        mc.parent(locator_ctrl, w=True)

        mc.delete(locator_ctrl_grp)

        locator_ctrl_shape = mc.listRelatives(locator_ctrl, s=True)
        
        mc.parent(locator_ctrl_shape, pyramid_ctrl, r=True, shape=True)
        
        mc.delete(locator_ctrl)



        