# -*- coding: utf-8 -*-
# test orienté_objet
# classe Musique déf par titre, BPM_debut, BPM_fin, pitch

# ------------------------------
# import des librairies nécessaires

import csv


# --------------------
# Calcule le nombre de ligne du csv
def csvcount(filename):
    with open(filename, 'r') as f:
        i = 0
        for ligne in f:
            i += 1
    return i


# -----------------------------------
# transfo chaine de caractere '140' en 140 + nombre

def conversion(chaine):
    '''

    :param chaine:
    :return:
    '''
    correc = chaine[0:len(chaine)]
    correcnombre = float(correc)
    return correcnombre


# -----------------------

#-----------------------
#classe musique
"""expliquer ce que c'est"""
class Musique:#def classe musique
    #titre, BPM_debut, BPM_fin, pitch
    def _init_(self, titre, emplacement, BPM_moy, BPM_debut, BPM_fin, pitch):#methode constructeur
       self.titre = titre #il faut extraire les données du csv
       self.emplacement = emplacement
       self.BPM_moy = BPM_moy
       self.BPM_debut = BPM_debut
       self.BPM_fin = BPM_fin
       self.pitch = pitch


# --------------------------------------------
# extraction du csv et copie dans classe Musique
# recuperation de la colonne BPM_debut dans le csv

fname1 = "testprojetinfo.csv"
file1 = open(fname1, "rb")
for i in range(cvscount(testprojetinfo.csv)):
    try:
        reader = csv.reader(file1)
        for row in reader:
            #
            # N'affiche que certaines colonnes
            #
            print
            row[0], row[1]
            titre
            "i" = Musique(row[0], conversion(row[1]), conversion(row[2]), row[3])
            i = i + 1

    finally:
        file1.close()
    # test daffichage
    titre.titre1
    titree.titre2
    
#------------------------------------------------------
#Tri bpm avec méthode du "plus court chemin"
#Idée : on calcule la différence de bpm entre chaque musique et on cherche le min de la somme des différences totales

#---------------------------
#Recherche du premier point
#ie le BPMmini du tableau

def BPMmini (tableaucool):
    BPM_min = 1000000
    i=0
    while i<len(tableaucool):
        if tableaucool[i]<= BPM_min:
            BPM_min = tableaucool[i]
        i=i+1
    return BPM_min


def BPMmaxi (tableaucool):
    BPM_max = 0
    i=0
    while i<len(tableaucool):
        if tableaucool[i]>= BPM_max:
            BPM_max = tableaucool[i]
        i=i+1
    return BPM_max


def tribpm (tableaucool):
    resultat = []
    resultat.append(BPMmini(tableaucool))
    sommet = (BPMmini(tableaucool))
    j=0
    i=0
    compteur = 100000
    print resultat
    for j in range (len(tableaucool)):
        while i<(len(tableaucool)):
            #if tableaucool[i] > sommet:
            #   print "test1"
            if abs(resultat[j]-tableaucool[i])<=compteur and tableaucool[i]>resultat[j]:
                compteur = abs(resultat[j]-tableaucool[i])
                    #if sommet == BPMmaxi(tableaucool):
                    #    return resultat
                sommet = tableaucool[i]
                print "test2"
            i=i+1
        resultat.append(sommet)
        j=j+1

    return resultat


tableaucool=[130,138,124,112]
print(tribpm(tableaucool))

    
    
