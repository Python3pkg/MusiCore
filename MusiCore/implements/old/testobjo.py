# coding: utf-8
# test orienté_objet
# classe Musique déf par titre, BPM_debut, BPM_fin, pitch

# ------------------------------
# import des librairies nécessaires

import csv
from random import randint
import numpy as np


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
    correc = chaine[0:len(chaine)]
    correcnombre = float(correc)
    return correcnombre


# -----------------------
# classe musique
class Musique:  # def classe musique
    # titre, BPM_debut, BPM_fin,BPM_moy, pitch
    """
    titre = ""
    emplacement = ""
    BPM_moy = 0
    BPM_debut = 0
    BPM_fin = 0
    pitch = ""
    """

    def __init__(self, titre, emplacement, BPM_moy, BPM_debut, BPM_fin, pitch):  # methode constructeur
        self.titre = titre  # il faut extraire les données du csv
        self.emplacement = emplacement
        self.BPM_moy = BPM_moy
        self.BPM_debut = BPM_debut
        self.BPM_fin = BPM_fin
        self.pitch = pitch


a = Musique("a", "b", "c", "d", "e", "f")
print(a.BPM_moy)

# --------------------------------------------
# extraction du csv et copie dans classe Musique
# recuperation de la colonne BPM_debut dans le csv
# tableauMus contient les objets Musiques extraits du  csv
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
"""  # erreur inconnue
# ----------------------------------------------------
# test

"""print tableaucool"""


# ------------------------------------------------------
# ------------------------------------------------------
# TRI BPM AVEC METHODE DU PLUS COURT CHEMIN
# #Idée : on calcule la différence de bpm entre chaque musique et on cherche le min de la somme des différences totales

# ---------------------------
# Recherche du premier point
# ie le BPMmini du tableau

def BPMmini(tableaucool):
    BPM_min = 1000000  # on part d'un BPM de base "infini"
    i = 0
    while i < len(tableaucool):
        if tableaucool[i] <= BPM_min:
            BPM_min = tableaucool[i]
        i = i + 1
    return BPM_min


# inutilisé pour le moment, sera supprimé si non nécessaire
def BPMmaxi(tableaucool):
    BPM_max = 0
    i = 0
    while i < len(tableaucool):
        if tableaucool[i] >= BPM_max:
            BPM_max = tableaucool[i]
        i = i + 1
    return BPM_max


# ----------------
# tri bpm
# à partir d'un tableau de BPMs (extraits des objets), création d'un nouveau tableau "resultat" avec les BPMs triés
# Avec cette méthode, il est possible d'inclure le tri harmonique et de le comparer au tri BPM avec des poids,
# ce qui était impossible avec un tri "classique" à 1 entrée.
# Remarque, ici BPM moyen seulement
# !!!! Ne gère pas les cas d'égalité de bpm !!!! à modifier (voir plus bas)
# Implémenter le BPm_debut et le BPm_fin

def tribpm(tableaucool):
    resultat = []
    resultat.append(BPMmini(tableaucool))
    sommet = (BPMmini(tableaucool))
    j = 0
    i = 0
    compteur = 100000
    for j in range(len(tableaucool) - 1):
        while i < (len(tableaucool)):
            if abs(resultat[j] - tableaucool[i]) <= compteur and tableaucool[i] > resultat[j]:
                compteur = abs(resultat[j] - tableaucool[i])
                sommet = tableaucool[i]
            i = i + 1
        resultat.append(sommet)
        j = j + 1
        compteur = 100000
        i = 0
    return resultat


# test
tableaucool = [130, 138, 124, 112]
print(tribpm(tableaucool))


# Si 2 bpms sont identiques, il les ajouter les uns à la suite des autres et cibler le tri en fonction de l'harmonique
# (à venir)

# --------------------------------------
# Test tri harmonique+trim bpm mixé
# architecture du tri harmonique
#
# laMi , laMa , faMa , doMa
#
# Idée : prendre la première musique donnée et la considérer comme la musique de référence avec l'harmonique de référence
# A partir de là, on donne à cette harmo la valeur 1 et on ajoute 1 pour chaque harmo adjacente dans la roue, puis 2 etc...
# Les harmo correspondant à des valeurs numériques, on les soustrait comme avec le bpm pour trouver le min de la différence


def CalculInitHarmo():
    # Harmo de base : doMa (ie) DoMajeur
    # doMa = 1 puis ses voisins = 2 etc.
    return ()


def NumerotationHarmo(tableauharmo):
    # on définit de base une harmo de référence, on effecture les calculs avec (préréférencés) puis on décale les indices
    # pour le faire correspondre à l'harmo1 du tableau des harmoniques

    # Décalage indice : on prend ce que renvoie CalculInitHarmo, on calcule la différence DoMaj - Harmo1 puis on décale
    # les indices pour que les valeurs correspondent.

    # On effectue les différences via un algorithme similaire au tri BPM
    return ()


# -----------------------------------------
# Implémentation d'un algorithme génétique pour aboutir au tri final
mus1 = Musique("titre1", "coucou", 125, 80, 130, 1)
mus2 = Musique("titre2", "coucou2", 110, 78, 130, 12)
mus3 = Musique("titre3", "coucou3", 102, 90, 129, 13)
mus4 = Musique("titre4", "coucou4", 105, 28, 85, 24)
mus5 = Musique("titre5", "coucou5", 139, 38, 58, 6)
mus6 = Musique("titre6", "coucou5", 194, 48, 45, 3)
mus7 = Musique("titre7", "coucou6", 193, 55, 34, 8)
tableaudobjets = [mus1, mus2, mus3, mus4, mus5, mus6, mus7]
print
tableaudobjets[1].titre

"""
def voyageur_genetique(tableaudobjets):


    #titre, BPM_debut, BPM_fin,BPM_moy, pitch
    #titre = ""
    #emplacement = ""
    #BPM_moy = 0
    #BPM_debut = 0
    #BPM_fin = 0
    #pitch = ""

    j = 1
    num_solution = str(j)
    #for j in range (100):  #100 solutions init, arbitraire
     #  "solution" + num_solution = []
      #  j+=1
    solution1 = [1]
    solution2 =[]
    solution3 =[]
    solution4 = []

    print solution1
    #création de la population initiale de solutions
    #la solution doit passer par tous les points ET ne pas comporter de doublons
    j = 1
    num_solution = str(j)
    solution = "solution" + num_solution
    nbre_solution = 0

    #Détermination du nombre de solutions
    if len(tableaudobjets)<=100:
        nbre_solution = len(tableaudobjets)
    else:
        nbre_solution = 100


    for j in range (nbre_solution):
        for i in range (len(tableaudobjets)):
            if tableaudobjets[i-1] != tableaudobjets[i]:
                solution.append(tableaudobjets[randint(2,len(tableaudobjets))])
                j += 1

    print (solution1)  #?????? non fonctionnel


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

    return()
