#        Son Of a BiggusDickusV0_3 


import sys
import os
from PySide6.QtWidgets import *
from BiggusDickusV0_3.GUI.mainUI import mainWindows


def main():
    app = QApplication()
    exe = mainWindows()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
