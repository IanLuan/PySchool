from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeAdm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(680, 200))
        MainWindow.setMaximumSize(QtCore.QSize(680, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.btnMaterias.setGeometry(QtCore.QRect(460, 130, 200, 90))
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
        self.btnProfessores.setGeometry(QtCore.QRect(240, 130, 200, 90))
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
        self.btnServidores = QtWidgets.QPushButton(self.centralwidget)
        self.btnServidores.setGeometry(QtCore.QRect(20, 130, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnServidores.setFont(font)
        self.btnServidores.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        self.btnServidores.setIcon(icon1)
        self.btnServidores.setIconSize(QtCore.QSize(32, 32))
        self.btnServidores.setObjectName("btnServidores")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(620, 334, 32, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("")
        self.btnExit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("interface/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon4)
        self.btnExit.setIconSize(QtCore.QSize(32, 32))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.btnCargos = QtWidgets.QPushButton(self.centralwidget)
        self.btnCargos.setGeometry(QtCore.QRect(20, 240, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCargos.setFont(font)
        self.btnCargos.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("interface/icons/work.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCargos.setIcon(icon5)
        self.btnCargos.setIconSize(QtCore.QSize(32, 32))
        self.btnCargos.setObjectName("btnCargos")
        self.btnPerfil = QtWidgets.QPushButton(self.centralwidget)
        self.btnPerfil.setGeometry(QtCore.QRect(240, 240, 200, 90))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPerfil.setFont(font)
        self.btnPerfil.setStyleSheet("border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("interface/icons/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPerfil.setIcon(icon6)
        self.btnPerfil.setIconSize(QtCore.QSize(32, 32))
        self.btnPerfil.setObjectName("btnPerfil")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Início"))
        self.btnMatricula.setText(_translate("MainWindow", "Matrícula"))
        self.btnAlunos.setText(_translate("MainWindow", "Alunos"))
        self.btnMaterias.setText(_translate("MainWindow", "Matérias"))
        self.btnProfessores.setText(_translate("MainWindow", "Professores"))
        self.btnTurmas.setText(_translate("MainWindow", "Turmas"))
        self.btnServidores.setText(_translate("MainWindow", "Servidores"))
        self.btnExit.setToolTip(_translate("MainWindow", "<html><head/><body style=\"background-color: #fff;\"><p>Sair</p></body></html>"))
        self.btnCargos.setText(_translate("MainWindow", "Cargos"))
        self.btnPerfil.setText(_translate("MainWindow", "Perfil do Adm"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_homeAdm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
