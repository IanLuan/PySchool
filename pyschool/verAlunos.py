import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verTodasTurmas import *

import matriculaAluno
import homeServidor
import homeAdm

# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_verTurmas()
tela.setupUi(MainWindow)

def cadastrarAlunos(id, type):
    MainWindow.close()
    matriculaAluno.startMatriculaAluno(id, type)

def voltarHome(id, type):
    MainWindow.close()

    if type == "administrador":
        homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)

def adicionarAlunos():

	# SELECT AQUI PARA ME RETORNAR A LISTA DE TODOS OS ALUNOS
    alunos = ["João", "marcos"]

    for aluno in alunos:
        tela.model.appendRow(QStandardItem(aluno))

def startAlunos(id, type):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Alunos'])
    #tela.table.setSelectionBehavior(QAbstractItemView.SelectRows)
    tela.table.setColumnWidth(0, 350)
    adicionarAlunos()

    # Cadastrar Cargo
    tela.btnTurma.clicked.connect(partial(cadastrarAlunos, id, type))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id, type))


    # run
    MainWindow.show()
