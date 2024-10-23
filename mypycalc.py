#mypycalc.py
"""
Design a simple calculator using the Model-View-Controller design pattern.
"""
import sys
#to connect signals with methods that need to take extra arguments.
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

## constants
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35  #the display height in pixels
BUTTON_SIZE = 40
ERROR_MSG = "ERROR"

## classes
class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""
    def __init__(self):
        super().__init__()      #__ = dunder
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}   # a list of lists
        buttonsLayout = QGridLayout()
        keyBoard = [
           ["7", "8", "9", "/", "C"],
           ["4", "5", "6", "*", "("],
           ["1", "2", "3", "-", ")"],
           ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text"""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display"""
        self.setDisplayText("")


def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class PyCalc:
    """PyCalc's controller class."""

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)



def main():
    """"PyCalc's main function"""
    pycalcApp = QApplication([])
    pycalcwindow = PyCalcWindow()
    pycalcwindow.show()
    PyCalc(model=evaluateExpression, view=pycalcwindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()
