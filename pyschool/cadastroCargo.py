import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from cargo import Cargo
from database import database
from interface.cadastroServidorWindow import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroCargo()
tela.setupUi(MainWindow)

def cadastrarCargo():

    try:
        cargo = Cargo(tela.lineCargo.text())

        database.inserirCargo(tela.lineCargo.text())
        tela.lineCargo.setText("")

        msg = QMessageBox(None)
        msg.setWindowTitle("Cadastro Realizado")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.show()
        msg.exec_()

    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Digite o nome do cargo antes de confirmar!")
        msg.show()
        msg.exec_()


tela.btnCadastrar.clicked.connect(cadastrarCargo)

MainWindow.show()
sys.exit(app.exec_())
