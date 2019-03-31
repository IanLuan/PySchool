# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeProfessor(object):
    def setupUi(self, homeProfessor):
        homeProfessor.setObjectName("homeProfessor")
        homeProfessor.resize(680, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeProfessor.sizePolicy().hasHeightForWidth())
        homeProfessor.setSizePolicy(sizePolicy)
        homeProfessor.setMinimumSize(QtCore.QSize(680, 380))
        homeProfessor.setMaximumSize(QtCore.QSize(680, 380))
        self.centralwidget = QtWidgets.QWidget(homeProfessor)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(638, 338, 32, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("")
        self.btnExit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("interface/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon)
        self.btnExit.setIconSize(QtCore.QSize(32, 32))
        self.btnExit.setFlat(True)
        self.btnExit.setObjectName("btnExit")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 660, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.btnTurmas = QtWidgets.QPushButton(self.centralwidget)
        self.btnTurmas.setGeometry(QtCore.QRect(12, 338, 211, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTurmas.sizePolicy().hasHeightForWidth())
        self.btnTurmas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnTurmas.setFont(font)
        self.btnTurmas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnTurmas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnTurmas.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("interface/icons/turma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTurmas.setIcon(icon1)
        self.btnTurmas.setObjectName("btnTurmas")
        self.btnPerfil = QtWidgets.QPushButton(self.centralwidget)
        self.btnPerfil.setGeometry(QtCore.QRect(488, 338, 143, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPerfil.sizePolicy().hasHeightForWidth())
        self.btnPerfil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPerfil.setFont(font)
        self.btnPerfil.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnPerfil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPerfil.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("interface/icons/person.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPerfil.setIcon(icon2)
        self.btnPerfil.setObjectName("btnPerfil")
        homeProfessor.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeProfessor)
        QtCore.QMetaObject.connectSlotsByName(homeProfessor)

    def retranslateUi(self, homeProfessor):
        _translate = QtCore.QCoreApplication.translate
        homeProfessor.setWindowTitle(_translate("homeProfessor", "Início"))
        self.btnExit.setToolTip(_translate("homeProfessor", "Sair"))
        self.btnTurmas.setText(_translate("homeProfessor", "Ver turma selecionada"))
        self.btnPerfil.setText(_translate("homeProfessor", "Ver Perfil"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeProfessor = QtWidgets.QMainWindow()
    ui = Ui_homeProfessor()
    ui.setupUi(homeProfessor)
    homeProfessor.show()
    sys.exit(app.exec_())
