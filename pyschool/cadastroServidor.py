import sys
import os.path
import shutil
#from pyschool.interface.cadastroServidorWindow import *
#from pyschool.servidor import *
#from pyschool.database import database
from database import database
from interface.cadastroServidorWindow import *
from servidor import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroServidor()
tela.setupUi(MainWindow)

def carregarFoto(event):
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
        new_pixmap = QPixmap(os.path.join(urlCompleta, nome_arquivo))
        new_pixmap = pixmap.scaled(150, 180, QtCore.Qt.IgnoreAspectRatio)
        tela.lblFoto.setPixmap(new_pixmap)

def cadastrarServidor():
    servidor = Servidor(tela.lineNome.text(),tela.dateNascimento.text(),tela.cbSexo.currentText(),tela.lineRg.text(),
                        tela.lineCpf.text(),tela.lineTelefone.text(),tela.lineRua.text(),tela.lineBairro.text(),tela.spinNumero.text(),tela.lineCep.text(),
                        tela.lineCidade.text(),tela.cbEstado.currentText(),tela.lineEmail.text(),tela.lineSenha.text(),tela.cbEstadoCivil.currentText(),
                        "foto",tela.rbSim.isChecked(),"Secretário")
    database.inserirServidor(servidor)

#Definir ícone inicial
pixmap = QPixmap("perfil.png")
new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
tela.lblFoto.setPixmap(new_pixmap)

#Evento de carregar foto
tela.lblFoto.mousePressEvent = carregarFoto

#Botão cadastrar acionado
tela.btnCadatrar.clicked.connect(cadastrarServidor)

MainWindow.show()
sys.exit(app.exec_())
