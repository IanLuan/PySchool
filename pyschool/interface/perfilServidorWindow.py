# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perfilServidor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_perfilServidor(object):
    def setupUi(self, perfilServidor):
        perfilServidor.setObjectName("perfilServidor")
        perfilServidor.resize(952, 647)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(perfilServidor.sizePolicy().hasHeightForWidth())
        perfilServidor.setSizePolicy(sizePolicy)
        perfilServidor.setMinimumSize(QtCore.QSize(952, 200))
        perfilServidor.setMaximumSize(QtCore.QSize(952, 760))
        perfilServidor.setLayoutDirection(QtCore.Qt.LeftToRight)
        perfilServidor.setStyleSheet("background-color: rgb(21, 143, 181)")
        self.centralwidget = QtWidgets.QWidget(perfilServidor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("backgroundcolor: rgb(255,255,255)")
        self.centralwidget.setObjectName("centralwidget")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(10, 610, 111, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVoltar.sizePolicy().hasHeightForWidth())
        self.btnVoltar.setSizePolicy(sizePolicy)
        self.btnVoltar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnVoltar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 5px -9px 3px #000;")
        self.btnVoltar.setObjectName("btnVoltar")
        self.framezao = QtWidgets.QFrame(self.centralwidget)
        self.framezao.setGeometry(QtCore.QRect(10, 0, 931, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framezao.sizePolicy().hasHeightForWidth())
        self.framezao.setSizePolicy(sizePolicy)
        self.framezao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")
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
        self.linePessoais = QtWidgets.QFrame(self.framePessoais)
        self.linePessoais.setGeometry(QtCore.QRect(320, 32, 300, 1))
        self.linePessoais.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.linePessoais.setFrameShape(QtWidgets.QFrame.HLine)
        self.linePessoais.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linePessoais.setObjectName("linePessoais")
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
        self.lblNumero = QtWidgets.QLabel(self.frameEndereco)
        self.lblNumero.setGeometry(QtCore.QRect(740, 50, 71, 16))
        self.lblNumero.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblNumero.setObjectName("lblNumero")
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
        self.lblNumero.raise_()
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
        self.frameComplementares.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frameComplementares.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameComplementares.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameComplementares.setObjectName("frameComplementares")
        self.lblInfoComplementares = QtWidgets.QLabel(self.frameComplementares)
        self.lblInfoComplementares.setGeometry(QtCore.QRect(0, 10, 931, 41))
        self.lblInfoComplementares.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblInfoComplementares.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfoComplementares.setObjectName("lblInfoComplementares")
        self.lblCargo = QtWidgets.QLabel(self.frameComplementares)
        self.lblCargo.setGeometry(QtCore.QRect(740, 60, 55, 23))
        self.lblCargo.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblCargo.setObjectName("lblCargo")
        self.lblEmail = QtWidgets.QLabel(self.frameComplementares)
        self.lblEmail.setGeometry(QtCore.QRect(10, 60, 55, 23))
        self.lblEmail.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblEmail.setObjectName("lblEmail")
        self.cbCargo = QtWidgets.QComboBox(self.frameComplementares)
        self.cbCargo.setEnabled(False)
        self.cbCargo.setGeometry(QtCore.QRect(740, 90, 171, 28))
        self.cbCargo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbCargo.setObjectName("cbCargo")
        self.lineInfo = QtWidgets.QFrame(self.frameComplementares)
        self.lineInfo.setGeometry(QtCore.QRect(320, 50, 300, 1))
        self.lineInfo.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.lineInfo.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineInfo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineInfo.setObjectName("lineInfo")
        self.lblTelefone = QtWidgets.QLabel(self.frameComplementares)
        self.lblTelefone.setGeometry(QtCore.QRect(470, 60, 91, 23))
        self.lblTelefone.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTelefone.setObjectName("lblTelefone")
        self.lineEmail = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineEmail.setGeometry(QtCore.QRect(10, 90, 431, 28))
        self.lineEmail.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEmail.setReadOnly(True)
        self.lineEmail.setObjectName("lineEmail")
        self.lineTelefone = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineTelefone.setGeometry(QtCore.QRect(470, 90, 251, 28))
        self.lineTelefone.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineTelefone.setReadOnly(True)
        self.lineTelefone.setObjectName("lineTelefone")
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
        self.btnVoltar.raise_()
        perfilServidor.setCentralWidget(self.centralwidget)

        self.retranslateUi(perfilServidor)
        self.cbEstadoCivil.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(perfilServidor)

    def retranslateUi(self, perfilServidor):
        _translate = QtCore.QCoreApplication.translate
        perfilServidor.setWindowTitle(_translate("perfilServidor", "Perfil Servidor"))
        self.btnVoltar.setText(_translate("perfilServidor", "Voltar"))
        self.lblPessoais.setText(_translate("perfilServidor", "Informações Pessoais"))
        self.lblNome.setText(_translate("perfilServidor", "Nome Completo"))
        self.lblCpf.setText(_translate("perfilServidor", "CPF"))
        self.lblEstadoCivil.setText(_translate("perfilServidor", "Estado Civil"))
        self.lblNascimento.setText(_translate("perfilServidor", "Nascimento"))
        self.lblRg.setText(_translate("perfilServidor", "RG"))
        self.cbEstadoCivil.setItemText(0, _translate("perfilServidor", "Solteiro(a)"))
        self.cbEstadoCivil.setItemText(1, _translate("perfilServidor", "Casado(a)"))
        self.cbEstadoCivil.setItemText(2, _translate("perfilServidor", "Separado(a)"))
        self.cbEstadoCivil.setItemText(3, _translate("perfilServidor", "Divorciado(a)"))
        self.cbEstadoCivil.setItemText(4, _translate("perfilServidor", "Viúvo(a)"))
        self.lblSexo.setText(_translate("perfilServidor", "Sexo"))
        self.cbSexo.setItemText(0, _translate("perfilServidor", "Feminino"))
        self.cbSexo.setItemText(1, _translate("perfilServidor", "Masculino"))
        self.cbSexo.setItemText(2, _translate("perfilServidor", "Outro"))
        self.lblFotolbl.setText(_translate("perfilServidor", "Foto"))
        self.lineCpf.setInputMask(_translate("perfilServidor", "000.000.000-00"))
        self.lblEndereco.setText(_translate("perfilServidor", "Endereço"))
        self.lblRua.setText(_translate("perfilServidor", "Rua"))
        self.lblNumero.setText(_translate("perfilServidor", "Número"))
        self.lblBairro.setText(_translate("perfilServidor", "Bairro"))
        self.lblCep.setText(_translate("perfilServidor", "CEP"))
        self.lblCidade.setText(_translate("perfilServidor", "Cidade"))
        self.lblEstado.setText(_translate("perfilServidor", "Estado"))
        self.cbEstado.setItemText(0, _translate("perfilServidor", "Acre (AC)"))
        self.cbEstado.setItemText(1, _translate("perfilServidor", "Alagoas (AL)"))
        self.cbEstado.setItemText(2, _translate("perfilServidor", "Amapá (AP)"))
        self.cbEstado.setItemText(3, _translate("perfilServidor", "Amazonas (AM)"))
        self.cbEstado.setItemText(4, _translate("perfilServidor", "Bahia (BA)"))
        self.cbEstado.setItemText(5, _translate("perfilServidor", "Ceará (CE)"))
        self.cbEstado.setItemText(6, _translate("perfilServidor", "Distrito Federal (DF)"))
        self.cbEstado.setItemText(7, _translate("perfilServidor", "Espírito Santos (ES)"))
        self.cbEstado.setItemText(8, _translate("perfilServidor", "Goiás (GO)"))
        self.cbEstado.setItemText(9, _translate("perfilServidor", "Maranhão (MA)"))
        self.cbEstado.setItemText(10, _translate("perfilServidor", "Mato Grosso (MT)"))
        self.cbEstado.setItemText(11, _translate("perfilServidor", "Mato Grosso do Sul (MS)"))
        self.cbEstado.setItemText(12, _translate("perfilServidor", "Minas Gerais (MG)"))
        self.cbEstado.setItemText(13, _translate("perfilServidor", "Pará (PA)"))
        self.cbEstado.setItemText(14, _translate("perfilServidor", "Paraíba (PB)"))
        self.cbEstado.setItemText(15, _translate("perfilServidor", "Paraná (PR)"))
        self.cbEstado.setItemText(16, _translate("perfilServidor", "Pernambuco (PR)"))
        self.cbEstado.setItemText(17, _translate("perfilServidor", "Piauí (PI)"))
        self.cbEstado.setItemText(18, _translate("perfilServidor", "Rio de Janeiro (RJ)"))
        self.cbEstado.setItemText(19, _translate("perfilServidor", "Rio Grande do Norte (RN)"))
        self.cbEstado.setItemText(20, _translate("perfilServidor", "Rondônia (RO)"))
        self.cbEstado.setItemText(21, _translate("perfilServidor", "Roraima (RR)"))
        self.cbEstado.setItemText(22, _translate("perfilServidor", "Santa Catarina (SC)"))
        self.cbEstado.setItemText(23, _translate("perfilServidor", "São Paulo (SP)"))
        self.cbEstado.setItemText(24, _translate("perfilServidor", "Sergipe (SE)"))
        self.cbEstado.setItemText(25, _translate("perfilServidor", "Tocantins (TO)"))
        self.lineCep.setInputMask(_translate("perfilServidor", "00000-000"))
        self.lblInfoComplementares.setText(_translate("perfilServidor", "Informações Complementares"))
        self.lblCargo.setText(_translate("perfilServidor", "Cargo"))
        self.lblEmail.setText(_translate("perfilServidor", "Email"))
        self.lblTelefone.setText(_translate("perfilServidor", "Telefone"))
        self.lineTelefone.setInputMask(_translate("perfilServidor", "(00) 0 0000-0000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    perfilServidor = QtWidgets.QMainWindow()
    ui = Ui_perfilServidor()
    ui.setupUi(perfilServidor)
    perfilServidor.show()
    sys.exit(app.exec_())
