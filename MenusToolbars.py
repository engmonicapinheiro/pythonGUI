#Menus and tool
from configFileCreator import Window
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
      QApplication,
      QLabel,
      QMenu,
      QMainWindow,
      QToolBar,
)
from PyQt6.QtGui import QAction, QIcon
import qrc_resources


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
