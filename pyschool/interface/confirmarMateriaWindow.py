# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmarMateria.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 414)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.btnConfirmar = QtWidgets.QPushButton(Dialog)
        self.btnConfirmar.setGeometry(QtCore.QRect(140, 370, 111, 31))
        self.btnConfirmar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 123, 28);\n"
"box-shadow: 5px -9px 3px #000;\n"
"\n"
"\n"
"")
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.frameLaranja = QtWidgets.QFrame(Dialog)
        self.frameLaranja.setGeometry(QtCore.QRect(10, 0, 381, 9))
        self.frameLaranja.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"border-radius: 0.2px;\n"
"")
        self.frameLaranja.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLaranja.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLaranja.setObjectName("frameLaranja")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 381, 341))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 520))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Escolher Matéria"))
        self.btnConfirmar.setText(_translate("Dialog", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

