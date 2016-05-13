#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

###Fonctions internes au GUI

def getpath(path):
    k = 0
    while path[len(path) - k - 1] != "/":
       k = k + 1
    return path[len(path) - k:len(path)-4]

def exportPlaylist():
    mat=[]
    for row in playlist:
        mat.append(row[:])
    return mat

def exportPaths():
    mat=[]
    for row in playlist:
        mat.append(row[-1])
    return mat

def actualize(mat):
    for i,row in enumerate(mat):
      playlist[i]=row
    return None

###Gestion des signaux###

class Handler:
 
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        return None

    def onOpen(self, button):
        selected=dialog.get_filenames()
        for row in selected:
            playlist.append([getpath(row), None,  None, None, row])
        return None

    def onBPM(self, button):
         print('test')
#        implements.parseaudio.parseaudio(exportPaths(), True, False)
#        actualize()

    def onHarm(self, button):
         print('test')
#        implements.parseaudio.parseaudio(exportPaths(), False, True)
#        actualize()

    def onBoth(self, button):
         print('test')
#        implements.parseaudio.parseaudio(exportPaths(), True, True)
#        actualize()

    def onLaunch(self, button):
         print('test')
#        implements.tri()
#        actualize()


###Importation du fichier Glade

builder = Gtk.Builder()
builder.add_from_file("UI2.glade")
builder.connect_signals(Handler())

###Definition des objets directement interagis

window = builder.get_object("Main")
waiter = builder.get_object("Waiter")
dialog = builder.get_object("FileChooser")
playlist = builder.get_object("Playlist")
ponderation= builder.get_object("ponderation")

###Affichage et lancement du Main###

window.show_all()
Gtk.main()
