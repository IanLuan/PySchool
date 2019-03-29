import sys
from pyschool.interface.cadastroCargoWindow import *
from pyschool.database import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#from database import database
#from interface.cadastroServidorWindow import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroCargo()
tela.setupUi(MainWindow)

def cadastrarCargo():
    database.inserirCargo(tela.lineCargo.text())
    tela.lineCargo.setText("")

tela.btnCadastrar.clicked.connect(cadastrarCargo)

MainWindow.show()
sys.exit(app.exec_())
