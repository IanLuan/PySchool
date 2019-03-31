# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfilProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_perfilProfessor(object):
    def setupUi(self, perfilProfessor):
        perfilProfessor.setObjectName("perfilProfessor")
        perfilProfessor.resize(952, 654)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(perfilProfessor.sizePolicy().hasHeightForWidth())
        perfilProfessor.setSizePolicy(sizePolicy)
        perfilProfessor.setMinimumSize(QtCore.QSize(952, 200))
        perfilProfessor.setMaximumSize(QtCore.QSize(952, 760))
        perfilProfessor.setLayoutDirection(QtCore.Qt.LeftToRight)
        perfilProfessor.setStyleSheet("background-color: rgb(21, 143, 181)")
        self.centralwidget = QtWidgets.QWidget(perfilProfessor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QWidget{\n"
"backgroundcolor: rgb(255,255,255)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(10, 610, 111, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCancelar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 5px -9px 3px #000;")
        self.btnCancelar.setObjectName("btnCancelar")
        self.framezao = QtWidgets.QFrame(self.centralwidget)
        self.framezao.setGeometry(QtCore.QRect(10, 0, 931, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framezao.sizePolicy().hasHeightForWidth())
        self.framezao.setSizePolicy(sizePolicy)
        self.framezao.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"}")
        self.framezao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framezao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framezao.setObjectName("framezao")
        self.framePessoais = QtWidgets.QFrame(self.framezao)
        self.framePessoais.setGeometry(QtCore.QRect(0, 30, 931, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePessoais.sizePolicy().hasHeightForWidth())
        self.framePessoais.setSizePolicy(sizePolicy)
        self.framePessoais.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.framePessoais.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePessoais.setObjectName("framePessoais")
        self.lblPessoais = QtWidgets.QLabel(self.framePessoais)
        self.lblPessoais.setGeometry(QtCore.QRect(0, -4, 931, 39))
        self.lblPessoais.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblPessoais.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPessoais.setObjectName("lblPessoais")
        self.lblNome = QtWidgets.QLabel(self.framePessoais)
        self.lblNome.setGeometry(QtCore.QRect(10, 45, 181, 23))
        self.lblNome.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblNome.setObjectName("lblNome")
        self.lblCpf = QtWidgets.QLabel(self.framePessoais)
        self.lblCpf.setGeometry(QtCore.QRect(10, 112, 55, 23))
        self.lblCpf.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblCpf.setObjectName("lblCpf")
        self.lblEstadoCivil = QtWidgets.QLabel(self.framePessoais)
        self.lblEstadoCivil.setGeometry(QtCore.QRect(10, 180, 111, 23))
        self.lblEstadoCivil.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblEstadoCivil.setObjectName("lblEstadoCivil")
        self.lblNascimento = QtWidgets.QLabel(self.framePessoais)
        self.lblNascimento.setGeometry(QtCore.QRect(740, 180, 121, 23))
        self.lblNascimento.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblNascimento.setObjectName("lblNascimento")
        self.lblRg = QtWidgets.QLabel(self.framePessoais)
        self.lblRg.setGeometry(QtCore.QRect(470, 112, 55, 23))
        self.lblRg.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblRg.setTextFormat(QtCore.Qt.PlainText)
        self.lblRg.setObjectName("lblRg")
        self.cbEstadoCivil = QtWidgets.QComboBox(self.framePessoais)
        self.cbEstadoCivil.setEnabled(False)
        self.cbEstadoCivil.setGeometry(QtCore.QRect(10, 210, 431, 28))
        self.cbEstadoCivil.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbEstadoCivil.setMaxVisibleItems(5)
        self.cbEstadoCivil.setObjectName("cbEstadoCivil")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.dateNascimento = QtWidgets.QDateEdit(self.framePessoais)
        self.dateNascimento.setEnabled(True)
        self.dateNascimento.setGeometry(QtCore.QRect(740, 210, 171, 28))
        self.dateNascimento.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateNascimento.setReadOnly(True)
        self.dateNascimento.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateNascimento.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateNascimento.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.dateNascimento.setObjectName("dateNascimento")
        self.lblSexo = QtWidgets.QLabel(self.framePessoais)
        self.lblSexo.setGeometry(QtCore.QRect(470, 180, 55, 31))
        self.lblSexo.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblSexo.setObjectName("lblSexo")
        self.cbSexo = QtWidgets.QComboBox(self.framePessoais)
        self.cbSexo.setEnabled(False)
        self.cbSexo.setGeometry(QtCore.QRect(470, 210, 251, 28))
        self.cbSexo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.lineInfo_2 = QtWidgets.QFrame(self.framePessoais)
        self.lineInfo_2.setGeometry(QtCore.QRect(320, 32, 300, 1))
        self.lineInfo_2.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.lineInfo_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineInfo_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineInfo_2.setObjectName("lineInfo_2")
        self.lblFotolbl = QtWidgets.QLabel(self.framePessoais)
        self.lblFotolbl.setGeometry(QtCore.QRect(740, 45, 40, 23))
        self.lblFotolbl.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblFotolbl.setObjectName("lblFotolbl")
        self.lineNome = QtWidgets.QLineEdit(self.framePessoais)
        self.lineNome.setGeometry(QtCore.QRect(10, 75, 711, 28))
        self.lineNome.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineNome.setReadOnly(True)
        self.lineNome.setObjectName("lineNome")
        self.lineCpf = QtWidgets.QLineEdit(self.framePessoais)
        self.lineCpf.setGeometry(QtCore.QRect(10, 140, 431, 28))
        self.lineCpf.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCpf.setReadOnly(True)
        self.lineCpf.setObjectName("lineCpf")
        self.lineRg = QtWidgets.QLineEdit(self.framePessoais)
        self.lineRg.setGeometry(QtCore.QRect(470, 140, 251, 28))
        self.lineRg.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRg.setReadOnly(True)
        self.lineRg.setObjectName("lineRg")
        self.lblFoto = QtWidgets.QLabel(self.framePessoais)
        self.lblFoto.setGeometry(QtCore.QRect(790, 40, 121, 141))
        self.lblFoto.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"")
        self.lblFoto.setText("")
        self.lblFoto.setPixmap(QtGui.QPixmap("../../../OneDrive/Área de Trabalho/icons/perfil.png"))
        self.lblFoto.setObjectName("lblFoto")
        self.frameEndereco = QtWidgets.QFrame(self.framezao)
        self.frameEndereco.setGeometry(QtCore.QRect(0, 290, 931, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameEndereco.sizePolicy().hasHeightForWidth())
        self.frameEndereco.setSizePolicy(sizePolicy)
        self.frameEndereco.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameEndereco.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frameEndereco.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEndereco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEndereco.setObjectName("frameEndereco")
        self.lblEndereco = QtWidgets.QLabel(self.frameEndereco)
        self.lblEndereco.setEnabled(False)
        self.lblEndereco.setGeometry(QtCore.QRect(0, 0, 931, 31))
        self.lblEndereco.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblEndereco.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEndereco.setObjectName("lblEndereco")
        self.lblRua = QtWidgets.QLabel(self.frameEndereco)
        self.lblRua.setGeometry(QtCore.QRect(10, 47, 55, 16))
        self.lblRua.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblRua.setObjectName("lblRua")
        self.lblNum = QtWidgets.QLabel(self.frameEndereco)
        self.lblNum.setGeometry(QtCore.QRect(740, 50, 71, 16))
        self.lblNum.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblNum.setObjectName("lblNum")
        self.lblBairro = QtWidgets.QLabel(self.frameEndereco)
        self.lblBairro.setGeometry(QtCore.QRect(10, 105, 55, 16))
        self.lblBairro.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblBairro.setObjectName("lblBairro")
        self.lblCep = QtWidgets.QLabel(self.frameEndereco)
        self.lblCep.setGeometry(QtCore.QRect(470, 47, 55, 16))
        self.lblCep.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblCep.setObjectName("lblCep")
        self.lblCidade = QtWidgets.QLabel(self.frameEndereco)
        self.lblCidade.setGeometry(QtCore.QRect(470, 105, 55, 16))
        self.lblCidade.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblCidade.setObjectName("lblCidade")
        self.lblEstado = QtWidgets.QLabel(self.frameEndereco)
        self.lblEstado.setGeometry(QtCore.QRect(740, 110, 55, 16))
        self.lblEstado.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblEstado.setObjectName("lblEstado")
        self.lineRua = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineRua.setGeometry(QtCore.QRect(10, 70, 431, 28))
        self.lineRua.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRua.setReadOnly(True)
        self.lineRua.setObjectName("lineRua")
        self.spinNumero = QtWidgets.QSpinBox(self.frameEndereco)
        self.spinNumero.setGeometry(QtCore.QRect(740, 70, 171, 28))
        self.spinNumero.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.spinNumero.setReadOnly(True)
        self.spinNumero.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinNumero.setMaximum(5000)
        self.spinNumero.setObjectName("spinNumero")
        self.cbEstado = QtWidgets.QComboBox(self.frameEndereco)
        self.cbEstado.setEnabled(False)
        self.cbEstado.setGeometry(QtCore.QRect(740, 130, 171, 28))
        self.cbEstado.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbEstado.setObjectName("cbEstado")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.cbEstado.addItem("")
        self.lineEndereco = QtWidgets.QFrame(self.frameEndereco)
        self.lineEndereco.setGeometry(QtCore.QRect(320, 35, 300, 1))
        self.lineEndereco.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.lineEndereco.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineEndereco.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineEndereco.setObjectName("lineEndereco")
        self.lineBairro = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineBairro.setGeometry(QtCore.QRect(10, 130, 431, 28))
        self.lineBairro.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineBairro.setReadOnly(True)
        self.lineBairro.setObjectName("lineBairro")
        self.lineCep = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCep.setGeometry(QtCore.QRect(470, 70, 251, 28))
        self.lineCep.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCep.setReadOnly(True)
        self.lineCep.setObjectName("lineCep")
        self.lineCidade = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCidade.setGeometry(QtCore.QRect(470, 130, 251, 28))
        self.lineCidade.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCidade.setReadOnly(True)
        self.lineCidade.setObjectName("lineCidade")
        self.lblRua.raise_()
        self.lblNum.raise_()
        self.lblBairro.raise_()
        self.lblCep.raise_()
        self.lblCidade.raise_()
        self.lblEstado.raise_()
        self.lineRua.raise_()
        self.spinNumero.raise_()
        self.cbEstado.raise_()
        self.lblEndereco.raise_()
        self.lineEndereco.raise_()
        self.lineBairro.raise_()
        self.lineCep.raise_()
        self.lineCidade.raise_()
        self.frameComplementares = QtWidgets.QFrame(self.framezao)
        self.frameComplementares.setGeometry(QtCore.QRect(0, 460, 931, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameComplementares.sizePolicy().hasHeightForWidth())
        self.frameComplementares.setSizePolicy(sizePolicy)
        self.frameComplementares.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.frameComplementares.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameComplementares.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameComplementares.setObjectName("frameComplementares")
        self.lblInfoComplementares = QtWidgets.QLabel(self.frameComplementares)
        self.lblInfoComplementares.setGeometry(QtCore.QRect(0, 10, 931, 41))
        self.lblInfoComplementares.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblInfoComplementares.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfoComplementares.setObjectName("lblInfoComplementares")
        self.lblMaterias = QtWidgets.QLabel(self.frameComplementares)
        self.lblMaterias.setGeometry(QtCore.QRect(10, 60, 81, 23))
        self.lblMaterias.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblMaterias.setObjectName("lblMaterias")
        self.lblEmail = QtWidgets.QLabel(self.frameComplementares)
        self.lblEmail.setGeometry(QtCore.QRect(230, 60, 55, 23))
        self.lblEmail.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblEmail.setObjectName("lblEmail")
        self.lineInfo = QtWidgets.QFrame(self.frameComplementares)
        self.lineInfo.setGeometry(QtCore.QRect(320, 50, 300, 1))
        self.lineInfo.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.lineInfo.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineInfo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineInfo.setObjectName("lineInfo")
        self.lblTelefone = QtWidgets.QLabel(self.frameComplementares)
        self.lblTelefone.setGeometry(QtCore.QRect(740, 60, 91, 23))
        self.lblTelefone.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTelefone.setObjectName("lblTelefone")
        self.lineEmail = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineEmail.setGeometry(QtCore.QRect(230, 90, 491, 28))
        self.lineEmail.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEmail.setReadOnly(True)
        self.lineEmail.setObjectName("lineEmail")
        self.lineTelefone = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineTelefone.setGeometry(QtCore.QRect(740, 90, 161, 28))
        self.lineTelefone.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineTelefone.setReadOnly(True)
        self.lineTelefone.setObjectName("lineTelefone")
        self.btnMaterias = QtWidgets.QPushButton(self.frameComplementares)
        self.btnMaterias.setGeometry(QtCore.QRect(10, 90, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMaterias.sizePolicy().hasHeightForWidth())
        self.btnMaterias.setSizePolicy(sizePolicy)
        self.btnMaterias.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnMaterias.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnMaterias.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 123, 28);\n"
"box-shadow: 5px -9px 3px #000;\n"
"")
        self.btnMaterias.setObjectName("btnMaterias")
        self.frameLaranja = QtWidgets.QFrame(self.framezao)
        self.frameLaranja.setGeometry(QtCore.QRect(0, 0, 931, 9))
        self.frameLaranja.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"border-radius: 0.2px;\n"
"")
        self.frameLaranja.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLaranja.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLaranja.setObjectName("frameLaranja")
        self.frameLaranja.raise_()
        self.framePessoais.raise_()
        self.frameEndereco.raise_()
        self.frameComplementares.raise_()
        self.framezao.raise_()
        self.btnCancelar.raise_()
        perfilProfessor.setCentralWidget(self.centralwidget)

        self.retranslateUi(perfilProfessor)
        self.cbEstadoCivil.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(perfilProfessor)

    def retranslateUi(self, perfilProfessor):
        _translate = QtCore.QCoreApplication.translate
        perfilProfessor.setWindowTitle(_translate("perfilProfessor", "Perfil Professor"))
        self.btnCancelar.setText(_translate("perfilProfessor", "Cancelar"))
        self.lblPessoais.setText(_translate("perfilProfessor", "Informações Pessoais"))
        self.lblNome.setText(_translate("perfilProfessor", "Nome Completo"))
        self.lblCpf.setText(_translate("perfilProfessor", "CPF"))
        self.lblEstadoCivil.setText(_translate("perfilProfessor", "Estado Civil"))
        self.lblNascimento.setText(_translate("perfilProfessor", "Nascimento"))
        self.lblRg.setText(_translate("perfilProfessor", "RG"))
        self.cbEstadoCivil.setItemText(0, _translate("perfilProfessor", "Solteiro(a)"))
        self.cbEstadoCivil.setItemText(1, _translate("perfilProfessor", "Casado(a)"))
        self.cbEstadoCivil.setItemText(2, _translate("perfilProfessor", "Separado(a)"))
        self.cbEstadoCivil.setItemText(3, _translate("perfilProfessor", "Divorciado(a)"))
        self.cbEstadoCivil.setItemText(4, _translate("perfilProfessor", "Viúvo(a)"))
        self.lblSexo.setText(_translate("perfilProfessor", "Sexo"))
        self.cbSexo.setItemText(0, _translate("perfilProfessor", "Feminino"))
        self.cbSexo.setItemText(1, _translate("perfilProfessor", "Masculino"))
        self.cbSexo.setItemText(2, _translate("perfilProfessor", "Outro"))
        self.lblFotolbl.setText(_translate("perfilProfessor", "Foto"))
        self.lineCpf.setInputMask(_translate("perfilProfessor", "000.000.000-00"))
        self.lineRg.setText(_translate("perfilProfessor", "Mayara"))
        self.lblEndereco.setText(_translate("perfilProfessor", "Endereço"))
        self.lblRua.setText(_translate("perfilProfessor", "Rua"))
        self.lblNum.setText(_translate("perfilProfessor", "Número"))
        self.lblBairro.setText(_translate("perfilProfessor", "Bairro"))
        self.lblCep.setText(_translate("perfilProfessor", "CEP"))
        self.lblCidade.setText(_translate("perfilProfessor", "Cidade"))
        self.lblEstado.setText(_translate("perfilProfessor", "Estado"))
        self.cbEstado.setItemText(0, _translate("perfilProfessor", "Acre (AC)"))
        self.cbEstado.setItemText(1, _translate("perfilProfessor", "Alagoas (AL)"))
        self.cbEstado.setItemText(2, _translate("perfilProfessor", "Amapá (AP)"))
        self.cbEstado.setItemText(3, _translate("perfilProfessor", "Amazonas (AM)"))
        self.cbEstado.setItemText(4, _translate("perfilProfessor", "Bahia (BA)"))
        self.cbEstado.setItemText(5, _translate("perfilProfessor", "Ceará (CE)"))
        self.cbEstado.setItemText(6, _translate("perfilProfessor", "Distrito Federal (DF)"))
        self.cbEstado.setItemText(7, _translate("perfilProfessor", "Espírito Santos (ES)"))
        self.cbEstado.setItemText(8, _translate("perfilProfessor", "Goiás (GO)"))
        self.cbEstado.setItemText(9, _translate("perfilProfessor", "Maranhão (MA)"))
        self.cbEstado.setItemText(10, _translate("perfilProfessor", "Mato Grosso (MT)"))
        self.cbEstado.setItemText(11, _translate("perfilProfessor", "Mato Grosso do Sul (MS)"))
        self.cbEstado.setItemText(12, _translate("perfilProfessor", "Minas Gerais (MG)"))
        self.cbEstado.setItemText(13, _translate("perfilProfessor", "Pará (PA)"))
        self.cbEstado.setItemText(14, _translate("perfilProfessor", "Paraíba (PB)"))
        self.cbEstado.setItemText(15, _translate("perfilProfessor", "Paraná (PR)"))
        self.cbEstado.setItemText(16, _translate("perfilProfessor", "Pernambuco (PR)"))
        self.cbEstado.setItemText(17, _translate("perfilProfessor", "Piauí (PI)"))
        self.cbEstado.setItemText(18, _translate("perfilProfessor", "Rio de Janeiro (RJ)"))
        self.cbEstado.setItemText(19, _translate("perfilProfessor", "Rio Grande do Norte (RN)"))
        self.cbEstado.setItemText(20, _translate("perfilProfessor", "Rondônia (RO)"))
        self.cbEstado.setItemText(21, _translate("perfilProfessor", "Roraima (RR)"))
        self.cbEstado.setItemText(22, _translate("perfilProfessor", "Santa Catarina (SC)"))
        self.cbEstado.setItemText(23, _translate("perfilProfessor", "São Paulo (SP)"))
        self.cbEstado.setItemText(24, _translate("perfilProfessor", "Sergipe (SE)"))
        self.cbEstado.setItemText(25, _translate("perfilProfessor", "Tocantins (TO)"))
        self.lineCep.setInputMask(_translate("perfilProfessor", "00000-000"))
        self.lblInfoComplementares.setText(_translate("perfilProfessor", "Informações Complementares"))
        self.lblMaterias.setText(_translate("perfilProfessor", "Matérias"))
        self.lblEmail.setText(_translate("perfilProfessor", "Email"))
        self.lblTelefone.setText(_translate("perfilProfessor", "Telefone"))
        self.lineTelefone.setInputMask(_translate("perfilProfessor", "(00) 0 0000-0000"))
        self.btnMaterias.setText(_translate("perfilProfessor", "Ver Matérias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    perfilProfessor = QtWidgets.QMainWindow()
    ui = Ui_perfilProfessor()
    ui.setupUi(perfilProfessor)
    perfilProfessor.show()
    sys.exit(app.exec_())

