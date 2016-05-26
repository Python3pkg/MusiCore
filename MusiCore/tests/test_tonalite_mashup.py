# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm
import implements.Analyse

# fonction de tests permettant de tester la detection de la tonalité
# les musiques analysées sont prises de facon aléatoire sur le web
# afin d'estimer au mieux la detection de la tonalité

k = 1

######################################################
# Musique 1
flag_analyse = 0  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.Analyse.analyse(
        "/home/gerox/Téléchargements/Bastille - Pompeii.mp3",
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

'''
# résultat:
       - le test est correct
       - on trouve:
            C#m avec un coef de corr:
            0.571969213155
            EM avec un coef de corr:
            0.79918209089
            Em avec un coef de corr:
            0.642170783417
            AM avec un coef de corr:
            0.645622655019
       - la tonalité attendu est AM
 commentaire: '''
######################################################

######################################################
# Musique 2
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Audien feat. Ruby Prophet - Circles.mp3
       - le test est exact
       - on trouve:
            C#m avec un coef de corr:
            0.726874815079
            EM avec un coef de corr:
            0.939131036696
            AM avec un coef de corr:
            0.649298623007
            BM avec un coef de corr:
            0.557362534793
       - la tonalité attendu est AM
 commentaire: '''
######################################################

######################################################
# Musique 3
flag_analyse = 1  # ce flag est mis à 1 si l'on veut analyser la musique
if flag_analyse == 1:
    print('la musique n° %s est analysé' % k)
    analyse = implements.Analyse.analyse(
        "/home/gerox/Téléchargements/Mako - Our Story [Free].mp3",
        'bdd')
    y, s = analyse.extrairedatamusic()
    Fs = 44100  # sampling rate
    notefreq = analyse.analysefft(y, Fs, 80,
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

'''
# résultat:
       - le test est correct
       - on trouve:
            FM avec un coef de corr:
            0.604609999543
            Fm avec un coef de corr:
            0.806040792941
       - la tonalité attendu est AM
 commentaire: '''
######################################################

# ----------------------------------------------------
# Mashup n°2
# ----------------------------------------------------

######################################################
# Musique 1
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Deorro Five hour
       - le test est exact
       - on trouve:
            Dm avec un coef de corr:
            0.706816702113
            FM avec un coef de corr:
            0.625704578341
       - la tonalité attendu est FM
 commentaire: '''
######################################################

######################################################
# Musique 2
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Rather Be
       - le test est exact
       - on trouve:
            F#M avec un coef de corr:
            0.515285760366
            G#m avec un coef de corr:
            0.623401029396
            BM avec un coef de corr:
            0.647802221814
       - la tonalité attendu est G#m
 commentaire: '''
######################################################

######################################################
# Musique 3
# Analyse à l'aide de l'interface graphique
''' résultat:
fichier /home/gerox/Téléchargements/Tritonal feat Phoebe
       - le test est exact
       - on trouve:
            C#M avec un coef de corr:
            0.500978580867
            C#m avec un coef de corr:
            0.565600049356
            F#M avec un coef de corr:
            0.699044079929
            F#m avec un coef de corr:
            0.712539932281
            BM avec un coef de corr:
            0.511669205908
       - la tonalité attendu est F#m
 commentaire: '''
######################################################
