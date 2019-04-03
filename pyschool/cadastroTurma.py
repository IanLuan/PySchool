import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface.cadastroTurmaWindow import *
from interface.escolherMateriasDialog import *

from database.database import Database
from turma import Turma

database = Database()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_CadastroTurma()
tela.setupUi(MainWindow)

Dialog = QtWidgets.QDialog()
dialog = Ui_Dialog()
dialog.setupUi(Dialog)

global materias_confirmadas
materias_confirmadas = ""

def escolherMaterias():

    materias = database.mostrarMateriasProfessor()

    for i, mat_prof in enumerate(materias):
        materias[i] = mat_prof[0] + " - Prof. "+ mat_prof[1]

    #Adicionar os widgets na tela uma só vez
    if dialog.layout.isEmpty():
        for i, v in enumerate(materias):
            materias[i] = QCheckBox(v)
            materias[i].setStyleSheet("font: 25 15pt \"Malgun Gothic Semilight\";\n")
            dialog.layout.addWidget(materias[i])

    dialog.btnConfirmar.clicked.connect(confirmarMaterias)

    Dialog.exec_()
    Dialog.show()


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
    msg.setIcon(QMessageBox.Information)
    msg.setText("\n".join(materias_confirmadas))
    msg.exec_()
    msg.show()


def escolherSerie():
    if tela.cbSerie.currentText() == "Outro":
        tela.lineSerie.setReadOnly(False)
        tela.lineSerie.setText("")
    else:
        tela.lineSerie.setReadOnly(True)
        tela.lineSerie.setText(tela.cbSerie.currentText())

def cadastrarTurma():

    try:
        if materias_confirmadas == "":
            raise ValueError

        # Pegar dados
        if tela.lineSerie.text() != "":
            serie = tela.lineSerie.text()
        else:
            serie = tela.cbSerie.currentText()

        turma = Turma(serie, tela.spinMax.text(), tela.lineGrupo.text(), True)

        # Salvar no Banco
        database.inserirTurma(turma)

        # Criando classe
        database.inserirClasse(materias_confirmadas)

        # Limpar campos
        tela.cbSerie.setCurrentIndex(0)
        tela.lineSerie.setText("")
        tela.lineGrupo.setText("")
        tela.lineMaterias.setText("")
        tela.spinMax.setValue(30)

        #Limpando checkbox
        index = dialog.layout.count()
        for x in range(index):
            dialog.layout.itemAt(x).widget().setCheckState(False)

        #Setando novas turmas ao cbBox
        tela.cbSerie.clear()
        series = []
        series = database.mostrarSeries()
        series.append("Outro")
        tela.cbSerie.addItems(series)

        msg = QMessageBox(None)
        msg.setWindowTitle("Sucesso")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()
        msg.show()

    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, escolha a(s) matéria(s) da turma")
        msg.exec_()
        msg.show()

def startCadastroTurma(id):
    #Adicionando Séries ao CbBox
    series = database.mostrarSeries()
    series.append("Outro")
    tela.cbSerie.addItems(series)

    # Escolhendo Série
    tela.lineSerie.setText(tela.cbSerie.currentText())
    tela.cbSerie.currentTextChanged.connect(escolherSerie)
    tela.btnMaterias.clicked.connect(escolherMaterias)
    tela.btnCadastrar.clicked.connect(cadastrarTurma)

    # Verificar
    tela.lineMaterias.mousePressEvent = verificarMaterias


    MainWindow.show()

