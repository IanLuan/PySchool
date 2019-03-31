import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from database import database
#from interface.login import *

from pyschool.interface.loginWindow import *
from pyschool.database import database
from pessoa import Pessoa

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_login()
tela.setupUi(MainWindow)

def logar():

    email = tela.lineEmail.text()
    senha = tela.lineSenha.text()
    sucessful = False

    try:
        pessoa = Pessoa(None, None, None, None, None, None, None, email, senha, None, None)
        id, type = pessoa.autenticar(email, senha)

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


