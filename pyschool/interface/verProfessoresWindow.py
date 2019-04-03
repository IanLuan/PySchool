# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verProfessores.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verProfessores(object):
    def setupUi(self, verProfessores):
        verProfessores.setObjectName("verProfessores")
        verProfessores.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verProfessores.sizePolicy().hasHeightForWidth())
        verProfessores.setSizePolicy(sizePolicy)
        verProfessores.setMinimumSize(QtCore.QSize(370, 380))
        verProfessores.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verProfessores)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 350, 321))
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
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setCornerButtonEnabled(False)
        self.table.verticalHeader().setVisible(False)
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
        self.btnProfessores = QtWidgets.QPushButton(self.centralwidget)
        self.btnProfessores.setGeometry(QtCore.QRect(210, 338, 149, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProfessores.sizePolicy().hasHeightForWidth())
        self.btnProfessores.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnProfessores.setFont(font)
        self.btnProfessores.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnProfessores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProfessores.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/alunos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProfessores.setIcon(icon)
        self.btnProfessores.setObjectName("btnProfessores")
        verProfessores.setCentralWidget(self.centralwidget)

        self.retranslateUi(verProfessores)
        QtCore.QMetaObject.connectSlotsByName(verProfessores)

    def retranslateUi(self, verProfessores):
        _translate = QtCore.QCoreApplication.translate
        verProfessores.setWindowTitle(_translate("verProfessores", "Professores"))
        self.btnVoltar.setText(_translate("verProfessores", "Voltar"))
        self.btnProfessores.setText(_translate("verProfessores", "+ Professores"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verProfessores = QtWidgets.QMainWindow()
    ui = Ui_verProfessores()
    ui.setupUi(verProfessores)
    verProfessores.show()
    sys.exit(app.exec_())
