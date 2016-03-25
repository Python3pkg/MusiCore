# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.analyseaudio
import os

# test
analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
# print(analyse1.extraire_path())
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/AC-DC - Highway to Hell.mp3", "fichier_csv")
# print(analyse1.extraire_path())
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Daft Punk - Get Lucky ft. Pharrell Williams.mp3",
                                           "fichier_csv")
# print(analyse1.extraire_path())
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)

analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Happy - Pharrell Williams.mp3", "fichier_csv")
# print(analyse1.extraire_path())
if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
    y, sr = analyse1.extrairedatamusic()
    analyse1.analyse_bpm(y, sr)
