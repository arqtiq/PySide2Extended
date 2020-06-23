from PySide2.QtWidgets import QFrame

class QHLine(QFrame):
    def __init__(self, color=None):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Plain)
        if color:
            self.setStyleSheet("background-color: " + color)


class QVLine(QFrame):
    def __init__(self, color=None):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Plain)
        if color:
            self.setStyleSheet("background-color: " + color)