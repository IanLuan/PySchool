import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verServidoresWindow import *

import cadastroServidor
import homeServidor
import homeAdm


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_servidores()
tela.setupUi(MainWindow)

database = Database()

def voltarHome(id):
    MainWindow.close()
    homeAdm.startHomeAdm(id)

def adicionarServidores():
    servidores = []
    servidores = database.mostrarServidores()
    for servidor in servidores:
        tela.model.appendRow(QStandardItem(servidor))

def cadastrarServidores(id):
    cadastroServidor.startCadastroServidor(id)

def startServidores(id):

    # Configurar tabela
    tela.model = QStandardItemModel()
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Servidores'])
    tela.table.setColumnWidth(0, 350)
    adicionarServidores()

    # Cadastrar Matéria
    tela.btnServidores.clicked.connect(partial(cadastrarServidores, id))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id))

    # run
    MainWindow.show()
