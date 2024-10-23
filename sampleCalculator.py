import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QWidget,)



app = QApplication([])
window = QWidget()
window.setWindowTitle("Sample calculator App")
window.setGeometry(200, 200, 400, 100)
#helloMsg = QLabel("<h1>Hello a second time, World!</h1>", parent=window)
#helloMsg.move(60, 15)

#layout = QHBoxLayout()
#layout.addWidget(QPushButton("Left"))
#layout.addWidget(QPushButton("Center"))
#layout.addWidget(QPushButton("Right"))
#window.setLayout(layout)

#VerticalLayout = QVBoxLayout()
#VerticalLayout.addWidget(QPushButton("Top"))
#VerticalLayout.addWidget(QPushButton("Center"))
#VerticalLayout.addWidget(QPushButton("Bottom"))
#window.setLayout(VerticalLayout)

#layout = QGridLayout()
#layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
#layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
#layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
#layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
#layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
#layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
#layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
#layout.addWidget(QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2)
#window.setLayout(layout)

layout = QFormLayout()
layout.addRow("Name:", QLineEdit())
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())