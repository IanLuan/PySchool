import sys
import os.path
import shutil

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#from interface.escolherMateriasDialog import *
from pyschool.interface.escolherMateriasDialog import *
#from database import database
from pyschool.database import database
#from interface.cadastroProfessorWindow import *
from pyschool.interface.perfilProfessorWindow import *
#from endereco import *
from pyschool.endereco import *
#from professor import *
from pyschool.professor import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_perfilProfessor()
tela.setupUi(MainWindow)

professor = database.mostrarDadosProfessor(4)
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

def verMaterias():
    msg = QMessageBox()
    msg.setWindowTitle("Matérias")
    msg.setIcon(QMessageBox.Information)
    msg.setText("\n".join(professor.getMateria()))
    msg.show()
    msg.exec_()

tela.btnMaterias.clicked.connect(verMaterias)

MainWindow.show()
sys.exit(app.exec_())
