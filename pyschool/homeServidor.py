import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeServidorWindow import *

import perfilServidor
import matriculaAluno
import verTurmas
import verAlunos
import verProfessores


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeServidor()
tela.setupUi(MainWindow)


def professores(id, type):
    MainWindow.close()
    verProfessores.startProfessor(id, type)

def alunos(id, type):
    MainWindow.close()
    verAlunos.startAlunos(id, type)

def turmas(id, type):
    MainWindow.close()
    verTurmas.startTurmas(id, type)

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

    # Turmas
    tela.btnTurmas.clicked.connect(partial(turmas, id, "servidor"))

    # Alunos
    tela.btnAlunos.clicked.connect(partial(alunos, id, "servidor"))

    # Professores
    tela.btnProfessores.clicked.connect(partial(professores, id, "servidor"))

    MainWindow.show()