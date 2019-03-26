import PyQt5

app = QtWidgets.QApplication([])
tela = uic.loadUi("cadastroServidor.ui")
tela.show()
sys.exit(app.exec_())