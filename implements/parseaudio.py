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


def parseaudio(nomanalyse=None, flag_bpm=False, flag_tonalite=False):
    '''

    exemple de test :
    analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv")
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
    '''

    if nomanalyse is None:
        raise ValueError("Error: il manque le nom de l'analyse")
    output = implements.analyseaudio.csv_musicore('output_ui')
    nom_analyse = implements.analyseaudio.csv_musicore(nomanalyse)
    nom_analyse.clear()
    path_to_music = output.get_column(0)
    print(path_to_music)
    k = 1

    for i in path_to_music:
        numanalyse = str(k)
        analyse = "analyse" + numanalyse
        print(analyse + " : fichier " + i)
        analyse = implements.analyseaudio.analyse(i, output.path_to_csv_file, output.path_to_database)
        output_csv = []

        research = output.find_title_in_database(analyse.extraire_path()[0])

        # Distinction des différentes analyses, bpm ou tonalité suivant les choix de l'utilisateur

        if research[0] == True:
            print(research[3])
            if research[2] != '//' and research[3] > 4:  # toutes les données de l'anaylse sont dans la base de données
                print('toutes les infomations sur la musique sont présentes')
                print(research[1])
                output_csv = nom_analyse.get_row_database(research[1])
                nom_analyse.add_list(nom_analyse.path_to_csv_file,
                                     output_csv)  # rajout des données dans le csv de l'analyse

            if (research[2] != '//' or research[4] == '**Musique atonale**') and research[
                3] < 5:  # il n'y a que le bpm dans la base de données
                print("il n'y a que les informations sur l'analyse bpm")
                if flag_bpm == True:  # l'utilisateur veut analyser le bpm
                    output_csv = nom_analyse.get_row_database(research[0])[:4]
                if flag_tonalite == True:
                    y, s = analyse.extrairedatamusic()
                    Fs = 44100  # sampling rate
                    notefreq = analyse.analysefft(y, Fs, 50,
                                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
                    tonalite = analyse.rechercheaccords(notefreq)
                    output_csv = output_csv + tonalite

                nom_analyse.delete_row_database(research[1])  # on remove la ligne de la base de données
                nom_analyse.add_list(nom_analyse.path_to_database,
                                     output_csv)  # rajout des données dans la base de données
                nom_analyse.add_list(nom_analyse.path_to_csv_file,
                                     output_csv)  # rajout des données dans le csv de l'analyse

            if research[2] == '//' or research[2] == '**Musique atonale**':  # il y seulement l'analyse de la tonalité
                print("il n'y a que les informations sur l'analyse de la tonalité")
                if flag_bpm == True:
                    y, sr = analyse.extrairedatamusic()  # extraction des données des musiques
                    output_csv = analyse.analyse_bpm(y, sr)  # analyse bpm
                if flag_tonalite == True:
                    output_csv = output_csv + nom_analyse.get_row_database(research[0])[1:]
                nom_analyse.delete_row_database(research[1])  # on remove la ligne de la base de données
                nom_analyse.add_list(nom_analyse.path_to_database,
                                     output_csv)  # rajout des données dans la base de données
                nom_analyse.add_list(nom_analyse.path_to_csv_file,
                                     output_csv)  # rajout des données dans le csv de l'analyse

        else:
            bpm = []
            tonalite = []
            if flag_tonalite != False or flag_bpm != False:
                y, sr = analyse.extrairedatamusic()  # extraction des données des musiques
                if flag_bpm == True:
                    bpm = analyse.analyse_bpm(y, sr)  # analyse bpm
                if flag_tonalite == True:
                    Fs = 44100  # sampling rate
                    notefreq = analyse.analysefft(y, Fs, 50,
                                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
                    tonalite = analyse.rechercheaccords(notefreq)
                nom_analyse.add_list(nom_analyse.path_to_database, bpm + tonalite)
                nom_analyse.add_list(nom_analyse.path_to_csv_file, bpm + tonalite)
        k += 1
