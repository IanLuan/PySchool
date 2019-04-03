from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_servidores(object):
    def setupUi(self, verServidores):
        verServidores.setObjectName("verServidores")
        verServidores.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verServidores.sizePolicy().hasHeightForWidth())
        verServidores.setSizePolicy(sizePolicy)
        verServidores.setMinimumSize(QtCore.QSize(370, 380))
        verServidores.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verServidores)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(12, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVoltar.sizePolicy().hasHeightForWidth())
        self.btnVoltar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnVoltar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnVoltar.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        self.btnVoltar.setObjectName("btnVoltar")
        self.btnServidores = QtWidgets.QPushButton(self.centralwidget)
        self.btnServidores.setGeometry(QtCore.QRect(236, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnServidores.sizePolicy().hasHeightForWidth())
        self.btnServidores.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnServidores.setFont(font)
        self.btnServidores.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnServidores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnServidores.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/alunos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnServidores.setIcon(icon)
        self.btnServidores.setObjectName("btnServidores")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 351, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.setStyleSheet("QHeaderView::section {\n"
        "border: 2px solid rgb(255, 123, 28);\n"
        "border-radius: 15px;\n"
        "background-color: rgb(255, 123, 28);\n"
        "color: #fff;\n"
        "font-size: 12px;\n"
        " }\n"
        "\n"
        "QTableView {\n"
        "background-color: #fff;\n"
        "selection-background-color: rgb(255, 123, 28);\n"
        "selection-color: #fff;\n"
        "color: rgb(255, 123, 28); }")
        self.table.setObjectName("table")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setCornerButtonEnabled(False)
        self.table.verticalHeader().setVisible(False)
        verServidores.setCentralWidget(self.centralwidget)

        self.retranslateUi(verServidores)
        QtCore.QMetaObject.connectSlotsByName(verServidores)

    def retranslateUi(self, verServidores):
        _translate = QtCore.QCoreApplication.translate
        verServidores.setWindowTitle(_translate("verMateria", "Início"))
        self.btnVoltar.setText(_translate("verMateria", "Voltar"))
        self.btnServidores.setText(_translate("verMateria", "+ Servidor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verServidores = QtWidgets.QMainWindow()
    ui = Ui_servidores()
    ui.setupUi(verServidores)
    verServidores.show()
    sys.exit(app.exec_())

