import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class FaderWidget(QWidget):
    def __init__(self, stack, old_widget, new_widget, duration=333): 
        super().__init__(new_widget)
        
        self.old_pixmap = QPixmap(stack.size())
        self.pixmap_opacity = 1.0
        old_widget.render(self.old_pixmap)
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(duration)
        self.timeline.start()
        
        self.resize(stack.size())
        self.show()
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value): 
        self.pixmap_opacity = 1.0 - value
        self.repaint()

class QStackedFadeWidget (QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.fade_duration = 333

    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self, self.currentWidget(), self.widget(index), self.fade_duration)
        super().setCurrentIndex(index)