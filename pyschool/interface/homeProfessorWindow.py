# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeProfessor(object):
    def setupUi(self, homeProfessor):
        homeProfessor.setObjectName("homeProfessor")
        homeProfessor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(homeProfessor)
        self.centralwidget.setObjectName("centralwidget")
        homeProfessor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homeProfessor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        homeProfessor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homeProfessor)
        self.statusbar.setObjectName("statusbar")
        homeProfessor.setStatusBar(self.statusbar)

        self.retranslateUi(homeProfessor)
        QtCore.QMetaObject.connectSlotsByName(homeProfessor)

    def retranslateUi(self, homeProfessor):
        _translate = QtCore.QCoreApplication.translate
        homeProfessor.setWindowTitle(_translate("homeProfessor", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeProfessor = QtWidgets.QMainWindow()
    ui = Ui_homeProfessor()
    ui.setupUi(homeProfessor)
    homeProfessor.show()
    sys.exit(app.exec_())

