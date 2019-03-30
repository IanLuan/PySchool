import sys
from interface.cadastroMateriaWindow import *
from database import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroMateria()
tela.setupUi(MainWindow)

def cadastrarMateria():
    database.inserirMateria(tela.lineMateria.text())
    tela.lineMateria.setText("")

tela.btnCadastrar.clicked.connect(cadastrarMateria)

MainWindow.show()
sys.exit(app.exec_())

