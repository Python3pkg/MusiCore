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
#       - Le résultat est:
#            CM avec un coef de corr:
#            0.824807923792
#            Cm avec un coef de corr:
#            0.563191807204
#            FM avec un coef de corr:
#            0.661283271996
#            Gm avec un coef de corr:
#            0.500330723771
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
#       - résultat:
#            CM avec un coef de corr:
#            0.605096298645
#            FM avec un coef de corr:
#            0.595927064442
# FM et CM au lieu de GM
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
    notefreq = analyse.analysefft(y, Fs, 50,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'A#m':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
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
#       - le test n'est pas exacte
#       - résultat:
#            C#M avec un coef de corr:
#            0.659716483494
#            A#m avec un coef de corr:
#            0.915701551523
#       - on devait trouver FM
######################################################

######################################################
# Musique 4
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/GESAFFELSTEIN - PURSUIT (Official video - CENSORED version).mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'Am':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
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
#       - le test n'est pas exact
#       - on trouve:
#            GM avec un coef de corr:
#            0.69657217525
#            Gm avec un coef de corr:
#            0.669347802381
#       - On attendait du Am
# commentaires: la tonalité G est très proche de celle Am
######################################################

######################################################
# Musique 5
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/Let It Be- The Beatles Lyrics........[lyrics in Description].mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'CM':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
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
#       - on trouve:
#            CM avec un coef de corr:
#            0.593796252183
#            GM avec un coef de corr:
#            0.68405750302
#            Gm avec un coef de corr:
#            0.635288511302
#       - la tonalité attendu est CM
# commentaire: le résultat est cohérent, les tonalités trouvées sont proches
######################################################

######################################################
# Musique 6
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Michael Jackson - Thriller (w-lyrics).mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'C#':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test est correct
       - on trouve:
            C#M avec un coef de corr:
            0.507794943227
            C#m avec un coef de corr:
            0.900575830736
            EM avec un coef de corr:
            0.608769779924
       - la tonalité attendu est C#
 commentaire: le résultat est exact'''
######################################################

######################################################
# Musique 7
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/michael jackson black or white lyrics.mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'C#':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test est correct
       - on trouve:
            EM avec un coef de corr:
            0.793720128828
            BM avec un coef de corr:
            0.539968427621
       - la tonalité attendu est EM
 commentaire: le résultat est exact'''
######################################################

######################################################
# Musique 8
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Hans Zimmer - Time (Inception).mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'Dm':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test n'est pas totalement correct
       - on trouve:
            DM avec un coef de corr:
            0.687974859795
            AM avec un coef de corr:
            0.809512035404
            Am avec un coef de corr:
            0.76264055654
       - la tonalité attendu est Dm
 commentaire: le résultat est exact'''
######################################################

######################################################
# Musique 9
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/Gladiator Super Theme Song (Honor Him, Elysium, & Now We Are Free).mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'Em':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test est correct
       - on trouve:
            EM avec un coef de corr:
            0.856747911425
            Em avec un coef de corr:
            0.527556472328
            AM avec un coef de corr:
            0.661303407986
            BM avec un coef de corr:
            0.59916512513
       - la tonalité attendu est Em
 commentaire: '''
######################################################

######################################################
# Musique 10
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse("/home/gerox/Téléchargements/Sweet Child O'Mine Lyrics-Guns N'Roses.mp3",
                                              'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 100,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

    # test de détection de la tonalite
    flag_fail = 0
    for i in tonalite:
        if i == 'C#M':  # c'est ici qu'il faut mettre la tonalité à tester pour le fichier audio
            print('le test est correct')
            flag_fail = 1
    if flag_fail == 0:
        print("le test n'est pas correct")
        flag_fail = 0
else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test est correct
       - on trouve:
            C#M avec un coef de corr:
            0.57060815046
            Fm avec un coef de corr:
            0.715678986153
            A#m avec un coef de corr:
            0.630658783386
       - la tonalité attendu est C#M
 commentaire: '''
######################################################

######################################################
# Musique 11
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/Guns N' Roses - November Rain(with lyrics).mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 100,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test n'est pas correct
       - on trouve:
            CM avec un coef de corr:
            0.556848860533
            Dm avec un coef de corr:
            0.511944128084
            FM avec un coef de corr:
            0.882426943681
            Fm avec un coef de corr:
            0.585747329741
            A#M avec un coef de corr:
            0.67630211599
       - la tonalité attendu est BM
 commentaire: '''
######################################################

######################################################
# Musique 12
flag_analyse = 1  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/You Could Be Mine-Guns N' Roses W- Lyrics.mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 100,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test n'est pas exactement correct mais très proche
       - on trouve:
            FM avec un coef de corr:
            0.851978362491
            Fm avec un coef de corr:
            0.766608584352
            A#M avec un coef de corr:
            0.603117107834
       - la tonalité attendu est F#
 commentaire: '''
######################################################
