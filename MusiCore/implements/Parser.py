# -*- coding: utf-8 -*-

'''
permet de parcourir les fichiers audio contenu dans un fichier csv et de lancer leur analyse
Ce module est initié par l'interface graphique
'''

############################################################################################

import MusiCore.implements.Analyse as Analyse
import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def getdirpath():
    '''
    :return:le chemin du repertoire MusiCore
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def switch_tonalite(list_tonalite):
    # Mineur
    mineur_tonalité = ['G#m', 'D#m', 'A#m', 'Fm', 'Cm', 'Gm', 'Dm', 'Am', 'Em', 'Bm', 'F#m', 'C#m']
    mineur_equivalent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Majeur
    majeur_tonalité = ['BM', 'F#M', 'C#M', 'G#M', 'D#M', 'A#M', 'FM', 'CM', 'GM', 'DM', 'AM', 'EM']
    majeur_equivalent = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    for i in range(len(list_tonalite)):
        for j in range(len(mineur_tonalité)):
            if list_tonalite[i] == mineur_tonalité[j]:
                list_tonalite[i] = mineur_equivalent[j]
        for w in range(len(majeur_tonalité)):
            if list_tonalite[i] == majeur_tonalité[w]:
                list_tonalite[i] = majeur_equivalent[w]
    return list_tonalite


def analyseBPM(mat, playlist):
    flag_bpm = True
    flag_tonalite = False
    nomanalyse = 'test'

    # on initialise l'analyse
    nom_analyse = Analyse.csv_musicore(nomanalyse)
    nom_analyse.clear()
    k = 1

    for i in mat:  # on parcourt la liste de musique
        numanalyse = str(k)
        analysed = "analyse" + numanalyse
        print(analysed + " : fichier " + i)
        analysed = Analyse.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)
        get_bpm = parser(nom_analyse, analysed, True, False)
        print(get_bpm)
        playlist[k - 1][2] = float(get_bpm[1])
        playlist[k - 1][1] = str(get_bpm[-1])
        k += 1
    return playlist


def analyseHarm(mat, playlist):
    flag_bpm = False
    flag_tonalite = True
    nomanalyse = 'test'

    # on itnitialise l'analyse
    nom_analyse = Analyse.csv_musicore(nomanalyse)
    nom_analyse.clear()
    k = 1

    for i in mat:  # on parcourt la liste de musique
        numanalyse = str(k)
        analysed = "analyse" + numanalyse
        print(analysed + " : fichier " + i)
        analysed = Analyse.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)

        get_tonalite = parser(nom_analyse, analysed, False,
                              True)
        print(get_tonalite)
        if get_tonalite[4] == '**Musique atonale**':
            playlist[k - 1][3] = get_tonalite[4]
        else:
            playlist[k - 1][3] = str(get_tonalite[-2])
        playlist[k - 1][1] = get_tonalite[-1]
        while Gtk.events_pending():
            Gtk.main_iteration()
        k += 1
    return playlist


def analyseBoth(mat, playlist):
    print("vous avez cliqué sur le bouton d'anlyse des deux caractéristiques")
    flag_bpm = True
    flag_tonalite = True
    nomanalyse = 'test'

    # on itnitialise l'analyse
    nom_analyse = Analyse.csv_musicore(nomanalyse)
    nom_analyse.clear()
    k = 1

    for i in mat:  # on parcourt la liste de musique
        numanalyse = str(k)
        analysed = "analyse" + numanalyse
        print(analysed + " : fichier " + i)
        analysed = Analyse.analyse(i, nom_analyse.path_to_csv_file, nom_analyse.path_to_database)

        get_bpm = parser(nom_analyse, analysed, True, True)
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
    return playlist


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
