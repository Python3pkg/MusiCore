#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Aurélien BETTINI


import librosa
import os
import csv

# Analyse Tonale
from scipy import fft, arange, ifft
import matplotlib.pyplot as plt
import numpy

###############################################################################
# class `csv`
###############################################################################

class csv_musicore:
    '''Classe permettant la manipuation de fichiers cvs
    '''

    def __init__(self, nom_fichier_csv):
        '''

        :param nom_fichier_csv: nom du fichier csv qui sera enregistré dans le dossier database
        :return: None
        '''

        if nom_fichier_csv is None:
            raise ValueError('Error csv: nom_fichier_csv is empty')
        else:
            self.rootfolder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.path_to_csv_file = self.rootfolder + '/database/' + nom_fichier_csv  # chemin vers le fichier csv
            self.path_to_database = self.rootfolder + '/database/database'  # chemin vers la base de données

    def is_file(self, path_to_file):
        '''

        :param path_to_file: chemin du fichier csv qui va être ouvert
        :return: retour True si le fichier existe, False sinon
        '''
        if os.path.isfile(path_to_file) == True:
            return True
        else:
            return False

    def add_list(self, csv_file, liste):
        '''
        permet de rajouter une liste dans un fichier csv

        :param list: liste dont les élements vont être ajoutés à un fichier csv

        '''

        if isinstance(liste, list) == False:
            raise ValueError('la liste doit être un objet list')

        fname = csv_file
        if os.path.isfile(csv_file) == True:  # si le fichier existe:
            try:  # rajoute seulement les lignes voulu
                print('add_list: le fichier ' + self.path_to_csv_file + ' existe, rajout des donnees dans le csv')
                file = open(fname, "a")  # l'option 'a' permet de ne pas ecraser le fichier
                # Creation de l'ecrivain CSV
                writer = csv.writer(file)
                # Ecriture des donnees.
                writer.writerow(liste)

            finally:
                # Fermeture du fichier source
                file.close()

        else:  # si le fichier n'existe pas
            try:
                # ouverture du fichier
                print(
                    "add_list: le fichier " + csv_file + " n'existe pas, creation d'un nouveau fichier csv")
                file = open(fname, 'w')

                # Creation de l'ecrivain'' CSV
                writer = csv.writer(file)

                # Ecriture de la ligne d'en-tete avec le titre des colonnes.
                # writer.writerow(['NomFichier', 'BpmMoyen', 'BpmDebut', 'BpmFin'])  # il faudra rajouter la tonalité

                # Ecriture des donnees.
                writer.writerow(liste)
            finally:
                # Fermeture du fichier source
                file.close()
        return None

    def find_title_in_database(self, titre):
        '''
        regarde si le titre de la muif os.path.isfile(pathtobdd) == True:sique existe deja dans la base de données

        :param titre: le titre du fichier audio dont on veut vérifier si il existe dans le fichier csv
        :return: True si le fichier audio à deja été analysé
        Afin de vérifier si un fichier audio à deja été analysé, on compare les titres audio deja analysés dans la base de donnée avec le titre du fichier que l'on veut analyser

        '''

        if isinstance(titre, str) == False:
            raise ValueError('le titre doit être un string (str)')

        fname = self.path_to_database
        file = open(fname, "rt")  # file = open(fname, "rb") python 2.7
        num_row = 0
        try:
            reader = csv.reader(file)
            for row in (reader):
                #
                # N'affiche que certaines colonnes
                #
                if len(row) != 0:
                    if (row[0] == titre):
                        print('Le fichier existe deja dans la base de donnée')
                        if len(row) < 5:
                            return [True, num_row, row[1], len(row), None]
                        else:
                            return [True, num_row, row[1], len(row), row[4]]
                    num_row += 1
        finally:
            file.close()
        return [False]

    def add_column(self, path_to_csv_file, list_a_rajouter, col=None):

        if isinstance(list_a_rajouter, list) == False:
            raise ValueError('la liste doit être un objet list')
        with open(path_to_csv_file, 'rt') as input, open(self.rootfolder + '/database/temp.csv', 'wt') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')

            all = []
            # row = next(reader)
            # row.insert(0, 'ID')
            # row.append('ID')
            # all.append(row)
            count = 0
            for row in reader:
                if col == None:
                    row.append(list_a_rajouter[count])
                else:
                    row.insert(col, list_a_rajouter[count])
                all.append(row)
                count += 1
            writer.writerows(all)
            os.remove(path_to_csv_file)
            os.rename(self.rootfolder + '/database/temp.csv', path_to_csv_file)
        return

    def get_column(self, num_col):
        '''
        getter pour obtneir la colonne num_col du fichier csv de l'analyse

        :param num_col: numéro de la colonne que l'on souhaite obtenir
        :return: list (colonne num_col)

        '''
        fname = self.path_to_csv_file
        file = open(fname, "rt")  # on ouvre le fichier csv de la base de donnée
        colonne = []

        if isinstance(num_col, int) == False:
            raise ValueError('la liste doit être un entier')

        try:
            reader = csv.reader(file)  # on initialise le reader csv
            for row in (reader):
                colonne.append(row[num_col])
        finally:
            file.close()
        return colonne

    def get_row(self, num_row):
        '''

        :param num_row: numéro de la ligne que l'on souhaite obtenir
        :return: list (ligne num_row)

        '''
        if isinstance(num_row, int) == False:
            raise ValueError('la liste doit être un entier')

        fname = self.path_to_csv_file
        file = open(fname, "rt")  # on ouvre le fichier csv de la base de donnée
        flag_row = 0
        try:
            reader = csv.reader(file)  # on initialise le reader csv
            for row in (reader):
                if flag_row == num_row:
                    return row
                flag_row += 1
        finally:
            file.close()
        return False

    def get_column_database(self, num_col):
        '''

        :param num_col: numéro de la colonne de la base de données
        :return: list (colonne de la base de données)

        '''
        if isinstance(num_col, int) == False:
            raise ValueError('la liste doit être un entier')

        fname = self.path_to_database
        file = open(fname, "rt")  # on ouvre le fichier csv de la base de donnée
        colonne = []
        try:
            reader = csv.reader(file)  # on initialise le reader csv
            for row in (reader):
                colonne.append(row[num_col])
        finally:
            file.close()
        return colonne

    def get_row_database(self, num_row):
        '''

        :param num_row: numéro de la ligne que l'on souhaite obtenir
        :return: list (ligne num_row de la base de données)

        '''
        if isinstance(num_row, int) == False:
            raise ValueError('la liste doit être un entier')

        fname = self.path_to_database
        file = open(fname, "rt")  # on ouvre le fichier csv de la base de donnée
        flag_row = 0
        try:
            reader = csv.reader(file)  # on initialise le reader csv
            for row in (reader):
                if flag_row == num_row:
                    return row
                flag_row += 1
        finally:
            file.close()
        return False

    def delete_row(self, num_row):
        '''

        :param num_row: numéro de la ligne à supprimer
        :return: None

        '''
        if isinstance(num_row, int) == False:
            raise ValueError('la liste doit être un entier')

        with open(self.path_to_csv_file, 'rt') as input, open(self.rootfolder + '/database/temp.csv', 'wt') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')
            all = []
            count = 0
            for row in reader:
                if count != num_row:
                    all.append(row)
                print(count)
                count += 1
            writer.writerows(all)
            os.remove(self.path_to_csv_file)
            os.rename(self.rootfolder + '/database/temp.csv', self.path_to_csv_file)

        return None

    def delete_column(self, num_col):
        '''

        :param num_col: numéro de la colonne à supprimer
        :return: None

        '''
        if isinstance(num_col, int) == False:
            raise ValueError('la liste doit être un entier')

        with open(self.path_to_csv_file, 'rt') as input, open(self.rootfolder + '/database/temp.csv', 'wt') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')
            all = []
            count = 0
            for row in reader:
                all.append(row[0:num_col] + row[num_col + 1:])
                count += 1
            writer.writerows(all)
            os.remove(self.path_to_csv_file)
            os.rename(self.rootfolder + '/database/temp.csv', self.path_to_csv_file)
        return

    def delete_row_database(self, num_row):
        '''

        :param num_row: numéro de la colonne de la base de données à supprimer
        :return: None

        '''
        if isinstance(num_row, int) == False:
            raise ValueError('la liste doit être un entier')

        with open(self.path_to_database, 'rt') as input, open(self.rootfolder + '/database/temp.csv', 'wt') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')
            all = []
            count = 0
            for row in reader:
                if count != num_row:
                    all.append(row)
                count += 1
            writer.writerows(all)
            os.remove(self.path_to_database)
            os.rename(self.rootfolder + '/database/temp.csv', self.path_to_database)

        return

    def delete_column_database(self, num_col):
        '''

        :param num_col: numéro de la colonne de la base de données à supprimer
        :return: None

        '''
        if isinstance(num_col, int) == False:
            raise ValueError('la liste doit être un entier')

        with open(self.path_to_database, 'rt') as input, open(self.rootfolder + '/database/temp.csv', 'wt') as output:
            reader = csv.reader(input, delimiter=',')
            writer = csv.writer(output, delimiter=',')
            all = []
            count = 0
            for row in reader:
                all.append(row[0:num_col] + row[num_col + 1:])
                count += 1
            writer.writerows(all)
            os.remove(self.path_to_database)
            os.rename(self.rootfolder + '/database/temp.csv', self.path_to_database)
        return

    def nombre_ligne_csv(self):
        '''

        :return: nombre de ligne deans le fichier csv

        '''
        with open(self.path_to_csv_file, 'rt') as input:
            reader = csv.reader(input, delimiter=',')
            count = 0
            for row in reader:
                count += 1
        return count

    def clear(self):
        '''
        permet de supprimer le fichier csv de l'analyse

        :return: None

        '''
        if self.is_file(self.path_to_csv_file) == True:
            os.remove(self.path_to_csv_file)
            print('fichier :' + self.path_to_csv_file + ' supprimé')
        else:
            print("le fichier n'existe pas")

    def safe_state(self):
        '''
        vérifie que le fichier csv n'a pas de problème c'est à dire des sauts de lignes blanc

        :return: boolean
        '''
        with open(self.path_to_csv_file, 'rt') as input:
            reader = csv.reader(input, delimiter=',')
            count = 1
            for row in reader:
                # print(len(row))
                if len(row) == 0:
                    self.delete_row(count - 1)
                    count -= 1
                count += 1
        return

    def safe_state_database(self):
        '''
        vérifie que la fichier csv de la base de donné est dans un bon état

        :return: boolean

        '''
        with open(self.path_to_database, 'rt') as input:
            reader = csv.reader(input, delimiter=',')
            count = 1
            list = []
            for row in reader:
                print(len(row))
                if len(row) == 0:
                    self.delete_row_database(count - 1)
                    count -= 1
                count += 1
        return list


