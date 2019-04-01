import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from interface.loginWindow import *
from database.database import Database
from pessoa import Pessoa

database = Database()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_login()
tela.setupUi(MainWindow)
database = Database()

def logar():

    email = tela.lineEmail.text()
    senha = tela.lineSenha.text()

    try:
        if email == "":
            raise ValueError
        if senha == "":
            raise ValueError

        id, type = database.autenticar(email, senha)

        print(type)

        if id == None:
            raise UserWarning

        if type == "professor":
            pass

        elif type == "servidor":
            pass

        elif type == "administrador":
            pass

    except UserWarning:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Email ou senha incorretos. Por favor, tente novamente.")
        msg.show()
        msg.exec_()

    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, preencha todos os campos.")
        msg.show()
        msg.exec_()

tela.btnEntrar.clicked.connect(logar)

MainWindow.show()
sys.exit(app.exec_())


