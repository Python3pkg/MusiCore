#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import MusiCore.implements.Parser as Parser
import MusiCore.implements.Exportation as Exportation


def getpath(path):
    k = 0
    while path[len(path) - k - 1] != "/":
        k = k + 1
    return path[len(path) - k:len(path) - 4]

def exportPlaylist():
    mat = []
    for row in playlist:
        mat.append(row[:])
    return mat


def importPlaylist(mat):
    playlist = []
    for row in mat:
        playlist.append(row[:])
    return mat

def exportPaths():
    mat = []
    for row in playlist:
        mat.append(row[-1])
    return mat

def exportTitleandpath():
    mat = []
    for row in playlist:
        mat.append(list(row[k] for k in [0, -1]))
    return mat

def export_tonalite():
    mat = []
    for row in playlist:
        mat.append(row[3])
    return mat

def actualize(mat):
    for i, row in enumerate(mat):
        playlist[i] = row
    return None

###Gestion des signaux###

class Handler(Gtk.Window):
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        return None

    def onOpen(self, button):
        selected = dialog.get_filenames()
        for row in selected:
            playlist.append([getpath(row), None, None, None, row])
        return None

    def onBPM(self, button):
        '''

        :param button:
        :return:
        '''

        print("vous avez cliqué sur le bouton d'analyse du bpm")
        mat = Parser.analyseBPM(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None

    def onHarm(self, button):
        print("vous avez cliqué sur le bouton d'anlyse de la tonalité")
        mat = Parser.analyseHarm(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None


    def onBoth(self, button):
        print("vous avez cliqué sur le bouton d'anlyse des deux caractéristiques")
        mat = Parser.analyseBoth(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None

    def onLaunch(self, button):
        print('test')
        liste = switch_tonalite(export_tonalite())
        print(liste)

        k = 0
        for i in liste:
            playlist[k][3] = str(i)
            k += 1

    #        implements.tri() actualize()

    def onM3u(self, widget):
        saver = Gtk.FileChooserDialog("Please select a file to save the playlist", self,
                                      Gtk.FileChooserAction.SAVE,
                                      (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                       Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        response = saver.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            loc = saver.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            loc = " "
        saver.destroy()
        Exportation.m3u(loc, exportPaths())
        return None

    def onMp3(self, widget):
        saver = Gtk.FileChooserDialog("Please select a file to save the song", self,
                                      Gtk.FileChooserAction.SAVE,
                                      (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                       Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
        response = saver.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            loc = saver.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            loc = " "
        saver.destroy()
        Exportation.mp3(loc, exportPaths())
        return None

    def onVLC(self, button):
        file = open("save")
        loc = "vlc " + file.read()
        file.close()
        os.system(loc)
        return None

###Importation du fichier Glade

builder = Gtk.Builder()
builder.add_from_file("./implements/UI.glade")
builder.connect_signals(Handler())

###Definition des objets directement interagis

window = builder.get_object("Main")
waiter = builder.get_object("Waiter")
dialog = builder.get_object("FileChooser")
playlist = builder.get_object("Playlist")
ponderation = builder.get_object("ponderation")


def showUI():
  window.show_all()
  Gtk.main()
  return None
