# -*- coding: utf-8 -*-

'''
permet de parcourir les fichiers audio contenu dans un fichier csv et de lancer leur analyse
Ce module est initié par l'interface graphique
'''

############################################################################################

import implements.analyseaudio
import csv
import os
import sys


def getdirpath():
    '''
    :return:le chemin du repertoire MusiCore
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parseaudio(nomanalyse=None):
    '''
    exemple de test :
    analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv")
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
    '''

    if nomanalyse is None:
        raise ValueError("Error: il manque le nom de l'analyse")

    # On determine les chemins des fichiers necessaire à l'analyse des musiques
    bddfilepath = getdirpath() + "/BDDMusic/BDDMusic"
    print("La base de données de musique ce situe: " + bddfilepath)

    output_ui = getdirpath() + "/BDDMusic/output_ui"
    print("Le fichier à analyser ce situe: " + output_ui)

    pathfichiercsv = getdirpath() + "/BDDMusic/" + nomanalyse
    print("Le fichier de la playlist est " + pathfichiercsv)

    # Verifie si on peut ouvrir le fichier
    try:
        with open(output_ui):
            pass
    except IOError:
        print("parseaudio: Erreur! Le fichier output_ui n'a pas pu etre ouvert ou n'existe pas")
        sys.exit(0)

    # ouverture du fichier csv
    fname = output_ui
    file = open(fname, "rt")  # file = open(fname, "rb") python 2.7
    k = 1

    try:
        reader = csv.reader(file)
        for row in (reader):

            pathtoaudiofile = row[0]  # emplecement du fichier audio

            numanalyse = str(k)
            analyse = "analyse" + numanalyse
            print(analyse + " : fichier " + row[0])
            analyse = implements.analyseaudio.analyse(row[0], pathfichiercsv, bddfilepath, )

            if (analyse.islineincsc(analyse.extraire_path()[0]) == False):
                y, sr = analyse.extrairedatamusic()
                analyse.analyse_bpm(y, sr)

            k += 1

    finally:
        file.close()


'''
    analyse1 = implements.analyseaudio.analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
    # print(analyse1.extraire_path())
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
'''
