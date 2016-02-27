from __future__ import print_function
import librosa
import os

#----------------------------- Analyse du BPM -------------------------------
#fonctionne pour le mp3, wav
#entree: (position du fichier dans le systeme)

def extraire_path(path):
    """
    :param path: chemin absolue d'une fichier audio
    :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]
    Comment: permet d'extraire d'un chemin absolu le nom du fichier une list:

    """
    path1=path[::-1]
    k=0
    while path[len(path)-k-1]!="/":
        k=k+1
    return [path[len(path)-k:], path[:len(path)-k-1] ]

#print(extraire_path('/home/bettini/Musique/Deorro.wav')[0])
#print(list)


def analyse_bpm(pathtofile,fichier_csv):
    """
    :param pathtofile: chemin absolue du fichier audio dont on veut analyser le bpm
    :param fichier_csv:
    :return:
    Comment:

    """
    # On l'emplacement courant a dossier ou se situe la musique
    os.chdir(extraire_path(pathtofile)[1])
    #retval = os.getcwd()
    #print("Le dossier courant est %s" % retval)


    #filename le fichier qui va etre analyse
    filename = extraire_path(pathtofile)[0]

    #enregistrement du fichier audio comme une forme d'onde 'y'
    #enrigistrement de taux d'echantillon en 'sr'
    y, sr = librosa.load(filename)

    # execution du tracker bpm par default
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # Converti les sequences d'indice de beat en un chronogramme
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    #enregistrement du fichier csv
    print('enregistrement du fichier csv')
    #librosa.output.times_csv('beat_times.csv', beat_times)
    librosa.output.times_csv('fichier_csv.csv', beat_times)
    #lecteur_csv.read_csv(beat_times.csv)

analyse_bpm("/home/bettini/Musique/Deorro.wav", "fichier_csv") #test de mesure de BPM

