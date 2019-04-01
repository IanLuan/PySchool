# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verCargos.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verCargos(object):
    def setupUi(self, verCargos):
        verCargos.setObjectName("verCargos")
        verCargos.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verCargos.sizePolicy().hasHeightForWidth())
        verCargos.setSizePolicy(sizePolicy)
        verCargos.setMinimumSize(QtCore.QSize(370, 380))
        verCargos.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verCargos)
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
        self.btnCargo = QtWidgets.QPushButton(self.centralwidget)
        self.btnCargo.setGeometry(QtCore.QRect(236, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCargo.sizePolicy().hasHeightForWidth())
        self.btnCargo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnCargo.setFont(font)
        self.btnCargo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCargo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCargo.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/work.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCargo.setIcon(icon)
        self.btnCargo.setObjectName("btnCargo")
        verCargos.setCentralWidget(self.centralwidget)

        self.retranslateUi(verCargos)
        QtCore.QMetaObject.connectSlotsByName(verCargos)

    def retranslateUi(self, verCargos):
        _translate = QtCore.QCoreApplication.translate
        verCargos.setWindowTitle(_translate("verCargos", "Início"))
        self.btnVoltar.setText(_translate("verCargos", "Voltar"))
        self.btnCargo.setText(_translate("verCargos", "+ Cargo"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verCargos = QtWidgets.QMainWindow()
    ui = Ui_verCargos()
    ui.setupUi(verCargos)
    verCargos.show()
    sys.exit(app.exec_())
