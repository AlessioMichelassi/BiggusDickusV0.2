BiggusDickus

The name comes from Monty Python's Life of Brian simply beacause the world is divided into people like BiggusDickus sketch and the others. Now, something completely different:

You can use PySide or PyQt to create gret GUI, but if you are lazy like me and don't want to spend whole days writing the same structure to create a main window and a menu you can use BiggusDickus.

 menu = {'New': 'File', 'Open': 'File', 'Save': 'File', 'Save As': 'File', '-  ': 'File', 'Export': 'File',
        '- ': 'File', 'Print': 'File', 'Print Preview': 'File', '-': 'File', 'Quit': 'File', 'Undo': 'Edit',
        'Redo': 'Edit', '-    ': 'Edit', 'cut': 'Edit', 'copy': 'Edit', 'paste': 'Edit', 'PasteFromHistory': 'Edit',
        'Delete': 'Edit', '-   ': 'Edit', 'SelectAll': 'Edit', 'zoomIn': 'View', 'zoomOut': 'View',
        'scaleToFit': 'View', 'drawLine': 'Draw', 'drawCircle': 'Draw', 'drawRectangle': 'Draw', 'drawText': 'Draw',
        'Resize': 'Filter', 'Rotate': '*Transform', 'Translate': '*Transform', 'Perspective': '*Transform',
        'Simple': '*Erode', 'Reflect': '*Erode', 'Dilate': '*Erode', 'Opening': '*Erode', 'Closing': '*Erode',
        'Binary': '*Threshold', 'BinaryInverted': '*Threshold', 'Trunc': '*Threshold', 'ToZero': '*Threshold',
        'ToZeroInverted': '*Threshold', 'AdaptiveMean': '*Threshold', 'AdaptiveGaussian': '*Threshold',
        'Otzu': '*Threshold', 'Bilateral': '*Denoise', 'InPainting': '*Denoise', 'blur2D': '*Blur', 'Average': '*Blur',
        'Gaussian': '*Blur', 'Median': '*Blur', 'FaceDetection': 'MachineLearning', 'EyeDetection': 'MachineLearning',
        'SmileDetection': 'MachineLearning', 'CornerDetection': 'MachineLearning', 'LineDetection': 'MachineLearning',
        'CircleDetection': 'MachineLearning', 'DocumentDetection': 'MachineLearning'}

If you have a dictionary like this where the key il the name of the menu Action and the value is the name of the menu BD can create the menu structure, including shortCut keys, icon Image and link to a function. For creating division line you can use the minus as first char '-': 'File', and if you need to create a subMenu you can use the * as first char Dilate': '*Erode'.

The program create a main.py that call the mainUI.py where the QMainWindows will created in this way. In the mainUI.py you'll find something like this:
Son Of a BiggusDickusV0_3

import sys import os from PySide6.QtWidgets import * from PySide6.QtGui import *

class mainWindows(QMainWindow):

def __init__(self, *args, **kwargs):
    QMainWindow.__init__(self, *args, **kwargs)
    self.mainMenu = self.menuBar()
    self.Init_MainMenu()
    self.initUI()

def initUI(self):
    self.setWindowTitle("BiggusDickusV0_3")
    self.statusBar().showMessage("ready", 3000)
    self.show()

def Init_MainMenu(self):
    self.Init_MenuFile()
    self.Init_MenuEdit()
    self.Init_MenuView()
    self.Init_MenuDraw()
    self.Init_MenuFilter()
    self.Init_MenuMachineLearning()

..... def Init_MenuFile(self): # FILE menuFile = self.mainMenu.addMenu("File") # NEW new_Action = menuFile.addAction("New") new_Action.setIcon(QIcon.fromTheme("document-new")) new_Action.setShortcut(QKeySequence.New) new_Action.triggered.connect(self.doNew) menuFile.addAction(new_Action) ....
ACTION DEFINITION

def doNew(self):
    self.toBeImplemented()

def doOpen(self):
    self.toBeImplemented()

def doSave(self):
    self.toBeImplemented()

.....

So at this point what you need to do is to connect a main Widget to the main Windows and fill up the function of the menuAction
