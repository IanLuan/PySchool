from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastroProfessor(object):
    def setupUi(self, cadastroProfessor):
        cadastroProfessor.setObjectName("cadastroProfessor")
        cadastroProfessor.resize(952, 685)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cadastroProfessor.sizePolicy().hasHeightForWidth())
        cadastroProfessor.setSizePolicy(sizePolicy)
        cadastroProfessor.setMinimumSize(QtCore.QSize(952, 200))
        cadastroProfessor.setMaximumSize(QtCore.QSize(952, 760))
        cadastroProfessor.setLayoutDirection(QtCore.Qt.LeftToRight)
        cadastroProfessor.setStyleSheet("background-color: rgb(21, 143, 181)")
        self.centralwidget = QtWidgets.QWidget(cadastroProfessor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QWidget{\n"
"backgroundcolor: rgb(255,255,255)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnCadatrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadatrar.setGeometry(QtCore.QRect(830, 652, 111, 30))
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
        self.btnCancelar.setGeometry(QtCore.QRect(10, 652, 111, 30))
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
        self.framezao.setGeometry(QtCore.QRect(10, 0, 931, 647))
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
        self.label_3 = QtWidgets.QLabel(self.framePessoais)
        self.label_3.setGeometry(QtCore.QRect(10, 45, 181, 23))
        self.label_3.setStyleSheet("font: 75 10pt \"Malgun Gothic\";\n"
"color: rgb(136, 136, 136)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.framePessoais)
        self.label_4.setGeometry(QtCore.QRect(10, 112, 55, 23))
        self.label_4.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.framePessoais)
        self.label_5.setGeometry(QtCore.QRect(10, 180, 111, 23))
        self.label_5.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.framePessoais)
        self.label_6.setGeometry(QtCore.QRect(740, 180, 121, 23))
        self.label_6.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.framePessoais)
        self.label_8.setGeometry(QtCore.QRect(470, 112, 55, 23))
        self.label_8.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setObjectName("label_8")
        self.cbEstadoCivil = QtWidgets.QComboBox(self.framePessoais)
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
        self.dateNascimento.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateNascimento.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.dateNascimento.setMinimumDate(QtCore.QDate(1900, 9, 14))
        self.dateNascimento.setObjectName("dateNascimento")
        self.label_10 = QtWidgets.QLabel(self.framePessoais)
        self.label_10.setGeometry(QtCore.QRect(470, 180, 55, 31))
        self.label_10.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_10.setObjectName("label_10")
        self.cbSexo = QtWidgets.QComboBox(self.framePessoais)
        self.cbSexo.setGeometry(QtCore.QRect(470, 210, 251, 28))
        self.cbSexo.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbSexo.setObjectName("cbSexo")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.line_3 = QtWidgets.QFrame(self.framePessoais)
        self.line_3.setGeometry(QtCore.QRect(320, 32, 300, 1))
        self.line_3.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_21 = QtWidgets.QLabel(self.framePessoais)
        self.label_21.setGeometry(QtCore.QRect(740, 45, 40, 23))
        self.label_21.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_21.setObjectName("label_21")
        self.lineNome = QtWidgets.QLineEdit(self.framePessoais)
        self.lineNome.setGeometry(QtCore.QRect(10, 75, 711, 28))
        self.lineNome.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineNome.setObjectName("lineNome")
        self.lineCpf = QtWidgets.QLineEdit(self.framePessoais)
        self.lineCpf.setGeometry(QtCore.QRect(10, 140, 431, 28))
        self.lineCpf.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCpf.setObjectName("lineCpf")
        self.lineRg = QtWidgets.QLineEdit(self.framePessoais)
        self.lineRg.setGeometry(QtCore.QRect(470, 140, 251, 28))
        self.lineRg.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRg.setObjectName("lineRg")
        self.lblFoto = QtWidgets.QLabel(self.framePessoais)
        self.lblFoto.setGeometry(QtCore.QRect(790, 40, 121, 141))
        self.lblFoto.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"")
        self.lblFoto.setText("")
        self.lblFoto.setPixmap(QtGui.QPixmap("icons/perfil.png"))
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
        self.label = QtWidgets.QLabel(self.frameEndereco)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 31))
        self.label.setStyleSheet("font: 25 12pt \"Malgun Gothic Semilight\";\n"
"color: rgb(21, 143, 181);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.frameEndereco)
        self.label_11.setGeometry(QtCore.QRect(10, 47, 55, 16))
        self.label_11.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frameEndereco)
        self.label_12.setGeometry(QtCore.QRect(740, 50, 71, 16))
        self.label_12.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frameEndereco)
        self.label_13.setGeometry(QtCore.QRect(10, 105, 55, 16))
        self.label_13.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frameEndereco)
        self.label_14.setGeometry(QtCore.QRect(470, 47, 55, 16))
        self.label_14.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frameEndereco)
        self.label_15.setGeometry(QtCore.QRect(470, 105, 55, 16))
        self.label_15.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frameEndereco)
        self.label_16.setGeometry(QtCore.QRect(740, 110, 55, 16))
        self.label_16.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_16.setObjectName("label_16")
        self.lineRua = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineRua.setGeometry(QtCore.QRect(10, 70, 431, 28))
        self.lineRua.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineRua.setObjectName("lineRua")
        self.spinNumero = QtWidgets.QSpinBox(self.frameEndereco)
        self.spinNumero.setGeometry(QtCore.QRect(740, 70, 171, 28))
        self.spinNumero.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.spinNumero.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinNumero.setMaximum(5000)
        self.spinNumero.setObjectName("spinNumero")
        self.cbEstado = QtWidgets.QComboBox(self.frameEndereco)
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
        self.line_2 = QtWidgets.QFrame(self.frameEndereco)
        self.line_2.setGeometry(QtCore.QRect(320, 35, 300, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineBairro = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineBairro.setGeometry(QtCore.QRect(10, 130, 431, 28))
        self.lineBairro.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineBairro.setObjectName("lineBairro")
        self.lineCep = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCep.setGeometry(QtCore.QRect(470, 70, 251, 28))
        self.lineCep.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCep.setObjectName("lineCep")
        self.lineCidade = QtWidgets.QLineEdit(self.frameEndereco)
        self.lineCidade.setGeometry(QtCore.QRect(470, 130, 251, 28))
        self.lineCidade.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineCidade.setObjectName("lineCidade")
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.lineRua.raise_()
        self.spinNumero.raise_()
        self.cbEstado.raise_()
        self.label.raise_()
        self.line_2.raise_()
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
        self.label_17 = QtWidgets.QLabel(self.frameComplementares)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 55, 23))
        self.label_17.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frameComplementares)
        self.label_18.setGeometry(QtCore.QRect(470, 125, 55, 16))
        self.label_18.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.frameComplementares)
        self.label_20.setGeometry(QtCore.QRect(10, 125, 55, 23))
        self.label_20.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n"
