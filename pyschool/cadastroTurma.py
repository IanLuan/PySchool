import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface.cadastroTurmaWindow import *
from interface.escolherMateriasDialog import *

import database.database as database
from turma import Turma

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_CadastroTurma()
tela.setupUi(MainWindow)

Dialog = QtWidgets.QDialog()
dialog = Ui_Dialog()
dialog.setupUi(Dialog)


def escolherMaterias():

    materias = database.mostrarMaterias()

    #Adicionar os widgets na tela uma só vez
    if dialog.layout.isEmpty():
        for i, v in enumerate(materias):
            materias[i] = QCheckBox(v)
            materias[i].setStyleSheet("font: 25 15pt \"Malgun Gothic Semilight\";\n")
            dialog.layout.addWidget(materias[i])

    dialog.btnConfirmar.clicked.connect(confirmarMaterias)

    Dialog.show()
    Dialog.exec_()

def confirmarMaterias():

    index = dialog.layout.count()
    itens = []
    for x in range(index):
        itens.append(dialog.layout.itemAt(x).widget())

    materias_selecionadas = []

    for x in itens:
        if x.isChecked():
            materias_selecionadas.append(x.text())
    Dialog.close()

    tela.lineMaterias.setText(", ".join(materias_selecionadas))
    global materias_confirmadas
    materias_confirmadas = materias_selecionadas

def verificarMaterias(event):
    
    msg = QMessageBox()
    msg.setWindowTitle("Matérias")
    msg.setText(", ".join(materias_confirmadas))
    msg.show()
    msg.exec_()


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
tela.btnMaterias.clicked.connect(escolherMaterias)
tela.btnCadastrar.clicked.connect(cadastrarTurma)

# Verificar
tela.lineMaterias.mousePressEvent = verificarMaterias


MainWindow.show()
sys.exit(app.exec_())

