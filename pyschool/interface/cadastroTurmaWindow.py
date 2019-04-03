from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroTurma(object):
    def setupUi(self, CadastroTurma):
        CadastroTurma.setObjectName("CadastroTurma")
        CadastroTurma.resize(500, 215)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroTurma.sizePolicy().hasHeightForWidth())
        CadastroTurma.setSizePolicy(sizePolicy)
        CadastroTurma.setMinimumSize(QtCore.QSize(500, 215))
        CadastroTurma.setMaximumSize(QtCore.QSize(500, 215))
        CadastroTurma.setStyleSheet("")
        CadastroTurma.setTabShape(QtWidgets.QTabWidget.Rounded)
        CadastroTurma.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(CadastroTurma)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.cbSerie = QtWidgets.QComboBox(self.centralwidget)
        self.cbSerie.setGeometry(QtCore.QRect(15, 26, 350, 27))
        self.cbSerie.setAutoFillBackground(True)
        self.cbSerie.setStyleSheet("")
        self.cbSerie.setObjectName("cbSerie")
        self.lblEscolha = QtWidgets.QLabel(self.centralwidget)
        self.lblEscolha.setGeometry(QtCore.QRect(16, 2, 181, 23))
        self.lblEscolha.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color:#fff;")
        self.lblEscolha.setObjectName("lblEscolha")
        self.lblTurma = QtWidgets.QLabel(self.centralwidget)
        self.lblTurma.setGeometry(QtCore.QRect(376, 2, 117, 23))
        self.lblTurma.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color:#fff;")
        self.lblTurma.setObjectName("lblTurma")
        self.lblMax = QtWidgets.QLabel(self.centralwidget)
        self.lblMax.setGeometry(QtCore.QRect(364, 56, 135, 23))
        self.lblMax.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color:#fff;")
        self.lblMax.setObjectName("lblMax")
        self.spinMax = QtWidgets.QSpinBox(self.centralwidget)
        self.spinMax.setGeometry(QtCore.QRect(385, 80, 101, 27))
        self.spinMax.setProperty("value", 30)
        self.spinMax.setObjectName("spinMax")
        self.lineGrupo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineGrupo.setGeometry(QtCore.QRect(385, 26, 100, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineGrupo.sizePolicy().hasHeightForWidth())
        self.lineGrupo.setSizePolicy(sizePolicy)
        self.lineGrupo.setMinimumSize(QtCore.QSize(20, 0))
        self.lineGrupo.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineGrupo.setFont(font)
        self.lineGrupo.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineGrupo.setText("")
        self.lineGrupo.setClearButtonEnabled(True)
        self.lineGrupo.setObjectName("lineGrupo")
        self.lineSerie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSerie.setGeometry(QtCore.QRect(15, 78, 350, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineSerie.sizePolicy().hasHeightForWidth())
        self.lineSerie.setSizePolicy(sizePolicy)
        self.lineSerie.setMinimumSize(QtCore.QSize(20, 0))
        self.lineSerie.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSerie.setFont(font)
        self.lineSerie.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineSerie.setText("")
        self.lineSerie.setReadOnly(True)
        self.lineSerie.setPlaceholderText("Série")
        self.lineSerie.setClearButtonEnabled(True)
        self.lineSerie.setObjectName("lineSerie")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(15, 174, 470, 31))
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
        self.lblEscolha_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblEscolha_2.setGeometry(QtCore.QRect(16, 56, 181, 23))
        self.lblEscolha_2.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color:#fff;")
        self.lblEscolha_2.setObjectName("lblEscolha_2")
        self.btnMaterias = QtWidgets.QPushButton(self.centralwidget)
        self.btnMaterias.setGeometry(QtCore.QRect(15, 132, 147, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMaterias.sizePolicy().hasHeightForWidth())
        self.btnMaterias.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnMaterias.setFont(font)
        self.btnMaterias.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnMaterias.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnMaterias.setStyleSheet("\n"
"border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"box-shadow: 5px -9px 3px #000;\n"
"color: #fff;\n"
"")
        self.btnMaterias.setObjectName("btnMaterias")
        self.lineMaterias = QtWidgets.QLineEdit(self.centralwidget)
        self.lineMaterias.setGeometry(QtCore.QRect(168, 132, 317, 31))
        self.lineMaterias.setStyleSheet("QLineEdit { \n"
"border: 5px solid white;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineMaterias.setReadOnly(True)
        self.lineMaterias.setObjectName("lineMaterias")
        self.lblMateria = QtWidgets.QLabel(self.centralwidget)
        self.lblMateria.setGeometry(QtCore.QRect(180, 110, 55, 23))
        self.lblMateria.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: #fff;")
        self.lblMateria.setObjectName("lblMateria")
        self.lblEscolha.raise_()
        self.lblTurma.raise_()
        self.lblMax.raise_()
        self.cbSerie.raise_()
        self.spinMax.raise_()
        self.lineGrupo.raise_()
        self.lineSerie.raise_()
        self.btnCadastrar.raise_()
        self.lblEscolha_2.raise_()
        self.btnMaterias.raise_()
        self.lineMaterias.raise_()
        self.lblMateria.raise_()
        CadastroTurma.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroTurma)
        QtCore.QMetaObject.connectSlotsByName(CadastroTurma)

    def retranslateUi(self, CadastroTurma):
        _translate = QtCore.QCoreApplication.translate
        CadastroTurma.setWindowTitle(_translate("CadastroTurma", "Cadastrar Turma"))
        self.lblEscolha.setText(_translate("CadastroTurma", "Escolha a série"))
        self.lblTurma.setText(_translate("CadastroTurma", "Turma"))
        self.lblMax.setText(_translate("CadastroTurma", "Máximo de Alunos"))
        self.lineGrupo.setPlaceholderText(_translate("CadastroTurma", "A"))
        self.btnCadastrar.setText(_translate("CadastroTurma", "Cadastrar"))
        self.lblEscolha_2.setText(_translate("CadastroTurma", "Série escolhida"))
        self.btnMaterias.setText(_translate("CadastroTurma", "Definir Matérias"))
        self.lblMateria.setText(_translate("CadastroTurma", "Matérias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadastroTurma = QtWidgets.QMainWindow()
    ui = Ui_CadastroTurma()
    ui.setupUi(CadastroTurma)
    CadastroTurma.show()
    sys.exit(app.exec_())

