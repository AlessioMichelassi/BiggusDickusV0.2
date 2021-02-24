from Utility.utility import ifNotInCode


class mainGUIGenerator(object):
    _import = []
    _mainClass = []
    _mainInit = []
    _initUI = []
    codeToWrite = []
    path = ""

    def __init__(self, mainPath, softwareTitle):
        self.mainPath = mainPath
        self.softwareTitle = softwareTitle
        self.createImport()
        self.createMainGuiClass()
        self.createMainInit()
        self.createInitUI()
        self.SaveFile()

    def createImport(self):
        ifNotInCode(self._import, "import sys\n")
        ifNotInCode(self._import, "import os\n")
        ifNotInCode(self._import, "from PySide6.QtWidgets import *\n")
        ifNotInCode(self._import, "from PySide6.QtGui import *\n\n\n")

    def createMainGuiClass(self):
        ifNotInCode(self._mainClass, "class mainWindows(QMainWindow):\n\n")

    def createMainInit(self):
        """
            def __init__(self):
                QMainWindow.__init__(self)
                self.initUI()
                self.setWindowTitle("Biggus Diskus v0.1")
                self.statusBar().showMessage("ready", 3000)

        :return: self._mainInit
        """
        ifNotInCode(self._mainInit, "    def __init__(self, *args, **kwargs):\n")
        ifNotInCode(self._mainInit, "        QMainWindow.__init__(self, *args, **kwargs)\n")
        ifNotInCode(self._mainInit, "        self.mainMenu = self.menuBar()\n")
        ifNotInCode(self._mainInit, "        self.Init_MainMenu()\n")
        ifNotInCode(self._mainInit, "        self.initUI()\n\n")

    def createInitUI(self):
        ifNotInCode(self._initUI, F"    def initUI(self):\n")
        ifNotInCode(self._initUI, F"        self.setWindowTitle(\"{self.softwareTitle}\")\n")
        ifNotInCode(self._initUI, F"        self.statusBar().showMessage(\"ready\", 3000)\n")
        ifNotInCode(self._initUI, F"        self.show()\n\n")

    def SaveFile(self):
        fileName = F"{self.mainPath}/{self.softwareTitle}/GUI/mainUI.py"
        fileToSave = open(fileName, 'w')
        fileToSave.write(F"#        Son Of a {self.softwareTitle} \n\n\n")
        fileToSave.close()
        with open(fileName, 'a') as save:
            for eachLine in self._import:
                save.write(str(eachLine))
            for eachLine in self._mainClass:
                save.write(str(eachLine))
            for eachLine in self._mainInit:
                save.write(str(eachLine))
            for eachLine in self._initUI:
                save.write(str(eachLine))
