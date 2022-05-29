# objects to last selected object verts
import maya.cmds as mc

import random

import maya.mel as mel

#mel.eval('select -r pylon_inst1 pylon_inst14 pylon_inst pylon_inst2 pylon_inst3 pylon_inst4 pylon_inst5 pylon_inst6 pylon_inst7 pylon_inst8 pylon_inst9 pylon_inst10 pylon_inst13 pylon_inst11 pylon_inst12 giant_ball;')


def scatter_to_vert_pos_and_norm(   normal_orient = True, # if true super random should be false, vice versa
                                    move_up_down = -5, # only effects if normal_orient is true
                                    normal_orient_rand = True,
                                    super_rand_rot = False,
                                    rand_rot = False ):

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
        

        # NOTES
        # could make use of normal constraint/ geometry constraint to spread out more

'''
scatter_to_vert_pos_and_norm(   normal_orient = True, 
                                move_up_down = -5, 
                                normal_orient_rand = True,
                                super_rand_rot = False,
                                rand_rot = False )
'''

def simple_scatter(normal_orient = True):
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


#simple_scatter(normal_orient = False)


def random_rotate(x_rot_amnt = 1.0, y_rot_amnt = 1.0, z_rot_amnt = 1.0):
    mySel = mc.ls(sl=True, flatten=True)

    for i in mySel:
        mc.select(i)
        mc.rotate(  random.triangular( -360, 360 ) * x_rot_amnt,
                    random.triangular( -360, 360 ) * y_rot_amnt,
                    random.triangular( -360, 360 ) * z_rot_amnt,
                    relative=True,
                    objectSpace=True,
                    forceOrderXYZ=True
                    )

    mc.select(mySel)



#random_rotate(x_rot_amnt = .01, y_rot_amnt = 1.0, z_rot_amnt = .01)



def random_scale(   xScl_low = 1, xScl_high = 1, # scale is relative
                    yScl_low = 1, yScl_high = 1, # 1 is to multuply scale by 1, therefore keep the same
                    zScl_low = 1, zScl_high = 1
                    ):

    mySel = mc.ls(sl=True)

    # scale each in selection randomly
    for i in mySel:
        mc.select(i)

        # reset to 1 for multiple iterations, without infinite increasing scale
        mc.setAttr('.scale', 1, 1, 1)

        # triangular( low, high, mode ) # floating point
        # mode is at 1 to creat better probability to get smaller
        # will trend towards higher since can only get so small, but no height limit, so reset above
        mc.scale(   random.triangular( xScl_low, xScl_high, 1 ), # triangular function allows floating point
                    random.triangular( yScl_low, yScl_high, 1 ),
                    random.triangular( zScl_low, zScl_high, 1 ),
                    relative=True
                    )

    mc.select(mySel)


random_scale(   xScl_low = 1, xScl_high = 1, 
                yScl_low = 0.333, yScl_high = 3,
                zScl_low = 1, zScl_high = 1
                )



#to push object down or up
def simple_move(x_trans_amnt = 0, y_trans_amnt = 0, z_trans_amnt = 0):
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

#simple_move(x_trans_amnt = 0, y_trans_amnt = -5, z_trans_amnt = 0)