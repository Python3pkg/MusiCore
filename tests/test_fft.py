# -*- coding: utf-8 -*-
# fonction de test de l'analyse de la tonalité

import implements.analyseaudio as analyseaudio

# test numéro 1

analyse = analyseaudio.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv", 'bdd')
y, s = analyse.extrairedatamusic()

Fs = 44100  # sampling rate
notefreq = analyse.analysefft(y, Fs, 3,
                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
analyse.rechercheaccords(notefreq)
