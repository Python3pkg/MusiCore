# -*- coding: utf-8 -*-

'''
anlalyse audio de fichier audio:
-analyse du bpm
-analyse de la tonalité (harmonique)
'''
from __future__ import print_function
import librosa
import os
import csv
import sys

# Analyse Tonale
# from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
import matplotlib.pyplot as plt
# from numpy import sin, linspace, pi
from scipy.io.wavfile import read, write
import numpy

###############################################################################
# class `analyse`
###############################################################################
'''
Permet d'effectuer des analyses de musiques
fonctionne pour le mp3, wav
'''

class analyse:
    '''Classe définissant l'analyse d'une musique. On a l'analyse bpm et l'analyse de la tonalité
    '''

    def __init__(self, PathToFile=None, NomFichierCsv=None, pathtobdd=None):  # méthode constructeur
        '''

        :param PathToFile: chemin jusqu'au fichier audio
        :param NomFichierCsv: chemin jusqu'au fichier csv qui être crée par l'analyse
        :param pathtobdd: chemin jusqu'au fichier de la bdd
        :return: None

        '''

        if PathToFile is None:
            raise ValueError('Error: PathToFile is emplty')
        else:
            self.PathToFile = PathToFile  # chemin du fichier audio
        if NomFichierCsv is None:
            raise ValueError('Error: NomFichierCsv is empty')
        else:
            self.NomFichierCsv = NomFichierCsv  # chemin du fichier csv qui va être crée pour cette analyse
        if pathtobdd is None:
            self.pathtobdd = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/BDDMusic/BDDMusic"
        else:
            self.pathtobdd = pathtobdd  # chemin du fichier csv étant la base de donnée: par défaut '~/MusiCore/BDDMusic/BDDMusic'


    def extraire_path(self):
        """
        permet d'extraire d'un chemin absolu le nom du fichier une list

        :param path: chemin absolue d'une fichier audio
        :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]

        """

        # path1=path[::-1]
        k = 0
        while self.PathToFile[len(self.PathToFile) - k - 1] != "/":
            k = k + 1
        return [self.PathToFile[len(self.PathToFile) - k:],
                self.PathToFile[:len(self.PathToFile) - k - 1]]  # path to directory , file name

    def ecrirecsv(self, pathtobdd, list):
        '''
        :param list: liste dont les élements vont être ajoutés à un fichier csv

        '''

        fname = pathtobdd
        if os.path.isfile(pathtobdd) == True:  # si le fichier existe:
            try:  # rajoute seulement les lignes voulu
                print('ecrirecsv: le fichier ' + pathtobdd + ' existe, rajout des donnees dans le csv')
                file = open(fname, "a")  # l'option 'a' permet de ne pas ecraser le fichier
                # Creation de l'ecrivain CSV
                writer = csv.writer(file)

                # Ecriture des donnees.
                writer.writerow(list)

            finally:
                # Fermeture du fichier source
                file.close()

        else:  # si le fichier n'existe pas
            try:  # rajoute une entete
                print("ecrirecsv: le fichier " + pathtobdd + " n'existe pas, creation d'un nouveau fichier csv")
                file = open(fname, 'w')
                # Creation de l'ecrivain'' CSV
                writer = csv.writer(file)

                # Ecriture de la ligne d'en-tete avec le titre des colonnes.
                writer.writerow(['Emplacement', 'NomFichier', 'BpmMoyen', 'BpmDebut', 'BpmFin'])

                # Ecriture des quelques donnees.
                writer.writerow(list)
            finally:
                # Fermeture du fichier source
                file.close()


    def islineincsc(self, titre):
        '''
        blabla

        :param titre: le titre du fichier audio dont on veut vérifier si il existe dans le fichier csv
        :return: True si le fichier audio à deja été analysé
        Afin de vérifier si un fichier audio à deja été analysé, on compare les titres audio deja analysés dans la base de donnée avec le titre du fichier que l'on veut analyser

        '''

        fname = self.pathtobdd
        file = open(fname, "rt")  # file = open(fname, "rb") python 2.7
        try:
            reader = csv.reader(file)
            for row in (reader):
                #
                # N'affiche que certaines colonnes
                #
                if (len(row) != 5):
                    return False

                else:

                    # print("row = " + row[1])
                    # print("titre = " + titre)
                    if (row[1] == titre):
                        print('Le fichier existe deja dans la base de donnée')
                        print('Ecriture des données existantes de la bdd dans le fichier ' + self.NomFichierCsv)
                        self.ecrirecsv(self.NomFichierCsv, row)
                        return True
        finally:
            file.close()

        return False


    def extrairedatamusic(self):
        '''
        extrait les données de n'importe quel format de fichier supporté par l'api audioread

        :return: données de la musique sous forme de liste

        '''

        path = self.extraire_path()[1]
        filename = self.extraire_path()[0]  # filename le fichier qui va etre analyse

        # On l'emplacement courant a dossier ou se situe la musique
        os.chdir(self.extraire_path()[1])

        # on charge le fichier de musique
        return librosa.load(filename)


    def analyse_bpm(self, y, sr):
        """
        determine le bpm d'une musique
        exemple de test:
                        analyse1 = analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
                        y, sr = analyse1.extrairedatamusic()
                        analyse1.analyse_bpm(y, sr)

        :param pathtofile: chemin absolue du fichier audio dont on veut analyser le bpm
        :param fichier_csv: fichier csv dans lequel sera enregistre les bpms du morceau (nom de la playlist en cours)
        :Comment ecrit dans le fichier csv a la fin

        """

        # creation de la liste qui va etre exportee dans le csv
        ElemCsv = [self.PathToFile, self.extraire_path()[0]]

        # enregistrement du fichier audio comme une forme d'onde 'y' ; enrigistrement de taux d'echantillon en 'sr'
        # TODO: cette fonction est le goulot d'etranglement du programme, a ameliorer...

        # execution du tracker bpm par default
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        # Converti les sequences d'indice de beat en un chronogramme correspondant aux impulsions d'énergie au cours de la musique
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)

        # calcul du bpm du debut et de la fin de la musique dans le cas d'un changement au cours de la musique
        bpm_d = 0
        bpm_f = 0
        for i in range(100):
            bpm_d = bpm_d + (beat_times[i + 1] - beat_times[i])
            bpm_f = bpm_f + (beat_times[len(beat_times) - i - 1] - beat_times[len(beat_times) - i - 2])

        # on complete la lste qui va etre mis dans le csv
        ElemCsv.append(tempo)
        ElemCsv.append(60 / (bpm_d / 100))
        ElemCsv.append(60 / (bpm_f / 100))
        print("la liste qui va etre implementé est: ", ElemCsv)

        # ecriture des donnees dans la base de donnée et le fichier de playlist
        self.ecrirecsv(self.pathtobdd, ElemCsv)  # fichier
        self.ecrirecsv(self.NomFichierCsv, ElemCsv)

    def analysefft(self, y=None, Fs=None, k=None, afficher=False):
        '''
        Analyse fft d'un signal

        :param y: l'amplitude su signal audio
        :param Fs: la fréquence d'échantillonnage
        :param k: le nombre d'échantillon que l'on veut analyser dans la musique
        :return: retourne la fft du fichier audio

        '''
        if k is None:
            raise ValueError("il manque la valeur k")
        if y is None or Fs is None:
            raise ValueError("Les arguments y ou Fs sont manquants")

        tempsmusique = (2 * (len(y) / 44100))  # calcul de la durée de la musique
        print("la musique à une durée de: %s secondes" % tempsmusique)
        tfft = int(len(y) / 2)  # on commence l'analyse des echantillons au milieu de la musique
        notesfreq = numpy.zeros((k, 10))
        notesampli = numpy.zeros((k, 10))
        sommeY = 0

        for i in range(k):
            # print("nb d'éléments dans la liste y: %s" % len(y))
            y2 = y[tfft + 33000 * (i - 1):tfft + 33000 * (i)]

            n = len(y2)  # longueur du signal
            k2 = arange(n)
            T = n / Fs
            frq = k2 / T  # two sides frequency range
            freq = frq[range(int(n / 2))]  # one side frequency range

            # réalisation de la fft et normalisation

            Y = fft(y2) / n
            Y = abs(Y[range(int(n / 2))])

            # affichage des samples analysées sous matplotlib dans le cas ou afficher = True

            if afficher == True:
                list1 = []  # création de la liste contenant les intervalles de temps pour afficher le signal temporel
                for z in range(33000):
                    list1.append(z / 44100)

                plt.plot(freq, abs(Y))
                plt.show()

                plt.plot(list1, y2)
                plt.show()

            for j in range(10):

                # on cherche les pics dans la fft afin de déterminer les fréquences des notes dans le morceaux

                maximumY = Y[500 + 200 * j]
                maximumX = freq[500 + 200 * j]
                for w in range(200):
                    if Y[500 + w + 200 * j] > maximumY:
                        maximumY = Y[500 + w + 200 * j]
                        maximumX = freq[500 + w + 200 * j]
                # print("j= %s" % j)
                # print("i= %s" % i)
                notesfreq[i, j] = maximumX
                notesampli[i, j] = maximumY
                sommeY = sommeY + maximumY

            # On discrimine par rapport aux fréquences qui n'ont pas des amplitudes assez élevées

            sommeY = sommeY / 10
            for i2 in range(10):
                if notesampli[i, i2] < sommeY:
                    notesampli[i, i2] = 0
                    notesfreq[i, i2] = 0

        return notesfreq  # retour de la fft Y et de la fréquence qui va être l'abscisse de la fft

    def rechercheaccords(self, freq):
        '''
        permet de recercher les accords ou notes correspondantes aux fréquences présentent dans la matrice fred

        :param freq: matrice à 2 dim qui permet contenant les fréquences de plusieurs samples
        :return: les notes correspondants à la matrices des fréquences

        '''
        # fréquences des notes dans la gamme tempérée
        f0 = 32.70  # do ou si#
        f1 = 34.6444  # do# ou ré(b)
        f2 = 36.7045  # ré
        f3 = 38.8870  # ré# ou mi♭
        f4 = 41.1994  # mi ou fa♭
        f5 = 43.6492  # fa ou mi♯
        f6 = 46.2447  # fa♯ ou sol♭
        f7 = 48.9946  # sol
        f8 = 51.9080  # sol♯ ou la♭
        f9 = 54.9946  # la
        f10 = 58.2647  # la♯ ou si♭
        f11 = 61.7293  # si ou do♭

        # equivalent notes en notation américaines
        f0note = 'C'
        f1note = 'C#'
        f2note = 'D'
        f3note = 'D#'
        f4note = 'E'
        f5note = 'F'
        f6note = 'F#'
        f7note = 'G'
        f8note = 'G#'
        f9note = 'A'
        f10note = 'A#'
        f11note = 'B'

        #recherche des notes tempérées équivalentes aux fréquences obtenu par l'analyse fft
        matricenote = []  # numpy.zeros((len(freq), 10))

        for i in range(len(freq)):

            matricetemporelle = []

            for j in range(10):

                # print(freq[i, j])
                mult2 = 0
                while freq[i, j] / (2 ** mult2) > 62:
                    mult2 += 1

                note = freq[i, j] / (2 ** mult2)  # la note fait partie de l'intervalles des fréquences fondamentales

                if note >= (f0 - (f1 - f0) / 2) and note < (f0 + (f1 - f0) / 2):
                    matricetemporelle.append(f0note)
                if note >= (f1 - (f2 - f1) / 2) and note < (f1 + (f2 - f1) / 2):
                    matricetemporelle.append(f1note)
                if note >= (f2 - (f3 - f2) / 2) and note < (f2 + (f3 - f2) / 2):
                    matricetemporelle.append(f2note)
                if note >= (f3 - (f4 - f5) / 2) and note < (f3 + (f4 - f3) / 2):
                    matricetemporelle.append(f3note)
                if note >= (f4 - (f5 - f4) / 2) and note < (f4 + (f5 - f4) / 2):
                    matricetemporelle.append(f4note)
                if note >= (f5 - (f6 - f5) / 2) and note < (f6 + (f6 - f5) / 2):
                    matricetemporelle.append(f5note)
                if note >= (f6 - (f7 - f6) / 2) and note < (f6 + (f7 - f6) / 2):
                    matricetemporelle.append(f6note)
                if note >= (f7 - (f8 - f7) / 2) and note < (f7 + (f8 - f7) / 2):
                    matricetemporelle.append(f7note)
                if note >= (f8 - (f9 - f8) / 2) and note < (f8 + (f9 - f8) / 2):
                    matricetemporelle.append(f8note)
                if note >= (f9 - (f10 - f9) / 2) and note < (f9 + (f10 - f9) / 2):
                    matricetemporelle.append(f9note)
                if note >= (f10 - (f11 - f10) / 2) and note < (f10 + (f11 - f10) / 2):
                    matricetemporelle.append(f10note)
                if note >= (f11 - (f11 - f10) / 2) and note < (f11 + (f11 - f10) / 2):
                    matricetemporelle.append(f11note)

            matricenote.append(matricetemporelle)
        # print(matricenote)
        # recherche des possibles accords
        matriceaccords = []
        matricepoidsnotes = []

        a = [['C', 'F', 'G', 'A']['F', 'C', 'A#', 'D']['A#', 'F', 'G', 'D#']['D#', 'A#', 'C', 'G#']
             ['G#', 'D#', 'F', 'C#']['C#', 'G#', 'A#', 'F#']['F#', 'C#', 'D#', 'B']['B', 'F#', 'G#', 'E']
             ['E', 'B', 'C#', 'A']['A', 'E', 'F#', 'D']['D', 'A', 'B', 'G']['G', 'D', 'E', 'C']  # major keys
             ['A', 'E', 'C', 'D']['D', 'A', 'F', 'G']['G', 'D', 'A#', 'C']['C', 'G', 'D#', 'F']
             ['F', 'C', 'A#', 'G#']['A#', 'F', 'D#', 'C#']['D#', 'A#', 'F#', 'G#']['G#', 'D#', 'B', 'C#']
             ['C#', 'G#', 'E', 'F#']['F#', 'C#', 'A', 'B']['B', 'F#', 'D', 'E']['E', 'B', 'G', 'A']]  # minor keys

        for i in matricenote:

            for j in i:



        return matricenote

# ======================================================
# Fonctions annexes
# ======================================================

# plot(frq, abs(Y), 'r')  # plotting the spectrum
# xlabel('Freq (Hz)')
# ylabel('|Y(freq)|')
# y = y[: 441000]
# exemple fft
# rate,data=read('/home/bettini/Musique/Deorro.wav')
# x = numpy.arange(0,2000,100)

'''
analyse = analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv", 'bdd')
y, s = analyse.extrairedatamusic()

list1 = []  # création de la liste contenant les intervalles de temps pour afficher le signal temporel
for i in range(33000):
    list1.append(i / 44100)

Fs = 44100  # sampling rate
analyse.analysefft(y, Fs, 2, False)'''
