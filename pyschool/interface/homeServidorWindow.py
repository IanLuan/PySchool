from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeServidor(object):
    def setupUi(self, homeServidor):
        homeServidor.setObjectName("homeServidor")
        homeServidor.resize(680, 260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeServidor.sizePolicy().hasHeightForWidth())
        homeServidor.setSizePolicy(sizePolicy)
        homeServidor.setMinimumSize(QtCore.QSize(680, 260))
        homeServidor.setMaximumSize(QtCore.QSize(680, 260))
        self.centralwidget = QtWidgets.QWidget(homeServidor)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnMatricula = QtWidgets.QPushButton(self.centralwidget)
        self.btnMatricula.setGeometry(QtCore.QRect(20, 20, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnMatricula.setFont(font)
        self.btnMatricula.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/matricula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMatricula.setIcon(icon)
        self.btnMatricula.setIconSize(QtCore.QSize(32, 32))
        self.btnMatricula.setFlat(False)
        self.btnMatricula.setObjectName("btnMatricula")
        self.btnAlunos = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlunos.setGeometry(QtCore.QRect(240, 20, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAlunos.setFont(font)
        self.btnAlunos.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("interface/icons/alunos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlunos.setIcon(icon1)
        self.btnAlunos.setIconSize(QtCore.QSize(32, 32))
        self.btnAlunos.setObjectName("btnAlunos")
        self.btnMaterias = QtWidgets.QPushButton(self.centralwidget)
        self.btnMaterias.setGeometry(QtCore.QRect(240, 130, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnMaterias.setFont(font)
        self.btnMaterias.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("interface/icons/materias.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMaterias.setIcon(icon2)
        self.btnMaterias.setIconSize(QtCore.QSize(32, 32))
        self.btnMaterias.setObjectName("btnMaterias")
        self.btnProfessores = QtWidgets.QPushButton(self.centralwidget)
        self.btnProfessores.setGeometry(QtCore.QRect(20, 130, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnProfessores.setFont(font)
        self.btnProfessores.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.btnProfessores.setIcon(icon1)
        self.btnProfessores.setIconSize(QtCore.QSize(32, 32))
        self.btnProfessores.setObjectName("btnProfessores")
        self.btnTurmas = QtWidgets.QPushButton(self.centralwidget)
        self.btnTurmas.setGeometry(QtCore.QRect(460, 20, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTurmas.setFont(font)
        self.btnTurmas.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("interface/icons/turma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTurmas.setIcon(icon3)
        self.btnTurmas.setIconSize(QtCore.QSize(32, 32))
        self.btnTurmas.setObjectName("btnTurmas")
        self.btnPerfil = QtWidgets.QPushButton(self.centralwidget)
        self.btnPerfil.setGeometry(QtCore.QRect(460, 130, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPerfil.setFont(font)
        self.btnPerfil.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("interface/icons/person.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPerfil.setIcon(icon4)
        self.btnPerfil.setIconSize(QtCore.QSize(32, 32))
        self.btnPerfil.setObjectName("btnPerfil")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(620, 224, 32, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("")
        self.btnExit.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("interface/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon5)
        self.btnExit.setIconSize(QtCore.QSize(32, 32))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        homeServidor.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeServidor)
        QtCore.QMetaObject.connectSlotsByName(homeServidor)

    def retranslateUi(self, homeServidor):
        _translate = QtCore.QCoreApplication.translate
        homeServidor.setWindowTitle(_translate("homeServidor", "Início"))
        self.btnMatricula.setText(_translate("homeServidor", "Matrícula"))
        self.btnAlunos.setText(_translate("homeServidor", "Alunos"))
        self.btnMaterias.setText(_translate("homeServidor", "Matérias"))
        self.btnProfessores.setText(_translate("homeServidor", "Professores"))
        self.btnTurmas.setText(_translate("homeServidor", "Turmas"))
        self.btnPerfil.setText(_translate("homeServidor", "Perfil do Servidor"))
        self.btnExit.setToolTip(_translate("homeServidor", "Sair"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeServidor = QtWidgets.QMainWindow()
    ui = Ui_homeServidor()
    ui.setupUi(homeServidor)
    homeServidor.show()
    sys.exit(app.exec_())
