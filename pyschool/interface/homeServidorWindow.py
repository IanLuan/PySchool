# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeServidor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeServidor(object):
    def setupUi(self, HomeServidor):
        HomeServidor.setObjectName("HomeServidor")
        HomeServidor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(HomeServidor)
        self.centralwidget.setObjectName("centralwidget")
        HomeServidor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeServidor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        HomeServidor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeServidor)
        self.statusbar.setObjectName("statusbar")
        HomeServidor.setStatusBar(self.statusbar)

        self.retranslateUi(HomeServidor)
        QtCore.QMetaObject.connectSlotsByName(HomeServidor)

    def retranslateUi(self, HomeServidor):
        _translate = QtCore.QCoreApplication.translate
        HomeServidor.setWindowTitle(_translate("HomeServidor", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeServidor = QtWidgets.QMainWindow()
    ui = Ui_HomeServidor()
    ui.setupUi(HomeServidor)
    HomeServidor.show()
    sys.exit(app.exec_())