"""

"""
dictOfStuff = {}
j = 1
num_solution = str(j)
solution = "solution" + num_solution
for j in range (100):  #100 solutions init, arbitraire
    dictOfStuff["solution"+str(j)] = []

"""

# création de la population initiale de solutions
# la solution doit passer par tous les points ET ne pas comporter de doublons

# Détermination du nombre de solutions
if len(tableaudobjets) <= 100:
    nbre_solution = len(tableaudobjets)
else:
    nbre_solution = 100

    # Création de la matrice bpm avec 4 solutions initiales
matrice_solutionsBPM = np.zeros((nbre_solution, len(tableaudobjets)))
matrice_solutionsHARMO = np.zeros((nbre_solution, len(tableaudobjets)))


def creationtabl_BPM():
    i = 0
    tabl_BPM = []
    for i in range(len(tableaudobjets)):
        tabl_BPM.append(tableaudobjets[i].BPM_moy)
        i += 1
    return (tabl_BPM)


def creationtabl_HARMO():
    i = 0
    tabl_HARMO = []
    for i in range(len(tableaudobjets)):
        tabl_HARMO.append(tableaudobjets[i].pitch)
        i += 1
    return (tabl_HARMO)


print(creationtabl_HARMO())
print(creationtabl_BPM())
A = creationtabl_BPM()
B = creationtabl_HARMO()
j = 0
i = 0
k = 0
l = 0
valeur_random = 0
tabl_valeurrandom = []
for j in range(nbre_solution):
    # pour chaque ligne on ajoute toutes les musiques -> solution
    # il faut prendre un chiffre de tabl_bpm, le recopier et supprimer le bpm traité pr pas doublon)
    for i in range(len(tableaudobjets)):
        valeur_random = randint(0, len(A) - 1)
        matrice_solutionsBPM[j, i] = A[valeur_random]
        matrice_solutionsHARMO[j, i] = B[valeur_random]
        del A[valeur_random]
        del B[valeur_random]
        i += 1
    A = creationtabl_BPM()
    B = creationtabl_HARMO()
    j += 1

A = creationtabl_HARMO()
B = creationtabl_BPM()
print
matrice_solutionsHARMO
# print matrice_solutionsBPM


"""
    for j in range (nbre_solution):
    #pour chaque ligne on ajoute toutes les musiques -> solution
    #il faut prendre un chiffre de tabl_bpm, le recopier et supprimer le bpm traité pr pas doublon)
    for i in range (len(tableaudobjets)):
        derniere_val_donnee = tableaudobjets[randint(0,len(tableaudobjets)-1)].BPM_moy
        for k in range (len(stockage_valeurs)):
            if stockage_valeurs[0] == 0:
                matrice_solutionsBPM[i,j] = derniere_val_donnee
                stockage_valeurs[0] = derniere_val_donnee
            else:
                if derniere_val_donnee == stockage_valeurs[k]:
                    k += 1
            #Si la valeur est déjà dans le tableau, alors on la skip
                else:
                #ok la valeur a pas été prise, on peut l'ajouter sans soucis
                    matrice_solutionsBPM[i,j] = derniere_val_donnee
                    i += 1
                    k += 1
                    stockage_valeurs.append(derniere_val_donnee)
    j += 1
