import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeAdmWindow import *

import matriculaAluno
import verCargos
import perfilAdministrador
import verTurmas
import verAlunos
import verProfessores
import verMaterias
import login
import verServidores


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeAdm()
tela.setupUi(MainWindow)


def professores(id, type):
    MainWindow.close()
    verProfessores.startProfessor(id, type)

def servidores(id):
    MainWindow.close()
    verServidores.startServidores(id)

def alunos(id, idTurma, type):
    MainWindow.close()
    verAlunos.startAlunos(id, None, type)

def turmas(id, type):
    MainWindow.close()
    verTurmas.startTurmas(id, type)

def perfil(id):
    MainWindow.close()
    perfilAdministrador.startPerfilAdm(id)

def cargos(id):
    MainWindow.close()
    verCargos.startCargos(id)

def matricula(id, type):
    MainWindow.close()
    matriculaAluno.startMatriculaAluno(id, type)

def materias(id, type):
    MainWindow.close()
    verMaterias.startMaterias(id, type)

def sair():
    MainWindow.close()
    login.startLogin()

def startHomeAdm(id):

    # Matricula
    tela.btnMatricula.clicked.connect(partial(matricula, id, "administrador"))

    # Turmas
    tela.btnTurmas.clicked.connect(partial(turmas, id, "administrador"))

    # Alunos
    tela.btnAlunos.clicked.connect(partial(alunos, id, None, "administrador"))
    
    # Cargos
    tela.btnCargos.clicked.connect(partial(cargos, id))

    # Perfil
    tela.btnPerfil.clicked.connect(partial(perfil, id))

    # Professores
    tela.btnProfessores.clicked.connect(partial(professores, id, "administrador"))

    # Matérias
    tela.btnMaterias.clicked.connect(partial(materias, id, "administrador"))

    # Servidores
    tela.btnServidores.clicked.connect(partial(servidores, id))

    # Sair
    tela.btnExit.clicked.connect(sair)

    MainWindow.show()