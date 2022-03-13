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
        print('#________________________#')
        print('TEST!!! TEST!!! TEST!!!')
        print('#________________________#')
            
        






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
