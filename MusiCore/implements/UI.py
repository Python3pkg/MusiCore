#!/usr/bin/env python

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import analyseaudio
import parse_audio_2
import Exportation
from pydub import AudioSegment
import os


###Fonctions internes au GUI

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
        print("vous avez cliqué sur le bouton d'analyse du bpm")
        flag_bpm = True
        flag_tonalite = False
        nomanalyse = 'test'

        # on initialise l'analyse
        nom_analyse = analyseaudio.csv_musicore(nomanalyse)
        nom_analyse.clear()
        k = 1

        for i in exportPaths():  # on parcourt la liste de musique
            numanalyse = str(k)
            analyse = "analyse" + numanalyse
            print(analyse + " : fichier " + i)
            analyse = analyseaudio.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)
            get_bpm = parse_audio_2.parser(nom_analyse, analyse, True, False)
            print(get_bpm)
            playlist[k - 1][2] = float(get_bpm[3])
            playlist[k - 1][1] = str(get_bpm[-1])
            while Gtk.events_pending():
                Gtk.main_iteration()
            k += 1
            #        implements.parseaudio.parseaudio(exportPaths(), True, False)
            #        actualize()'''

    def onHarm(self, button):
        print("vous avez cliqué sur le bouton d'anlyse de la tonalité")
        flag_bpm = False
        flag_tonalite = True
        nomanalyse = 'test'

        # on itnitialise l'analyse
        nom_analyse = analyseaudio.csv_musicore(nomanalyse)
        nom_analyse.clear()
        k = 1

        for i in exportPaths():  # on parcourt la liste de musique
            numanalyse = str(k)
            analyse = "analyse" + numanalyse
            print(analyse + " : fichier " + i)
            analyse = analyseaudio.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)

            get_tonalite = parse_audio_2.parser(nom_analyse, analyse, False,
                                                True)
            print(get_tonalite)
            if get_tonalite[4] == '**Musique atonale**':
                playlist[k - 1][3] = get_tonalite[4]
            else:
                playlist[k - 1][3] = str(get_tonalite[5])
            playlist[k - 1][1] = get_tonalite[-1]
            while Gtk.events_pending():
                Gtk.main_iteration()
            k += 1
            #        implements.parseaudio.parseaudio(exportPaths(), False, True)
            #        actualize()

    def onBoth(self, button):

        print("vous avez cliqué sur le bouton d'anlyse des deux caractéristiques")
        flag_bpm = True
        flag_tonalite = True
        nomanalyse = 'test'

        # on itnitialise l'analyse
        nom_analyse = analyseaudio.csv_musicore(nomanalyse)
        nom_analyse.clear()
        k = 1

        for i in exportPaths():  # on parcourt la liste de musique
            numanalyse = str(k)
            analyse = "analyse" + numanalyse
            print(analyse + " : fichier " + i)
            analyse = analyseaudio.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)

            get_bpm = parse_audio_2.parser(nom_analyse, analyse, True, True)
            print(get_bpm)
            playlist[k - 1][2] = float(get_bpm[3])
            if get_bpm[4] == '**Musique atonale**':
                playlist[k - 1][3] = get_bpm[4]
            else:
                playlist[k - 1][3] = get_bpm[-2]
            playlist[k - 1][1] = get_bpm[-1]
            while Gtk.events_pending():
                Gtk.main_iteration()
            k += 1

    def onLaunch(self, button):
        print('test')
        # print(exportPlaylist())
        playlist[0][1] = '3'

    #        implements.tri()
    #        actualize()

    def on_selection_button_clicked(self, widget):
        """Called on any of the button clicks"""
        print('coucou')

    def onM3u(self, widget):
        saver = Gtk.FileChooserDialog("Please choose a file", self,
                                      Gtk.FileChooserAction.SAVE,
                                      (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                       Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = saver.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            loc = saver.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            loc = " "
        saver.destroy()
        if loc != " ":
            pl = open(loc, "w")
            pl.write("#EXTM3U")
            resultat = exportPaths()
            for i in resultat:
                pl.write("\n")
                pl.write(i)
            pl.close()
            os.system("echo " + loc + ">../database/save")
        return None

    def onMp3(self, widget):
        saver = Gtk.FileChooserDialog("Please choose a file", self,
                                      Gtk.FileChooserAction.SAVE,
                                      (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                       Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = saver.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            loc = saver.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
            loc = " "
        saver.destroy()
        if loc != " ":
            resultat = exportPaths()
            song = AudioSegment.from_mp3(resultat[0])
            playlist = song
            for i in range(1, len(resultat)):
                song = AudioSegment.from_mp3(resultat[i])
                playlist = playlist.append(song, crossfade=(10 * 1000))
            playlist = playlist.fade_out(10)
            out_f = open(loc, 'wb')
            playlist.export(out_f, format='mp3')
            os.system("echo " + loc + ">../database/save")

    def onVLC(self, button):
        file = open("../database/save")
        loc = "vlc " + file.read()
        file.close()
        os.system(loc)
        return None


###Importation du fichier Glade

builder = Gtk.Builder()
builder.add_from_file("UI2.glade")
builder.connect_signals(Handler())

###Definition des objets directement interagis

window = builder.get_object("Main")
waiter = builder.get_object("Waiter")
dialog = builder.get_object("FileChooser")
playlist = builder.get_object("Playlist")
ponderation = builder.get_object("ponderation")

###Affichage et lancement du Main###

window.show_all()
Gtk.main()
