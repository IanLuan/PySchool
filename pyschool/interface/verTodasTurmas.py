# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verTodasTurmas.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verTurmas(object):
    def setupUi(self, verTurmas):
        verTurmas.setObjectName("verTurmas")
        verTurmas.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verTurmas.sizePolicy().hasHeightForWidth())
        verTurmas.setSizePolicy(sizePolicy)
        verTurmas.setMinimumSize(QtCore.QSize(370, 380))
        verTurmas.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verTurmas)
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
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setCornerButtonEnabled(False)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setDefaultSectionSize(0)
        self.table.horizontalHeader().setMinimumSectionSize(0)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(0)
        self.table.verticalHeader().setMinimumSectionSize(0)
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
        self.btnTurma = QtWidgets.QPushButton(self.centralwidget)
        self.btnTurma.setGeometry(QtCore.QRect(236, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTurma.sizePolicy().hasHeightForWidth())
        self.btnTurma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTurma.setFont(font)
        self.btnTurma.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnTurma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnTurma.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/turma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTurma.setIcon(icon)
        self.btnTurma.setObjectName("btnTurma")
        verTurmas.setCentralWidget(self.centralwidget)

        self.retranslateUi(verTurmas)
        QtCore.QMetaObject.connectSlotsByName(verTurmas)

    def retranslateUi(self, verTurmas):
        _translate = QtCore.QCoreApplication.translate
        verTurmas.setWindowTitle(_translate("verTurmas", "Início"))
        self.btnVoltar.setText(_translate("verTurmas", "Voltar"))
        self.btnTurma.setText(_translate("verTurmas", "+Turma"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verTurmas = QtWidgets.QMainWindow()
    ui = Ui_verTurmas()
    ui.setupUi(verTurmas)
    verTurmas.show()
    sys.exit(app.exec_())
