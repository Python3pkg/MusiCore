# -*- coding: utf-8 -*-
# author: Aurélien BETTINI

'''
test du module parseaudio
parcourt toutes les musiques étant dans le fichier database/test_parseaudio
'''

import implements.Parser
import implements.Analyse

############################################################################################
# test du parser valide avec 2 musiques (True, True)
# mettre le chemin des fichiers audios que l'on souhaite analyser ci dessous
Musique1 = implements.Parser.getdirpath() + "/tests/Abba - Waterloo.mp3"
path_to_files = [Musique1]

# on instancie l'objet csv ou les résultats vont être écrits
csv_analyse = implements.Analyse.csv_musicore('test')
csv_analyse.clear()

# lancement du test du parser
try:
    k = 1
    for i in path_to_files:
        analysed = implements.Analyse.analyse(i, 'test')
        resultat_parser = implements.Parser.parser(csv_analyse, analysed, True, True)
        # print(resultat_parser+'\033[94m')
        k += 1
except:
    print('un probleme est survenue')
print(("\033[1;32;40m Test 1 OK   \033[0;30;47m %s          \033[0m  " % resultat_parser))
############################################################################################

############################################################################################
# test du parser valide avec 2 musiques (False False)

# on instancie l'objet csv ou les résultats vont être écrits
csv_analyse = implements.Analyse.csv_musicore('test')
csv_analyse.clear()

# lancement du test du parser
try:
    k = 1
    for i in path_to_files:
        analysed = implements.Analyse.analyse(i, 'test')
        resultat_parser = implements.Parser.parser(csv_analyse, analysed, False, False)
        k += 1
except:
    print('un probleme est survenue')
print(("\033[1;32;40m Test 2 OK   \033[0;30;47m %s          \033[0m  " % resultat_parser))
############################################################################################

############################################################################################
# test du parser valide avec 2 musiques (True False)

# on instancie l'objet csv ou les résultats vont être écrits
csv_analyse = implements.Analyse.csv_musicore('test')
csv_analyse.clear()

# lancement du test du parser
try:
    k = 1
    for i in path_to_files:
        analysed = implements.Analyse.analyse(i, 'test')
        resultat_parser = implements.Parser.parser(csv_analyse, analysed, True, False)
        k += 1
except:
    print('un probleme est survenue')
print(("\033[1;32;40m Test 3 OK   \033[0;30;47m %s          \033[0m  " % resultat_parser))
############################################################################################

############################################################################################
# test du parser non valide avec 2 musiques (True False)
resultat_parser = []
# on instancie l'objet csv ou les résultats vont être écrits
csv_analyse = implements.Analyse.csv_musicore('test')
csv_analyse.clear()

# lancement du test du parser
try:
    k = 1
    for i in path_to_files:
        analysed = implements.Analyse.analyse(i, 'test')
        resultat_parser = implements.Parser.parser(csv_analyse, analysed, False)
        k += 1
except:
    print("\033[1;32;40m Test 4 OK   \033[0;30;47m           \033[0m  ")

    ############################################################################################
