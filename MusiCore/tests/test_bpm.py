# -*- coding: utf-8 -*-
# author: Aurélien BETTINI
# fonction de test de l'analyse bpm
import implements.Analyse
import os

# Test de l'analyse du BPM
# Il faut mettre le chemin des fichiers à analyser dans l'instanciation des objets analyse
#
# Commenaires: L'analyse du BPM est correct dans la majorité des cas
# seul les musiques avec beaucoup de batteries peuvent engendrer un problème

analyse1 = implements.Analyse.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv")
if os.path.isfile("/home/gerox/Musique/Deorro.wav") == True:
    y, sr = analyse1.extrairedatamusic()
    bpm = analyse1.analyse_bpm(y, sr)
    print("\033[1;32;40m BPM 1 OK   \033[0;30;47m %s          \033[0m  " % bpm)
else:
    print("la musique n'existe pas")

analyse1 = implements.Analyse.analyse("/home/gerox/Musique/AC-DC - Highway to Hell.mp3", "fichier_csv")
if os.path.isfile("/home/gerox/Musique/AC-DC - Highway to Hell.mp3") == True:
    y, sr = analyse1.extrairedatamusic()
    bpm = analyse1.analyse_bpm(y, sr)
    print("\033[1;32;40m BPM 2 OK   \033[0;30;47m %s          \033[0m  " % bpm)
else:
    print("la musique n'existe pas")

analyse1 = implements.Analyse.analyse("/home/gerox/Musique/Daft Punk - Get Lucky ft. Pharrell Williams.mp3",
                                           "fichier_csv")
if os.path.isfile("/home/gerox/Musique/Daft Punk - Get Lucky ft. Pharrell Williams.mp3") == True:
    y, sr = analyse1.extrairedatamusic()
    bpm = analyse1.analyse_bpm(y, sr)
    print("\033[1;32;40m BPM 3 OK   \033[0;30;47m %s          \033[0m  " % bpm)
else:
    print("la musique n'existe pas")

analyse1 = implements.Analyse.analyse("/home/gerox/Musique/Happy - Pharrell Williams.mp3", "fichier_csv")
if os.path.isfile("/home/gerox/Musique/Happy - Pharrell Williams.mp3") == True:
    y, sr = analyse1.extrairedatamusic()
    bpm = analyse1.analyse_bpm(y, sr)
    print("\033[1;32;40m BPM 4 OK   \033[0;30;47m %s          \033[0m  " % bpm)
else:
    print("la musique n'existe pas")
