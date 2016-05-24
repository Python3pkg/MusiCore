# -*- coding: utf-8 -*-

'''
permet de parcourir les fichiers audio contenu dans un fichier csv et de lancer leur analyse
Ce module est initié par l'interface graphique
'''

############################################################################################

import analyseaudio
import csv
import os
import sys


def getdirpath():
    '''
    :return:le chemin du repertoire MusiCore
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parser(nom_analyse, analyse, flag_bpm, flag_tonalite):
    '''

    exemple de test :
    analyse1 = implements.analyseaudio.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv")
    if (analyse1.islineincsc(analyse1.extraire_path()[0]) == False):
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
    '''

    output_csv = []
    research = nom_analyse.find_title_in_database(analyse.extraire_path()[0])

    # Distinction des différentes analyses, bpm ou tonalité suivant les choix de l'utilisateur

    if research[0] == True:
        print(research[3])
        if research[2] != '//' and research[3] > 5:  # toutes les données de l'anaylse sont dans la base de données
            print('toutes les infomations sur la musique sont présentes')
            print(research[1])
            output_csv = nom_analyse.get_row_database(research[1])
            return output_csv
            # nom_analyse.add_list(nom_analyse.path_to_csv_file,output_csv)  # rajout des données dans le csv de l'analyse

        if research[2] != '//' and research[3] == 5:  # il n'y a que le bpm dans la base de données
            print("il n'y a que les informations sur l'analyse bpm")
            bpm = nom_analyse.get_row_database(research[1])[1:4]
            tonalite = []
            output_csv = [analyse.extraire_path()[0]]
            time = nom_analyse.get_row_database(research[1])[-1]

            if flag_bpm == True:  # l'utilisateur veut analyser le bpm
                output_csv = output_csv + bpm

            if flag_tonalite == True:
                y, s = analyse.extrairedatamusic()
                Fs = 44100  # sampling rate
                notefreq = analyse.analysefft(y, Fs, 50,
                                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
                tonalite = analyse.rechercheaccords(notefreq)
                output_csv = output_csv + tonalite

            nom_analyse.delete_row_database(research[1])  # on remove la ligne de la base de données
            nom_analyse.add_list(nom_analyse.path_to_database, [analyse.extraire_path()[0]] + bpm + tonalite + [
                str(time)])  # rajout des données dans la base de données

            return output_csv + [str(time)]
            # nom_analyse.add_list(nom_analyse.path_to_csv_file,output_csv)  # rajout des données dans le csv de l'analyse

        if research[2] == '//' or research[2] == '**Musique atonale**':  # il y seulement l'analyse de la tonalité
            print("il n'y a que les informations sur l'analyse de la tonalité")
            bpm = []
            tonalite = []
            if flag_bpm == True:
                y, sr = analyse.extrairedatamusic()  # extraction des données des musiques
                bpm = analyse.analyse_bpm(y, sr)  # analyse bpm
            if flag_tonalite == True:
                tonalite = [1]  # on met le temps de la musique dedans
            nom_analyse.delete_row_database(research[1])  # on remove la ligne de la base de données
            nom_analyse.add_list(nom_analyse.path_to_database, [
                analyse.extraire_path()[0]] + bpm + tonalite)  # rajout des données dans la base de données

            return [analyse.extraire_path()[0]] + bpm + tonalite
            # nom_analyse.add_list(nom_analyse.path_to_csv_file,output_csv)  # rajout des données dans le csv de l'analyse

    else:
        print("La musique n'est pas dans la base de données")
        bpm = []
        tonalite = []
        if flag_tonalite != False or flag_bpm != False:
            y, sr = analyse.extrairedatamusic()  # extraction des données des
            if flag_bpm == True:
                bpm = analyse.analyse_bpm(y, sr)  # analyse bpm
            if flag_tonalite == True:
                Fs = 44100  # sampling rate
                notefreq = analyse.analysefft(y, Fs, 50,
                                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
                tonalite = analyse.rechercheaccords(notefreq)

            nom_analyse.add_list(nom_analyse.path_to_database,
                                 [analyse.extraire_path()[0]] + bpm + tonalite + [str(analyse.time)])
            # nom_analyse.add_list(nom_analyse.path_to_csv_file, bpm + tonalite)
            return [analyse.extraire_path()[0]] + bpm + tonalite + [analyse.time]
            # k += 1
