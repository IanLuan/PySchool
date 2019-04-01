import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeServidorWindow import *


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeServidor()
tela.setupUi(MainWindow)

def startHomeServidor(id):
    MainWindow.show()