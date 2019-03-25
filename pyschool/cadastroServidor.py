# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroServidor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cadastroServidor(object):
    def setupUi(self, cadastroServidor):
        cadastroServidor.setObjectName("cadastroServidor")
        cadastroServidor.resize(952, 752)
        cadastroServidor.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"")
        self.centralwidget = QtWidgets.QWidget(cadastroServidor)
        self.centralwidget.setStyleSheet("backgroundcolor: rgb(255,255,255)")
        self.centralwidget.setObjectName("centralwidget")
        self.framePessoais = QtWidgets.QFrame(self.centralwidget)
        self.framePessoais.setGeometry(QtCore.QRect(10, 10, 931, 231))
        self.framePessoais.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePessoais.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePessoais.setObjectName("framePessoais")
        self.lblPessoais = QtWidgets.QLabel(self.framePessoais)
        self.lblPessoais.setGeometry(QtCore.QRect(0, 0, 931, 31))
        self.lblPessoais.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";")
        self.lblPessoais.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPessoais.setObjectName("lblPessoais")
        self.line = QtWidgets.QFrame(self.framePessoais)
        self.line.setGeometry(QtCore.QRect(240, 30, 461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.framePessoais)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 181, 23))
        self.label_3.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.framePessoais)
        self.label_4.setGeometry(QtCore.QRect(10, 105, 55, 23))
        self.label_4.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.framePessoais)
        self.label_5.setGeometry(QtCore.QRect(10, 165, 111, 23))
        self.label_5.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.framePessoais)
        self.label_6.setGeometry(QtCore.QRect(470, 105, 121, 23))
        self.label_6.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.framePessoais)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 691, 28))
        self.textEdit.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.framePessoais)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 130, 431, 28))
        self.textEdit_2.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_7 = QtWidgets.QLabel(self.framePessoais)
        self.label_7.setGeometry(QtCore.QRect(770, 10, 121, 91))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.framePessoais)
        self.label_8.setGeometry(QtCore.QRect(660, 105, 55, 23))
        self.label_8.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.textEdit_3 = QtWidgets.QTextEdit(self.framePessoais)
        self.textEdit_3.setGeometry(QtCore.QRect(660, 130, 261, 28))
        self.textEdit_3.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.framePessoais)
        self.comboBox.setGeometry(QtCore.QRect(10, 190, 431, 28))
        self.comboBox.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.framePessoais)
        self.dateEdit.setGeometry(QtCore.QRect(470, 130, 171, 28))
        self.dateEdit.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateEdit.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.dateEdit.setObjectName("dateEdit")
        self.label_9 = QtWidgets.QLabel(self.framePessoais)
        self.label_9.setGeometry(QtCore.QRect(660, 165, 91, 23))
        self.label_9.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_9.setObjectName("label_9")
        self.textEdit_4 = QtWidgets.QTextEdit(self.framePessoais)
        self.textEdit_4.setGeometry(QtCore.QRect(660, 190, 261, 28))
        self.textEdit_4.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_10 = QtWidgets.QLabel(self.framePessoais)
        self.label_10.setGeometry(QtCore.QRect(470, 165, 55, 16))
        self.label_10.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.framePessoais)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 190, 171, 28))
        self.comboBox_2.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 257, 931, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 31))
        self.label.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(230, 30, 461, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.label_11.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(760, 50, 71, 16))
        self.label_12.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 55, 16))
        self.label_13.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(470, 50, 55, 16))
        self.label_14.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(470, 110, 55, 16))
        self.label_15.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(760, 110, 55, 16))
        self.label_16.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_16.setObjectName("label_16")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 431, 28))
        self.lineEdit.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(760, 70, 161, 28))
        self.spinBox.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 130, 431, 28))
        self.textEdit_5.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_6.setGeometry(QtCore.QRect(470, 70, 271, 28))
        self.textEdit_6.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_7.setGeometry(QtCore.QRect(470, 130, 271, 28))
        self.textEdit_7.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(760, 130, 161, 28))
        self.comboBox_3.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 450, 931, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 931, 41))
        self.label_2.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(230, 40, 461, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 55, 23))
        self.label_17.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(470, 130, 55, 16))
        self.label_18.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(470, 60, 121, 23))
        self.label_19.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(10, 120, 55, 23))
        self.label_20.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_20.setObjectName("label_20")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 90, 431, 28))
        self.comboBox_4.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(470, 90, 95, 20))
        self.radioButton.setStyleSheet("font: 9pt \"Leelawadee UI Semilight\";\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(550, 90, 95, 20))
        self.radioButton_2.setStyleSheet("font: 9pt \"Leelawadee UI Semilight\";\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.textEdit_8 = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 150, 431, 28))
        self.textEdit_8.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 150, 451, 28))
        self.lineEdit_2.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnCadatrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadatrar.setGeometry(QtCore.QRect(820, 670, 111, 30))
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
"background-color: rgb(255, 255, 255);")
        self.btnCadatrar.setObjectName("btnCadatrar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(20, 670, 111, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCancelar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"border: 0.7px solid grey;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.btnCancelar.setObjectName("btnCancelar")
        cadastroServidor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(cadastroServidor)
        self.statusbar.setStyleSheet("backgroundcolor: #000000")
        self.statusbar.setObjectName("statusbar")
        cadastroServidor.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(cadastroServidor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 26))
        self.menubar.setStyleSheet("backgroundcolor: rgb(59, 59, 59)")
        self.menubar.setObjectName("menubar")
        cadastroServidor.setMenuBar(self.menubar)

        self.retranslateUi(cadastroServidor)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cadastroServidor)

    def retranslateUi(self, cadastroServidor):
        _translate = QtCore.QCoreApplication.translate
        cadastroServidor.setWindowTitle(_translate("cadastroServidor", "MainWindow"))
        self.lblPessoais.setText(_translate("cadastroServidor", "Informações Pessoais"))
        self.label_3.setText(_translate("cadastroServidor", "Nome Completo"))
        self.label_4.setText(_translate("cadastroServidor", "CPF"))
        self.label_5.setText(_translate("cadastroServidor", "Estado Civil"))
        self.label_6.setText(_translate("cadastroServidor", "Nascimento"))
        self.label_7.setText(_translate("cadastroServidor", "AQUI FICA A FOTO"))
        self.label_8.setText(_translate("cadastroServidor", "RG"))
        self.comboBox.setItemText(0, _translate("cadastroServidor", "Solteiro(a)"))
        self.comboBox.setItemText(1, _translate("cadastroServidor", "Casado(a)"))
        self.comboBox.setItemText(2, _translate("cadastroServidor", "Separado(a)"))
        self.comboBox.setItemText(3, _translate("cadastroServidor", "Divorciado(a)"))
        self.comboBox.setItemText(4, _translate("cadastroServidor", "Viúvo(a)"))
        self.label_9.setText(_translate("cadastroServidor", "Telefone"))
        self.label_10.setText(_translate("cadastroServidor", "Sexo"))
        self.comboBox_2.setItemText(0, _translate("cadastroServidor", "Feminino"))
        self.comboBox_2.setItemText(1, _translate("cadastroServidor", "Masculino"))
        self.comboBox_2.setItemText(2, _translate("cadastroServidor", "Outro"))
        self.label.setText(_translate("cadastroServidor", "Endereço"))
        self.label_11.setText(_translate("cadastroServidor", "Rua"))
        self.label_12.setText(_translate("cadastroServidor", "Número"))
        self.label_13.setText(_translate("cadastroServidor", "Bairro"))
        self.label_14.setText(_translate("cadastroServidor", "CEP"))
        self.label_15.setText(_translate("cadastroServidor", "Cidade"))
        self.label_16.setText(_translate("cadastroServidor", "Estado"))
        self.comboBox_3.setItemText(0, _translate("cadastroServidor", "Acre (AC)"))
        self.comboBox_3.setItemText(1, _translate("cadastroServidor", "Alagoas (AL)"))
        self.comboBox_3.setItemText(2, _translate("cadastroServidor", "Amapá (AP)"))
        self.comboBox_3.setItemText(3, _translate("cadastroServidor", "Amazonas (AM)"))
        self.comboBox_3.setItemText(4, _translate("cadastroServidor", "Bahia (BA)"))
        self.comboBox_3.setItemText(5, _translate("cadastroServidor", "Ceará (CE)"))
        self.comboBox_3.setItemText(6, _translate("cadastroServidor", "Distrito Federal (DF)"))
        self.comboBox_3.setItemText(7, _translate("cadastroServidor", "Espírito Santos (ES)"))
        self.comboBox_3.setItemText(8, _translate("cadastroServidor", "Goiás (GO)"))
        self.comboBox_3.setItemText(9, _translate("cadastroServidor", "Maranhão (MA)"))
        self.comboBox_3.setItemText(10, _translate("cadastroServidor", "Mato Grosso (MT)"))
        self.comboBox_3.setItemText(11, _translate("cadastroServidor", "Mato Grosso do Sul (MS)"))
        self.comboBox_3.setItemText(12, _translate("cadastroServidor", "Minas Gerais (MG)"))
        self.comboBox_3.setItemText(13, _translate("cadastroServidor", "Pará (PA)"))
        self.comboBox_3.setItemText(14, _translate("cadastroServidor", "Paraíba (PB)"))
        self.comboBox_3.setItemText(15, _translate("cadastroServidor", "Paraná (PR)"))
        self.comboBox_3.setItemText(16, _translate("cadastroServidor", "Pernambuco (PR)"))
        self.comboBox_3.setItemText(17, _translate("cadastroServidor", "Piauí (PI)"))
        self.comboBox_3.setItemText(18, _translate("cadastroServidor", "Rio de Janeiro (RJ)"))
        self.comboBox_3.setItemText(19, _translate("cadastroServidor", "Rio Grande do Norte (RN)"))
        self.comboBox_3.setItemText(20, _translate("cadastroServidor", "Rondônia (RO)"))
        self.comboBox_3.setItemText(21, _translate("cadastroServidor", "Roraima (RR)"))
        self.comboBox_3.setItemText(22, _translate("cadastroServidor", "Santa Catarina (SC)"))
        self.comboBox_3.setItemText(23, _translate("cadastroServidor", "São Paulo (SP)"))
        self.comboBox_3.setItemText(24, _translate("cadastroServidor", "Sergipe (SE)"))
        self.comboBox_3.setItemText(25, _translate("cadastroServidor", "Tocantins (TO)"))
        self.label_2.setText(_translate("cadastroServidor", "Informações Complementares"))
        self.label_17.setText(_translate("cadastroServidor", "Cargo"))
        self.label_18.setText(_translate("cadastroServidor", "Senha"))
        self.label_19.setText(_translate("cadastroServidor", "Admistrador"))
        self.label_20.setText(_translate("cadastroServidor", "Email"))
        self.radioButton.setText(_translate("cadastroServidor", "Sim"))
        self.radioButton_2.setText(_translate("cadastroServidor", "Não"))
        self.btnCadatrar.setText(_translate("cadastroServidor", "Cadastrar"))
        self.btnCancelar.setText(_translate("cadastroServidor", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastroServidor = QtWidgets.QMainWindow()
    ui = Ui_cadastroServidor()
    ui.setupUi(cadastroServidor)
    cadastroServidor.show()
    sys.exit(app.exec_())

