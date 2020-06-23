import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


AREA_SPLIT_X = 15

class QLinkRadioButton(QRadioButton):

    link_clicked = Signal()

    def __init__(self, text, color):
        super().__init__(text)
        self.setStyleSheet("color: {0}; text-decoration: underline".format(color))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        if event.x() < AREA_SPLIT_X:
            super().mousePressEvent(event)
        else:
            self.link_clicked.emit()