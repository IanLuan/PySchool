# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matricula.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_matricularAluno(object):
    def setupUi(self, matricularAluno):
        matricularAluno.setObjectName("matricularAluno")
        matricularAluno.resize(952, 685)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(matricularAluno.sizePolicy().hasHeightForWidth())
        matricularAluno.setSizePolicy(sizePolicy)
        matricularAluno.setMinimumSize(QtCore.QSize(952, 685))
        matricularAluno.setMaximumSize(QtCore.QSize(952, 760))
        matricularAluno.setLayoutDirection(QtCore.Qt.LeftToRight)
        matricularAluno.setStyleSheet("background-color: rgb(21, 143, 181)")
        self.centralwidget = QtWidgets.QWidget(matricularAluno)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("backgroundcolor: rgb(255,255,255)")
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadatrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadatrar.setGeometry(QtCore.QRect(830, 640, 111, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCadatrar.sizePolicy().hasHeightForWidth())
        self.btnCadatrar.setSizePolicy(sizePolicy)
        self.btnCadatrar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCadatrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCadatrar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 123, 28);\n"
"box-shadow: 5px -9px 3px #000;\n"
"")
        self.btnCadatrar.setObjectName("btnCadatrar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(10, 640, 111, 30))
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
        self.framezao.setGeometry(QtCore.QRect(10, 0, 931, 627))
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
        self.framePessoais.setGeometry(QtCore.QRect(0, 10, 931, 273))
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
        self.lblPessoais.setGeometry(QtCore.QRect(0, -4, 931, 31))
        self.lblPessoais.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblPessoais.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPessoais.setObjectName("lblPessoais")
        self.lblNome = QtWidgets.QLabel(self.framePessoais)
        self.lblNome.setGeometry(QtCore.QRect(10, 24, 181, 23))
        self.lblNome.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblNome.setObjectName("lblNome")
        self.lblCpf = QtWidgets.QLabel(self.framePessoais)
        self.lblCpf.setGeometry(QtCore.QRect(10, 84, 55, 23))
        self.lblCpf.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblCpf.setObjectName("lblCpf")
        self.lblEstadoCivil = QtWidgets.QLabel(self.framePessoais)
        self.lblEstadoCivil.setGeometry(QtCore.QRect(10, 152, 111, 23))
        self.lblEstadoCivil.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblEstadoCivil.setObjectName("lblEstadoCivil")
        self.lblNascimento = QtWidgets.QLabel(self.framePessoais)
        self.lblNascimento.setGeometry(QtCore.QRect(740, 152, 121, 23))
        self.lblNascimento.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblNascimento.setObjectName("lblNascimento")
        self.lblRg = QtWidgets.QLabel(self.framePessoais)
        self.lblRg.setGeometry(QtCore.QRect(470, 84, 55, 23))
        self.lblRg.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblRg.setTextFormat(QtCore.Qt.PlainText)
        self.lblRg.setObjectName("lblRg")
        self.cbEstadoCivil = QtWidgets.QComboBox(self.framePessoais)
        self.cbEstadoCivil.setGeometry(QtCore.QRect(10, 182, 431, 28))
        self.cbEstadoCivil.setStyleSheet("QComboBox {\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}")
        self.cbEstadoCivil.setMaxVisibleItems(5)
        self.cbEstadoCivil.setObjectName("cbEstadoCivil")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.cbEstadoCivil.addItem("")
        self.dateNascimento = QtWidgets.QDateEdit(self.framePessoais)
        self.dateNascimento.setGeometry(QtCore.QRect(740, 182, 171, 28))
        self.dateNascimento.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateNascimento.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateNascimento.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateNascimento.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.dateNascimento.setObjectName("dateNascimento")
        self.lblSexo = QtWidgets.QLabel(self.framePessoais)
        self.lblSexo.setGeometry(QtCore.QRect(470, 152, 55, 31))
        self.lblSexo.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblSexo.setObjectName("lblSexo")
        self.cbSexo = QtWidgets.QComboBox(self.framePessoais)
        self.cbSexo.setGeometry(QtCore.QRect(470, 182, 251, 28))
        self.cbSexo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.lineInfo = QtWidgets.QFrame(self.framePessoais)
        self.lineInfo.setGeometry(QtCore.QRect(320, 26, 300, 1))
        self.lineInfo.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.lineInfo.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineInfo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineInfo.setObjectName("lineInfo")
        self.lblFotolbl = QtWidgets.QLabel(self.framePessoais)
        self.lblFotolbl.setGeometry(QtCore.QRect(740, 16, 40, 23))
        self.lblFotolbl.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblFotolbl.setObjectName("lblFotolbl")
        self.lineNome = QtWidgets.QLineEdit(self.framePessoais)
        self.lineNome.setGeometry(QtCore.QRect(10, 54, 711, 28))
        self.lineNome.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineNome.setObjectName("lineNome")
        self.lineCpf = QtWidgets.QLineEdit(self.framePessoais)
        self.lineCpf.setGeometry(QtCore.QRect(10, 112, 431, 28))
        self.lineCpf.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCpf.setObjectName("lineCpf")
        self.lineRg = QtWidgets.QLineEdit(self.framePessoais)
        self.lineRg.setGeometry(QtCore.QRect(470, 112, 251, 28))
        self.lineRg.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRg.setObjectName("lineRg")
        self.lblFoto = QtWidgets.QLabel(self.framePessoais)
        self.lblFoto.setGeometry(QtCore.QRect(790, 11, 121, 141))
        self.lblFoto.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"")
        self.lblFoto.setText("")
        self.lblFoto.setObjectName("lblFoto")
        self.lblSerie = QtWidgets.QLabel(self.framePessoais)
        self.lblSerie.setGeometry(QtCore.QRect(150, 210, 55, 31))
        self.lblSerie.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblSerie.setObjectName("lblSerie")
        self.cbSerie = QtWidgets.QComboBox(self.framePessoais)
        self.cbSerie.setGeometry(QtCore.QRect(150, 240, 191, 28))
        self.cbSerie.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbSerie.setCurrentText("")
        self.cbSerie.setFrame(True)
        self.cbSerie.setObjectName("cbSerie")
        self.lblTipoSanguineo = QtWidgets.QLabel(self.framePessoais)
        self.lblTipoSanguineo.setGeometry(QtCore.QRect(10, 210, 125, 31))
        self.lblTipoSanguineo.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTipoSanguineo.setObjectName("lblTipoSanguineo")
        self.cbTipoSanguineo = QtWidgets.QComboBox(self.framePessoais)
        self.cbTipoSanguineo.setGeometry(QtCore.QRect(10, 240, 121, 28))
        self.cbTipoSanguineo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbTipoSanguineo.setObjectName("cbTipoSanguineo")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.cbTipoSanguineo.addItem("")
        self.lblTelefone = QtWidgets.QLabel(self.framePessoais)
        self.lblTelefone.setGeometry(QtCore.QRect(740, 210, 105, 31))
        self.lblTelefone.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTelefone.setObjectName("lblTelefone")
        self.lineTelefoneAluno = QtWidgets.QLineEdit(self.framePessoais)
        self.lineTelefoneAluno.setGeometry(QtCore.QRect(740, 240, 171, 28))
        self.lineTelefoneAluno.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefoneAluno.setObjectName("lineTelefoneAluno")
        self.lblEmail = QtWidgets.QLabel(self.framePessoais)
        self.lblEmail.setGeometry(QtCore.QRect(470, 210, 105, 31))
        self.lblEmail.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblEmail.setObjectName("lblEmail")
        self.lineEmail = QtWidgets.QLineEdit(self.framePessoais)
        self.lineEmail.setGeometry(QtCore.QRect(470, 240, 251, 28))
        self.lineEmail.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEmail.setText("")
        self.lineEmail.setObjectName("lineEmail")
        self.lblGrupo = QtWidgets.QLabel(self.framePessoais)
        self.lblGrupo.setGeometry(QtCore.QRect(350, 210, 55, 31))
        self.lblGrupo.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblGrupo.setObjectName("lblGrupo")
        self.cbGrupo = QtWidgets.QComboBox(self.framePessoais)
        self.cbGrupo.setGeometry(QtCore.QRect(350, 240, 91, 28))
        self.cbGrupo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbGrupo.setCurrentText("")
        self.cbGrupo.setFrame(True)
        self.cbGrupo.setObjectName("cbGrupo")
        self.frameEndereco = QtWidgets.QFrame(self.framezao)
        self.frameEndereco.setGeometry(QtCore.QRect(0, 474, 931, 303))
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
        self.lblRua.setGeometry(QtCore.QRect(10, 39, 55, 16))
        self.lblRua.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblRua.setObjectName("lblRua")
        self.lblNumero = QtWidgets.QLabel(self.frameEndereco)
        self.lblNumero.setGeometry(QtCore.QRect(740, 42, 71, 16))
        self.lblNumero.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblNumero.setObjectName("lblNumero")
        self.lblBairro = QtWidgets.QLabel(self.frameEndereco)
        self.lblBairro.setGeometry(QtCore.QRect(10, 97, 55, 16))
        self.lblBairro.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblBairro.setObjectName("lblBairro")
        self.lblCep = QtWidgets.QLabel(self.frameEndereco)
        self.lblCep.setGeometry(QtCore.QRect(470, 39, 55, 16))
        self.lblCep.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblCep.setObjectName("lblCep")
        self.lblCidade = QtWidgets.QLabel(self.frameEndereco)
        self.lblCidade.setGeometry(QtCore.QRect(470, 97, 55, 16))
        self.lblCidade.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblCidade.setObjectName("lblCidade")
        self.lblEstado = QtWidgets.QLabel(self.frameEndereco)
        self.lblEstado.setGeometry(QtCore.QRect(740, 102, 55, 16))
        self.lblEstado.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.lblEstado.setObjectName("lblEstado")
        self.lineRua = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineRua.setGeometry(QtCore.QRect(10, 62, 431, 28))
        self.lineRua.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRua.setObjectName("lineRua")
        self.spinNumero = QtWidgets.QSpinBox(self.frameEndereco)
        self.spinNumero.setGeometry(QtCore.QRect(740, 62, 171, 28))
        self.spinNumero.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.spinNumero.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinNumero.setMaximum(5000)
        self.spinNumero.setObjectName("spinNumero")
        self.cbEstado = QtWidgets.QComboBox(self.frameEndereco)
        self.cbEstado.setGeometry(QtCore.QRect(740, 122, 171, 28))
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
        self.lineBairro.setGeometry(QtCore.QRect(10, 122, 431, 28))
        self.lineBairro.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineBairro.setObjectName("lineBairro")
        self.lineCep = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCep.setGeometry(QtCore.QRect(470, 62, 251, 28))
        self.lineCep.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCep.setObjectName("lineCep")
        self.lineCidade = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCidade.setGeometry(QtCore.QRect(470, 122, 251, 28))
        self.lineCidade.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
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
        self.frameLaranja = QtWidgets.QFrame(self.framezao)
        self.frameLaranja.setGeometry(QtCore.QRect(0, 0, 931, 9))
        self.frameLaranja.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"border-radius: 0.2px;\n"
