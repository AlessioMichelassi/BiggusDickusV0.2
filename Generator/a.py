from Utility.utility import ifNotInCode


class a:
    initMenuCode = []
    menuCode = []

    def createInitMenuCode(self):
        """
        For each menuTitle in the dictionary the software create
        a menu ad a function for defining it
            def init_Menu(self):
                self.Init_MenuFile() -> viene inserito dopo
                self.Init_MenuEdit()
        :return: self.initMenuCode
        """
        ifNotInCode(self.initMenuCode, "    def init_Menu(self):\n")

    def menuGenerator(self, menu: dict):

        '''
            def Init_MenuFile(self):                    <- inserisce il titolo
            #        File                               <- inserisce il commento con il nome del menu
            menuFile = self.mainMenu.addMenu("File")    <- aggiunge il nome del menu al menù principale
            #                NEW                        <- inserisce il commento con la action
            new_Action = menuFile.addAction("New")      <- inserisce la action
            new_Action.setIcon("New", QIcon.fromTheme("document-new"))
            new_Action.setShortcut(QKeySequence.New)
            new_Action.setToolTip("The icon used for the action to create a new contact in an address book application. ")
            menuFile.addAction(self.doNew)
        :param menu:
        :return:
        '''

        lastMenuTitle = next(iter(menu.values()))
        self.generateFirstPart(menu, lastMenuTitle)

    def generateFirstPart(self, menu: dict, lastMenuTitle):
        for menuAction, menuTitle in menu:
            if not menuTitle == lastMenuTitle:
                lastMenuTitle = menuTitle
                # aggiunge la definizione per richiamare l'inizializzatore del nuovo menu
                ifNotInCode(self.initMenuCode, F"        self.Init_Menu{menuTitle}()\n")
                # Se il titolo del menu è diverso dal precedente crea una definizione di menu con il nuovo titolo
                ifNotInCode(self.initMenuCode, F"    self.init_Menu{menuTitle}(self):\n")
                # METTE IL COMMENTO DEL MENU
                ifNotInCode(self.menuCode, F"        #        {menuTitle.title()}\n")
                # crea la parte menuFile = self.mainMenu.addMenu("File")
                self.menuCode.append(F"        menu{menuTitle} = self.mainMenu.addMenu(\"{menuTitle}\")\n")
            for _menuAction, _menuTitle in menu:
                if not _menuAction == "-":
                    if _menuTitle == lastMenuTitle:
                        # INSERISCE IL TITOLO DELLA ACTION
                        ifNotInCode(self.menuCode, F"        #                {_menuAction.upper()}\n")
                        # INSERISCE LA ACTION
                        sentence = F"{_menuAction.lower().replace(' ', '_')}_Action = " \
                                   F"menu{_menuTitle}.addAction(\"{_menuAction}\")\n"
                        ifNotInCode(self.menuCode, sentence)
                        ################################################################
                        #                   L'icona viene inserita se viene trovata
                        #                       nel dizionario delle icone
                        #                            INSERT ICON
                        sentence = F"        {_menuAction.lower().replace(' ', '')}" \
                                   F"_Action.setIcon(QIcon.fromTheme(\"{_menuTitle}\"))\n"
                        ifNotInCode(self.menuCode, sentence)
                        declaration = _menuTitle
                        ################################################################
                        #                   La ShorCut viene inserita se viene trovata
                        #                       nel dizionario delle shortCut
                        #                           INSERT SHORTCUT
                        sentence = F"        {_menuAction.lower().replace(' ', '')}" \
                                   F"_Action.setShortcut(QKeySequence.{_menuTitle.capitalize().replace(' ', '')})\n"
                        ifNotInCode(self.menuCode, sentence)
                        # INSERT HINT
                        for keyT, valueT in definition.definitionDictionary.items():
                            if declaration == keyT:
                                sentence = F"        {key.lower().replace(' ', '')}_Action.setToolTip(\"{valueT}\")\n"
                                ifNotInCode(self.menuCode, sentence)
                        ################################################################
                        #                   Se la hint non viene trovata viene inserito
                        #                       il nome della action...
                        for keyT, valueT in definition.definitionDictionary.items():
                            if declaration == keyT:
                                sentence = F"        {key.lower().replace(' ', '')}_Action.setToolTip(\"{valueT}\")\n"
                                ifNotInCode(self.menuCode, sentence)
                        ################################################################
                        #                   LA Action viene collegata al menu
                        #                       openFile.triggered.connect(self.doOpenFile)
                        #                       fileMenu.addAction(openFile)
                        sentence = F"        {_menuAction.lower().replace(' ', '')}" \
                                   F".triggered.connect.(self.do(\"{_menuTitle}\"))\n"
                        ifNotInCode(self.menuCode, sentence)
                        sentence = F"        {lastMenuTitle}.addAction({_menuTitle})\n"
                        ifNotInCode(self.menuCode, sentence)
                        ################################################################
                        #                   Crea la Action in un'altra parte del cdice
                        sentence = "\n#    ACTION DEFINITION\n"
                        ifNotInCode(self.function, sentence)
                        sentence = F"    def do{_menuAction.replace(' ', '_')}(self):\n        self.toBeImplemented()\n\n"
                        ifNotInCode(self.function, sentence)
                    else:
                        sentence = F"        menu{self.MenuTitle}.addSeparator()\n"
                        ifNotInCode(self.menuCode, sentence)