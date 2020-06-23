import PySide2
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import urllib
import threading


class Fit:
    Width = 0
    Height = 1

class QImageBox(QLabel):
    clicked = Signal()
    rightClicked = Signal()

    def __init__(self, img=None, alignment=Qt.AlignCenter, parent=None):
        super(QImageBox, self).__init__(parent=parent)
        self.setAlignment(alignment)
        self.set_image(img)
        self.set_hover_image(None)
        self.hover_enabled = False


    def set_image(self, img):
        self.image = img
        self.setPixmap(img)

    def get_image(self):
        return self.image


    def set_hover_image(self, img, enable=False):
        self.hover_image = img
        if img and enable:
            self.hover_enabled = True

    def set_hover_enabled(self, enabled):
        self.hover_enabled = enabled

    def set_hand_cursor(self):
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def swap_images(self):
        if not self.image or not self.hover_image:
            return
        i = self.image
        self.set_image(self.hover_image)
        self.set_hover_image(i)

    def set_url_image(self, url):
        t = threading.Thread(target=self.__async_download_image, kwargs={'url':url})
        t.start()
        
    def __async_download_image(self, **kwargs):
        img = self.get_url_image(kwargs['url'])
        self.set_image(img)

    def get_url_image(self, url: str) -> QPixmap:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    img_data = urllib.request.urlopen(req).read()
    img = QImage()
    img.loadFromData(img_data)
    return QPixmap(img)


    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.rightClicked.emit()
        elif event.button() == Qt.LeftButton:
            self.clicked.emit()

    def enterEvent(self, event):
        if self.hover_enabled:
            if self.hover_image:
                self.setPixmap(self.hover_image)

    def leaveEvent(self, event):
        self.setPixmap(self.image)


    def resize_fit(self, s, fit):
        if fit == Fit.Width:
            if self.image:
                self.set_image(self.image.scaledToWidth(s))
            if self.hover_image:
                self.set_hover_image(self.hover_image.scaledToWidth(s))
        elif fit == Fit.Height:
            if self.image:
                self.set_image(self.image.scaledToHeight(s))
            if self.hover_image:
                self.set_hover_image(self.hover_image.scaledToHeight(s))
        
        self.resize(self.image.size())