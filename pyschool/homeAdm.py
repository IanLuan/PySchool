import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.homeAdmWindow import *


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_homeAdm()
tela.setupUi(MainWindow)

def startHomeAdm(id):
    MainWindow.show()