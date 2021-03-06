from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(350, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMaximumSize(QtCore.QSize(350, 450))
        login.setStyleSheet("background-color:  rgb(21, 143, 181)\n"
"")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.lblBemVindo = QtWidgets.QLabel(self.centralwidget)
        self.lblBemVindo.setGeometry(QtCore.QRect(75, 64, 200, 77))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lblBemVindo.setFont(font)
        self.lblBemVindo.setStyleSheet("color: #fff;")
        self.lblBemVindo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBemVindo.setObjectName("lblBemVindo")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 146, 350, 107))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEmail = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEmail.sizePolicy().hasHeightForWidth())
        self.lineEmail.setSizePolicy(sizePolicy)
        self.lineEmail.setMinimumSize(QtCore.QSize(20, 0))
        self.lineEmail.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEmail.setFont(font)
        self.lineEmail.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEmail.setClearButtonEnabled(True)
        self.lineEmail.setObjectName("lineEmail")
        self.verticalLayout.addWidget(self.lineEmail)
        self.lineSenha = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSenha.sizePolicy().hasHeightForWidth())
        self.lineSenha.setSizePolicy(sizePolicy)
        self.lineSenha.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineSenha.setFont(font)
        self.lineSenha.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineSenha.setClearButtonEnabled(True)
        self.lineSenha.setObjectName("lineSenha")
        self.verticalLayout.addWidget(self.lineSenha)
        self.btnEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(22, 258, 307, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnEntrar.setFont(font)
        self.btnEntrar.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.btnEntrar.setObjectName("btnEntrar")
        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.lblBemVindo.setText(_translate("login", "Bem-vindo!"))
        self.lineEmail.setPlaceholderText(_translate("login", "email"))
        self.lineSenha.setPlaceholderText(_translate("login", "senha"))
        self.btnEntrar.setText(_translate("login", "Entrar"))