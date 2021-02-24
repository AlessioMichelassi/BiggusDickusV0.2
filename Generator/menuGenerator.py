from Utility.DefinitionDictionary import definition
from Utility.utility import ifNotInCode


class menuCreator(object):
    # In this there will the code for import the stuff needed for the menu
    _import = []
    # in this there will the code for the main __init__
    mainClassDefinition = []
    # In the for every KEy of the dictionary it contain a definition calling
    initMenuCode = []
    # for every key of the diction ir create the menu definition using the value ad add call to function, shortcut
    menuCode = []
    # here there will the list of the function of the action
    function = []
    # this contain the finalCode
    finalCode = []
    # this is the menuTitle
    MenuTitle = None
    isStarPassed = False

    def __init__(self, mainPath, softwareTitle, menuDictionary):
        """
        Accetta un dizionario creato mome   menuAction : menuTitolo
        il ciclo for serve a differenziare il titolo e a far ripartire l'algoritmo
        menuFile = {"New": "File", "Open": "File", "Save": "File", "Save As": "File", "-1": "File", "Quit": "File",
            "Undo": "Edit", "Redo": "Edit", "-2": "Edit", "cut": "Edit", "copy": "Edit", "paste": "Edit",
            "PasteFromHistory": "Edit", "Delete": "Edit", "-3": "Edit", "SelectAll": "Edit"
            }
        :param mainPath:
        :param softwareTitle:
        :param menuDictionary:
        """
        self.mainPath = mainPath
        self.softwareTitle = softwareTitle
        lastKey = ""
        self.menuGenerator(menuDictionary)
        self.createFunctionFromMenuAction(menuDictionary, self.function)
        for key, value in menuDictionary.items():
            if lastKey != value:

                lastKey = value

        self.SaveFile()

    def menuTitleExtractor(self):
        pass

    def isIconInDictionary(self, menuAction, code):
        for key, value in definition.iconDictionary.items():
            if key == menuAction.lower().replace(' ', ''):
                sentence = F"        {menuAction.lower().replace(' ', '')}_Action.setIcon(QIcon.fromTheme(\"{value}\"))\n"
                ifNotInCode(code, sentence)

    def isShortCutInTheDictionary(self, menuAction, code):
        for keyShortCut, valueShortCut in definition.shortCutDictionary.items():
            if keyShortCut == menuAction.replace(' ', '').lower():
                sentence = F"        {menuAction.lower().replace(' ', '_')}" \
                           F"_Action.setShortcut({valueShortCut})\n"
                ifNotInCode(code, sentence)

    def isHintInTheDictionary(self, menuAction, code):
        for keyHint, valueHint in definition.definitionDictionary.items():
            if keyHint == menuAction.replace(' ', '').lower():
                sentence = F"        {menuAction.lower().replace(' ', '_')}" \
                           F"_Action..setToolTip({valueHint})\n"
                ifNotInCode(code, sentence)

    def createFunctionFromMenuAction(self, menu, code):
        for menuAction, menuTitle in menu.items():
            if not menuAction.startswith('-'):
                sentence = "\n#    ACTION DEFINITION\n"
                ifNotInCode(self.function, sentence)
                sentence = F"    def do{menuAction.replace(' ', '_')}(self):\n        self.toBeImplemented()\n\n"
                ifNotInCode(code, sentence)
        sentence = "    def toBeImplemented(self):\n"
        ifNotInCode(self.function, sentence)
        sentence = F"        self.statusBar().showMessage(\"To Be Implemented\", 3000)\n\n"
        ifNotInCode(code, sentence)

    def menuGenerator(self, menu):
        for menuTitle in menu.values():
            if not menuTitle.startswith('*'):
                # in self._initMenuCode aggiunge:
                #   self.Init_MenuFile()    <- o il titolo del nuovo menù da creare
                ifNotInCode(self.initMenuCode, F"    def Init_MainMenu(self):\n")
                ifNotInCode(self.initMenuCode, F"        self.Init_Menu{menuTitle}()\n")
        _lastMenuTitle = ""
        for _menuAction, _menuTitle in menu.items():

            if not _menuAction.startswith('-'):
                # FINAL CODE MAY LOOK LIKE THIS:
                '''    def Init_MenuFile(self):
                            #        File
                            menuFile = self.mainMenu.addMenu("File")
                            #                NEW
                            new_Action = menuFile.addAction("New")
                            new_Action.setIcon(QIcon.fromTheme("document-new"))
                            new_Action.setShortcut(QKeySequence.New)
                            new_Action.triggered.connect(self.doNew)
                            menuFile.addAction(new_Action)
                '''
                if not _menuTitle.startswith('*'):
                    _lastMenuTitle = _menuTitle
                    sentence = F"\n    def Init_Menu{_menuTitle}(self):\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        #        {_menuTitle.upper()}\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        menu{_menuTitle} = self.mainMenu.addMenu(\"{_menuTitle}\")\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        #                {_menuAction.upper()}\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        {_menuAction.lower().replace(' ', '_')}_Action = menu{_menuTitle}.addAction(\"{_menuAction}\")\n"
                    ifNotInCode(self.menuCode, sentence)
                    # Search for the icon in the dictionary
                    self.isIconInDictionary(_menuAction, self.menuCode)
                    # Search for the ShortCutKey in the dictionaty
                    self.isShortCutInTheDictionary(_menuAction, self.menuCode)
                    # Search for the Hint in the dictionaty
                    self.isHintInTheDictionary(_menuAction, self.menuCode)
                    sentence = F"        {_menuAction.lower().replace(' ', '_')}_Action.triggered.connect(self.do{_menuAction.replace(' ', '_')})\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        menu{_menuTitle}.addAction({_menuAction.lower().replace(' ', '_')}_Action)\n"
                    ifNotInCode(self.menuCode, sentence)
                elif _menuTitle.startswith('*'):
                    _menuActionStar = _menuAction
                    _menuSubmenuStar = _menuTitle.replace('*', '')

                    '''
                    #####################################
                    menuSubmenu = menuMenuTitle.addMenu("subMenu")
                    #                MOVE
                    menuAction_Action = menu*Translate.addAction("Move")
                    menuAction_Action.triggered.connect(self.doMenuAction)
                    menuSubmenu.addAction(menuAction_Action)
                    '''
                    self.menuCode.append("        #####################################\n")
                    sentence = F"        menu{_menuSubmenuStar} = menu{_lastMenuTitle}.addMenu(\"{_menuSubmenuStar}\")\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        #                {_menuAction.upper()}\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        {_menuAction.lower().replace(' ', '_')}_Action = menu{_menuSubmenuStar}.addAction(\"{_menuAction}\")\n"
                    ifNotInCode(self.menuCode, sentence)
                    # Search for the icon in the dictionary
                    self.isIconInDictionary(_menuAction, self.menuCode)
                    # Search for the ShortCutKey in the dictionaty
                    self.isShortCutInTheDictionary(_menuAction, self.menuCode)
                    # Search for the Hint in the dictionaty
                    self.isHintInTheDictionary(_menuAction, self.menuCode)
                    sentence = F"        {_menuAction.lower().replace(' ', '_')}_Action.triggered.connect(self.do{_menuAction.replace(' ', '_')})\n"
                    ifNotInCode(self.menuCode, sentence)
                    sentence = F"        menu{_menuSubmenuStar}.addAction({_menuAction.lower().replace(' ', '_')}_Action)\n"
                    ifNotInCode(self.menuCode, sentence)

            elif _menuAction.startswith('-'):
                self.menuCode.append("        #####################################\n")
                self.menuCode.append(F"        menu{_menuTitle}.addSeparator()\n")

    def SaveFile(self):
        fileName = F"{self.mainPath}/{self.softwareTitle}/GUI/mainUI.py"
        print(fileName)
        # fileToSave = open(fileName, 'w')
        # fileToSave.write(F"#        Son Of a {self.softwareTitle} \n\n\n")
        # fileToSave.close()
        with open(fileName, 'a') as save:
            for eachLine in self.mainClassDefinition:
                save.write(str(eachLine))
            for eachLine in self.initMenuCode:
                save.write(str(eachLine))
            for eachLine in self.menuCode:
                save.write(str(eachLine))
            for eachLine in self.function:
                save.write(str(eachLine))
