import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class QFlatDoubleBar(QWidget):
    def __init__(self, color, back_color=None):
        super().__init__()
        self.progress1 = 0
        self.progress2 = 0
        self.maximum = 100

        self.back_color = back_color
        self.fore_color = color

    def set_progress(self, index, progress):
        if index == 0:
            self.progress1 = progress
        elif index == 1:
            self.progress2 = progress
        else:
            return
        self.update()
    def set_progresses(self, p1, p2):
        self.set_progress(0, p1)
        self.set_progress(1, p2)

    def set_maximum(self, maximum):
        self.maximum = maximum
        if self.progress1 != 0 and self.progress2 != 0:
            self.update()

    def get_ratio(self, index):
        if index == 0:
            return self.progress1 / self.maximum
        elif index == 1:
            return self.progress2 / self.maximum
        else:
            return None
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        
        if self.back_color:
            qp.fillRect(0, 0, self.width(), self.height(), self.back_color)

        h = self.height() / 2
        if self.progress1 != 0:
            qp.fillRect(0, 0, int(self.get_ratio(0) * self.width()), h, self.fore_color)
        if self.progress2 != 0:
            qp.fillRect(0, h, int(self.get_ratio(1) * self.width()), h, self.fore_color)

        qp.end()

class QFlatProgressBar(QWidget):
    def __init__(self, color, back_color=None):
        super().__init__()
        self.progress = 0
        self.maximum = 100

        self.back_color = back_color
        self.fore_color = color

    def set_progress(self, progress):
        self.progress = progress
        self.update()

    def set_maximum(self, maximum):
        self.maximum = maximum
        if self.progress != 0:
            self.update()

    def get_ratio(self):
        return self.progress / self.maximum

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        
        if self.back_color:
            qp.fillRect(0, 0, self.width(), self.height(), self.back_color)

        if self.progress != 0:
            qp.fillRect(0, 0, int(self.get_ratio() * self.width()), self.height(), self.fore_color)

        qp.end()