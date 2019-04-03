import sys
import os.path
import shutil

from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

from interface.perfilProfessorWindow import *
from database.database import Database
import homeProfessor

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_perfilProfessor()
tela.setupUi(MainWindow)
database_professor = Database()


def voltarHome(id):
    MainWindow.close()
    homeProfessor.startHomeProfessor(id)

def verMaterias(professor):
    msg = QMessageBox()
    msg.setWindowTitle("Matérias")
    msg.setIcon(QMessageBox.Information)
    msg.setText("\n".join(professor.getMateria()))
    msg.show()
    msg.exec_()

# Inicializar tela
def startPerfilProfessor(id):
    professor = database_professor.mostrarDadosProfessor(id)

    data= professor.getNascimento()
    dia, mes, ano = data.split("/")
    tela.dateNascimento.setDate(QtCore.QDate(int(ano), int(mes), int(dia)))
    tela.lineNome.setText(professor.getNome())
    tela.cbSexo.setCurrentText(professor.getSexo())
    tela.lineRg.setText(professor.getRg())
    tela.lineCpf.setText(professor.getCpf())
    tela.lineTelefone.setText(professor.getTelefone())
    tela.lineRua.setText(professor.getEndereco().getRua())
    tela.lineBairro.setText(professor.getEndereco().getBairro())
    tela.spinNumero.setValue(int(professor.getEndereco().getNumero()))
    tela.lineCep.setText(professor.getEndereco().getCep())
    tela.lineCidade.setText(professor.getEndereco().getCidade())
    tela.cbEstado.setCurrentText(professor.getEndereco().getEstado())
    tela.lineEmail.setText(professor.getEmail())
    tela.cbEstadoCivil.setCurrentText(professor.getEstadoCivil())

    split = professor.getFoto().split("pyschool/")
    foto = os.path.dirname(os.path.abspath(__file__)) + "/" + split[1]
    pixmap = QPixmap(foto)
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)

    tela.btnMaterias.clicked.connect(partial(verMaterias,professor))
    tela.btnCancelar.clicked.connect(partial(voltarHome, id))

    MainWindow.show()