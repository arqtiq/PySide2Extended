import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class QNumericBox(QSpinBox):
    returnPressed = Signal()

    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key.Key_Return:
            self.returnPressed.emit()