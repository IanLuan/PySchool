from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_background(object):
    def setupUi(self, background):
        background.setObjectName("background")
        background.resize(350, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(background.sizePolicy().hasHeightForWidth())
        background.setSizePolicy(sizePolicy)
        background.setMaximumSize(QtCore.QSize(350, 450))
        background.setStyleSheet("background-color:  rgb(21, 143, 181)\n"
"")
        self.centralwidget = QtWidgets.QWidget(background)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 18, 349, 77))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 100, 350, 197))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.email = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)
        self.email.setMinimumSize(QtCore.QSize(20, 0))
        self.email.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.email.setClearButtonEnabled(True)
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.cpf = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpf.sizePolicy().hasHeightForWidth())
        self.cpf.setSizePolicy(sizePolicy)
        self.cpf.setMinimumSize(QtCore.QSize(20, 0))
        self.cpf.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cpf.setFont(font)
        self.cpf.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.cpf.setClearButtonEnabled(True)
        self.cpf.setObjectName("cpf")
        self.verticalLayout.addWidget(self.cpf)
        self.data = QtWidgets.QDateEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.data.setFont(font)
        self.data.setStyleSheet("QDateEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"fontsize: 30px;\n"
"padding-bottom: 2px;\n"
"}")
        self.data.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.data.setDate(QtCore.QDate(1999, 1, 1))
        self.data.setObjectName("data")
        self.verticalLayout.addWidget(self.data)
        self.novasenha = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.novasenha.sizePolicy().hasHeightForWidth())
        self.novasenha.setSizePolicy(sizePolicy)
        self.novasenha.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.novasenha.setFont(font)
        self.novasenha.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.novasenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.novasenha.setClearButtonEnabled(True)
        self.novasenha.setObjectName("novasenha")
        self.verticalLayout.addWidget(self.novasenha)
        self.novasenha2 = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.novasenha2.sizePolicy().hasHeightForWidth())
        self.novasenha2.setSizePolicy(sizePolicy)
        self.novasenha2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.novasenha2.setFont(font)
        self.novasenha2.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.novasenha2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.novasenha2.setClearButtonEnabled(True)
        self.novasenha2.setObjectName("novasenha2")
        self.verticalLayout.addWidget(self.novasenha2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(22, 306, 307, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.pushButton.setObjectName("pushButton")
        background.setCentralWidget(self.centralwidget)

        self.retranslateUi(background)
        QtCore.QMetaObject.connectSlotsByName(background)

    def retranslateUi(self, background):
        _translate = QtCore.QCoreApplication.translate
        background.setWindowTitle(_translate("background", "MainWindow"))
        self.label.setText(_translate("background", "Esqueceu a senha?"))
        self.email.setPlaceholderText(_translate("background", "email"))
        self.cpf.setInputMask(_translate("background", "000.000.000-00"))
        self.cpf.setPlaceholderText(_translate("background", "CPF"))
        self.novasenha.setPlaceholderText(_translate("background", "Nova senha"))
        self.novasenha2.setPlaceholderText(_translate("background", "Confirme a nova senha"))
        self.pushButton.setText(_translate("background", "Confirmar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QMainWindow()
    ui = Ui_background()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())
