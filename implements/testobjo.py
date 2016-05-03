# coding: utf-8
#test orienté_objet
#classe Musique déf par titre, BPM_debut, BPM_fin, pitch

#------------------------------
#import des librairies nécessaires

import csv
from random import randint

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
# !!!! Ne gère pas les cas d'égalité de bpm !!!! à modifier (voir plus bas)
# Implémenter le BPm_debut et le BPm_fin

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

#--------------------------------------
#Test tri harmonique+trim bpm mixé
#architecture du tri harmonique
#
# laMi , laMa , faMa , doMa
#
# Idée : prendre la première musique donnée et la considérer comme la musique de référence avec l'harmonique de référence
# A partir de là, on donne à cette harmo la valeur 1 et on ajoute 1 pour chaque harmo adjacente dans la roue, puis 2 etc...
# Les harmo correspondant à des valeurs numériques, on les soustrait comme avec le bpm pour trouver le min de la différence


def CalculInitHarmo():
    #Harmo de base : doMa (ie) DoMajeur
    # doMa = 1 puis ses voisins = 2 etc.
    return ()


def NumerotationHarmo (tableauharmo):
    # on définit de base une harmo de référence, on effecture les calculs avec (préréférencés) puis on décale les indices
    #pour le faire correspondre à l'harmo1 du tableau des harmoniques

    #Décalage indice : on prend ce que renvoie CalculInitHarmo, on calcule la différence DoMaj - Harmo1 puis on décale
    # les indices pour que les valeurs correspondent.

    # On effectue les différences via un algorithme similaire au tri BPM
    return()


#-----------------------------------------
#Implémentation d'un algorithme génétique pour aboutir au tri final
mus1 = Musique("titre1","coucou",125,80,130,2)
mus2 = Musique("titre2","coucou2",110,78,130,6)
mus3 = Musique("titre3","coucou3",102,90,129,8)
mus4 = Musique("titre4","coucou4",105,28,85,15)
tableaudobjets = [mus1,mus2,mus3,mus4]


def voyageur_genetique(tableaudobjets):


    #titre, BPM_debut, BPM_fin,BPM_moy, pitch
    """
    titre = ""
    emplacement = ""
    BPM_moy = 0
    BPM_debut = 0
    BPM_fin = 0
    pitch = ""
    """

    #for i in range (100):  #100 solutions init, arbitraire
     #   solution"i" = []
    solution1 = []
    solution2 = []
    solution3 = []
    solution4 = []

    #création de la population initiale de solutions
    #la solution doit passer par tous les points ET ne pas comporter de doublons
    for i in range (len(tableaudobjets)):
        #for j in range (len(tableaudobjets)):
         #   if tableaudobjets[i] != tableaudobjets[j]:
                solution1.append(tableaudobjets[randint(2,len(tableaudobjets))])
                solution2.append(tableaudobjets[randint(2,len(tableaudobjets))])
                solution3.append(tableaudobjets[randint(2,len(tableaudobjets))])
                solution4.append(tableaudobjets[randint(2,len(tableaudobjets))])

    solution1 = [mus1,mus2,mus3,mus4]
    print (solution1[1].titre)  #?????? non fonctionnel

    #Evaluation des individus
    #1. évaluation des écarts
    #Pour chaque solution, calculer la somme des écarts succesifs en bpm et les ajouter dans un tableau
    # sumBPM = [49,59,38,103] -> 4 individus, pour le premier individu, la somme des écarts entre les BPm
    # de ses musiques vaut 49

    def ecart_bpm ():
        tab_sumbpm = []
        compteurbpm = 0
        for h in range [0,100]:
            for i in range (len(solution1)-1):  #parcourir les indices à l'envers pr éviter val abs
                compteurbpm = abs(solution"h"[i].BPM_moy - solution"h"[i].BPM_moy)
            tab_sumbpm.append(compteurbpm)
            compteurbpm = 0
        return tab_sumbpm

    #POur chaque solution, calculer la somme des écarts successifs en harmos et les ajouter dans un tableau
    def ecart_harmo ():
        tab_sumharmo = []
        compteurharmo = 0
        for h in range [0,100]:
            for i in range (len(solution1)-1):  #parcourir les indices à l'envers pr éviter val abs
                compteur = abs(solution"h"[i].pitch - solution"h"[i].pitch)
            tab_sumharmo.append(compteurharmo)
            compteurharmo = 0
        return tab_sumharmo
    # Rappel : on cherche solution telle que min(bpm) ET min(harmo) Trouver méthode de discrimination
    #  (par pondération ou on considère les 2 var comme pas comparables -> méthode de domination)
    # On veut comparer les solutions entre elles !!

    coeff_ponderation = 0 #définir une condition donnant la valeur du coeff en fonction des pref utilisateur
    def ponderation ():
        for i in range (100):
            if

    #2. Création de nouveaux individus par sélection ou mutation (peut-être combiner les deux)
    # Remarque : mutation = par ex, on échange la place de 2 musiques sur un invidu
    #création de 100 nouvelles solutions par permutation aléatoire
    def mutation ():
        for i in range [1,100]:
            solution
    # 3. Insertion des nouveaux individus dans la population
    #quoi qu'il arrive, on reste toujours avec 100 individus. On prend les 100 meilleurs => il faut refaire l'évaluatio
    # n des écarts !
    #ou alors on fait l'évaluation des écarts maintenant ...
    # => OK ON A EU NOTRE DEUXIEME GENERATION

    def selection ():



    # 5. On recommence N fois pr avoir N+1 génération jusqu'à ce qu'on trouve un truc qui semble pas mal (mini 10 gén,
    # 500 = solutions fixes)
    # créer boucle au début de l'algo génétique

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
