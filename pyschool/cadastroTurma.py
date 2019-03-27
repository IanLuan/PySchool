import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface.cadastroTurmaWindow import *

from turma import Turma

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = CadastroTurmaTela()
tela.setupUi(MainWindow)

def escolherSerie():
    if tela.cbSerie.currentText() == "Outro":
        tela.lineSerie.setReadOnly(False)
    else:
        tela.lineSerie.setReadOnly(True)
        tela.lineSerie.setText("")
    

def cadastrarTurma():

    # Pegar dados
    if tela.lineSerie.text() != "":
        serie = tela.lineSerie.text()
    else:
        serie = tela.cbSerie.currentText()

    turma = Turma(serie, tela.lineGrupo.text(), tela.spinMax.text())


    # Salvar no Banco

    # Limpar campos
    tela.lineSerie.setText("")
    tela.lineGrupo.setText("")
    tela.spinMax.setValue(30)


     

# Escolhendo Série
tela.cbSerie.currentTextChanged.connect(escolherSerie)
tela.btnCadastrar.clicked.connect(cadastrarTurma)

MainWindow.show()
sys.exit(app.exec_())

