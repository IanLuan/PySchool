import sys
from pyschool.interface.cadastroMateriaWindow import *
from pyschool.database import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#from database import database
#from interface.cadastroServidorWindow import *

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

