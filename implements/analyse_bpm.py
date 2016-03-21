from __future__ import print_function
import librosa
import os
import csv

#----------------------------- Analyse du BPM -------------------------------
#fonctionne pour le mp3, wav
#entree: (position du fichier dans le systeme)

def extraire_path(path):
    """
    :param path: chemin absolue d'une fichier audio
    :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]
    Comment: permet d'extraire d'un chemin absolu le nom du fichier une list:
    """

    #path1=path[::-1]
    k=0
    while path[len(path)-k-1]!="/":
        k=k+1
    return [path[len(path)-k:], path[:len(path)-k-1] ]


def ecrirecsv(pathtofile, list):

    #verifie si on peut ouvrir le fichier
    try:
        with open(pathtofile): pass
    except IOError:
        print("Erreur! Le fichier n'a pas pu etre ouvert")

    fname = pathtofile
                                                                        #l'option 'a' permet de ne pas ecraser le fichier

    if os.path.isfile(pathtofile) == True:                                      #si le fichier existe:
        try:                                                            #rajoute seulement les lignes voulu
            print('le fichier existe')
            file = open(fname, "a")
            # Creation de l'ecrivain'' CSV
            writer = csv.writer(file)

            # Ecriture des donnees.
            writer.writerow( list )

        finally:
            # Fermeture du fichier source
            file.close()

    else:                                                               #si le fichier n'existe pas
        try:                                                            #rajoute une entete
            print("le fichier n'existe pas")
            file = open(fname, "wb")
            # Creation de l'ecrivain'' CSV
            writer = csv.writer(file)

            # Ecriture de la ligne d'en-tete avec le titre des colonnes.

            writer.writerow( ('Emplacement','NomFichier','BpmMoyen','BpmDebut', 'BpmFin') )
            #
            # Ecriture des quelques donnees.
            writer.writerow( list )
        finally:
            # Fermeture du fichier source
            file.close()



def analyse_bpm(pathtofile,NomFichierCsv):
    """
    :param pathtofile: chemin absolue du fichier audio dont on veut analyser le bpm
    :param fichier_csv: fichier csv dans lequel sera enregistre les bpms du morceau (nom de la playlist en cours)
    :return:
    Comment:
    """

    path=extraire_path(pathtofile)[1]
    filename = extraire_path(pathtofile)[0]    #filename le fichier qui va etre analyse

    # On l'emplacement courant a dossier ou se situe la musique
    os.chdir(extraire_path(pathtofile)[1])

    #creation de la liste qui va etre exportee dans le csv
    ElemCsv=[path,filename]

    #enregistrement du fichier audio comme une forme d'onde 'y' ; enrigistrement de taux d'echantillon en 'sr'
    #TODO: cette fonction est le goulot d'etranglement du programme, a ameliorer...
    y, sr = librosa.load(filename)

    # execution du tracker bpm par default
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    #bpm moyen
    #print('tempo moyen: {:.2f} BPM'.format(tempo))

    #Converti les sequences d'indice de beat en un chronogramme
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    #calcul du bpm du debut et de la fin de la musique dans le cas d'un changement au cours de la musique
    bpm_d=0
    bpm_f=0
    for i in range(100):
        bpm_d=bpm_d+(beat_times[i+1]-beat_times[i])
        bpm_f=bpm_f+(beat_times[len(beat_times)-i-1]-beat_times[len(beat_times)-i-2])
    #print("BPM_debut = %s" %(60/(bpm_d/100)))

    #on complete la lste qui va etre mis dans le csv
    ElemCsv.append(tempo)
    ElemCsv.append(60/(bpm_d/100))
    ElemCsv.append(60/(bpm_f/100))


    #ecriture des donnees dans le fichier csv
    ecrirecsv('/home/bettini/PycharmProjects/MusiCore/BDDMusic/BDDMusic',ElemCsv)

    return




def LigneExisteCsv(pathtofile):
    # Ouverture du fichier source.
    #
    # D'apres la documentation, le mode ''b'' est
    # *obligatoire* sur les plate-formes ou il est
    # significatif. Dans la pratique, il est conseille
    # de toujours le mettre.
    #
    fname = pathtofile
    file = open(fname, "rb")

    try:
        # Creation du ''lecteur'' CSV.
        #
        reader = csv.reader(file)
        #
        #  Le ''lecteur'' est iterable, et peut etre utilise
        # dans une boucle ''for'' pour extraire les
        # lignes une par une.
        for row in reader:
	        print(row)
    finally:
        file.close()                                                   # Fermeture du fichier source