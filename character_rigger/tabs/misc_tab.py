import maya.cmds as mc

import sys

from PySide2 import QtCore
import PySide2

from re import search


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


    def rename_first(self):
        current_part = mc.textField('current_part_text', query=True, text=True)
        replace_part = mc.textField('replace_part_text', query=True, text=True)
        mySel = mc.ls(sl=1)
        for i in mySel:
            mySel_name = i.replace(current_part, replace_part, 1)
            print(mySel_name)
            mc.rename(i, mySel_name)


    def parent_scale_multi(self):
        # parent and scale constrain between last two selectd objects
        mySel = mc.ls(sl=True)
        for i in mySel:
            if i != mySel[-1] and i != mySel[-2]:
                mc.parentConstraint([ mySel[-1], mySel[-2] ], i, mo=1, weight=1)
                mc.scaleConstraint([ mySel[-1], mySel[-2] ], i, weight=1)


    def parent_multi(self):
        # parent constrain between last two selectd objects (no scale constrain)
        mySel = mc.ls(sl=True)
        for i in mySel:
            if i != mySel[-1] and i != mySel[-2]:
                mc.parentConstraint([ mySel[-1], mySel[-2] ], i, mo=1, weight=1)


    def multi_set_driven_key(self):
        # get textfield values
        swch_attr_nm = mc.textField('swch_attr_name', query=True, text=True)
        W0_text_var = mc.textField('W0_text', query=True, text=True)
        
        mySel = mc.ls(sl=True)
        # single constraint switch
        for jnt in mySel:
            # last selection is control with switch
            if jnt != mySel[-1]:
                # get scale constraint of jnt
                get_jnt_cnst = mc.listConnections(jnt, type='constraint')
                jnt_cnst = get_jnt_cnst[0]
                # list attributes to get W0 and W1
                jnt_cnst_attr = mc.listAttr(jnt_cnst)
                # get the weight names of the constrain
                for i in jnt_cnst_attr:
                    if 'W0' in i:
                        weight_0_var = '.' + i
                    if 'W1' in i:
                        weight_1_var = '.' + i

                if W0_text_var == '0':
                    # W0 = 0, switch 0, W0 = 1, switch 1, W1 opposite
                    # alternative is to disconnect/ unlock and use '.target[0].targetWeight'
                    mc.setAttr((mySel[-1] + swch_attr_nm), 0)
                    mc.setAttr( (jnt_cnst + weight_0_var),  0)
                    mc.setAttr( (jnt_cnst + weight_1_var),  1)

                    mc.setDrivenKeyframe((jnt_cnst + weight_0_var), currentDriver = (mySel[-1] + swch_attr_nm))
                    mc.setDrivenKeyframe((jnt_cnst + weight_1_var), currentDriver = (mySel[-1] + swch_attr_nm))

                    mc.setAttr((mySel[-1] + swch_attr_nm), 1)
                    mc.setAttr( (jnt_cnst + weight_0_var),  1)
                    mc.setAttr( (jnt_cnst + weight_1_var),  0)

                    mc.setDrivenKeyframe((jnt_cnst + weight_0_var), currentDriver = (mySel[-1] + swch_attr_nm) )
                    mc.setDrivenKeyframe((jnt_cnst + weight_1_var), currentDriver = (mySel[-1] + swch_attr_nm) )

                if W0_text_var == '1':
                    # W0 = 0, switch 1, W0 = 1, switch 0, W1 opposite
                    # alternative is to disconnect/ unlock and use '.target[0].targetWeight'
                    mc.setAttr((mySel[-1] + swch_attr_nm), 0)
                    mc.setAttr( (jnt_cnst + weight_0_var),  1)
                    mc.setAttr( (jnt_cnst + weight_1_var),  0)

                    mc.setDrivenKeyframe((jnt_cnst + weight_0_var), currentDriver = (mySel[-1] + swch_attr_nm))
                    mc.setDrivenKeyframe((jnt_cnst + weight_1_var), currentDriver = (mySel[-1] + swch_attr_nm))

                    mc.setAttr((mySel[-1] + swch_attr_nm), 1)
                    mc.setAttr( (jnt_cnst + weight_0_var),  0)
                    mc.setAttr( (jnt_cnst + weight_1_var),  1)

                    mc.setDrivenKeyframe((jnt_cnst + weight_0_var), currentDriver = (mySel[-1] + swch_attr_nm) )
                    mc.setDrivenKeyframe((jnt_cnst + weight_1_var), currentDriver = (mySel[-1] + swch_attr_nm) )
            
    def scale_multi_const(self):
        # scale const multi to last selected
        mySel = mc.ls(sl=True)
        for i in mySel:
            if i != mySel[-1]:
                mc.scaleConstraint(mySel[-1], i, weight=1)

    def set_multi_attr(self):
        #set multiple object boolean or number value
        #get value and attribute name
        attr_name = mc.textField('attr_name_text', query=True, text=True)
        attr_value = mc.textField('attr_value_text', query=True, text=True)
        #get selection
        mySel = mc.ls(sl=True)
        # set multiple selected objects attributes
        attr_value_list = attr_value.split(',')
        try:
            #if list single number long
            if len(attr_value_list) == 1:
                print('___1___')
                for i in mySel:
                    mc.setAttr ( (i + attr_name), float(attr_value) )
            # if list 3 number array
            if len(attr_value_list) == 3:
                val1 = float(attr_value_list[0])
                val2 = float(attr_value_list[1])
                val3 = float(attr_value_list[2])
                print('___3____')
                for i in mySel:
                    mc.setAttr ( (i + attr_name), val1, val2, val3 )
            else:
                print('Enter 1 number or 3 numbers seperated by commas')
        except:
            mc.warning('Probably entered attribute wrong, string instead of number, or wrong number of values.')



            
        






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
