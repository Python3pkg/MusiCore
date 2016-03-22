# coding: utf-8
#test orienté_objet
#classe Musique déf par titre, BPM_debut, BPM_fin, pitch

#------------------------------
#import des librairies nécessaires

import csv

#--------------------
#Calcule le nombre de ligne du csv
def csvcount(filename):
    with open(filename, 'r') as f:
        i = 0
        for ligne in f:
            i += 1
    return i

#-----------------------------------
#transfo chaine de caractere '140' en 140 + nombre

def conversion(chaine):
    correc=chaine[0:len(chaine)]
    correcnombre=float(correc)
    return correcnombre

#-----------------------

class Musique:#def classe musique
    #titre, BPM_debut, BPM_fin, pitch
    def _init_(self, titre, BPM_debut, BPM_fin, pitch):#methode constructeur
       self.titre = titre #il faut extraire les données du csv
       self.BPM_debut = BPM_debut
       self.BPM_fin = BPM_fin
       self.pitch = pitch


#--------------------------------------------
#extraction du csv et copie dans classe Musique
#recuperation de la colonne BPM_debut dans le csv

fname1 = "testprojetinfo.csv"
file1 = open(fname1, "rb")
for i in range (cvscount(testprojetinfo.csv)):
    try:
        reader = csv.reader(file1)
        for row in reader:
            #
            # N'affiche que certaines colonnes
            #
            print row[0],row[1]
            titre"i"= Musique(row[0], conversion(row[1]), conversion(row[2]), row[3])
            i=i+1

    finally:
    file1.close()
    #test daffichage
    titre.titre1
    titree.titre2