"""

# Evaluation de la qualité des solutions
# Détermination de la somme des écarts bpm pour chaque solution
tabl_BPMsoustrait = []  # contient l'écart entre chaque musique pr chaque solution
result_soustrac = 0
j = 0
i = 0
for i in range(nbre_solution):
    for j in range(1):
        while j + 1 <= (len(A) - 1):
            result_soustrac += abs(matrice_solutionsBPM[i, j] - matrice_solutionsBPM[i, j + 1])
            j += 1
        tabl_BPMsoustrait.append(result_soustrac)
        result_soustrac = 0
    i = i + 1

print
result_soustrac
print
tabl_BPMsoustrait

# Détermination de la somme des écarts harmo pr chaque solution
tabl_HARMOsoustrait = []  # contient l'écart harmo entre chaque musique pr chaque solution
result_soustrac2 = 0
matrice_pitchs = range(25)
x = 0
y = 0
i = 0
j = 0
for i in range(nbre_solution):
    for j in range(1):
        while j + 1 <= (len(B) - 1):
            x = matrice_solutionsHARMO[i, j]
            y = matrice_solutionsHARMO[i, j + 1]
            if x <= 12 and y <= 12:  # cas des harmos majeures
                if abs(matrice_solutionsHARMO[i, j] - matrice_solutionsHARMO[i, j + 1]) <= 7:
                    result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y))
                else:
                    if x > y:
                        result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(x + y))
                    else:
                        result_soustrac2 += abs(matrice_pitchs.index(y) - matrice_pitchs.index(x + y))
                j += 1
            elif x > 12 and y > 12:  # cas des harmos mineures
                if abs(matrice_solutionsHARMO[i, j] - matrice_solutionsHARMO[i, j + 1]) <= 7:
                    result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y))
                else:
                    if x > y:
                        result_soustrac2 += abs(matrice_pitchs.index(x - 12) - matrice_pitchs.index(x + y - 12 - 12))
                    else:
                        result_soustrac2 += abs(matrice_pitchs.index(y - 12) - matrice_pitchs.index(x + y - 12 - 12))
                j += 1
            else:  # cas où on a une différence mineur/majeur
                if x > 12:
                    x = x - 12
                else:
                    y = y - 12
                if abs(x - y) <= 7:
                    result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y)) + 1
                else:
                    if x > y:
                        result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(x + y)) + 1
                    else:
                        result_soustrac2 += abs(matrice_pitchs.index(y) - matrice_pitchs.index(x + y)) + 1
                j += 1
        tabl_HARMOsoustrait.append(result_soustrac2)
        result_soustrac2 = 0
    i = i + 1
print
tabl_HARMOsoustrait

# FAIRE ECART HARMO + PONDERATION

# Création de nouveaux individus par mutation

matrice_solutionsMutationBPM = matrice_solutionsBPM
matrice_solutionsMutationHARMO = matrice_solutionsHARMO
random1 = randint(0, len(tableaudobjets) - 1)
random2 = randint(0, len(tableaudobjets) - 1)

for j in range(len(tableaudobjets)):
    matrice_solutionsMutationBPM[random1, j] = matrice_solutionsBPM[random2, j]
    matrice_solutionsMutationBPM[random2, j] = matrice_solutionsBPM[random1, j]
    j += 1

print
random1, random2
print
matrice_solutionsBPM
print
matrice_solutionsMutationBPM

# Calculer les écarts sur les matrices mutées
# A IMPLANTER (ok)

# On choisit les 2 meilleurs solutions des solutions initiales et les deux meilleurs des solutions mutées

# PONDERATION
a = 0  # Coefficient de pondération si il vaut 0 alors on tient pas compte des écarts harmos
b = 1  # si b vaut 0 et a = 1 alors on tient seulement compte du tri harmo
i = 0
valeur_ponderee = 0
tabl_BPMHARMOpondeesoustrait = []
a = 10  # cas où il y a la meme importance entre harmos et bpms
for i in range(len(tabl_BPMsoustrait)):
    valeur_ponderee = b * tabl_BPMsoustrait[i] + a * tabl_HARMOsoustrait[i]  # REGLER COEFF A POUR PONDERATION
    tabl_BPMHARMOpondeesoustrait.append(valeur_ponderee)
m = min(tabl_BPMHARMOpondeesoustrait)

print
m

# Création  de la nouvelle solution
i = 0
j = 0
k = 0
matrice_nouvellesolutionBPM = np.zeros((nbre_solution, len(tableaudobjets)))
matrice_nouvellessolutionHARMO = np.zeros((nbre_solution, len(tableaudobjets)))

for k in range(nbre_solution // 2):  # verif qu'on a bien Moitié moitié de solution
    for i in range(len(tabl_BPMHARMOpondeesoustrait) - 1):
        if tabl_BPMHARMOpondeesoustrait[i] == min(tabl_BPMHARMOpondeesoustrait):
            for j in range(len(tabl_BPMHARMOpondeesoustrait)):
                matrice_nouvellesolutionBPM[k, j] = matrice_solutionsBPM[i, j]
                matrice_nouvellessolutionHARMO[k, j] = matrice_solutionsHARMO[i, j]
                j += 1
                tabl_BPMHARMOpondeesoustrait[i] = 999999
        i += 1
    k += 1

print
matrice_nouvellessolutionHARMO
print
matrice_nouvellesolutionBPM
# Refaire l'opération avec matrice mutuée (créer fonction "nouvelles solutions")


# ce soir : échange ligne, tri sur matrice mutée (voir directement à inverser nombres sur tabl_bpm etc)
#          et matrice solution finale
