import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeServidorWindow import *

import perfilServidor
import matriculaAluno


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeServidor()
tela.setupUi(MainWindow)


def matricula(id, type):
    MainWindow.close()
    matriculaAluno.startMatriculaAluno(id, type)

def verPerfil(id):
    MainWindow.close()
    perfilServidor.startPerfilServidor(id)


def startHomeServidor(id):

    # Ver Perfil
    tela.btnPerfil.clicked.connect(partial(verPerfil,id))

    # Matrícula
    tela.btnMatricula.clicked.connect(partial(matricula, id, "servidor"))

    MainWindow.show()