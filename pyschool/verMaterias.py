import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verMateriasWindow import *

import cadastroMateria
import homeServidor
import homeAdm


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_materias()
tela.setupUi(MainWindow)

database = Database()

def voltarHome(id, type):
    MainWindow.close()
    if type == "administrador":
	    homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)

def adicionarMaterias():
    materias = []
    materias = database.mostrarMaterias()
    for materia in materias:
        tela.model.appendRow(QStandardItem(materia))

def cadastrarMaterias(id):
    cadastroMateria.startCadastroMateria(id)

def startMaterias(id, type):

    # Configurar tabela
    tela.model = QStandardItemModel()
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Cargos'])
    tela.table.setColumnWidth(0, 350)
    adicionarMaterias()

    # Cadastrar Matéria
    tela.btnMateria.clicked.connect(partial(cadastrarMaterias, id))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id, type))

    # run
    MainWindow.show()
