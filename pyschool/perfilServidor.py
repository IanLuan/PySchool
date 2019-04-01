import sys
import os.path
import shutil
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface.perfilServidorWindow import *
from database.database import Database
import homeServidor


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_perfilServidor()
tela.setupUi(MainWindow)
database = Database()


def voltarHome(id):
    MainWindow.close()
    homeServidor.startHomeServidor(id)


# Inicializar tela
def startPerfilServidor(id):
    servidor = database.mostrarDadosServidor(id)

    tela.lineNome.setText(servidor.getNome())
    tela.cbSexo.setCurrentText(servidor.getSexo())
    tela.lineRg.setText(servidor.getRg())
    tela.lineCpf.setText(servidor.getCpf())
    tela.lineTelefone.setText(servidor.getTelefone())
    tela.lineRua.setText(servidor.getEndereco().getRua())
    tela.lineBairro.setText(servidor.getEndereco().getBairro())
    tela.spinNumero.setValue(int(servidor.getEndereco().getNumero()))
    tela.lineCep.setText(servidor.getEndereco().getCep())
    tela.lineCidade.setText(servidor.getEndereco().getCidade())
    tela.cbEstado.setCurrentText(servidor.getEndereco().getEstado())
    tela.lineEmail.setText(servidor.getEmail())
    tela.cbEstadoCivil.setCurrentText(servidor.getEstadoCivil())
    tela.cbCargo.setCurrentText(servidor.getCargo())

    split = servidor.getFoto().split("pyschool/")
    foto = os.path.dirname(os.path.abspath(__file__)) + "/" + split[1]
    pixmap = QPixmap(foto)
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)

    tela.btnVoltar.clicked.connect(partial(voltarHome,id))

    MainWindow.show()