"color: rgb(136, 136, 136)")
        self.label_20.setObjectName("label_20")
        self.lineSenha = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineSenha.setGeometry(QtCore.QRect(470, 150, 441, 28))
        self.lineSenha.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineSenha.setObjectName("lineSenha")
        self.line = QtWidgets.QFrame(self.frameComplementares)
        self.line.setGeometry(QtCore.QRect(320, 50, 300, 1))
        self.line.setStyleSheet("background-color: rgb(255, 123, 28);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.frameComplementares)
        self.label_9.setGeometry(QtCore.QRect(740, 60, 91, 23))
        self.label_9.setStyleSheet("color: rgb(136, 136, 136);\n"
"font: 75 10pt \"Malgun Gothic\";")
        self.label_9.setObjectName("label_9")
        self.lineEmail = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineEmail.setGeometry(QtCore.QRect(10, 150, 431, 28))
        self.lineEmail.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEmail.setObjectName("lineEmail")
        self.lineTelefone = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineTelefone.setGeometry(QtCore.QRect(740, 90, 161, 28))
        self.lineTelefone.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineTelefone.setInputMethodHints(QtCore.Qt.ImhNone)
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
        self.lineMaterias = QtWidgets.QLineEdit(self.frameComplementares)
        self.lineMaterias.setGeometry(QtCore.QRect(220, 90, 501, 28))
        self.lineMaterias.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 5px;\n"
"font: 9pt \"Leelawadee UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineMaterias.setObjectName("lineMaterias")
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
        self.btnCadatrar.raise_()
        self.btnCancelar.raise_()
        cadastroProfessor.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastroProfessor)
        self.cbEstadoCivil.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cadastroProfessor)

    def retranslateUi(self, cadastroProfessor):
        _translate = QtCore.QCoreApplication.translate
        cadastroProfessor.setWindowTitle(_translate("cadastroProfessor", "Cadastrar Professor"))
        self.btnCadatrar.setText(_translate("cadastroProfessor", "Cadastrar"))
        self.btnCancelar.setText(_translate("cadastroProfessor", "Cancelar"))
        self.lblPessoais.setText(_translate("cadastroProfessor", "Informações Pessoais"))
        self.label_3.setText(_translate("cadastroProfessor", "Nome Completo"))
        self.label_4.setText(_translate("cadastroProfessor", "CPF"))
        self.label_5.setText(_translate("cadastroProfessor", "Estado Civil"))
        self.label_6.setText(_translate("cadastroProfessor", "Nascimento"))
        self.label_8.setText(_translate("cadastroProfessor", "RG"))
        self.cbEstadoCivil.setItemText(0, _translate("cadastroProfessor", "Solteiro(a)"))
        self.cbEstadoCivil.setItemText(1, _translate("cadastroProfessor", "Casado(a)"))
        self.cbEstadoCivil.setItemText(2, _translate("cadastroProfessor", "Separado(a)"))
        self.cbEstadoCivil.setItemText(3, _translate("cadastroProfessor", "Divorciado(a)"))
        self.cbEstadoCivil.setItemText(4, _translate("cadastroProfessor", "Viúvo(a)"))
        self.label_10.setText(_translate("cadastroProfessor", "Sexo"))
        self.cbSexo.setItemText(0, _translate("cadastroProfessor", "Feminino"))
        self.cbSexo.setItemText(1, _translate("cadastroProfessor", "Masculino"))
        self.cbSexo.setItemText(2, _translate("cadastroProfessor", "Outro"))
        self.label_21.setText(_translate("cadastroProfessor", "Foto"))
        self.lineCpf.setInputMask(_translate("cadastroProfessor", "000.000.000-00"))
        self.label.setText(_translate("cadastroProfessor", "Endereço"))
        self.label_11.setText(_translate("cadastroProfessor", "Rua"))
        self.label_12.setText(_translate("cadastroProfessor", "Número"))
        self.label_13.setText(_translate("cadastroProfessor", "Bairro"))
        self.label_14.setText(_translate("cadastroProfessor", "CEP"))
        self.label_15.setText(_translate("cadastroProfessor", "Cidade"))
        self.label_16.setText(_translate("cadastroProfessor", "Estado"))
        self.cbEstado.setItemText(0, _translate("cadastroProfessor", "Acre (AC)"))
        self.cbEstado.setItemText(1, _translate("cadastroProfessor", "Alagoas (AL)"))
        self.cbEstado.setItemText(2, _translate("cadastroProfessor", "Amapá (AP)"))
        self.cbEstado.setItemText(3, _translate("cadastroProfessor", "Amazonas (AM)"))
        self.cbEstado.setItemText(4, _translate("cadastroProfessor", "Bahia (BA)"))
        self.cbEstado.setItemText(5, _translate("cadastroProfessor", "Ceará (CE)"))
        self.cbEstado.setItemText(6, _translate("cadastroProfessor", "Distrito Federal (DF)"))
        self.cbEstado.setItemText(7, _translate("cadastroProfessor", "Espírito Santos (ES)"))
        self.cbEstado.setItemText(8, _translate("cadastroProfessor", "Goiás (GO)"))
        self.cbEstado.setItemText(9, _translate("cadastroProfessor", "Maranhão (MA)"))
        self.cbEstado.setItemText(10, _translate("cadastroProfessor", "Mato Grosso (MT)"))
        self.cbEstado.setItemText(11, _translate("cadastroProfessor", "Mato Grosso do Sul (MS)"))
        self.cbEstado.setItemText(12, _translate("cadastroProfessor", "Minas Gerais (MG)"))
        self.cbEstado.setItemText(13, _translate("cadastroProfessor", "Pará (PA)"))
        self.cbEstado.setItemText(14, _translate("cadastroProfessor", "Paraíba (PB)"))
        self.cbEstado.setItemText(15, _translate("cadastroProfessor", "Paraná (PR)"))
        self.cbEstado.setItemText(16, _translate("cadastroProfessor", "Pernambuco (PR)"))
        self.cbEstado.setItemText(17, _translate("cadastroProfessor", "Piauí (PI)"))
        self.cbEstado.setItemText(18, _translate("cadastroProfessor", "Rio de Janeiro (RJ)"))
        self.cbEstado.setItemText(19, _translate("cadastroProfessor", "Rio Grande do Norte (RN)"))
        self.cbEstado.setItemText(20, _translate("cadastroProfessor", "Rondônia (RO)"))
        self.cbEstado.setItemText(21, _translate("cadastroProfessor", "Roraima (RR)"))
        self.cbEstado.setItemText(22, _translate("cadastroProfessor", "Santa Catarina (SC)"))
        self.cbEstado.setItemText(23, _translate("cadastroProfessor", "São Paulo (SP)"))
        self.cbEstado.setItemText(24, _translate("cadastroProfessor", "Sergipe (SE)"))
        self.cbEstado.setItemText(25, _translate("cadastroProfessor", "Tocantins (TO)"))
        self.lineCep.setInputMask(_translate("cadastroProfessor", "00000-000"))
        self.lblInfoComplementares.setText(_translate("cadastroProfessor", "Informações Complementares"))
        self.label_17.setText(_translate("cadastroProfessor", "Matérias"))
        self.label_18.setText(_translate("cadastroProfessor", "Senha"))
        self.label_20.setText(_translate("cadastroProfessor", "Email"))
        self.label_9.setText(_translate("cadastroProfessor", "Telefone"))
        self.lineTelefone.setInputMask(_translate("cadastroProfessor", "(00) 0 0000-0000"))
        self.btnMaterias.setText(_translate("cadastroProfessor", "Definir Matérias"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cadastroProfessor = QtWidgets.QMainWindow()
    ui = Ui_cadastroProfessor()
    ui.setupUi(cadastroProfessor)
    cadastroProfessor.show()
    sys.exit(app.exec_())
