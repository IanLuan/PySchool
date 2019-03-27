import sys
from interface.cadastroServidorWindow import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroServidor()
tela.setupUi(MainWindow)

def enviarFoto(event):
    image = QFileDialog.getOpenFileName(None, 'Escolher foto', '', "Images(*.png *.jpeg *.jpg)")
    imagePath = image[0]
    if image[0] != "":
        pixmap = QPixmap(imagePath)
        new_pixmap = pixmap.scaled(150, 180, QtCore.Qt.IgnoreAspectRatio)

        #Setando foto no label
        tela.lblFoto.setPixmap(new_pixmap)

        #Salvando na pasta
        url = "../database/images/servidor.png"
        pixmap.save(url, "PNG")

#Definir ícone inicial
pixmap = QPixmap("../interface/icons/perfil.png")
new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
tela.lblFoto.setPixmap(new_pixmap)

#Evento de carregar foto
tela.lblFoto.mousePressEvent = enviarFoto

MainWindow.show()
sys.exit(app.exec_())
