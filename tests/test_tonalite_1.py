# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.analyseaudio
import os

# fonction de tests permettant de tester la detection de la tonalité
# les musiques analysées sont prises de facon aléatoire sur le web
# afin d'estimer au mieux la detection de la tonalité

k = 1

######################################################
# Musique 1
# test de la musique Taylor swift
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Taylor Swift - New Romantics.mp3",
                                              "fichier_csv",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 50,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'FM':
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

# résultat:
#       - le test est correct
######################################################

######################################################
# Musique 2
# test de la musique des beatles
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Beatles - Yellow Submarine.mp3",
                                              "fichier_csv",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 60,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'GM':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

# résultat:
#       - le test n'est pas correct
#       - FM et CM au lieu de GM
######################################################

######################################################
# Musique 3
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Musique/Alan Walker - Faded.mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 60,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'F#M':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

# résultat:
#       - le test est correct
#       - FM et CM au lieu de GM
######################################################

######################################################
# Musique 4
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Musique/Alan Walker - Faded.mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 60,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'G#M':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

# résultat:
#       - le test est correct
#       - on trouve G/ Gm / G#
######################################################
