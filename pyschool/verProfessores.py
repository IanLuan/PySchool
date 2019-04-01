import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verProfessoresWindow import *

import homeServidor
import homeAdm
import cadastroProfessor

# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_verProfessores()
tela.setupUi(MainWindow)

def cadastrarProfessores(id, type):
    MainWindow.close()
    cadastroProfessor.startCadastroProfessor(id)

def voltarHome(id, type):
    MainWindow.close()

    if type == "administrador":
        homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)

def adicionarProfessores():

	# SELECT AQUI PARA ME RETORNAR A LISTA DE TODOS OS ALUNOS
    professores = ["João", "marcos", "fabiana", "lalala","teste"]

    for professor in professores:
        tela.model.appendRow(QStandardItem(professor))

def startProfessor(id, type):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Alunos'])
    #tela.table.setSelectionBehavior(QAbstractItemView.SelectRows)
    tela.table.setColumnWidth(0, 350)
    adicionarProfessores()

    # Cadastrar Cargo
    tela.btnProfessores.clicked.connect(partial(cadastrarProfessores, id, type))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id, type))


    # run
    MainWindow.show()
