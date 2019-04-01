import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeServidorWindow import *

from perfilServidor import *


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeServidor()
tela.setupUi(MainWindow)


def verPerfil(id):
    MainWindow.close()
    startPerfilServidor(id)
    

def startHomeServidor(id):

    # Ver Perfil
    tela.btnPerfil.clicked.connect(partial(verPerfil,id))

    MainWindow.show()