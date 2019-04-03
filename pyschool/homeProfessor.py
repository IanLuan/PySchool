import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeProfessorWindow import *
import perfilProfessor
import verAlunos
import login


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeProfessor()
tela.setupUi(MainWindow)


def adicionarTurmas(id):

    database = Database()
    turmas = []
    turmas = database.mostrarTurmasProf(id)

    for tupla in turmas:
        row = []
        row.append(QStandardItem(str(tupla[0])))
        row.append(QStandardItem(tupla[1]))
        tela.model.appendRow(row)

def coletarDados(id,type):
    indexes = tela.table.selectionModel().selectedRows()

    idTurma = ""
    for index in indexes:
        row = index.row()
        idTurma = tela.model.data(tela.model.index(row, 0))

    if idTurma == "":
        raise UserWarning

    #Abra aqui a turma
    MainWindow.close()
    verAlunos.startAlunos(id, idTurma, type)

def coletar(id,type):
    try:
        coletarDados(id,type)
    except UserWarning:
        #msg = QMessageBox(None)
        #msg.setWindowTitle("Erro")
        #msg.setIcon(QMessageBox.Critical)
        #msg.setText("Por favor, primeiro selecione uma turma.")
        #msg.exec_()
        #msg.show()
        print("Por favor, primeiro selecione uma turma.")

    coletarDados(id,type)


def verPerfil(id):
    # abrir a tela do perfil
    MainWindow.close()
    perfilProfessor.startPerfilProfessor(id) 

def sair():
    MainWindow.close()
    login.startLogin()


def startHomeProfessor(id):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.table.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['id', 'Turmas'])
    tela.table.setSelectionBehavior(QAbstractItemView.SelectRows)
    tela.table.setColumnWidth(0, 50)
    tela.table.setColumnWidth(1, 605)
    adicionarTurmas(id)

    # Coletar Dados da turma
    tela.btnTurmas.clicked.connect(partial(coletar,id,"professor"))

    # Ver perfil
    tela.btnPerfil.clicked.connect(partial(verPerfil,id))

    # Sair
    tela.btnExit.clicked.connect(sair)

    # run
    MainWindow.show()