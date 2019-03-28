import sys
from pyschool.interface.cadastroProfessorWindow import *
from pyschool.servidor import *
from pyschool.endereco import *
from pyschool.database import database
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#from database import database
#from interface.cadastroServidorWindow import *
#from servidor import *
#from endereco import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroProfessor()
tela.setupUi(MainWindow)

MainWindow.show()
sys.exit(app.exec_())