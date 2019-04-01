import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeProfessorWindow import *
from perfilProfessor import *


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeProfessor()
tela.setupUi(MainWindow)


def adicionarTurmas():

    turmas = [(0, "história", 50), (0, "matemática", 25), (0, "ciências", 35)] 

    for tupla in turmas:
        row = []
        row.append(QStandardItem(str(tupla[0])))
        row.append(QStandardItem(tupla[1]))
        row.append(QStandardItem(str(tupla[2])))
        tela.model.appendRow(row)

def coletarDados():
    indexes = tela.table.selectionModel().selectedRows()

    for index in indexes:
        row = index.row()
        idTurma = tela.model.data(tela.model.index(row, 0))
        turma = tela.model.data(tela.model.index(row, 1))          
        qtdAlunos = tela.model.data(tela.model.index(row, 2))          
    
    print(idTurma, turma, qtdAlunos)

def verPerfil():
    # abrir a tela do perfil
    MainWindow.close()
    start() # função para inicializar a nova tela


# Configurar tabela
tela.model = QStandardItemModel()  
tela.table.setModel(tela.model)
tela.model.setHorizontalHeaderLabels(['id', 'Turmas', 'Alunos'])
tela.table.setSelectionBehavior(QAbstractItemView.SelectRows)
tela.table.setColumnWidth(0, 50)
tela.table.setColumnWidth(1, 560)
tela.table.setColumnWidth(2, 50)
adicionarTurmas()

# Coletar Dados da turma
tela.btnTurmas.clicked.connect(coletarDados)

# Ver perfil
tela.btnPerfil.clicked.connect(verPerfil)


# run
MainWindow.show()
sys.exit(app.exec_())