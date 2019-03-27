# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroTurma.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class CadastroTurmaTela(object):
    def setupUi(self, background):
        background.setObjectName("background")
        background.resize(500, 162)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(background.sizePolicy().hasHeightForWidth())
        background.setSizePolicy(sizePolicy)
        background.setMaximumSize(QtCore.QSize(2000, 450))
        background.setStyleSheet("")
        background.setTabShape(QtWidgets.QTabWidget.Rounded)
        background.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(background)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.cbSerie = QtWidgets.QComboBox(self.centralwidget)
        self.cbSerie.setGeometry(QtCore.QRect(15, 26, 341, 27))
        self.cbSerie.setAutoFillBackground(True)
        self.cbSerie.setStyleSheet("")
        self.cbSerie.setObjectName("cbSerie")
        self.cbSerie.addItem("")
        self.cbSerie.addItem("")
        self.cbSerie.addItem("")
        self.cbSerie.addItem("")
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
        self.lblMax.setGeometry(QtCore.QRect(364, 54, 135, 23))
        self.lblMax.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color:#fff;")
        self.lblMax.setObjectName("lblMax")
        self.spinMax = QtWidgets.QSpinBox(self.centralwidget)
        self.spinMax.setGeometry(QtCore.QRect(378, 80, 99, 27))
        self.spinMax.setProperty("value", 30)
        self.spinMax.setObjectName("spinMax")
        self.lineGrupo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineGrupo.setGeometry(QtCore.QRect(374, 26, 103, 27))
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
        self.lineSerie.setGeometry(QtCore.QRect(16, 78, 343, 31))
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
        self.lineSerie.setText(self.cbSerie.currentText())
        self.lineSerie.setReadOnly(True)
        self.lineSerie.setPlaceholderText("Série")
        self.lineSerie.setClearButtonEnabled(True)
        self.lineSerie.setObjectName("lineSerie")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(14, 122, 469, 31))
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
        self.lblEscolha.raise_()
        self.lblTurma.raise_()
        self.lblMax.raise_()
        self.cbSerie.raise_()
        self.spinMax.raise_()
        self.lineGrupo.raise_()
        self.lineSerie.raise_()
        self.btnCadastrar.raise_()
        background.setCentralWidget(self.centralwidget)

        self.retranslateUi(background)
        QtCore.QMetaObject.connectSlotsByName(background)

    def retranslateUi(self, background):
        _translate = QtCore.QCoreApplication.translate
        background.setWindowTitle(_translate("background", "Cadastrar Turma"))
        self.cbSerie.setItemText(0, _translate("background", "3º ano - Ensino Médio"))
        self.cbSerie.setItemText(1, _translate("background", "2º ano - Ensino Médio"))
        self.cbSerie.setItemText(2, _translate("background", "1º ano - Ensino Médio"))
        self.cbSerie.setItemText(3, _translate("background", "Outro"))
        self.lblEscolha.setText(_translate("background", "Escolha a série"))
        self.lblTurma.setText(_translate("background", "Turma"))
        self.lblMax.setText(_translate("background", "Máximo de Alunos"))
        self.lineGrupo.setPlaceholderText(_translate("background", "A"))
        self.btnCadastrar.setText(_translate("background", "Cadastrar"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background = QtWidgets.QMainWindow()
    ui = CadastroTurmaTela()
    ui.setupUi(background)
    background.show()
    sys.exit(app.exec_())
