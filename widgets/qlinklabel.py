import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import ui.style as style

class QLinkLabel(QLabel):

    clicked = Signal()

    def __init__(self, text, color):
        super().__init__(text)
        self.setStyleSheet("color: {0}; text-decoration: underline".format(color))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        self.clicked.emit()