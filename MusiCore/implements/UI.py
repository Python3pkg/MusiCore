#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import MusiCore.implements.Parser as Parser
import MusiCore.implements.Exportation as Exportation


def getpath(path):
    '''

    :param path: string (chemin d'accces à un fichier)
    :return: string (nom du fichier moins son extention)

    '''
    k = 0
    while path[len(path) - k - 1] != "/":
        k = k + 1
    return path[len(path) - k:len(path) - 4]

def exportPlaylist():
    '''

    :return: list (matrice contenant les valeurs de la TreeView)

    '''
    mat = []
    for row in playlist:
        mat.append(row[:])
    return mat


def importPlaylist(mat):
    '''

    :param mat: matrice à remplcer dans la treeview
    :return: list

    '''
    playlist = []
    for row in mat:
        playlist.append(row[:])
    return mat

def exportPaths():
    '''

    :return: list (liste des emplacement des musiques importées

    '''
    mat = []
    for row in playlist:
        mat.append(row[-1])
    return mat

def exportTitleandpath():
    '''

    :return: list (contient les titres et emplacement des musiques)
    '''

    mat = []
    for row in playlist:
        mat.append(list(row[k] for k in [0, -1]))
    return mat

def export_tonalite():
    '''

    :return: list (contient la tonalité des musiques)
    '''
    mat = []
    for row in playlist:
        mat.append(row[3])
    return mat

def actualize(mat):
    '''
    Permet d'actualiser la playlist

    :param mat: list
    :return: None
    '''
    for i, row in enumerate(mat):
        playlist[i] = row
    return None

###Gestion des signaux###

class Handler(Gtk.Window):
    '''
    Classe gérant les signants
    '''
    def onDeleteWindow(self, *args):
        '''

        :param args: permet de fermer la fenêtre
        :return:
        '''
        Gtk.main_quit(*args)
        return None

    def onOpen(self, button):
        '''

        :param button: permet d'ouvrir les fichiers
        :return:
        '''
        selected = dialog.get_filenames()
        for row in selected:
            playlist.append([getpath(row), None, None, None, row])
        return None

    def onBPM(self, button):
        '''

        :param button: bouton permettant de lancer l'analyse de la tonalité sur toutes les musiques importées
        :return: None
        '''

        print("vous avez cliqué sur le bouton d'analyse du bpm")
        mat = Parser.analyseBPM(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None

    def onHarm(self, button):
        '''

        :param button: bouton permettant de lancer l'analyse de la tonalité sur toutes les musiques importées
        :return: None
        '''
        print("vous avez cliqué sur le bouton d'anlyse de la tonalité")
        mat = Parser.analyseHarm(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None


    def onBoth(self, button):
        '''

        :param button: bouton permettant de lancer l'analyse de toutes les caractéristiques des musiques importées
        :return: None
        '''
        print("vous avez cliqué sur le bouton d'anlyse des deux caractéristiques")
        mat = Parser.analyseBoth(exportPaths(), exportPlaylist())
        playlist.clear()
        for i in range(len(mat)):
            playlist.append(mat[i])
        return None

    def onLaunch(self, button):
        '''

        :param button: bouton permettant de lancer le tri
        :return: None
        '''
        print('test')
        liste = switch_tonalite(export_tonalite())
        print(liste)

        k = 0
        for i in liste:
            playlist[k][3] = str(i)
            k += 1

    #        implements.tri() actualize()

    def onM3u(self, widget):
        '''

        :param widget: bonton permettant de lancer l'exportation d'un fichier m3u
        :return: None
        '''
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
        '''

        :param widget: bouton permettant de lancer l'exportation des fichiers mp3
        :return: None
        '''
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
        '''

        :param button: bouton lancant la lecture
        :return: None
        '''
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
    '''
    Permet d'afficher l'UI

    :return: None

    '''
  window.show_all()
  Gtk.main()
  return None
