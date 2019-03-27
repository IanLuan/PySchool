import sys
import os.path
import shutil
from interface.cadastroServidorWindow import *
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroServidor()
tela.setupUi(MainWindow)

def carregarFoto(event):
    image = QFileDialog.getOpenFileName(None, 'Escolher foto', '', "Images(*.png *.jpeg *.jpg)")
    imagePath = image[0]

    if image[0] != "":
        pixmap = QPixmap(imagePath)
        new_pixmap = pixmap.scaled(150, 180, QtCore.Qt.IgnoreAspectRatio)

        #Setando foto no label
        tela.lblFoto.setPixmap(new_pixmap)

        #Salvando na pasta
        nome_arquivo = imagePath.split("/")[-1]

        # Pegar o endereço da pessoa + a pasta do projeto
        url = "/PySchool/pyschool/database/images/"
        urlCompleta = os.getcwd() + url
        
        # Pegar Url das Imagens
        urlImages = url.split("/")
        urlImages = [x for x in urlImages if x != ""]
        urlImages = urlImages[2] +"/"+ urlImages[3] + "/"


        # Tratando existência
        repetido = False
        cont = 1
        while os.path.exists(urlCompleta + nome_arquivo):
            repetido = True
            nome_arquivo = nome_arquivo.split(".")
            if cont == 1:
                nome_arquivo = nome_arquivo[0] + "{}".format(cont) + "." + nome_arquivo[-1]
            else:
                nome_arquivo = nome_arquivo[0][:-1] + "{}".format(cont) + "." + nome_arquivo[-1]
            cont += 1

        #Tem que ver como tratar a existência
        """cont = 1
        while os.path.exists(url):
            format = "." + url.split(".")[-1]
            url_noformat = url.split(".")[:-1][-1]
            if "(" in url_noformat:
               url_noformat = url_noformat.split("(")
               url = url_noformat[0] + "(" + str(cont) + ")" + format
            else:
                url = url_noformat+ "(" + str(cont) + ")" + format
            cont = cont + 1"""

        # Copia a imagem para a url dada
        if repetido:
            shutil.copy(imagePath, os.path.join(urlCompleta, nome_arquivo))
        else:
            shutil.copy(imagePath, urlCompleta)

#Definir ícone inicial
pixmap = QPixmap("interface/icons/perfil.png")
new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
tela.lblFoto.setPixmap(new_pixmap)

#Evento de carregar foto
tela.lblFoto.mousePressEvent = carregarFoto

MainWindow.show()
sys.exit(app.exec_())
