import maya.cmds as mc

import random
import os
from pathlib import Path

#_________________Modeling Tab Methods __________________________#
#________________________________________________________________#

class modeling_class():

    # create random polygon objects 
    def create_random(self):
        for i in range(10):
            #random sphere
            mySphereRand = random.uniform(.5,3)
            mySphere = mc.polySphere(r=random.randrange(5,25,1), ch=0)
            mc.move(random.randrange(-200,200,1), random.randrange(-200,200,1), random.randrange(-200,200,1), mySphere, r=True, os=True)
            mc.scale(mySphereRand, mySphereRand, mySphereRand, mySphere, r=True, os=True)
            mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), mySphere, r=True, os=True)
            #random cube
            myCubeRand = random.uniform(5,25)
            myCubeRandA = random.uniform(.5,5)
            myCube = mc.polyCube(w=myCubeRand, h=random.uniform(5,50), d=myCubeRand, ch=0)
            mc.move(random.uniform(-200,200), random.uniform(-200,200), random.uniform(-200,200), myCube, r=True, os=True)
            mc.scale(myCubeRandA, random.uniform(.3,5), myCubeRandA, myCube, r=True, os=True)
            mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), myCube, r=True, os=True)
            #random cube
            myCylinderRand = random.uniform(.5,3)
            myCylinder = mc.polyCylinder(r=random.randrange(5,25,1), h=random.randrange(5,50,1), sc=1, ch=0)
            mc.move(random.randrange(-200,200,1), random.randrange(-200,200,1), random.randrange(-200,200,1), myCylinder, r=True, os=True)
            mc.scale(myCylinderRand, random.uniform(.5,5), myCylinderRand, myCylinder, r=True, os=True)
            mc.rotate(random.uniform(-360,360), random.uniform(-360,360), random.uniform(-360,360), myCylinder, r=True, os=True)

        #deselect all, back to main screen
        mc.select(cl=True)
        mc.setFocus("MayaWindow")


    #scatter selected randomly
    def scatter_selected(self):
        mySel = mc.ls(sl=True)
        myTrans = 300
        myRot = 360
        myScale = 3
        
        for i in mySel:
            #translate
            mc.setAttr((i + ".tx"), random.uniform(-myTrans,myTrans))
            mc.setAttr((i + ".ty"), random.uniform(-myTrans,myTrans))
            mc.setAttr((i + ".tz"), random.uniform(-myTrans,myTrans))
            #rotate
            mc.setAttr((i + ".rx"), random.uniform(-myRot,myRot))
            mc.setAttr((i + ".ry"), random.uniform(-myRot,myRot))
            mc.setAttr((i + ".rz"), random.uniform(-myRot,myRot))
            #scale
            #for uniform scale
            myScale_rand = random.uniform(.3 , myScale)
            mc.setAttr((i + ".sx"), myScale_rand)
            mc.setAttr((i + ".sy"), myScale_rand)
            mc.setAttr((i + ".sz"), myScale_rand)

    #scatter Objects to vertices of object
    def scatter_to_vertices(self):
        #get selection
        mySel = mc.ls(sl=True)
        #selection without last object
        objList = mySel[0:-1]
        #get verts of last object
        vtxIndexList = mc.getAttr(mySel[-1] + '.vrts', multiIndices=True)
        #create empty variable to be filled with vertext positions
        vtxIndexList_positions = []
        #get vert positions of last object
        for i in vtxIndexList:
            vertLoc = mc.xform(mySel[-1] + '.pnts[' + str(i) + ']', query=True, translation=True, worldSpace=True)
            vtxIndexList_positions.append(vertLoc)
        #get number of verts in list
        vtxIndexList_positions_length = len(vtxIndexList_positions)-1
        #assign objects to random vertex position of last object
        for i in objList:
            vtxIndexList_positions_length_rand = random.randrange(0,vtxIndexList_positions_length, 1)
            randVertPos = vtxIndexList_positions[vtxIndexList_positions_length_rand]
            mc.setAttr((i + ".translate"), randVertPos[0], randVertPos[1], randVertPos[2])

    #import default maya human sculpting base
    def create_human(self):
        mc.file("C:/Program Files/Autodesk/Maya2020/Examples/Modeling/Sculpting_Base_Meshes/Bipeds/HumanBody.ma", i=True)

    #make polygon arch
    def make_poly_arch(self):
        #create 2d arch plance polygon points
        mc.polyCreateFacet(ch=0, p=[(86.295876, -2.03746, 0), 
                                            (83.403091, 20.861275, 0), 
                                            (74.906509, 42.321198, 0), 
                                            (61.339996, 60.993904, 0), 
                                            (43.555984, 75.706116, 0), 
                                            (22.671909, 85.533417, 0), 
                                            (4.29153e-06, 88.37664, 0), 
                                            (-22.671909, 85.533417, 0), 
                                            (-43.555984, 75.706116, 0), 
                                            (-61.340004, 60.993904, 0), 
                                            (-74.906517, 42.321198, 0), 
                                            (-83.403099, 20.861275, 0), 
                                            (-86.295883, -2.03746, 0), 
                                            (-111.295883, -2.03746, 0), 
                                            (-107.617683, 27.078522, 0), 
                                            (-96.814186, 54.36504, 0), 
                                            (-79.564217, 78.107582, 0), 
                                            (-56.951653, 96.814316, 0), 
                                            (-30.397335, 109.30983, 0), 
                                            (4.29153e-06, 113.327309, 0), 
                                            (30.397335, 109.30983, 0), 
                                            (56.951653, 96.814316, 0), 
                                            (79.564209, 78.107582, 0), 
                                            (96.814178, 54.36504, 0), 
                                            (107.617676, 27.078522, 0), 
                                            (111.295876, -2.03746, 0)]
                                            )
        #triangulate
        mc.polyTriangulate(ch=0)
        #quadrangulate
        mc.polyQuad(ch=0)
        #extrude to make 3d
        mc.polyExtrudeFacet(tz=-30, ch=0)
        #rename arch
        myArch = mc.rename('poly_arch')
        #clear selection (b/c faces selected after extrude)
        mc.select(cl=True)
        #select edges for bevel
        mc.select((myArch + '.e' + '[0:11]'), add=True)
        mc.select((myArch + '.e' + '[13:24]'), add=True)
        mc.select((myArch + '.e' + '[41]',
                    myArch + '.e' + '[46]',
                    myArch + '.e' + '[51]',
                    myArch + '.e' + '[56]',
                    myArch + '.e' + '[61]',
                    myArch + '.e' + '[66]',
                    myArch + '.e' + '[71]',
                    myArch + '.e' + '[76]',
                    myArch + '.e' + '[81]',
                    myArch + '.e' + '[86]',
                    myArch + '.e' + '[91]',
                    myArch + '.e' + '[96]'),
                    add=True)
        mc.select((myArch + '.e' + '[44]',
                    myArch + '.e' + '[49]',
                    myArch + '.e' + '[54]',
                    myArch + '.e' + '[59]',
                    myArch + '.e' + '[64]',
                    myArch + '.e' + '[69]',
                    myArch + '.e' + '[74]',
                    myArch + '.e' + '[79]',
                    myArch + '.e' + '[84]',
                    myArch + '.e' + '[89]',
                    myArch + '.e' + '[94]',
                    myArch + '.e' + '[99]'),
                    add=True)
        #floor edges
        mc.select((myArch + '.e' + '[97]',
                    myArch + '.e' + '[98]',
                    myArch + '.e' + '[95]',
                    myArch + '.e' + '[25]',
                    myArch + '.e' + '[37]',
                    myArch + '.e' + '[39]',
                    myArch + '.e' + '[38]',
                    myArch + '.e' + '[12]'),
                    add=True)
        #bevel
        mc.polyBevel3(offset=3, segments=2, smoothingAngle=180, subdivideNgons=1, ch=0)
        #nonlinear flare deformer
        myFlare = mc.nonLinear(myArch, type='flare')
        mc.setAttr(myFlare[0] + '.startFlareZ', 3)
        mc.setAttr(myFlare[0] + '.endFlareZ', 0)
        #delete history and/ deformer
        mc.delete(myArch, ch=True)
        #enlarge arch
        mc.setAttr(myArch + '.scale', 2.5,2.5,2.5)
        #adjust position
        mc.setAttr(myArch + '.tz', 37.5)
        mc.setAttr(myArch + '.ty', -2.5)
        #center pivot
        mc.move(0, 0, 0, (myArch + '.scalePivot'), (myArch + '.rotatePivot'))
        #freeze transforms
        mc.makeIdentity(myArch, apply=True)
        #select arch
        mc.select(myArch)

    #export multiple objs into seperate files
    def mult_obj_exp(self):
        radio_button = mc.radioButtonGrp( 'obj_radio_button', query=True, sl=True)
        if radio_button == 1:
            radio_button_val = 'OBJexport'
            export_opt = ('groups=0; ptgroups=0; materials=0; smoothing=1; normals=1;')
        elif radio_button == 2:
            radio_button_val = 'FBX export'
            export_opt = ('v=0;')
        elif radio_button == 3:
            radio_button_val = 'mayaAscii'
            export_opt = ('v=0;')
        elif radio_button == 4:
            radio_button_val = 'Redshift Proxy'
            export_opt = ('v=0;')
        
        path_dir = mc.textFieldButtonGrp('obj_exp_text', query=True, text=True)
        
        mySel = mc.ls(sl=1)
        for i in mySel:
            mc.select(i)
            mc.file(    str(path_dir + i),
                        type=radio_button_val,
                        es=1, # export selected 
                        f=1, # force
                        pr=1,
                        options=export_opt, 
                        )


    #import multiple objs (including redshift proxy)
    def mult_obj_imp(self):
        '''
        radio_button = mc.radioButtonGrp( 'obj_radio_button', query=True, sl=True)
        if radio_button == 1:
            radio_button_val = 'OBJ'
            imp_opt = ('mo=1;lo=0')
        elif radio_button == 2:
            radio_button_val = 'FBX'
            imp_opt = ('v=0;')
        elif radio_button == 3:
            radio_button_val = 'mayaAscii'
            imp_opt = ('v=0;')
        elif radio_button == 4:
            radio_button_val = 'Redshift Proxy'
            imp_opt = ('v=0;')
        '''
        obj_paths0 = mc.textFieldButtonGrp('obj_imp_text', query=True, text=True)
        obj_paths1 = obj_paths0.replace("'","") # remove extra quotation
        obj_paths2 = obj_paths1.strip('][').split(', ') #convert string back to list


        for i in obj_paths2:
            obj_suffix = Path(i).suffix
            obj_name = Path(i).stem

            if obj_suffix == '.obj':
                #radio_button_val = 'OBJ'
                imp_opt = ('mo=1;lo=0')
            elif obj_suffix == '.fbx':
                #radio_button_val = 'FBX'
                imp_opt = ('v=0;')
            elif obj_suffix == '.ma':
                #radio_button_val = 'mayaAscii'
                imp_opt = ('v=0;')

            if obj_suffix == '.obj' or obj_suffix == '.fbx' or obj_suffix == '.ma':
                mc.file(i, #file path
                        #type=radio_button_val,
                        i=1, # import
                        iv=1, #ignoreVersion
                        mnc=0, #mergeNamespacesOnClash
                        ra=1, #renameAll
                        #rpr=obj_name, #renamingPrefix
                        f=1, # force
                        pr=1, # preserve references
                        itr='keep', #importTimeRange
                        options=imp_opt, 
                        )

            if obj_suffix == '.rs':
                
                proxy_node = mc.createNode('RedshiftProxyMesh', name='rsProxy_node_' + obj_name)

                mc.setAttr(proxy_node + '.fileName', i, type='string') # set redshift proxy path
                mc.setAttr(proxy_node + '.displayMode', 1) # Preview Mesh
                mc.setAttr(proxy_node + '.displayPercent', 5) # Preview Mesh

                shp_node = mc.createNode('mesh')

                mc.sets(e=True, forceElement='initialShadingGroup')

                mc.connectAttr(proxy_node + '.outMesh', shp_node + '.inMesh')

                trans_node0 = mc.listRelatives(shp_node, parent=True)
                trans_node = mc.rename(trans_node0, 'rsProxy_' + obj_name)



    def browse_files(self):
        path_dir = mc.fileDialog2(  fileMode=3, #3 The name of a directory. Only directories are displayed in the dialog.
                                    caption='Choose Location',
                                    dialogStyle=2,
                                    okCaption='Accept')

        if path_dir: mc.textFieldButtonGrp('obj_exp_text', edit=True, text=path_dir[0] + '/') 

    def browse_files_import(self):
        #print('WORKING!')
        imp_path_dir = mc.fileDialog2(  fileMode=4, #4 Then names of one or more existing files.
                                        caption='Choose Objects to Import',
                                        dialogStyle=2,
                                        okCaption='Accept')

        if imp_path_dir: mc.textFieldButtonGrp('obj_imp_text', edit=True, text=str(imp_path_dir)) 

    # for testing file locations
    def file_spot(self):
        test_path = os.path.abspath( os.path.join(__file__, "..", "..", "other") + "test.obj" )
        print(test_path)
