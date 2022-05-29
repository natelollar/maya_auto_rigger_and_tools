# objects to last selected object verts
import maya.cmds as mc

import random

import maya.mel as mel

mel.eval('select -r pylon_inst1 pylon_inst14 pylon_inst pylon_inst2 pylon_inst3 pylon_inst4 pylon_inst5 pylon_inst6 pylon_inst7 pylon_inst8 pylon_inst9 pylon_inst10 pylon_inst13 pylon_inst11 pylon_inst12 pCube1;')


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


scatter_to_vert_pos_and_norm(   normal_orient = True, 
                                move_up_down = -5, 
                                normal_orient_rand = True,
                                super_rand_rot = False,
                                rand_rot = False )