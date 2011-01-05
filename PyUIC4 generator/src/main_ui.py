# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/alcko/Aptana Studio Workspace/PyUIC4 generator/main.ui'
#
# Created: Wed Jan  5 13:28:07 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 16, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Xcheck = QtGui.QCheckBox(self.centralwidget)
        self.Xcheck.setChecked(True)
        self.Xcheck.setObjectName("Xcheck")
        self.horizontalLayout_2.addWidget(self.Xcheck)
        self.Dcheck = QtGui.QCheckBox(self.centralwidget)
        self.Dcheck.setObjectName("Dcheck")
        self.horizontalLayout_2.addWidget(self.Dcheck)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.filelistw = QtGui.QListWidget(self.centralwidget)
        self.filelistw.setObjectName("filelistw")
        self.verticalLayout.addWidget(self.filelistw)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearbtn = QtGui.QPushButton(self.centralwidget)
        self.clearbtn.setObjectName("clearbtn")
        self.horizontalLayout.addWidget(self.clearbtn)
        self.removebtn = QtGui.QPushButton(self.centralwidget)
        self.removebtn.setObjectName("removebtn")
        self.horizontalLayout.addWidget(self.removebtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addbtn = QtGui.QPushButton(self.centralwidget)
        self.addbtn.setObjectName("addbtn")
        self.horizontalLayout.addWidget(self.addbtn)
        self.gobtn = QtGui.QPushButton(self.centralwidget)
        self.gobtn.setObjectName("gobtn")
        self.horizontalLayout.addWidget(self.gobtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyUIC4 GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.Xcheck.setText(QtGui.QApplication.translate("MainWindow", "Generate running code (-x)", None, QtGui.QApplication.UnicodeUTF8))
        self.Dcheck.setText(QtGui.QApplication.translate("MainWindow", "Debug info about the process (-d)", None, QtGui.QApplication.UnicodeUTF8))
        self.clearbtn.setText(QtGui.QApplication.translate("MainWindow", "Clear list", None, QtGui.QApplication.UnicodeUTF8))
        self.removebtn.setText(QtGui.QApplication.translate("MainWindow", "Remove item", None, QtGui.QApplication.UnicodeUTF8))
        self.addbtn.setText(QtGui.QApplication.translate("MainWindow", "Add .ui files", None, QtGui.QApplication.UnicodeUTF8))
        self.gobtn.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

