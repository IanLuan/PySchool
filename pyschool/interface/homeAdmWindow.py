# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeAdm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_homeAdm(object):
    def setupUi(self, homeAdm):
        homeAdm.setObjectName("homeAdm")
        homeAdm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(homeAdm)
        self.centralwidget.setObjectName("centralwidget")
        homeAdm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homeAdm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        homeAdm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homeAdm)
        self.statusbar.setObjectName("statusbar")
        homeAdm.setStatusBar(self.statusbar)

        self.retranslateUi(homeAdm)
        QtCore.QMetaObject.connectSlotsByName(homeAdm)

    def retranslateUi(self, homeAdm):
        _translate = QtCore.QCoreApplication.translate
        homeAdm.setWindowTitle(_translate("homeAdm", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeAdm = QtWidgets.QMainWindow()
    ui = Ui_homeAdm()
    ui.setupUi(homeAdm)
    homeAdm.show()
    sys.exit(app.exec_())

