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
#classe musique
class Musique:#def classe musique
    #titre, BPM_debut, BPM_fin,BPM_moy, pitch
    """
    titre = ""
    emplacement = ""
    BPM_moy = 0
    BPM_debut = 0
    BPM_fin = 0
    pitch = ""
    """
    def __init__(self, titre, emplacement, BPM_moy, BPM_debut, BPM_fin, pitch):#methode constructeur
       self.titre = titre #il faut extraire les données du csv
       self.emplacement = emplacement
       self.BPM_moy = BPM_moy
       self.BPM_debut = BPM_debut
       self.BPM_fin = BPM_fin
       self.pitch = pitch

a = Musique("a","b","c","d","e","f")
print(a.BPM_moy)

#--------------------------------------------
#extraction du csv et copie dans classe Musique
#recuperation de la colonne BPM_debut dans le csv
#tableauMus contient les objets Musiques extraits du  csv
"""
tableauMus = []
fname1 = "testprojetinfo.csv"
file1 = open(fname1, "rb")
for i in range (csvcount("testprojetinfo.csv")):
    try:
        reader = csv.reader(file1)
        for row in reader:
            #
            # N'affiche que certaines colonnes
            #
            print row[0],row[1]
            temp = Musique(row[0], row[1], conversion(row[2]), conversion(row[3]), conversion(row[4]), row[5])
            i=i+1
            tableauMus.append(temp)

    finally:
        file1.close()
    #test daffichage
    print tableauMus
""" #erreur inconnue
#----------------------------------------------------
#test

"""print tableaucool"""

#------------------------------------------------------
#------------------------------------------------------
# TRI BPM AVEC METHODE DU PLUS COURT CHEMIN
# #Idée : on calcule la différence de bpm entre chaque musique et on cherche le min de la somme des différences totales

#---------------------------
#Recherche du premier point
#ie le BPMmini du tableau

def BPMmini (tableaucool):
    BPM_min = 1000000 #on part d'un BPM de base "infini"
    i=0
    while i<len(tableaucool):
        if tableaucool[i]<= BPM_min:
            BPM_min = tableaucool[i]
        i=i+1
    return BPM_min

#inutilisé pour le moment, sera supprimé si non nécessaire
def BPMmaxi (tableaucool):
    BPM_max = 0
    i=0
    while i<len(tableaucool):
        if tableaucool[i]>= BPM_max:
            BPM_max = tableaucool[i]
        i=i+1
    return BPM_max


#----------------
# tri bpm
# à partir d'un tableau de BPMs (extraits des objets), création d'un nouveau tableau "resultat" avec les BPMs triés
# Avec cette méthode, il est possible d'inclure le tri harmonique et de le comparer au tri BPM avec des poids,
# ce qui était impossible avec un tri "classique" à 1 entrée.
# Remarque, ici BPM moyen seulement
def tribpm (tableaucool):
    resultat = []
    resultat.append(BPMmini(tableaucool))
    sommet = (BPMmini(tableaucool))
    j=0
    i=0
    compteur = 100000
    for j in range (len(tableaucool)-1):
        while i<(len(tableaucool)):
            if abs(resultat[j]-tableaucool[i])<=compteur and tableaucool[i]>resultat[j]:
                compteur = abs(resultat[j]-tableaucool[i])
                sommet = tableaucool[i]
            i=i+1
        resultat.append(sommet)
        j=j+1
        compteur=100000
        i=0
    return resultat

#test
tableaucool=[130,138,124,112]
print(tribpm(tableaucool))

# Si 2 bpms sont identiques, il les ajouter les uns à la suite des autres et cibler le tri en fonction de l'harmonique
#(à venir)

    
    
