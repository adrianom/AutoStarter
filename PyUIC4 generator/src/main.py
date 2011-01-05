#!/usr/bin/env python
'''
Created on 05/gen/2011
Semplice interfaccia grafica per pyuic4
Permette di aggiungere un'insieme di file di tipo ui(creati con QT Designer) e di convertirli
in file python, utilizzando il comando pyuic4 -o <file_output.py> [-x] <file_input.ui>
il parametro -o restituisce l'output su file
il parametro -x inserisce codice extra per l'esecuzione della classe
@author: alcko
'''
import sys
from PyQt4 import QtGui, QtCore
from main_ui import Ui_MainWindow
import commands
import os

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    __filenames = [] #lista globale,tiene conto della coda dei file(compresi path) da convertire
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connessione segnali ad eventi
        self.connect(self.ui.addbtn, QtCore.SIGNAL("clicked()"), self.Add_files)
        self.connect(self.ui.clearbtn, QtCore.SIGNAL("clicked()"), self.Clear)
        self.connect(self.ui.removebtn, QtCore.SIGNAL("clicked()"), self.Remove)
        self.connect(self.ui.gobtn, QtCore.SIGNAL("clicked()"), self.Convert)

        #Carico informazioni inziali sulla statusbar: verifico l'esistenza di pyuic4 e ne visualizzo la versione
        try:
            self.statusBar().showMessage(commands.getoutput('pyuic4 --version') + ' is Ready!')
        except:
            self.statusBar().showMessage('Pyuic4 not found!')
            self.ui.centralwidget.setEnabled(False)
    def Convert(self):
        for i  in self.__filenames:
            i = str(i)
            myparams = '-x'
            myoutfilename = os.path.dirname(i) + '/' + os.path.splitext(os.path.basename(i))[0] + "_ui.py'"
            os.system("pyuic4 -o '" + myoutfilename + ' ' + myparams + ' ' + "'" + i + "'")
        
            
    def Remove(self):
        if(self.ui.filelistw.count() > 0): #se ci sono elementi da eliminare
            del self.__filenames[self.ui.filelistw.currentRow()]
            self.ui.filelistw.takeItem(self.ui.filelistw.currentRow())
            
    def Clear(self):       
        self.__filenames = []
        self.ui.filelistw.clear()
        
    def Add_files(self): #dipende da QtGUi
        self.__filenames = QtGui.QFileDialog.getOpenFileNames(self, "Add .ui files...", sys.path[0], 'QtDesigner UI files (*.ui)')
        self.__filenames = self.Check_UIfiles(self.__filenames)
        #aggiungere i files alla listview
        for i in self.__filenames:
            self.ui.filelistw.addItems([i])
        self.ui.filelistw.setCurrentRow(0)
            
    def Check_UIfiles(self, myfilelist): #riciclabile in altri programmi, solo python
        #devo controllare se i file hanno l'intestazione xml per evitare di processare file,
        #con estensione, ui di altra natura
        #ricevo la listafiles caricati mediante Add_files e rilascio la stessa lista
        #mantenendo solo i file con intestazione xml
        app = [] #lista di supporto
        for i in range(0, len(myfilelist)):
            f = open(myfilelist[i], 'r')
            c = f.readline()
            if (c == '<?xml version="1.0" encoding="UTF-8"?>\n')or (c == '<?xml version="1.0" encoding="UTF-8"?>') :
                c = f.readline()
                if (c == '<ui version="4.0">\n') or (c == '<ui version="4.0">') :
                    app.append(myfilelist[i])            
        return app                         
  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
