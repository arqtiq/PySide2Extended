import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from threading import Timer

class QLineEditDelay(QLineEdit):

    textDelayChanged = Signal(str)

    def __init__(self, delay):
        super().__init__()
        
        self.delay = delay
        self.textChanged.connect(self.text_changed)
        self.timer = None

        self.charCountTrigger = 1

    def text_changed(self):
        if len(self.text()) < self.charCountTrigger:
            if self.text() != "":
                return

        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.delay, self.trigger_delay_changed)
        self.timer.start()

    def trigger_delay_changed(self):
        self.textDelayChanged.emit(self.text())

    def setCharCountTrigger(self, count):
        self.charCountTrigger = count