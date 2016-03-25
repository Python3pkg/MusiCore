# -*- coding: utf-8 -*-

'''
permet de parcourir les fichiers audio contenu dans un fichier csv et de lancer leur analyse
Ce module est initié par l'interface graphique
'''

############################################################################################

import implements.analyseaudio
import csv


def parseaudio(pathtocsvfile):
    # test etant ok
    analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
    # print(analyse1.extraire_path())
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)

    # ouverture du fichier csv
    fname = pathtocsvfile
    file = open(fname, "rt")  # file = open(fname, "rb") python 2.7
    k = 1

    try:
        reader = csv.reader(file)
        for row in (reader):

            pathtoaudiofile = row[0]  # emplecement du fichier audio

            numanalyse = str(k)
            analyse = "analyse" + numanalyse
            print(analyse + " : fichier " + row[0])
            analyse = implements.analyseaudio.analyse(row[0], "fichier_csv")

            if (analyse.islineincsc(analyse.extraire_path()[0]) == False):
                y, sr = analyse.extrairedatamusic()
                analyse.analyse_bpm(y, sr)

            k += 1

    finally:
        file.close()


# test
parseaudio('/home/bettini/PycharmProjects/MusiCore/BDDMusic/test_parseaudio')

'''
    analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
    # print(analyse1.extraire_path())
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
'''
