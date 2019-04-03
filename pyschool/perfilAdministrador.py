import sys
import os.path
import shutil

from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

from interface.perfilAdministradorWindow import *
from database.database import Database
from administrador import *
from endereco import *
import homeAdm

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_perfilAdministrador()
tela.setupUi(MainWindow)
database = Database()


def voltarHome(id):
    MainWindow.close()
    homeAdm.startHomeAdm(id)


def carregarFoto(event):
    global foto
    image = QFileDialog.getOpenFileName(None, 'Escolher foto', '', "Images(*.png *.jpeg *.jpg)")
    imagePath = image[0]

    if image[0] != "":
        pixmap = QPixmap(imagePath)

        #Salvando na pasta
        nome_arquivo = imagePath.split("/")[-1]

        # Pegar o endereço da pessoa + a pasta do projeto
        url = "/database/images/"
        urlCompleta = os.path.dirname(os.path.abspath(__file__)) + url

        # Tratando existência
        repetido = False
        cont = 1
        while os.path.exists(urlCompleta + nome_arquivo):
            repetido = True
            nome_arquivo = nome_arquivo.split(".")
            if cont == 1:
                nome_arquivo = nome_arquivo[0] + "({})".format(cont) + "." + nome_arquivo[-1]
            else:
                nome_arquivo = nome_arquivo[0][:-3] + "({})".format(cont) + "." + nome_arquivo[-1]
            cont += 1

        # Copia a imagem para a url dada
        if repetido:
            shutil.copy(imagePath, os.path.join(urlCompleta, nome_arquivo))
        else:
            shutil.copy(imagePath, urlCompleta)

        #Setando foto no label
        foto = os.path.join(urlCompleta, nome_arquivo)
        new_pixmap = QPixmap(os.path.join(urlCompleta, nome_arquivo))
        new_pixmap = new_pixmap.scaled(150, 180, QtCore.Qt.IgnoreAspectRatio)
        tela.lblFoto.setPixmap(new_pixmap)

def editarAdministrador(id):

    try:
        endereco = Endereco(tela.lineRua.text(), tela.lineBairro.text(), tela.spinNumero.text(), tela.lineCep.text(),
                            tela.lineCidade.text(), tela.cbEstado.currentText())
        database.updateEndereco(endereco, id, "administrador")

        id_endereco = database.retornarIdEndereco(id, "administrador")

        administrador = Administrador(tela.lineNome.text(), tela.dateNascimento.text(), tela.cbSexo.currentText(),
                                      tela.lineRg.text(), tela.lineCpf.text(), tela.lineTelefone.text(),
                                      id_endereco, tela.lineEmail.text(), tela.lineSenha.text(), tela.cbEstadoCivil.currentText(), foto,
                                      tela.cbCargo.currentText())
        database.updateAdministrador(id, administrador)

        msg = QMessageBox(None)
        msg.setWindowTitle("Sucesso")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Dados atualizados com sucesso!")
        msg.exec_()
        msg.show()

    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, preencha todos os campos")
        msg.show()
        msg.exec_()

def startPerfilAdm(id):
    administrador = database.mostrarDadosAdministrador(id)

    cargos = database.mostrarCargos()
    tela.cbCargo.addItems(cargos)

    data= administrador.getNascimento()
    dia, mes, ano = data.split("/")
    tela.dateNascimento.setDate(QtCore.QDate(int(ano), int(mes), int(dia)))
    tela.lineNome.setText(administrador.getNome())
    tela.cbSexo.setCurrentText(administrador.getSexo())
    tela.lineRg.setText(administrador.getRg())
    tela.lineCpf.setText(administrador.getCpf())
    tela.lineTelefone.setText(administrador.getTelefone())
    tela.lineRua.setText(administrador.getEndereco().getRua())
    tela.lineBairro.setText(administrador.getEndereco().getBairro())
    tela.spinNumero.setValue(int(administrador.getEndereco().getNumero()))
    tela.lineCep.setText(administrador.getEndereco().getCep())
    tela.lineCidade.setText(administrador.getEndereco().getCidade())
    tela.cbEstado.setCurrentText(administrador.getEndereco().getEstado())
    tela.lineEmail.setText(administrador.getEmail())
    tela.cbEstadoCivil.setCurrentText(administrador.getEstadoCivil())
    tela.cbCargo.setCurrentText(administrador.getCargo())
    tela.lineSenha.setText(administrador.getSenha())

    global foto
    split = administrador.getFoto().split("pyschool/")
    foto = os.path.dirname(os.path.abspath(__file__)) + "/" + split[1]
    pixmap = QPixmap(foto)
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)

    tela.btnEditar.clicked.connect(partial(editarAdministrador, id))
    tela.lblFoto.mousePressEvent = carregarFoto

    tela.btnVoltar.clicked.connect(partial(voltarHome, id))

    MainWindow.show()

