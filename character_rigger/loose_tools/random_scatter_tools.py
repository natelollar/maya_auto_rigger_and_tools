# objects to last selected object verts
from character_rigger.ar_rig import quadruped_leg_rig
import maya.cmds as mc

import random


class random_scatter_tools():
        
    def random_scatter_tool_options(self):

        # scatter_to_vert_pos_and_norm

        normal_orient_checkbox = mc.checkBox( 'normal_orient_checkbox', query=1, v=1 )

        move_up_down_text = mc.textField('move_up_down_text', query=True, text=True)

        normal_orient_random_checkbox = mc.checkBox( 'normal_orient_random_checkbox', query=1, v=1 )

        super_rand_rot_text = mc.checkBox( 'super_rand_rot_checkbox', query=1, v=1 )

        rand_rot_checkbox = mc.checkBox( 'rand_rot_checkbox', query=1, v=1 )

        # simple_scatter

        normal_orient_checkbox1 = mc.checkBox( 'normal_orient_checkbox1', query=1, v=1 )

        # random_rotate

        x_rot_low_text = mc.textField('x_rot_low_text', query=True, text=True)
        x_rot_high_text = mc.textField('x_rot_high_text', query=True, text=True)

        y_rot_low_text = mc.textField('y_rot_low_text', query=True, text=True)
        y_rot_high_text = mc.textField('y_rot_high_text', query=True, text=True)

        z_rot_low_text = mc.textField('z_rot_low_text', query=True, text=True)
        z_rot_high_text = mc.textField('z_rot_high_text', query=True, text=True)

        # random_scale

        scl_low_text = mc.textField('scl_low_text', query=True, text=True)

        scl_high_text = mc.textField('scl_high_text', query=True, text=True)


        return  normal_orient_checkbox,\
                move_up_down_text,\
                normal_orient_random_checkbox,\
                super_rand_rot_text,\
                rand_rot_checkbox,\
                normal_orient_checkbox1,\
                x_rot_low_text,\
                x_rot_high_text,\
                y_rot_low_text,\
                y_rot_high_text,\
                z_rot_low_text,\
                z_rot_high_text,\
                scl_low_text,\
                scl_high_text
                


    #scatter to last selected
    def scatter_to_vert_pos_and_norm(self):
        normal_orient = self.random_scatter_tool_options()[0] # if true super random should be false, vice versa
        move_up_down = float( self.random_scatter_tool_options()[1] ) # only effects if normal_orient is true
        normal_orient_rand = self.random_scatter_tool_options()[2]
        super_rand_rot = self.random_scatter_tool_options()[3]
        rand_rot = self.random_scatter_tool_options()[4] 



        #get selection
        mySel = mc.ls(sl=True, flatten=True)
        #selection without last object
        instObj = mySel[0:-1]
        # number of instance objects 
        instObj_len = len(instObj)
        # vertex placement object
        vrtObj = mySel[-1]
        # vert index list
        vrt_ind_lst = mc.getAttr(vrtObj + '.vrts', multiIndices=True)
        # vert index list random sample
        vrt_ind_lst_sample = random.sample(vrt_ind_lst, instObj_len)
        # vert position list
        #vrt_pos_lst = mc.getAttr(vrtObj + '.vtx[:]')


        rivet_lst = []
        #get vert positions of last object
        for i in vrt_ind_lst_sample:
            mc.select(vrtObj + '.pnts[' + str(i) + ']')
            mc.Rivet()
            rivet_obj = mc.ls(sl=True, type='transform')
            rivet_lst.append(rivet_obj)

        #print(rivet_lst)

        current_index = 0
        for rivet in rivet_lst:
            # set instance object to vertex and point in normals direction
            mc.parent(instObj[current_index], rivet)
            # zero out, position under rivet at vertex
            mc.setAttr(instObj[current_index] + '.translate', 0,0,0)


            if normal_orient == True:
                # orient to normals
                mc.setAttr(instObj[current_index] + '.rotate', 0,0,0)
                # point up and push down
                mc.setAttr(instObj[current_index] + '.rotateZ', -90) # point up
                mc.setAttr(instObj[current_index] + '.translateX', move_up_down) # push down
                if normal_orient_rand == True:
                    # randomly adjust inst obj tilt
                    mc.rotate( 
                                random.randrange(-20, 20, 1),
                                random.randrange(-360, 360, 1),
                                random.randrange(-20, 20, 1), 
                                relative=True, objectSpace=True, forceOrderXYZ=True
                                )

            if super_rand_rot == True:
                mc.setAttr( instObj[current_index] + '.rotate',
                            random.randrange(-360, 360, 1),
                            random.randrange(-360, 360, 1),
                            random.randrange(-360, 360, 1)
                            )

            if rand_rot == True:
                mc.rotate(  random.randrange(-360, 360, 1),
                            random.randrange(-360, 360, 1),
                            random.randrange(-360, 360, 1),
                            relative=True,
                            objectSpace=True,
                            forceOrderXYZ=True
                            )


            # unparent from rivet
            mc.Unparent(instObj[current_index])
            #delete rivet
            mc.delete(rivet)
            
            current_index += 1

        mc.select(mySel)

        #print(self.random_scatter_tool_options()[0])
        #print(self.random_scatter_tool_options()[1])
        #print(self.random_scatter_tool_options()[2])
        #print(self.random_scatter_tool_options()[3])
        #print(self.random_scatter_tool_options()[4])
            



    def simple_scatter(self):
        normal_orient = self.random_scatter_tool_options()[5] # if true super random should be false, vice versa
        

        #get selection
        mySel = mc.ls(sl=True, flatten=True)
        #selection without last object
        instObj = mySel[0:-1]
        # number of instance objects 
        instObj_len = len(instObj)
        # vertex placement object
        scatterObj = mySel[-1]

        #get bounding box points of last selected object (order: xmin ymin zmin xmax ymax zmax)
        root_selection_box_bb = mc.xform(scatterObj, ws=True, bb=True, q=True)

        bb_x_min = root_selection_box_bb[0]
        bb_y_min = root_selection_box_bb[1]
        bb_z_min = root_selection_box_bb[2]
        bb_x_max = root_selection_box_bb[3]
        bb_y_max = root_selection_box_bb[4]
        bb_z_max = root_selection_box_bb[5]

        for i in instObj:
            # position to closest geo surface of last selected
            mc.setAttr( i + '.tx', random.triangular( bb_x_min, bb_x_max ) )
            mc.setAttr( i + '.ty', random.triangular( bb_y_min, bb_y_max ) )
            mc.setAttr( i + '.tz', random.triangular( bb_z_min, bb_z_max ) )

            geo_const = mc.geometryConstraint(scatterObj, i)  #look at 'point on poly' too, for maintain offset
            mc.delete(geo_const)

            # orient in normal direction
            if normal_orient == True:
                nrml_const = mc.normalConstraint(scatterObj, i, aimVector=(0, 1, 0) )
                mc.delete(nrml_const)
        
        #reselect to scatter multiple times
        mc.select(instObj)
        mc.select(scatterObj, add=True)




    def random_rotate(self):
        x_rot_low = float(self.random_scatter_tool_options()[6])
        x_rot_high = float(self.random_scatter_tool_options()[7]) 
        y_rot_low = float(self.random_scatter_tool_options()[8])  
        y_rot_high = float(self.random_scatter_tool_options()[9]) 
        z_rot_low = float(self.random_scatter_tool_options()[10])  
        z_rot_high = float(self.random_scatter_tool_options()[11]) 

        mySel = mc.ls(sl=True, flatten=True)

        for i in mySel:
            mc.select(i)
            mc.rotate(  random.triangular( x_rot_low, x_rot_high ),
                        random.triangular( y_rot_low, y_rot_high ),
                        random.triangular( z_rot_low, z_rot_high ),
                        relative=True,
                        objectSpace=True,
                        forceOrderXYZ=True
                        )

        mc.select(mySel)




    # scale is relative # 1 is to multuply scale by 1, therefore keep the same
    def random_scale( self ):
        scl_low = float(self.random_scatter_tool_options()[12]) 
        scl_high = float(self.random_scatter_tool_options()[13])


        mySel = mc.ls(sl=True)

        # scale each in selection randomly
        for i in mySel:
            mc.select(i)

            # reset to 1 for multiple iterations, without infinite increasing scale
            mc.setAttr('.scale', 1, 1, 1)

            # for uniform scale
            rand_scl = random.triangular( scl_low, scl_high, 1 ) # triangular function allows floating point

            # triangular( low, high, mode ) # floating point
            # mode is at 1 to creat better probability to get smaller
            # will trend towards higher since can only get so small, but no height limit, so reset above
            mc.scale(   rand_scl, 
                        rand_scl,
                        rand_scl,
                        relative=True
                        )

        mc.select(mySel)




    #to push object down or up
    def simple_move(self):
        x_trans_amnt = mc.textField('x_trans_amnt_text', query=True, text=True)
        y_trans_amnt = mc.textField('y_trans_amnt_text', query=True, text=True) 
        z_trans_amnt = mc.textField('z_trans_amnt_text', query=True, text=True)

        mySel = mc.ls(sl=True, flatten=True)

        for i in mySel:
            mc.select(i)
            mc.move(    x_trans_amnt,
                        y_trans_amnt,
                        z_trans_amnt,
                        relative=True,
                        objectSpace=True,
                        worldSpaceDistance=True
                        )

        mc.select(mySel)



    def reset_translation(self):
        mySel = mc.ls(sl=True)

        for i in mySel:
            i_locked_attr = mc.listAttr(i, locked=True)
            i_tranX = 'translateX'
            i_tranY = 'translateY'
            i_tranZ = 'translateZ'
            # skip if locked attribute
            if i_locked_attr:
                # zero out individual unlocked values
                if i_tranX not in i_locked_attr:
                    mc.setAttr(i + '.translateX', 0)
                if i_tranY not in i_locked_attr:
                    mc.setAttr(i + '.translateY', 0)
                if i_tranZ not in i_locked_attr:
                    mc.setAttr(i + '.translateZ', 0)
            # else zero out all
            else:
                mc.setAttr(i + '.translate', 0, 0, 0)


    def reset_rotation(self):
        mySel = mc.ls(sl=True)

        for i in mySel:
            i_locked_attr = mc.listAttr(i, locked=True)
            i_rotX = 'rotateX'
            i_rotY = 'rotateY'
            i_rotZ = 'rotateZ'
            # skip if locked attribute
            if i_locked_attr:
                # zero out individual unlocked values
                if i_rotX not in i_locked_attr:
                    mc.setAttr(i + '.rotateX', 0)
                if i_rotY not in i_locked_attr:
                    mc.setAttr(i + '.rotateY', 0)
                if i_rotZ not in i_locked_attr:
                    mc.setAttr(i + '.rotateZ', 0)
            # else zero out all
            else:
                mc.setAttr(i + '.rotate', 0, 0, 0)


    def reset_scale(self):
        mySel = mc.ls(sl=True)

        for i in mySel:
            i_locked_attr = mc.listAttr(i, locked=True)
            i_scaleX = 'scaleX'
            i_scaleY = 'scaleY'
            i_scaleZ = 'scaleZ'
            # skip if locked attribute
            if i_locked_attr:
                # zero out individual unlocked values
                if i_scaleX not in i_locked_attr:
                    mc.setAttr(i + '.scaleX', 1)
                if i_scaleY not in i_locked_attr:
                    mc.setAttr(i + '.scaleY', 1)
                if i_scaleZ not in i_locked_attr:
                    mc.setAttr(i + '.scaleZ', 1)
            # else zero out all
            else:
                mc.setAttr(i + '.scale', 1, 1, 1)

    '''
    def redshift_displacement_off(self):
        mySel = mc.ls(sl=True)

        # scale each in selection randomly
        for i in mySel:
            mc.setAttr(i + '.rsEnableSubdivision', 0)
            mc.setAttr(i + '.rsEnableDisplacement', 0)

    def redshift_displacement_on(self):
        mySel = mc.ls(sl=True)

        # scale each in selection randomly
        for i in mySel:
            mc.setAttr(i + '.rsEnableSubdivision', 1)
            mc.setAttr(i + '.rsEnableDisplacement', 1)
    '''








'''
scatter_to_vert_pos_and_norm(   normal_orient = False, 
                                move_up_down = 0, 
                                normal_orient_rand = False,
                                super_rand_rot = False,
                                rand_rot = False )
'''

#simple_scatter(normal_orient = False)

#random_rotate(x_rot_amnt = 0, y_rot_amnt = 1, z_rot_amnt = 0)

#random_scale( scl_low = .333, scl_high = 1, )

#simple_move(x_trans_amnt = 0, y_trans_amnt = -5, z_trans_amnt = 0)

#redshift_displacement_off()


#print('Working!______')