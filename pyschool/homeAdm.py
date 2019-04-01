import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeAdmWindow import *
import matriculaAluno
import verCargos


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeAdm()
tela.setupUi(MainWindow)

def cargos(id):
    MainWindow.close()
    verCargos.startCargos(id)

def matricula(id, type):
    MainWindow.close()
    matriculaAluno.startMatriculaAluno(id, type)

def startHomeAdm(id):

    # matricula
    tela.btnMatricula.clicked.connect(partial(matricula, id, "administrador"))
    
    # Cargos
    tela.btnCargos.clicked.connect(partial(cargos, id))

    MainWindow.show()