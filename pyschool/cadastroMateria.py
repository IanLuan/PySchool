import sys
from interface.cadastroMateriaWindow import *
from database.database import Database
from materia import Materia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

database = Database()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroMateria()
tela.setupUi(MainWindow)

def cadastrarMateria():
    try:
        materia = Materia(tela.lineMateria.text())
        database.inserirMateria(materia.getNome())
        tela.lineMateria.setText("")

        msg = QMessageBox(None)
        msg.setWindowTitle("Cadastro Realizado")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()
        msg.show()


    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, primeiro digite o nome da matéria")
        msg.exec_()
        msg.show()


    except Warning:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Matéria já cadastrada. Tente novamente.")
        msg.exec_()
        msg.show()


def startCadastroMateria(id):
    tela.btnCadastrar.clicked.connect(cadastrarMateria)

    MainWindow.show()

