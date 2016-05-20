# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.analyseaudio
import os

# fonction de tests permettant de tester la detection de la tonalité
# les musiques analysées sont prises de facon aléatoire sur le web
# afin d'estimer au mieux la detection de la tonalité

# test de la musique Taylor swift
analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Taylor Swift - New Romantics.mp3", "fichier_csv",
                                          'bdd')
y, s = analyse.extrairedatamusic()
Fs = 44100  # sampling rate
notefreq = analyse.analysefft(y, Fs, 50,
                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
tonalite = analyse.rechercheaccords(notefreq)

# test unitaire
flag_fail = 0
for i in tonalite:
    if i == 'FM':
        print('le test est correct')
        flag_fail = 1
if flag_fail == 0:
    print("le test n'est pas correct")
    flag_fail = 0
