from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

import maya.cmds as cmds

# Boilerplate code, just copy and keep handy somewhere.
# import rigModule
# import importlib
# importlib.reload(rigModule)

# win = rigModule.windowGui()
# win.show()

def getMayaMainWin():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)

class windowGui():
    def __init__(self):
        pass
    
    def mk_body_part_layout(self):
        # title
        # body part drop down
        # size drop down
        # color drop down
        pass

    def mk_custom_handle_layout(self):
        # title
        # ik
        # fk
        # ikfk switch
        # spline
        # ribbon
        # custom switch tool multi select
        # color
        # size
        # shape
        pass

    def mk_skeleton_layout(self):
        # title
        # create:
        # simulate:
        # human modular skeleton
        # quad modular skele
        pass

    def mk_controller_layout(self):
        # title 
        # shape drop down
        # size drop down
        # color drop down
        pass

class rigModular():
    def __init__(self):
        pass

class wholeSkeletonModular():
    def __init__(self):
        pass

class bodyPartModular():
    def __init__(self):
        pass

class SwitchesHandlesControllers():
    def __init__(self):
        self.size = 1
        self.color = 25
        self.shape = 'Circle'

    def import_control(self):
        # basic controller importer
        cmds.file(f'\\RigConShapes\{self.shape}.ma',i=True, ns=':')
        con = cmds.ls(self.shape)
        # scale, color
        cmds.scale(self.size, self.size, self.size, con)
        cmds.setAttr(f'{self.shape}.overrideEnabled', 1)
        cmds.setAttr(f'{self.shape}.overrideColor', self.color)
        cmds.makeIdentity(con, apply=True)
        cmds.delete(con, ch=True)
        return con

