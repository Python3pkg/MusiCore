#fonction de test de l'analyse bpm
import analyse_bpm
import os
#test en analyse
analyse_bpm.analyse_bpm("/home/bettini/Musique/Deorro.wav", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
analyse_bpm.analyse_bpm("/home/bettini/Musique/AC-DC - Highway to Hell.mp3", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
analyse_bpm.analyse_bpm("/home/bettini/Musique/Daft Punk - Get Lucky ft. Pharrell Williams.mp3", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
analyse_bpm.analyse_bpm("/home/bettini/Musique/Happy - Pharrell Williams.mp3", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
#analyse_bpm.analyse_bpm("/home/bettini/Musique/", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
#analyse_bpm.analyse_bpm("/home/bettini/Musique/", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
#analyse_bpm.analyse_bpm("/home/bettini/Musique/", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)
#analyse_bpm.analyse_bpm("/home/bettini/Musique/", "fichier_csv") #test (.wav, chemin correct jusqu'au fichier)

#temps analyse bpm de 4 musiques:1min01sec


#test en ecriture
#analyse_bpm.ecrirecsv('/home/bettini/PycharmProjects/MusiCore/BDDMusic/BDDMusic', 'BDDMusic')