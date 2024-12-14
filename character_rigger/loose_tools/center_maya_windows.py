import maya.OpenMayaUI as omui
from PySide6 import QtWidgets
from shiboken6 import wrapInstance

def center_maya_windows():
    app = QtWidgets.QApplication.instance()
    screen_geometry = app.primaryScreen().geometry()
    for widget in app.topLevelWidgets():
        if widget.isWindow() and widget.isVisible():
            widget.move(
                (screen_geometry.width() - widget.width()) // 2,
                (screen_geometry.height() - widget.height()) // 2,
            )