###############################################################################
# class `analyse`
###############################################################################

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
            self.pathtobdd = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/database/database"
        else:
            self.pathtobdd = pathtobdd  # chemin du fichier csv étant la base de donnée: par défaut '~/MusiCore/database/database'
        self.time = 0

    def extraire_path(self):
        """
        permet d'extraire d'un chemin absolu le nom du fichier une list

        :param path: chemin absolue d'une fichier audio
        :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]

        """

        k = 0
        while self.PathToFile[len(self.PathToFile) - k - 1] != "/":
            k = k + 1
        return [self.PathToFile[len(self.PathToFile) - k:],
                self.PathToFile[:len(self.PathToFile) - k - 1]]  # path to directory , file name

    def clean_analyses(self):
        '''
        Permet de suppimer le fichier d'analyse

        :return: None
        '''
        for element in os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/database'):
            print(element)
            if element == 'database' or element == 'output_ui':
                return
            else:
                os.rmdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/database' + element)

    '''def rajout_colonne_csv(self, path_to_csv_file, titre, element_a_rajouter):
        with open(path_to_csv_file, 'r') as csvinput:
            with open(path_to_csv_file, 'w') as csvoutput:
                writer = csv.writer(csvoutput, lineterminator='\n')
                reader = csv.reader(csvinput)

                all = []
                row = next(reader)
                row.append(titre)
                all.append(row)

                for row in reader:
                    row.append(row[0])
                    all.append(row)

                writer.writerows(all)
        return'''

    def extrairedatamusic(self):
        '''
        extrait les données de n'importe quel format de fichier supporté par l'api audioread

        :return: données de la musique sous forme de liste

        '''

        path = self.extraire_path()[1]
        filename = self.extraire_path()[0]  # filename le fichier qui va etre analyse

        # On l'emplacement courant a dossier ou se situe la musique
        os.chdir(self.extraire_path()[1])

        y, s = librosa.load(filename)  # on charge le fichier de musique

        # calcul de la durée de la musique
        seconds = int(2 * (len(y) / 44100))
        minutes = str(seconds // 60)
        seconds = str(seconds % 60)
        self.time = minutes + ':' + seconds

        return y, s

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
        ElemCsv = []

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

        # on complete la lste qui va etre mis dans le de la base de donnée
        ElemCsv.append(tempo)
        ElemCsv.append(60 / (bpm_d / 100))
        ElemCsv.append(60 / (bpm_f / 100))

        return ElemCsv  # bpm debut, bpm fin , bpm moyen

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
            freq = frq[list(range(int(n / 2)))]  # one side frequency range

            # réalisation de la fft et normalisation

            Y = fft(y2) / n
            Y = abs(Y[list(range(int(n / 2)))])

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

        # recherche des notes tempérées équivalentes aux fréquences obtenu par l'analyse fft
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
        print(matricenote)
        # recherche des possibles accords
        matriceaccords = []

        a = [['C', 'F', 'G', 'A', 'Maj'], ['F', 'C', 'A#', 'D', 'Maj'], ['A#', 'F', 'G', 'D#', 'Maj'],
             ['D#', 'A#', 'C', 'G#', 'Maj'],
             ['G#', 'D#', 'F', 'C#', 'Maj'], ['C#', 'G#', 'A#', 'F#', 'Maj'], ['F#', 'C#', 'D#', 'B', 'Maj'],
             ['B', 'F#', 'G#', 'E', 'Maj'],
             ['E', 'B', 'C#', 'A', 'Maj'], ['A', 'E', 'F#', 'D', 'Maj'], ['D', 'A', 'B', 'G', 'Maj'],
             ['G', 'D', 'E', 'C', 'Maj'],  # major keys
             ['A', 'E', 'C', 'D', 'Min'], ['D', 'A', 'F', 'G', 'Min'], ['G', 'D', 'A#', 'C', 'Min'],
             ['C', 'G', 'D#', 'F', 'Min'],
             ['F', 'C', 'A#', 'G#', 'Min'], ['A#', 'F', 'D#', 'C#', 'Min'], ['D#', 'A#', 'F#', 'G#', 'Min'],
             ['G#', 'D#', 'B', 'C#', 'Min'],
             ['C#', 'G#', 'E', 'F#', 'Min'], ['F#', 'C#', 'A', 'B', 'Min'], ['B', 'F#', 'D', 'E', 'Min'],
             ['E', 'B', 'G', 'A', 'Min']]  # minor keys

        Min = 0
        Maj = 0
        # for i in range(len(matricenote)):
        for i in matricenote:
            # for j in range(len(matricenote[i])):
            poidsmax = 0
            accord = False
            for j in i:
                # on a toutes les informations pour selectionner les éléments de matricenote
                for w in a:
                    poids = 0
                    if j == w[0]:
                        for z in range(len(w) - 1):
                            for i1 in range(len(i)):
                                # print("i1 = %s" %i1)
                                # print("w[z+1] = %s" %w[z+1])
                                if w[z] == i[i1] and w[z] != j and w[z] != 'Min' and w[z] != 'Maj':
                                    poids += 1  # on calcul le poids de chaque notes dans l'accord

                    ''' if poids != 0:
                        # print("poids = %s et note: " % poids + j)
                    if poids == 2 and poidsmax != 0:
                        matriceaccords.append(j)'''
                    if poids > poidsmax:
                        accord = j
                        poidsmax = poids
                        M = w[4]

            if accord != False:
                matriceaccords.append(accord)
                if M == 'Maj':
                    Maj += 1
                if M == 'Min':
                    Min += 1

        # print(matriceaccords)
        print("Maj = %s" % Maj)
        print("Min = %s" % Min)

        # Krumhansl-Schmuckler key-finding algorithm
        DurationPitch = []
        DurationPitch.append(matriceaccords.count('C'))
        DurationPitch.append(matriceaccords.count('C#'))
        DurationPitch.append(matriceaccords.count('D'))
        DurationPitch.append(matriceaccords.count('D#'))
        DurationPitch.append(matriceaccords.count('E'))
        DurationPitch.append(matriceaccords.count('F'))
        DurationPitch.append(matriceaccords.count('F#'))
        DurationPitch.append(matriceaccords.count('G'))
        DurationPitch.append(matriceaccords.count('G#'))
        DurationPitch.append(matriceaccords.count('A'))
        DurationPitch.append(matriceaccords.count('A#'))
        DurationPitch.append(matriceaccords.count('B'))
        print(DurationPitch)

        MajorProfil = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
        MinorProfil = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
        Note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        Tonalite = ['//']
        list_tonalite = ''

        for i in range(12):
            Major = numpy.corrcoef(DurationPitch, MajorProfil)[0, 1]
            Minor = numpy.corrcoef(DurationPitch, MinorProfil)[0, 1]
            if Major > 0.5:
                print("%sM avec un coef de corr: " % (Note[i]))
                print(Major)
                Tonalite.append(Note[i] + "M")
                Tonalite.append(Major)
                # list_tonalite = list_tonalite + Note[i] + "M" + '/'

            if Minor > 0.5:
                print("%sm avec un coef de corr: " % (Note[i]))
                print(Minor)
                Tonalite.append(Note[i] + "m")
                Tonalite.append(Minor)
                # list_tonalite = list_tonalite + Note[i] + "m" + '/'

            temporel = DurationPitch[1:]  # on effectue une translation de la liste DurationPitch
            temporel.append(DurationPitch[0])
            DurationPitch = temporel

            # Décommenter pour avoir une estimation de la tonalité d'une musique
        # On regarde si la musique est harmonique
            # if self.is_music_harmonic(Tonalite) == False:
            # print("l'algo estime que la musique est atonale")
            # Tonalite = ['**Musique atonale**']
        else:
            print("l'algorithme estime que la musique est tonale")

        # Décommenter pour activé la détection double d'une tonalité
        # if self.major_plus_minor(Tonalite) != False:
        #    list_tonalite = self.major_plus_minor(Tonalite)

        tonalite_max = self.tonalite_max(Tonalite)

        return Tonalite + [tonalite_max]

    def tonalite_max(self, tonalite):
        '''

        :param tonalite: liste des tonalités trouvées dans la musique
        :return: renvoie si la musique est tonale ou atonale selon le critère que le coeff de correlation le plus élevé trouvé est plus faible que 0,7
        '''
        # on determine le coeff de correlation maximal
        tonalite_max = 0
        key_max = 0
        for i in range(len(tonalite) // 2):
            key = tonalite[2 * (i) + 1]
            coef_corr = tonalite[2 * (i + 1)]
            if coef_corr > tonalite_max:
                tonalite_max = coef_corr
                key_max = key
                print("la tonalité max est : %s" % key)

        return key_max

    def is_music_harmonic(self, tonalite):
        '''

        :param tonalite: liste des tonalités trouvées dans la musique
        :return: renvoie si la musique est tonale ou atonale selon le critère que le coeff de correlation le plus élevé trouvé est plus faible que 0,7
        '''
        # on determine le coeff de correlation maximal
        tonalite_max = 0
        for i in range(len(tonalite) // 2):
            key = tonalite[2 * (i)]
            coef_corr = tonalite[2 * (i + 1)]
            if coef_corr > tonalite_max:
                tonalite_max = coef_corr

        # on effectue une regression selon le fait que le taux de correlation est plus faible que 0.7
        if tonalite_max < 0.65:
            print('la musique est atonale')
            return False
        else:
            return True

    def major_plus_minor(self, tonalite):
        '''
        On regarde si la musique possède des tonalités majeurs et mineurs
        une même clé. Dans ce cas on prend le nom de la clé sans tenir
        compte des mineur et majeur

        :param tonalite: liste des tonalités trouvées dans la musique
        :return: renvoie si la musique est tonale ou atonale selon le critère que le coeff de correlation le plus élevé trouvé est plus faible que 0,7
        '''
        note_mineur = ['Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 'Am', 'A#m', 'Bm']
        note_majeur = ['CM', 'C#M', 'DM', 'D#M', 'EM', 'FM', 'F#M', 'GM', 'G#M', 'AM', 'A#M', 'BM']
        note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        list_key = []

        for i in range(len(tonalite) // 2):
            key = tonalite[2 * (i) + 1]
            coef_corr = tonalite[2 * (i)]
            list_key.append(key)

        for i in list_key:
            for j in range(len(note_mineur)):
                if i == note_mineur[j - 1]:
                    for w in list_key:
                        if w == note_majeur[j - 1] and w != i:
                            return note[j - 1]

        return False
