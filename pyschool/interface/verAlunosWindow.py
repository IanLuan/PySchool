# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verAlunos.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verAlunos(object):
    def setupUi(self, verAlunos):
        verAlunos.setObjectName("verAlunos")
        verAlunos.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verAlunos.sizePolicy().hasHeightForWidth())
        verAlunos.setSizePolicy(sizePolicy)
        verAlunos.setMinimumSize(QtCore.QSize(370, 380))
        verAlunos.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verAlunos)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tableCargos = QtWidgets.QTableView(self.centralwidget)
        self.tableCargos.setGeometry(QtCore.QRect(10, 10, 350, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableCargos.setFont(font)
        self.tableCargos.setStyleSheet("QHeaderView::section {\n"
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
        self.tableCargos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableCargos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCargos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCargos.setCornerButtonEnabled(False)
        self.tableCargos.setObjectName("tableCargos")
        self.tableCargos.horizontalHeader().setDefaultSectionSize(0)
        self.tableCargos.horizontalHeader().setMinimumSectionSize(0)
        self.tableCargos.verticalHeader().setVisible(False)
        self.tableCargos.verticalHeader().setDefaultSectionSize(0)
        self.tableCargos.verticalHeader().setMinimumSectionSize(0)
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
        self.btnAlunos = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlunos.setGeometry(QtCore.QRect(236, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAlunos.sizePolicy().hasHeightForWidth())
        self.btnAlunos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAlunos.setFont(font)
        self.btnAlunos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnAlunos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAlunos.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/alunos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlunos.setIcon(icon)
        self.btnAlunos.setObjectName("btnAlunos")
        verAlunos.setCentralWidget(self.centralwidget)

        self.retranslateUi(verAlunos)
        QtCore.QMetaObject.connectSlotsByName(verAlunos)

    def retranslateUi(self, verAlunos):
        _translate = QtCore.QCoreApplication.translate
        verAlunos.setWindowTitle(_translate("verAlunos", "Alunos"))
        self.btnVoltar.setText(_translate("verAlunos", "Voltar"))
        self.btnAlunos.setText(_translate("verAlunos", "+ Alunos"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verAlunos = QtWidgets.QMainWindow()
    ui = Ui_verAlunos()
    ui.setupUi(verAlunos)
    verAlunos.show()
    sys.exit(app.exec_())
