import maya.api.OpenMayaUI as omui
from PySide2.QtGui import QCursor
from shiboken2 import wrapInstance
from PySide2.QtWidgets import QWidget

def viewport_mouse_pos():
    # Get the active 3D view
    activeView = omui.M3dView.active3dView()

    # Get the global position of the cursor
    globalPos = QCursor.pos()

    # Get the widget for the active 3D view
    viewWidget = wrapInstance(int(activeView.widget()), QWidget)

    # Map global position to local position within the viewport
    localPos = viewWidget.mapFromGlobal(globalPos)

    return localPos.x(), localPos.y()

# Usage
x, y = viewport_mouse_pos()
print(x, y)