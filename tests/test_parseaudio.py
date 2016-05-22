# -*- coding: utf-8 -*-

'''
test du module parseaudio
parcourt toutes les musiques étant dans le fichier database/test_parseaudio
'''

import implements
import csv

############################################################################################

# test de création de la playlist playlistbob
# afin de lancer l'analyse, il faut lancer ce programme
Musique1 = implements.parseaudio.getdirpath() + "/tests/Abba - Waterloo.mp3"
Musique2 = implements.parseaudio.getdirpath() + "/tests/AC-DC - Highway to Hell.mp3"
Musique3 = implements.parseaudio.getdirpath() + "/tests/Bruno Mars - Treasure.mp3"
output_ui = implements.parseaudio.getdirpath() + "/database/output_ui"

fname = output_ui
file = open(fname, "w")  # file = open(fname, "rb") python 2.7
try:
    writer = csv.writer(file)
    writer.writerow([Musique1])
    writer.writerow([Musique2])
    writer.writerow([Musique3])

finally:
    file.close()

# test de parse audio (le fait de mettre True et True permet de lancer l'analyse bpm et harmonique)
implements.parseaudio.parseaudio("playlistbob", True, True)

############################################################################################
