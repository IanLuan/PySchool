import sys
import os.path
from interface.cadastroServidorWindow import *

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
        url = "../database/images/" + nome_arquivo


        #Tratando a existência de arquivos de mesmo nome
        cont = 1
        while os.path.exists(url):
            format = "." + url.split(".")[-1]
            url_noformat = url.split(".")[:-1][-1]
            if "(" in url_noformat:
               url_noformat = url_noformat.split("(")
               url = ".." + url_noformat[0] + "(" + str(cont) + ")" + format
            else:
                url = ".." + url_noformat+ "(" + str(cont) + ")" + format
            cont = cont + 1

        pixmap.save(url)

#Definir ícone inicial
pixmap = QPixmap("../interface/icons/perfil.png")
new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
tela.lblFoto.setPixmap(new_pixmap)

#Evento de carregar foto
tela.lblFoto.mousePressEvent = carregarFoto

MainWindow.show()
sys.exit(app.exec_())
