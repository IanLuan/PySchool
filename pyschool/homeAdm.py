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

# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeAdm()
tela.setupUi(MainWindow)


def professores(id, type):
    MainWindow.close()

def alunos(id, type):
    MainWindow.close()
    verAlunos.startAlunos(id, type)

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

def startHomeAdm(id):

    # Matricula
    tela.btnMatricula.clicked.connect(partial(matricula, id, "administrador"))

    # Turmas
    tela.btnTurmas.clicked.connect(partial(turmas, id, "administrador"))

    # Alunos
    tela.btnAlunos.clicked.connect(partial(alunos, id, "administrador"))
    
    # Cargos
    tela.btnCargos.clicked.connect(partial(cargos, id))

    # Perfil
    tela.btnPerfil.clicked.connect(partial(perfil, id))

    # Professores
    tela.btnProfessores.clicked.connect(partial(professores, id, "administrador"))

    MainWindow.show()