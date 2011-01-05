#!/usr/bin/env python


import sys
from PyQt4 import QtGui, QtCore
from main_ui import Ui_MainWindow
import AutoStart


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    p = AutoStart.AutoStart()
    a = p.ShowAll()
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connessione segnali ad eventi
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.VisualizzaProg)
      
    def VisualizzaProg(self):
        for i in range(0, len(self.a)):
            self.ui.lista.addTopLevelItem(QtGui.QTreeWidgetItem([self.a[i].Name]))
            self.ui.lista.topLevelItem(i).setIcon(0, QtGui.QIcon.fromTheme(self.a[i].Icon))
            # print(self.a[i].Name)
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.setWindowIcon(QtGui.QIcon.fromTheme("gnome-session"))
    window.show()
    sys.exit(app.exec_())
        
        
        
        
        

