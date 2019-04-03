import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verTodasTurmas import *

import cadastroTurma
import homeServidor
import homeAdm


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_verTurmas()
tela.setupUi(MainWindow)


def cadastrarTurmas(id):
	cadastroTurma.startCadastroTurma(id)

def voltarHome(id, type):
    MainWindow.close()

    if type == "administrador":
        homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)

def adicionarTurmas(id, type):

    database = Database()

    if type == "administrador" or type == "servidor":
        turmas = database.mostrarTodasTurmas()

    for turma in turmas:
        tela.model.appendRow(QStandardItem(turma))

def startTurmas(id, type):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Turmas'])
    #tela.table.setSelectionBehavior(QAbstractItemView.SelectRows)
    tela.table.setColumnWidth(0, 350)
    adicionarTurmas(id,type)

    # Cadastrar Cargo
    tela.btnTurma.clicked.connect(partial(cadastrarTurmas, id))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id, type))

    # run
    MainWindow.show()
