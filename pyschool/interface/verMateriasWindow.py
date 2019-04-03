from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_materias(object):
    def setupUi(self, verMaterias):
        verMaterias.setObjectName("verMaterias")
        verMaterias.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verMaterias.sizePolicy().hasHeightForWidth())
        verMaterias.setSizePolicy(sizePolicy)
        verMaterias.setMinimumSize(QtCore.QSize(370, 380))
        verMaterias.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verMaterias)
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
        self.btnMateria = QtWidgets.QPushButton(self.centralwidget)
        self.btnMateria.setGeometry(QtCore.QRect(236, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMateria.sizePolicy().hasHeightForWidth())
        self.btnMateria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnMateria.setFont(font)
        self.btnMateria.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnMateria.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnMateria.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/materias.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMateria.setIcon(icon)
        self.btnMateria.setObjectName("btnMateria")
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
        verMaterias.setCentralWidget(self.centralwidget)

        self.retranslateUi(verMaterias)
        QtCore.QMetaObject.connectSlotsByName(verMaterias)

    def retranslateUi(self, verMaterias):
        _translate = QtCore.QCoreApplication.translate
        verMaterias.setWindowTitle(_translate("verMateria", "Início"))
        self.btnVoltar.setText(_translate("verMateria", "Voltar"))
        self.btnMateria.setText(_translate("verMateria", "+ Matéria"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verMaterias = QtWidgets.QMainWindow()
    ui = Ui_materias()
    ui.setupUi(verMaterias)
    verMaterias.show()
    sys.exit(app.exec_())

