import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface.cadastroTurmaWindow import *

import database.database as database
from turma import Turma

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_CadastroTurma()
tela.setupUi(MainWindow)

def escolherSerie():
    if tela.cbSerie.currentText() == "Outro":
        tela.lineSerie.setReadOnly(False)
        tela.lineSerie.setText("")
    else:
        tela.lineSerie.setReadOnly(True)
        tela.lineSerie.setText(tela.cbSerie.currentText())

def cadastrarTurma():

    # Pegar dados
    if tela.lineSerie.text() != "":
        serie = tela.lineSerie.text()
    else:
        serie = tela.cbSerie.currentText()

    turma = Turma(serie, tela.lineGrupo.text(), tela.spinMax.text(), True)


    # Salvar no Banco
    database.inserirTurma(turma)

    # Limpar campos
    tela.cbSerie.setCurrentIndex(0)
    tela.lineSerie.setText("")
    tela.lineGrupo.setText("")
    tela.spinMax.setValue(30)

     

# Escolhendo Série
tela.lineSerie.setText(tela.cbSerie.currentText())
tela.cbSerie.currentTextChanged.connect(escolherSerie)
tela.btnCadastrar.clicked.connect(cadastrarTurma)

MainWindow.show()
sys.exit(app.exec_())

