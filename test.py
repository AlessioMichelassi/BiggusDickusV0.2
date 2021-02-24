class test:
	menu = {"Open": "File", "Copy": "*Edit"}

	menuAction = None
	menuTitle = None
	menuSub = None

	def __init__(self):
		self.isThereASubmenu(self.menu)

	def isThereASubmenu(self, menu):
		for _menuAction, _menuTitle in menu.items():
			if not _menuTitle.startswith('*'):
				self.createMenu(_menuAction, _menuTitle)
			else:
				self.createSubMenu(_menuAction, _menuTitle)

	def createMenu(self, _menuAction, _menuTitle):
		pass

	def createSubMenu(self, _menuAction, _menuTitle):
		print("a")
		pass


if __name__ == '__main__':
	test()
