import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

# Create widget

        label = QLabel(self)
        pixmap = QPixmap('image.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        image = QFileDialog.getOpenFileName(None, 'Escolher foto', '', "Images(*.png *.jpeg *.jpg)")
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        label.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())