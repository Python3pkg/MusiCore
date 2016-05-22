# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.analyseaudio
import os

# Test de l'analyse du BPM
# Il faut mettre le chemin des fichiers à analyser dans l'instanciation des objets analyse
#
# Commenaires: L'analyse du BPM est correct dans la majorité des cas
# seul les musiques avec beaucoup de batteries peuvent engendrer un problème

analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv")
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/AC-DC - Highway to Hell.mp3", "fichier_csv")
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Daft Punk - Get Lucky ft. Pharrell Williams.mp3",
                                           "fichier_csv")
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Happy - Pharrell Williams.mp3", "fichier_csv")
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)