"")
        self.frameLaranja.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLaranja.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLaranja.setObjectName("frameLaranja")
        self.framePais = QtWidgets.QFrame(self.framezao)
        self.framePais.setGeometry(QtCore.QRect(0, 280, 931, 199))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePais.sizePolicy().hasHeightForWidth())
        self.framePais.setSizePolicy(sizePolicy)
        self.framePais.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.framePais.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.framePais.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePais.setObjectName("framePais")
        self.lblPais = QtWidgets.QLabel(self.framePais)
        self.lblPais.setGeometry(QtCore.QRect(0, 10, 931, 31))
        self.lblPais.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.lblPais.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPais.setObjectName("lblPais")
        self.linePais = QtWidgets.QFrame(self.framePais)
        self.linePais.setGeometry(QtCore.QRect(320, 40, 300, 1))
        self.linePais.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.linePais.setFrameShape(QtWidgets.QFrame.HLine)
        self.linePais.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.linePais.setObjectName("linePais")
        self.lblNomePai = QtWidgets.QLabel(self.framePais)
        self.lblNomePai.setGeometry(QtCore.QRect(10, 50, 181, 23))
        self.lblNomePai.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblNomePai.setObjectName("lblNomePai")
        self.lineNomePai = QtWidgets.QLineEdit(self.framePais)
        self.lineNomePai.setGeometry(QtCore.QRect(10, 80, 431, 28))
        self.lineNomePai.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineNomePai.setObjectName("lineNomePai")
        self.lineNomeMae = QtWidgets.QLineEdit(self.framePais)
        self.lineNomeMae.setGeometry(QtCore.QRect(10, 150, 431, 28))
        self.lineNomeMae.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineNomeMae.setObjectName("lineNomeMae")
        self.lblNomeMae = QtWidgets.QLabel(self.framePais)
        self.lblNomeMae.setGeometry(QtCore.QRect(10, 120, 181, 23))
        self.lblNomeMae.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblNomeMae.setObjectName("lblNomeMae")
        self.lineCpfPai = QtWidgets.QLineEdit(self.framePais)
        self.lineCpfPai.setGeometry(QtCore.QRect(470, 80, 251, 28))
        self.lineCpfPai.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCpfPai.setObjectName("lineCpfPai")
        self.lblCpfPai = QtWidgets.QLabel(self.framePais)
        self.lblCpfPai.setGeometry(QtCore.QRect(470, 50, 181, 23))
        self.lblCpfPai.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblCpfPai.setObjectName("lblCpfPai")
        self.lblCpfMae = QtWidgets.QLabel(self.framePais)
        self.lblCpfMae.setGeometry(QtCore.QRect(470, 120, 181, 23))
        self.lblCpfMae.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.lblCpfMae.setObjectName("lblCpfMae")
        self.lineCpfMae = QtWidgets.QLineEdit(self.framePais)
        self.lineCpfMae.setGeometry(QtCore.QRect(470, 150, 251, 28))
        self.lineCpfMae.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCpfMae.setObjectName("lineCpfMae")
        self.lblTelefonePai = QtWidgets.QLabel(self.framePais)
        self.lblTelefonePai.setGeometry(QtCore.QRect(740, 50, 123, 23))
        self.lblTelefonePai.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTelefonePai.setObjectName("lblTelefonePai")
        self.lineTelefonePai = QtWidgets.QLineEdit(self.framePais)
        self.lineTelefonePai.setGeometry(QtCore.QRect(740, 80, 171, 28))
        self.lineTelefonePai.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefonePai.setObjectName("lineTelefonePai")
        self.lineTelefoneMae = QtWidgets.QLineEdit(self.framePais)
        self.lineTelefoneMae.setGeometry(QtCore.QRect(740, 150, 171, 28))
        self.lineTelefoneMae.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefoneMae.setObjectName("lineTelefoneMae")
        self.lblTelefoneMae = QtWidgets.QLabel(self.framePais)
        self.lblTelefoneMae.setGeometry(QtCore.QRect(740, 120, 139, 23))
        self.lblTelefoneMae.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.lblTelefoneMae.setObjectName("lblTelefoneMae")
        self.frameLaranja.raise_()
        self.framePessoais.raise_()
        self.frameEndereco.raise_()
        self.framePais.raise_()
        self.framezao.raise_()
        self.btnCadatrar.raise_()
        self.btnCancelar.raise_()
        matricularAluno.setCentralWidget(self.centralwidget)

        self.retranslateUi(matricularAluno)
        self.cbEstadoCivil.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(matricularAluno)

    def retranslateUi(self, matricularAluno):
        _translate = QtCore.QCoreApplication.translate
        matricularAluno.setWindowTitle(_translate("matricularAluno", "Matricular Aluno"))
        self.btnCadatrar.setText(_translate("matricularAluno", "Matricular"))
        self.btnCancelar.setText(_translate("matricularAluno", "Cancelar"))
        self.lblPessoais.setText(_translate("matricularAluno", "Informações do Aluno"))
        self.lblNome.setText(_translate("matricularAluno", "Nome Completo"))
        self.lblCpf.setText(_translate("matricularAluno", "CPF"))
        self.lblEstadoCivil.setText(_translate("matricularAluno", "Estado Civil"))
        self.lblNascimento.setText(_translate("matricularAluno", "Nascimento"))
        self.lblRg.setText(_translate("matricularAluno", "RG"))
        self.cbEstadoCivil.setItemText(0, _translate("matricularAluno", "Solteiro(a)"))
        self.cbEstadoCivil.setItemText(1, _translate("matricularAluno", "Casado(a)"))
        self.cbEstadoCivil.setItemText(2, _translate("matricularAluno", "Separado(a)"))
        self.cbEstadoCivil.setItemText(3, _translate("matricularAluno", "Divorciado(a)"))
        self.cbEstadoCivil.setItemText(4, _translate("matricularAluno", "Viúvo(a)"))
        self.lblSexo.setText(_translate("matricularAluno", "Sexo"))
        self.cbSexo.setItemText(0, _translate("matricularAluno", "Feminino"))
        self.cbSexo.setItemText(1, _translate("matricularAluno", "Masculino"))
        self.cbSexo.setItemText(2, _translate("matricularAluno", "Outro"))
        self.lblFotolbl.setText(_translate("matricularAluno", "Foto"))
        self.lineCpf.setInputMask(_translate("matricularAluno", "000.000.000-00"))
        self.lblSerie.setText(_translate("matricularAluno", "Série"))
        self.lblTipoSanguineo.setText(_translate("matricularAluno", "Tipo Sanguíneo"))
        self.cbTipoSanguineo.setCurrentText(_translate("matricularAluno", "A+"))
        self.cbTipoSanguineo.setItemText(0, _translate("matricularAluno", "A+"))
        self.cbTipoSanguineo.setItemText(1, _translate("matricularAluno", "A-"))
        self.cbTipoSanguineo.setItemText(2, _translate("matricularAluno", "B+"))
        self.cbTipoSanguineo.setItemText(3, _translate("matricularAluno", "B-"))
        self.cbTipoSanguineo.setItemText(4, _translate("matricularAluno", "AB+"))
        self.cbTipoSanguineo.setItemText(5, _translate("matricularAluno", "AB-"))
        self.cbTipoSanguineo.setItemText(6, _translate("matricularAluno", "O+"))
        self.cbTipoSanguineo.setItemText(7, _translate("matricularAluno", "O-"))
        self.lblTelefone.setText(_translate("matricularAluno", "Telefone"))
        self.lineTelefoneAluno.setInputMask(_translate("matricularAluno", "(00)00000-0000"))
        self.lineTelefoneAluno.setText(_translate("matricularAluno", "()-"))
        self.lblEmail.setText(_translate("matricularAluno", "Email"))
        self.lblGrupo.setText(_translate("matricularAluno", "Grupo"))
        self.lblEndereco.setText(_translate("matricularAluno", "Endereço do Aluno"))
        self.lblRua.setText(_translate("matricularAluno", "Rua"))
        self.lblNumero.setText(_translate("matricularAluno", "Número"))
        self.lblBairro.setText(_translate("matricularAluno", "Bairro"))
        self.lblCep.setText(_translate("matricularAluno", "CEP"))
        self.lblCidade.setText(_translate("matricularAluno", "Cidade"))
        self.lblEstado.setText(_translate("matricularAluno", "Estado"))
        self.cbEstado.setItemText(0, _translate("matricularAluno", "Acre (AC)"))
        self.cbEstado.setItemText(1, _translate("matricularAluno", "Alagoas (AL)"))
        self.cbEstado.setItemText(2, _translate("matricularAluno", "Amapá (AP)"))
        self.cbEstado.setItemText(3, _translate("matricularAluno", "Amazonas (AM)"))
        self.cbEstado.setItemText(4, _translate("matricularAluno", "Bahia (BA)"))
        self.cbEstado.setItemText(5, _translate("matricularAluno", "Ceará (CE)"))
        self.cbEstado.setItemText(6, _translate("matricularAluno", "Distrito Federal (DF)"))
        self.cbEstado.setItemText(7, _translate("matricularAluno", "Espírito Santos (ES)"))
        self.cbEstado.setItemText(8, _translate("matricularAluno", "Goiás (GO)"))
        self.cbEstado.setItemText(9, _translate("matricularAluno", "Maranhão (MA)"))
        self.cbEstado.setItemText(10, _translate("matricularAluno", "Mato Grosso (MT)"))
        self.cbEstado.setItemText(11, _translate("matricularAluno", "Mato Grosso do Sul (MS)"))
        self.cbEstado.setItemText(12, _translate("matricularAluno", "Minas Gerais (MG)"))
        self.cbEstado.setItemText(13, _translate("matricularAluno", "Pará (PA)"))
        self.cbEstado.setItemText(14, _translate("matricularAluno", "Paraíba (PB)"))
        self.cbEstado.setItemText(15, _translate("matricularAluno", "Paraná (PR)"))
        self.cbEstado.setItemText(16, _translate("matricularAluno", "Pernambuco (PR)"))
        self.cbEstado.setItemText(17, _translate("matricularAluno", "Piauí (PI)"))
        self.cbEstado.setItemText(18, _translate("matricularAluno", "Rio de Janeiro (RJ)"))
        self.cbEstado.setItemText(19, _translate("matricularAluno", "Rio Grande do Norte (RN)"))
        self.cbEstado.setItemText(20, _translate("matricularAluno", "Rondônia (RO)"))
        self.cbEstado.setItemText(21, _translate("matricularAluno", "Roraima (RR)"))
        self.cbEstado.setItemText(22, _translate("matricularAluno", "Santa Catarina (SC)"))
        self.cbEstado.setItemText(23, _translate("matricularAluno", "São Paulo (SP)"))
        self.cbEstado.setItemText(24, _translate("matricularAluno", "Sergipe (SE)"))
        self.cbEstado.setItemText(25, _translate("matricularAluno", "Tocantins (TO)"))
        self.lineCep.setInputMask(_translate("matricularAluno", "00000-000"))
        self.lblPais.setText(_translate("matricularAluno", "Informações dos Pais"))
        self.lblNomePai.setText(_translate("matricularAluno", "Nome do Pai"))
        self.lblNomeMae.setText(_translate("matricularAluno", "Nome da Mãe"))
        self.lineCpfPai.setInputMask(_translate("matricularAluno", "000.000.000-00"))
        self.lineCpfPai.setText(_translate("matricularAluno", "..-"))
        self.lblCpfPai.setText(_translate("matricularAluno", "CPF do Pai"))
        self.lblCpfMae.setText(_translate("matricularAluno", "CPF da Mãe"))
        self.lineCpfMae.setInputMask(_translate("matricularAluno", "000.000.000-00"))
        self.lineCpfMae.setText(_translate("matricularAluno", "..-"))
        self.lblTelefonePai.setText(_translate("matricularAluno", "Telefone do Pai"))
        self.lineTelefonePai.setInputMask(_translate("matricularAluno", "(00)00000-0000"))
        self.lineTelefonePai.setText(_translate("matricularAluno", "()-"))
        self.lineTelefoneMae.setInputMask(_translate("matricularAluno", "(00)00000-0000"))
        self.lineTelefoneMae.setText(_translate("matricularAluno", "()-"))
        self.lblTelefoneMae.setText(_translate("matricularAluno", "Telefone da Mãe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    matricularAluno = QtWidgets.QMainWindow()
    ui = Ui_matricularAluno()
    ui.setupUi(matricularAluno)
    matricularAluno.show()
    sys.exit(app.exec_())

