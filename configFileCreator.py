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
from functools import partial
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
        #self._createContextMenu()
        self._connectActions()


    def _createMenuBar(self):
        menuBar = self.menuBar()
        #creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)

        #adding the actions for the file menu
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
            #adding an open recent submenu
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
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

#    def _createContextMenu(self):
#        #setting contextMenuPolicy
#        self.centralWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
#        #Populating the widget with actions
#        self.centralWidget.addAction(self.newAction)
#        self.centralWidget.addAction(self.openAction)
#        self.centralWidget.addAction(self.saveAction)
#        self.centralWidget.addAction(self.copyAction)
#        self.centralWidget.addAction(self.pasteAction)
#        self.centralWidget.addAction(self.cutAction)

    #creating context menus through event handling
        #to override _createContextMenu
        #(just comment out self._createContextMenu in the constructor)
    def contextMenuEvent(self, event):
        #creating a menu object with the central widget as parent
        menu = QMenu(self.centralWidget)
        #populating the menu with actions
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
          #creating a separator action
        separator = QAction(self)
        separator.setSeparator(True)
          #adding the separator to the menu
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        #launching the menu
        menu.exec(event.globalPos())

    def populateOpenRecent(self):
        #step 1: remove the old options from the menu
        self.openRecentMenu.clear()

        #step 2: dinamically create the actions
        #just creates a list of 5 hypothetical files
        #replace this with real code
        actions = []
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)

        #step 3: add the actions to the menu
        self.openRecentMenu.addActions(actions)


    def _connectActions(self):
        #connect file actions >> action.triggered.connect(slot)
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        #connect edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        #connect help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)
        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)


    ## the slots
    def newFile(self):
        #logic for creating a new file goes here
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        #logic for opening an existing file goes here
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        #logic for saving a file goes here
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        #logic for copying content goes here
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        #logic for pasting content goes here
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        #logic for cutting content goes here
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        #logic for launching help goes here
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        #logic for showing an about dialog content goes here
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def openRecentFile(self, filename):
        self.centralWidget.setText(f"<b>{filename}</b> opened")






if __name__ == "__main__":
    print("Printing from the Window class file")
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
