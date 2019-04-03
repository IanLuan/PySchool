import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verAlunosWindow import *

import matriculaAluno
import homeServidor
import homeAdm

# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_verAlunos()
tela.setupUi(MainWindow)


def voltarHome(id, type):
    MainWindow.close()

    if type == "administrador":
        homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)

def adicionarAlunos(id, idTurma, type):
    alunos = []
    database = Database()

    if type == "administrador" or type == "servidor":
        alunos = database.mostrarTodosAlunos()
    elif type == "professor":
        print(type)
        alunos = database.mostrarAlunosProf(idTurma)

    if alunos == []:
        raise UserWarning

    for aluno in alunos:
        tela.model.appendRow(QStandardItem(aluno))

def startAlunos(id, idTurma, type):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.tableAlunos.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Alunos'])
    tela.tableAlunos.setColumnWidth(0, 350)

    try:
        adicionarAlunos(id, idTurma, type)
    except UserWarning:
        msg = QMessageBox(None)
        msg.setWindowTitle("Turma Vazia")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Não existem alunos matriculados nessa turma.")
        msg.exec_()
        msg.show()

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id, type))

    # run
    MainWindow.show()
