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
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
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
    '''
    classe définissant l'analyse d'une musique. On a l'analyse bpm et l'analyse de la tonalité
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
        :param path: chemin absolue d'une fichier audio
        :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]
        Comment: permet d'extraire d'un chemin absolu le nom du fichier une list:
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
        :param pathtofile: chemin absolue du fichier audio dont on veut analyser le bpm
        :param fichier_csv: fichier csv dans lequel sera enregistre les bpms du morceau (nom de la playlist en cours)
        :Comment ecrit dans le fichier csv a la fin
        :exemple de test
        analyse1 = analyse("/home/bettini/Musique/Deorro.wav", "fichier_csv")
        y, sr = analyse1.extrairedatamusic()
        analyse1.analyse_bpm(y, sr)
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


    def analysefft(self, y=None, Fs=None):
        '''

        :param y: l'amplitude su signal audio
        :param Fs: la fréquence d'échantillonnage
        :return: retourne la fft du fichier audio
        '''
        if y is None or Fs is None:
            raise ValueError("Les arguments y ou Fs sont manquants")

        n = len(y)  # longueur du signal
        k = arange(n) #
        T = n / Fs
        frq = k / T  # two sides frequency range
        print(frq)
        frq = frq[range(n / 2)]  # one side frequency range

        Y = fft(y) / n  # réalisation de la fft et normalisation
        Y = Y[range(n / 2)]

        return abs(Y)  #retour de la fft


    def recherchenote(self):
        '''

        :param self:
        :return:
        '''

        return

# ======================================================
# Fonctions annexes
# ======================================================

# plot(frq, abs(Y), 'r')  # plotting the spectrum
# xlabel('Freq (Hz)')
# ylabel('|Y(freq)|')

# exemple fft
'''Fs = 44100;  # sampling rate
#rate,data=read('/home/bettini/Musique/Deorro.wav')
#y = data[: 441000]
analyse1 = analyse("/home/gerox/Musique/Deorro.wav", "fichier_csv",'bdd')
y = analyse1.extrairedatamusic()
Y = analyse1.analysefft(y,Fs)
print(Y)

lungime = len(y)
timp = len(y) / 44100
t = linspace(0, timp, len(y))
print(len(y))
print(len(t))
'''
