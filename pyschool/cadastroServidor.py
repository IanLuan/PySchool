import sys
import os.path
import shutil
from functools import partial

#from pyschool.interface.cadastroServidorWindow import *
#from pyschool.servidor import *
#from pyschool.endereco import *
#from pyschool.database import database

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from database.database import Database
from interface.cadastroServidorWindow import *
from servidor import *
from administrador import *
from endereco import *

import homeAdm

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroServidor()
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

def cadastrarServidor():
    try:
        endereco = Endereco(tela.lineRua.text(),tela.lineBairro.text(),tela.spinNumero.text(),tela.lineCep.text(),
                            tela.lineCidade.text(),tela.cbEstado.currentText())
        database.inserirEndereco(endereco)

        id_endereco = database.retornarUltimoId("endereco")

        if tela.rbSim.isChecked():
            administrador = Administrador(tela.lineNome.text(), tela.dateNascimento.text(), tela.cbSexo.currentText(),
                                          tela.lineRg.text(), tela.lineCpf.text(), tela.lineTelefone.text(),
                                          id_endereco, tela.lineEmail.text(),
                                          tela.lineSenha.text(), tela.cbEstadoCivil.currentText(), foto, tela.cbCargo.currentText())

            database.inserirAdministrador(administrador)

        elif tela.rbNao.isChecked():
            servidor = Servidor(tela.lineNome.text(), tela.dateNascimento.text(), tela.cbSexo.currentText(), tela.lineRg.text(),
                                tela.lineCpf.text(), tela.lineTelefone.text(), id_endereco, tela.lineEmail.text(),
                                tela.lineSenha.text(), tela.cbEstadoCivil.currentText(), foto, tela.cbCargo.currentText())


            database.inserirServidor(servidor)

        else:
            raise ValueError

        tela.lineNome.setText("")
        tela.cbSexo.setCurrentIndex(0)
        tela.lineRg.setText("")
        tela.lineCpf.setText("")
        tela.lineTelefone.setText("")
        tela.lineRua.setText("")
        tela.lineBairro.setText("")
        tela.spinNumero.setValue(0)
        tela.lineCep.setText("")
        tela.lineCidade.setText("")
        tela.cbEstado.setCurrentIndex(0)
        tela.lineEmail.setText("")
        tela.lineSenha.setText("")
        tela.cbEstadoCivil.setCurrentIndex(0)
        definirIcone()
        tela.rbNao.setChecked(True)
        tela.cbCargo.setCurrentIndex(0)

        msg = QMessageBox(None)
        msg.setWindowTitle("Sucesso")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.show()
        msg.exec_()

    except ValueError:
        msg = QMessageBox(None)
        msg.setWindowTitle("Erro")
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Por favor, preencha todos os campos")
        msg.show()
        msg.exec_()

#Definir ícone inicial
def definirIcone():
    global foto
    pixmap = QPixmap(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    tela.lblFoto.setText(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)
    foto = os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png"

def startCadastroServidor(id):
    #Setando cargos no combobox Cargo
    cargos = database.mostrarCargos()
    tela.cbCargo.addItems(cargos)

    definirIcone()

    #Evento de carregar foto
    tela.lblFoto.mousePressEvent = carregarFoto

    #Botão cadastrar acionado
    tela.btnCadastrar.clicked.connect(cadastrarServidor)

    # Voltar
    tela.btnCancelar.clicked.connect(partial(voltarHome, id))

    MainWindow.show()

