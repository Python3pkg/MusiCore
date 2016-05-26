# -*- coding: utf-8 -*-
# author: Aurélien BETTINI
# fonction de test de l'analyse de la tonalité

import implements.Analyse as Analyse

# Test de le tonalité
# Mettre le chemin de la musique dont on veut analyser la tonalité dans l'instanciation de l'objet analyse
# Ceux-ci est la syntaxe pour pouvoir analyser la tonalité d'une musique

analyse = Analyse.analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv", 'bdd')
y, s = analyse.extrairedatamusic()
Fs = 44100  # sampling rate
notefreq = analyse.analysefft(y, Fs, 50,
                              False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
tonalite = analyse.rechercheaccords(notefreq)
print('tonalité')

''' Résultat:
la musique à une durée de: 308.964716553288 secondes
[['F', 'D', 'F', 'G', 'A', 'D'], ['F', 'A#', 'F', 'A'], ['F', 'C', 'G'], ['G', 'A#', 'F', 'G', 'D'], ['G', 'F', 'A', 'C'], ['A#', 'F'], ['A#', 'D', 'A'], ['A', 'A#', 'C', 'G', 'A#'], ['A', 'C'], ['G', 'A#', 'F', 'G', 'A#'], ['A', 'A#', 'F', 'A#'], ['A#', 'D', 'A#'], ['A#', 'F'], ['A', 'A#', 'A#'], ['G', 'F', 'G', 'A#'], ['A#', 'F', 'A#'], ['A#', 'D', 'A#', 'D'], ['A#', 'A#'], ['A#', 'A#'], ['G', 'F', 'G'], ['A#', 'A#', 'F'], ['A', 'A#', 'D', 'A#', 'D'], ['A#', 'D', 'A#'], ['A#', 'G', 'A#'], ['G', 'G', 'D', 'G'], ['G', 'C', 'D', 'G'], ['F', 'A#', 'F'], ['F', 'A#'], ['G', 'D', 'F', 'G'], ['G', 'G', 'D', 'G'], ['A', 'A', 'C'], ['F', 'A#', 'F'], ['F', 'A#'], ['G', 'G', 'D', 'G'], ['F', 'A#', 'F'], ['F', 'A#'], ['F', 'D', 'A'], ['F', 'C', 'G'], ['D', 'A', 'C', 'D'], ['A#', 'D'], ['F', 'C#', 'F'], ['F', 'D', 'F', 'A'], ['F', 'C'], ['G', 'D', 'F', 'G', 'D'], ['G', 'F', 'A', 'D'], ['G', 'F'], ['G', 'F', 'G'], ['A', 'A#', 'A#', 'F', 'A#'], ['A#', 'G'], ['G', 'F', 'G']]
Maj = 28
Min = 10
[4, 0, 10, 0, 0, 8, 0, 3, 0, 3, 10, 0]
Dm avec un coef de corr:
0.81366781661
FM avec un coef de corr:
0.691057793561
Gm avec un coef de corr:
0.576458723924
A#M avec un coef de corr:
0.857714083188
l'algorithme estime que la musique est tonale
tonalité'''
