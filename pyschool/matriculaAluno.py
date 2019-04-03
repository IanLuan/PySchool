import sys
import os.path
import shutil
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from database.database import Database
#from interface.matriculaWindow import *
from interface.matriculaWindow import *
from endereco import *
from aluno import *
import homeServidor
import homeAdm

database = Database()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_matricularAluno()
tela.setupUi(MainWindow)


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

#Definir ícone inicial
def definirIcone():
    global foto
    pixmap = QPixmap(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    tela.lblFoto.setText(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)
    foto = os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png"


def escolherSerie():
    tela.cbGrupo.clear()
    serie = tela.cbSerie.currentText()
    grupos = database.mostrarGruposAtivos(serie)
    tela.cbGrupo.addItems(grupos)

def cadastrarAluno():
    try:
        endereco = Endereco(tela.lineRua.text(), tela.lineBairro.text(), tela.spinNumero.text(), tela.lineCep.text(),
                            tela.lineCidade.text(), tela.cbEstado.currentText())
        database.inserirEndereco(endereco)

        id_endereco = database.retornarUltimoId("endereco")

        aluno = Aluno(tela.lineNome.text(), tela.dateNascimento.text(), tela.cbSexo.currentText(), tela.lineRg.text(), tela.lineCpf.text(),
                      tela.lineTelefoneAluno.text(), id_endereco, tela.lineEmail.text(), None, tela.cbEstadoCivil.currentText(),
                              foto, None, True, tela.lineNomePai.text(), tela.lineTelefonePai.text(), tela.lineCpfPai.text(),
                      tela.lineNomeMae.text(), tela.lineTelefoneMae.text(), tela.lineCpfMae.text(), tela.cbSerie.currentText(),
                      tela.cbTipoSanguineo.currentText(), tela.cbGrupo.currentText())
        database.inserirAluno(aluno)

        

        #id_aluno = database.retornarUltimoId("aluno")
        #database.inserirEnsino(id_aluno, materias_confirmadas)

    except ValueError:
        print("Campos vazios")
    
    tela.lineNome.setText("")
    tela.cbSexo.setCurrentIndex(0)
    tela.lineRg.setText("")
    tela.lineCpf.setText("")
    tela.lineTelefoneAluno.setText("")
    tela.lineRua.setText("")
    tela.lineBairro.setText("")
    tela.spinNumero.setValue(0)
    tela.lineCep.setText("")
    tela.lineCidade.setText("")
    tela.cbEstado.setCurrentIndex(0)
    tela.lineEmail.setText("")
    tela.cbEstadoCivil.setCurrentIndex(0)
    tela.lineNomePai.setText("")
    tela.lineTelefonePai.setText("")
    tela.lineCpfPai.setText("")
    tela.lineNomeMae.setText("")
    tela.lineTelefoneMae.setText("")
    tela.lineCpfMae.setText("")
    tela.cbTipoSanguineo.setCurrentIndex(0)
    tela.cbGrupo.setCurrentIndex(0)
    tela.cbSerie.setCurrentIndex(0)
    definirIcone()

def voltarHome(id, type):
    MainWindow.close()
    if type == "administrador":
        homeAdm.startHomeAdm(id)
    else:
        homeServidor.startHomeServidor(id)


def startMatriculaAluno(id, type):
    #Definindo ícone inicial
    definirIcone()

    #Definindo séries
    series = database.mostrarSeriesAtivas()
    tela.cbSerie.addItems(series)

    #Evento de carregar foto
    tela.lblFoto.mousePressEvent = carregarFoto

    #Botão matricular acionado
    tela.btnCadatrar.clicked.connect(cadastrarAluno)

    #Escolhendo série e grupo
    tela.cbSerie.currentTextChanged.connect(escolherSerie)

    # Cancelar
    tela.btnCancelar.clicked.connect(partial(voltarHome, id, type))

    MainWindow.show()