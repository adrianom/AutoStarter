#!/usr/bin/env python

import pygtk
import gtk 
import AutoStart
import gobject

        
class MyApp:
    builder = gtk.Builder()
    p = AutoStart.AutoStart()
    a = p.ShowAll()   
    def __init__(self):
        windowname = "MainWindow"
        gladefile = "main.ui"
        # Loads the UI from GtkBuilder XML file
        self.builder.add_from_file(gladefile)
        
        # Lets extract a reference to window object to use later
        self.window = self.builder.get_object(windowname)
      
        # SetUp degli eventi..un dizionario
        dic = {
            "on_showall_clicked" : self.VisualizzaProg,
            "on_MainWindow_destroy" : gtk.main_quit
        }
        self.builder.connect_signals (dic)
        
        
        #Get the treeView from the widget Tree
        self.progView = self.builder.get_object("lista")
        #Add all of the List Columns to the wineView
#        self.AggiungiColonna("Icona", 0, gtk.gdk.Pixbuf)
#        self.AggiungiColonna("Nome programma", 1)


        #Create the listStore Model to use with the wineView
        self.progList = gtk.ListStore(gtk.gdk.Pixbuf, gobject.TYPE_STRING)
        #Attache the model to the treeView
        self.progView.set_model(self.progList)	
        
        #self.mygtkimage = self.builder.get_object("image1")
       

        #Aggiungo le colonne
        col = gtk.TreeViewColumn()
        col.set_title('Icone')
        render_pixbuf = gtk.CellRendererPixbuf()
        col.pack_start(render_pixbuf, expand = False)
        col.add_attribute(render_pixbuf, 'pixbuf', 0)
        self.progView.append_column(col)

        col1 = gtk.TreeViewColumn()
        col1.set_title('Programmi')
        render_text = gtk.CellRendererText()
        col1.pack_start(render_text, expand = True)
        col1.add_attribute(render_text, 'text', 1)
        self.progView.append_column(col1)

    def VisualizzaProg(self, widget):
        for i in self.a:
            icon_theme = gtk.icon_theme_get_default()
            try:
                myIcon = None
                myIcon = icon_theme.load_icon(i.Icon, 16, 0) #devo caricarlo con il try except, in caso di file non esistente
            except:
                print("File icon of " + i.Name + " not found!")     
#            
            self.progList.append([myIcon, i.Name]) 

    
#    def AggiungiColonna(self, title, columnId, tipo = gobject.TYPE_STRING):
#        """This function adds a column to the list view.
#        First it create the gtk.TreeViewColumn and then set
#        some needed properties"""
#        if tipo == gobject.TYPE_STRING :                          
#            column = gtk.TreeViewColumn(title, gtk.CellRendererText(), text = columnId)
#        elif tipo == gtk.gdk.Pixbuf:
#            column = gtk.TreeViewColumn(title, gtk.CellRendererPixbuf())
#        column.set_resizable(True)
#        column.set_sort_column_id(columnId)
#        self.progView.append_column(column)
        

    
myapp = MyApp()
gtk.main()        
        
        
        
        
        
        

