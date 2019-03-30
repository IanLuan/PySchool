import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from database import database
#from interface.login import *
from pyschool.interface.homeAdmWindow import *
from pyschool.interface.homeServidorWindow import *
from pyschool.interface.homeProfessorWindow import *
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
            MainWindowProfessor = QtWidgets.QMainWindow()
            homeProfessor = Ui_homeProfessor()
            homeProfessor.setupUi(MainWindowProfessor)
            MainWindowProfessor.show()
            MainWindowProfessor.exec_()

        elif type == "servidor":
            MainWindowServidor = QtWidgets.QMainWindow()
            homeServidor = Ui_HomeServidor()
            homeServidor.setupUi(MainWindowServidor)
            MainWindowServidor.show()
            MainWindowServidor.exec_()
            
        elif type == "administrador":
            MainWindowAdm = QtWidgets.QMainWindow()
            homeAdm = Ui_homeAdm()
            homeAdm.setupUi(MainWindowAdm)
            MainWindowAdm.show()
            MainWindowAdm.exec_()

    except UserWarning:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        # msg.setWindowIcon(QtGui.QIcon("key.png"))
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Email ou senha incorretos. Por favor, tente novamente.")
        msg.show()
        msg.exec_()

tela.btnEntrar.clicked.connect(logar)

MainWindow.show()
sys.exit(app.exec_())


