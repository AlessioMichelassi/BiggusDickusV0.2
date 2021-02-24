from Utility.utility import utility as u, createDirectory, ifNotInCode


class mainGenerator(object):
    _import = []
    _mainDefinition = []
    _mainRun = []
    codeToWrite = []
    softwareTitle = "a"

    def __init__(self, mainPath, softwareTitle):
        self.path = F"/{mainPath}{softwareTitle}/"
        self.softwareTitle = softwareTitle
        createDirectory(mainPath, softwareTitle)
        self._import = []
        self.createImport()
        self.createMainDefinition()
        self.createMainRun()

        self.SaveFile()

    def createImport(self):
        ifNotInCode(self._import, "import sys\nimport os\nfrom PySide6.QtWidgets import *\n")
        ifNotInCode(self._import, F"from {self.softwareTitle}.GUI.mainUI import mainWindows\n\n\n")

    def createMainDefinition(self):
        ifNotInCode(self._mainDefinition, "def main():\n")
        ifNotInCode(self._mainDefinition, "    app = QApplication()\n")
        ifNotInCode(self._mainDefinition, "    exe = mainWindows()\n")
        ifNotInCode(self._mainDefinition, "    sys.exit(app.exec_())\n\n\n")

    def createMainRun(self):
        ifNotInCode(self._mainDefinition, "if __name__ == '__main__':\n")
        ifNotInCode(self._mainDefinition, "    main()\n")

    def SaveFile(self):
        fileName = self.path + "main.py"
        fileToSave = open(fileName, 'w')
        fileToSave.write(F"#        Son Of a {self.softwareTitle} \n\n\n")
        fileToSave.close()
        with open(fileName, 'a') as save:
            for eachLine in self._import:
                save.write(str(eachLine))
            for eachLine in self._mainDefinition:
                save.write(str(eachLine))
            for eachLine in self._mainRun:
                save.write(str(eachLine))
