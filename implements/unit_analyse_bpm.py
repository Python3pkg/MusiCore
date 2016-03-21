#fonction de test de l'analyse bpm
import analyse_bpm
import os

analyse_bpm.analyse_bpm("/home/bettini/Musique/Deorro.wav", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
assert analyse_bpm.ecrirecsv('/home/bettini/PycharmProjects/MusiCore/BDDMusic/BDDMusic', 'BDDMusic')