'''
Created on 03/gen/2011
PyQt
@author: alcko
'''

import os
from xdg.DesktopEntry import DesktopEntry
import gtk
import gobject

# Struttura ausiliaria del file desktop
class DeskStruct:
    Name = ""
    Exec = ""
    Comment = ""
    Autostart = True
    Icon = None #percorso dell'immagine rappresentante l'icona
    
class AutoStart:
    userpath = os.path.expanduser("~")
    user_path = os.path.expanduser("~")
    user_autostart = userpath + "/.config/autostart"
    xdg_autostart = "/etc/xdg/autostart"
    sys_autostart = "/usr/share/gnome/autostart"
    gdm_autostart = "/usr/share/gdm/autostart"

    
     
    #def GetAutoStartList():
        
        
    def ShowAll(self):#elenca tutti i file nelle 4 cartelle di autostart
        autolist = []
        
        path = self.user_autostart
        for file_name in os.listdir(path):
            myitem = DesktopEntry(path + '/' + file_name)
            #print(path + '/' + file_name)
            a = DeskStruct()
            a.Name = myitem.getName()
            a.Exec = myitem.getExec()
            a.Icon = myitem.getIcon()
            a.Comment = myitem.getComment()
            autolist.append(a) #lista di oggetti Deskstruct
              
        
        #path=self.xdg_autostart
        #autolist.append('     XDG files')
        #for file_name in os.listdir(path):
        #    autolist.append(path+'/'+file_name)
        #
        #path=self.sys_autostart
        #autolist.append('     Sys Files')
        #for file_name in os.listdir(path):
        #    autolist.append(path+'/'+file_name)
        #path=self.gdm_autostart
        #autolist.append('     GDM files')
        #for file_name in os.listdir(path):
        #    autolist.append(path+'/'+file_name)
        return autolist

    def newStarter(self, path, newstart):
        myitem = DesktopEntry(path)
        myitem.set("Name", newstart.Name)
        myitem.set("Exec", newstart.Exec)
        myitem.set("Comment", newstart.Comment)
        myitem.set("Type", "Application")
        myitem.set("Version", "1.0")
        myitem.set("X-GNOME-Autostart-enabled", newstart.Autostart)
        # Scrive il file .desktop
        myitem.write()

        
#    def ShowStarter(self, activated):
#        SList = []
#        return Slist
    
    def parseStarter(self, path):
        
        
        return True
