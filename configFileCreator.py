#the skeleton of a config file creator
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
      QApplication,
      QLabel,
      QMenu,
      QMainWindow,
      QToolBar,
      QSpinBox
)
from PyQt6.QtGui import QAction, QIcon
import qrc_resources


# First let's begin with menus and toolbars.
class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent = None):
        """Initialiser"""
        super().__init__(parent)
        self.setWindowTitle("Config files creator")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello World")
        self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.centralWidget)
        #for the actions:
        self._createActions()
        #for the menu bar:
        self._createMenuBar()
        #for the toolbar:
        self._createToolBars()
        self._createContextMenu()


    def _createMenuBar(self):
        menuBar = self.menuBar()
        #creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)

        #adding the actions for the file menu
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
           #adding a separator
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        #creating menus using a title
        #the edit menu
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
            #adding a separator before Find and replace
        editMenu.addSeparator()
        #find and replace submenu in the edit menu
        subfindMenu = editMenu.addMenu("Find and Replace")
        subfindMenu.addAction("Find...")
        subfindMenu.addAction("Replace...")

        #the help menu
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

        #the analyser menu
        analyserMenu = menuBar.addMenu("&Analyser")
        SolarSubanalyserMenu = analyserMenu.addMenu("Solar")
        SolarSubanalyserMenu.addAction("Single FID")
        SolarSubanalyserMenu.addAction("Dual FID")
        PulsarSubAnalyserMenu = analyserMenu.addAction("Pulsar")
        QuasarSubAnalyserMenu = analyserMenu.addAction("Quasar")


    def _createToolBars(self):
        #using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        #using a QToolBar object
        #edit toolbar
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
            #adding a widget to the edit toolbar
        editToolBar.addSeparator()
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)

        #using a QToolBar object and a toolbar area
        #blank for now
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(helpToolBar)

    def _createActions(self):
        #Creating actions using the first constructor
        #File actions
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        #self.newAction.setIcon(QIcon(":file-file.svg"))

        #creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)

    def _createContextMenu(self):
        #setting contextMenuPolicy
        self.centralWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        #Populating the widget with actions
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        self.centralWidget.addAction(self.cutAction)



if __name__ == "__main__":
    print("Printing from the Window class file")
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
