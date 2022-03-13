import maya.cmds as mc

import sys

from PySide2 import QtCore
import PySide2


class misc_tab_class():

    def python_maya_info(self):
        print('\n')
        print('_____________________')
        print ('Maya Major:  ' + str(mc.about(majorVersion=True) ) )
        print ('Maya Minor:  ' + str(mc.about(minorVersion=True) ) )
        print ('Maya API:  ' + str(mc.about(apiVersion=True) ) )
        print('_____________________')
        print ('Python:  ' +  str(sys.version) )
        #print ( str(sys.version_info) )
        print('_____________________')
        #print ( 'QtCore:  ' +  str(QtCore.qVersion()) )
        print ( 'QtCore:  ' +  str(QtCore.__version__ ) )
        #print ( QtCore.__version_info__ )
        print('_____________________')
        print ( 'PySide2:  ' +  str(PySide2.__version__ ) )
        #print ( PySide2.__version_info__ )
        print('_____________________')
        print ( 'OS:  ' +  str(mc.about(operatingSystemVersion=True) ) )
        print('_____________________')


    def function_test(self):
        print('|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|') 
        print('TEST!!! TEST!!! TEST!!!')
        print('|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|/\/\/\/\/\|') 


    def curve_vert_pos(self):
        #find nurbs curve CV's locations (control vertex's)
        #to copy and past into python for control creation
        print('\n')
        print('___________________________________________________________________') 
        mySel = mc.ls(sl=True)
        # avoid red error if nothing selected
        if mySel: 
            # get all shapes from selection
            mySel_shape = mc.listRelatives(mySel, s=True)

            # cycle through shapes
            for shape in mySel_shape:
                print('___________________________________________________________________') 
                print(shape) # print shape name ahead of its content
                vtxIndexList = mc.getAttr(shape + '.controlPoints', multiIndices=True) # get index list
                print (vtxIndexList) # print index list for user

                for vtx_pos in vtxIndexList:
                    # print vert position for each cv index
                    vertLoc = mc.xform(shape + '.cv[' + str(vtx_pos) + ']', query=True, translation=True, worldSpace=True)

                    # round/ limit decimal to 3, do not need more than 3 decimals for cmds.curve()
                    vertLoc_rounded_list = [] # create list to store rounded vert pos
                    for decimal in vertLoc:
                        vertLoc_rounded = round(decimal, 3)
                        vertLoc_rounded_list.append(vertLoc_rounded)

                    # change brackets to work with cmds.curve()
                    vertLoc_rounded_listA = str(vertLoc_rounded_list).replace('[', '(')
                    vertLoc_rounded_listB = vertLoc_rounded_listA.replace(']', ')')

                    # print rounded cv/ vert position for user
                    #print (vertLoc) #test if match 
                    print (vertLoc_rounded_listB) 
        else:
            mc.warning(':(______________________NEED SELECTION!!!!!_________________________:(')


    def reference_curve_shape(self):
        mySel = mc.ls(sl=True)
        for i in mySel:
            # list shapes under ctrl
            mySel_shape = mc.listRelatives(i, s=True)
            # incase curve has more than one shape
            for i in mySel_shape:
                # set display type of shape to reference
                mc.setAttr(i + '.overrideEnabled', 1)
                mc.setAttr(i + '.overrideDisplayType', 2)



            
        






# could make function for appending sys path or maya.env

#___ extra, appending system path and maya.env, instead of using scripts folder

# import sys
# import maya.cmds as mc

# for i in sys.path:
#     print (i)

# rigDir = 'D:\Videos\projects\character_auto_rigger\python'
# if not rigDir in sys.path:
#     sys.path.append( rigDir )
    
# if rigDir in sys.path:
#     sys.path.remove( rigDir )

#_______ or just put in maya.env instead of appending sys file
#_______ should in theory work as same as putting in script folder, if in maya.env
# ex.. PYTHONPATH = D:\Videos\projects\pluralsight_auto_rigger\code\python
# ex.. PATH = ...
