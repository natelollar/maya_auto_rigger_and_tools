from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.api.OpenMaya as om2
import maya.OpenMayaUI as omui

import random
import math


def maya_main_window():

    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
        
class OpenImportDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(OpenImportDialog, self).__init__(parent)

        self.setWindowTitle("OpenMaya Scatter Objects (No Undo)")
        self.setMinimumSize(300, 50)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.scatter_btn = QtWidgets.QPushButton("Scatter Objects")
        self.exit_btn = QtWidgets.QPushButton("Exit")

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.scatter_btn)
        button_layout.addWidget(self.exit_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(button_layout)
        
    def create_connections(self):
        self.scatter_btn.clicked.connect(self.scatter_objects)
        self.exit_btn.clicked.connect(self.close) # must be inherited method

    
    def scatter_objects(self):
        my_sel = om2.MGlobal.getActiveSelectionList().getSelectionStrings()	

        for i in my_sel:
            i_sel = om2.MSelectionList().add(i).getDependNode(0)
            
            om2.MFnTransform(i_sel).findPlug("tx", False).setDouble(random.triangular(-500,500))
            om2.MFnTransform(i_sel).findPlug("ty", False).setDouble(random.triangular(-500,500))
            om2.MFnTransform(i_sel).findPlug("tz", False).setDouble(random.triangular(-500,500))
            
            om2.MFnTransform(i_sel).findPlug("rx", False).setDouble( math.radians(random.triangular(-360,360) ) )
            om2.MFnTransform(i_sel).findPlug("ry", False).setDouble( math.radians(random.triangular(-360,360) ) )
            om2.MFnTransform(i_sel).findPlug("rz", False).setDouble( math.radians(random.triangular(-360,360) ) )
            
            uniform_scale = random.triangular(0.25,3)
            om2.MFnTransform(i_sel).findPlug("sx", False).setDouble(uniform_scale)
            om2.MFnTransform(i_sel).findPlug("sy", False).setDouble(uniform_scale)
            om2.MFnTransform(i_sel).findPlug("sz", False).setDouble(uniform_scale)




#if __name__ == '__main__':

try:
    open_import_dialog.close() # pylint: disable=E0601
    open_import_dialog.deleteLater()
except:
    pass

open_import_dialog = OpenImportDialog()
open_import_dialog.show()

    
'''
import imp

#--------------------------------------------------
# IMPORT ALL
#--------------------------------------------------
import pyside

import pyside.pyside_ui


#--------------------------------------------------
# REIMPORT ALL
#--------------------------------------------------
imp.reload( pyside )

imp.reload( pyside.pyside_ui )
'''