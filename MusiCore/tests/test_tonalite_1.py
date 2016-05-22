# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.analyseaudio

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
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
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

######################################################
# Musique 13
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Maroon 5 - Animals (Lyric Video).mp3
       - le test est correct
       - on trouve:
            EM avec un coef de corr:
            0.592502540854
            Em avec un coef de corr:
            0.744238329757
            BM avec un coef de corr:
            0.644929571144
            Bm avec un coef de corr:
            0.761439653742
       - la tonalité attendu est Em
 commentaire: '''
######################################################

######################################################
# Musique 14
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Martin Garrix - Animals (Original Mix).mp3
       - le test est exact
       - on trouve:
            FM avec un coef de corr:
            0.75628135324
            Fm avec un coef de corr:
            0.887582754622
       - la tonalité attendu est Fm
 commentaire: '''
######################################################

######################################################
# Musique 15
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/DVBBS & Borgeous - Tsunami (Original Mix).mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test est correct
       - on trouve:
            EM avec un coef de corr:
            0.65910470368
            Em avec un coef de corr:
            0.643754723088
            BM avec un coef de corr:
            0.5710621592
       - la tonalité attendu est EM
 commentaire: ne converge pas vers la bonne tonalité pour un nombre de sample de 50 mais converge vers la bonne tonalité pour un nombre de sample de 70'''
######################################################

######################################################
# Musique 16
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/The Chainsmokers - Roses ft. ROZES.mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 75,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test n'est pas exactement correct mais très proche
       - on trouve:
            EM avec un coef de corr:
            0.646616765141
            G#m avec un coef de corr:
            0.596894593123
            BM avec un coef de corr:
            0.804560604125
            Bm avec un coef de corr:
            0.641488693253
       - la tonalité attendu est EM
 commentaire: ne converge pas vers la bonne tonalité pour un nombre de sample de 50 mais converge vers une des bonne tonalité pour r un nombre de sample de 70'''
######################################################

######################################################
# Musique 17
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/DJ Snake - Middle (Audio) ft. Bipolar Sunshine.mp3
       - le test est exact
       - on trouve:
            C#m avec un coef de corr:
            0.838872692727
            EM avec un coef de corr:
            0.689721990147
            AM avec un coef de corr:
            0.751876373539
       - la tonalité attendu est C#m
 commentaire: '''
######################################################

######################################################
# Musique 18
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/DJ Snake - Middle (Audio) ft. Bipolar Sunshine.mp3
       - le test est exact
       - on trouve:
            C#m avec un coef de corr:
            0.838872692727
            EM avec un coef de corr:
            0.689721990147
            AM avec un coef de corr:
            0.751876373539
       - la tonalité attendu est C#m
 commentaire: '''
######################################################

######################################################
# Musique 19
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/The Chainsmokers - Don't Let Me Down (Audio) ft. Daya.mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 70,
                                  False)  # notesfreq est la matrice contenant les fréquences significatives des k samples analysés
    tonalite = analyse.rechercheaccords(notefreq)

else:
    print("la musique n° %s n'est pas analysé" % k)

k += 1
flag_analyse = 0

''' résultat:
       - le test n'est pas correct
       - on trouve:
            F#M avec un coef de corr:
            0.87070366969
            BM avec un coef de corr:
            0.633154344685
       - la tonalité attendu est G#m
 commentaire: '''
######################################################

######################################################
# Musique 20
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Skrillex & Diplo - Mind feat. Kai (Official Video).mp3
       - le test est exact
       - on trouve:
            C#M avec un coef de corr:
            0.720177779325
            A#m avec un coef de corr:
            0.938174825672
       - la tonalité attendu est A#m
 commentaire: '''
######################################################

######################################################
# Musique 20
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Skrillex & Diplo - Mind feat. Kai (Official Video).mp3
       - le test est exact
       - on trouve:
            C#M avec un coef de corr:
            0.720177779325
            A#m avec un coef de corr:
            0.938174825672
       - la tonalité attendu est A#m
 commentaire: '''
######################################################

######################################################
# Musique 21
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Ray Charles - Georgia On My Mind (The Orginal Song From The Albom).mp3
       - le test ne converge pas
       - on trouve:
            l'algo estime que la musique est atonale
            GM avec un coef de corr:
            0.617640192354
       - la chanson n'est pas tonale mais on trouve quelle peut être joué en Fm
 commentaire: '''
######################################################

######################################################
# Musique 22
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Stand By Me, Ben E King, 1961.mp3
       - le test est exact
       - on trouve:
            C#m avec un coef de corr:
            0.557784243064
            EM avec un coef de corr:
            0.610182701334
            F#m avec un coef de corr:
            0.625252756297
            AM avec un coef de corr:
            0.766851232757
       - la chanson doit avoir une tonalité de AM
 commentaire: '''
######################################################

######################################################
# Musique 23
flag_analyse = 1  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.analyseaudio.analyse(
        "/home/gerox/Téléchargements/Louis Armstrong - What a wonderful world Lyrics.mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 45,
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
            0.751591252341
            FM avec un coef de corr:
            0.713845278532
            Am avec un coef de corr:
            0.767634137075
       - la tonalité attendu est FM
 commentaire: '''
######################################################
