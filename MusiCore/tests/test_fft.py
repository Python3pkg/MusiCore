# -*- coding: utf-8 -*-
# # author: Aurélien BETTINI
# fonction de test de l'analyse de la tonalité

import implements.Analyse as Analyse

# test numéro 1
# Mettre le chemin de la musique dont on veut analyser la tonalité dans l'instanciation de l'objet analyse

analyse = Analyse.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv", 'bdd')
y, s = analyse.extrairedatamusic()

Fs = 44100  # sampling rate
notefreq = analyse.analysefft(y, Fs, 50,
                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
analyse.rechercheaccords(notefreq)
