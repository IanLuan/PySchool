from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cadastroMateria(object):
    def setupUi(self, cadastroMateria):
        cadastroMateria.setObjectName("cadastroMateria")
        cadastroMateria.resize(500, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cadastroMateria.sizePolicy().hasHeightForWidth())
        cadastroMateria.setSizePolicy(sizePolicy)
        cadastroMateria.setMaximumSize(QtCore.QSize(2000, 450))
        cadastroMateria.setStyleSheet("background-color:  rgb(21, 143, 181)\n"
"")
        self.centralwidget = QtWidgets.QWidget(cadastroMateria)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 500, 110))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineMateria = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineMateria.sizePolicy().hasHeightForWidth())
        self.lineMateria.setSizePolicy(sizePolicy)
        self.lineMateria.setMinimumSize(QtCore.QSize(20, 0))
        self.lineMateria.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineMateria.setFont(font)
        self.lineMateria.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineMateria.setClearButtonEnabled(True)
        self.lineMateria.setObjectName("lineMateria")
        self.verticalLayout.addWidget(self.lineMateria)
        self.btnCadastrar = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.verticalLayout.addWidget(self.btnCadastrar)
        cadastroMateria.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastroMateria)
        QtCore.QMetaObject.connectSlotsByName(cadastroMateria)

    def retranslateUi(self, cadastroMateria):
        _translate = QtCore.QCoreApplication.translate
        cadastroMateria.setWindowTitle(_translate("cadastroMateria", "Cadastrar Matéria"))
        self.lineMateria.setPlaceholderText(_translate("cadastroMateria", "Nome da Matéria"))
        self.btnCadastrar.setText(_translate("cadastroMateria", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastroMateria = QtWidgets.QMainWindow()
    ui = Ui_cadastroMateria()
    ui.setupUi(cadastroMateria)
    cadastroMateria.show()
    sys.exit(app.exec_())

