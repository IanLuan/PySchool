import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeProfessorWindow import *
import random

# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeProfessor()
tela.setupUi(MainWindow)

def populate():

    turmas = [("história", 50), ("matemática", 25), ("ciências", 35)]

    for tupla in turmas:
        row = []
        row.append(QStandardItem(tupla[0]))
        row.append(QStandardItem(str(tupla[1])))
        tela.model.appendRow(row)


tela.model = QStandardItemModel()  # SELECTING THE MODEL - FRAMEWORK THAT HANDLES QUERIES AND EDITS
tela.table.setModel(tela.model)  # SETTING THE MODEL
tela.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
tela.model.setHorizontalHeaderLabels(['Turmas', 'Alunos'])
tela.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
tela.table.setColumnWidth(0, 560)
tela.table.setColumnWidth(1, 70)
populate()



# run
MainWindow.show()
sys.exit(app.exec_())