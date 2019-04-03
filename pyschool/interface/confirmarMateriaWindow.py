from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirmarMateria(object):
    def setupUi(self, confirmarMateria):
        confirmarMateria.setObjectName("confirmarMateria")
        confirmarMateria.resize(400, 414)
        confirmarMateria.setStyleSheet("QconfirmarMateria{\n"
"background-color: rgb(21, 143, 181)\n"
"}")
        self.btnConfirmar = QtWidgets.QPushButton(confirmarMateria)
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
        self.frameLaranja = QtWidgets.QFrame(confirmarMateria)
        self.frameLaranja.setGeometry(QtCore.QRect(10, 0, 381, 10))
        self.frameLaranja.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"border-radius: 0.2px;\n"
"")
        self.frameLaranja.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLaranja.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLaranja.setObjectName("frameLaranja")
        self.scrollArea = QtWidgets.QScrollArea(confirmarMateria)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 381, 351))
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"background-color:rgb(255, 255, 255): \n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 349))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(255,255,255)")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(confirmarMateria)
        QtCore.QMetaObject.connectSlotsByName(confirmarMateria)

    def retranslateUi(self, confirmarMateria):
        _translate = QtCore.QCoreApplication.translate
        confirmarMateria.setWindowTitle(_translate("confirmarMateria", "Escolher Matéria"))
        self.btnConfirmar.setText(_translate("confirmarMateria", "Confirmar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmarMateria = QtWidgets.QDialog()
    ui = Ui_confirmarMateria()
    ui.setupUi(confirmarMateria)
    confirmarMateria.show()
    sys.exit(app.exec_())

