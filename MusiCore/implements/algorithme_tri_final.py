# coding: utf-8
# test orienté_objet
# classe Musique déf par titre, BPM_debut, BPM_fin, pitch

# ------------------------------
# import des librairies nécessaires

import csv
from random import randint
import numpy as np


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
    duree = ""
    """

    def __init__(self, titre, emplacement, BPM_moy, BPM_debut, BPM_fin, pitch, duree):  # methode constructeur
        self.titre = titre  # il faut extraire les données du csv
        self.emplacement = emplacement
        self.BPM_moy = BPM_moy
        self.BPM_debut = BPM_debut
        self.BPM_fin = BPM_fin
        self.pitch = pitch
        self.duree = duree


""" #Exemple
a = Musique("a","b","c","d","e","f","g")
print(a.BPM_moy)
"""

# -------------------------
# Importation de la matrice avec les infos et conversion en objet

# matrice_import = ??? à recevoir de tintin
#

# -----------------------------------------
# Implémentation d'un algorithme génétique pour aboutir au tri final
"""
mus1 = Musique("titre1","coucou",125,80,130,1,200)
mus2 = Musique("titre2","coucou2",110,78,130,12,300)
mus3 = Musique("titre3","coucou3",102,90,129,13,400)
mus4 = Musique("titre4","coucou4",105,28,85,24,200)
mus5 = Musique("titre5","coucou5",139,38,58,6,400)
mus6 = Musique("titre6","coucou5",194,48,45,3,405)
mus7 = Musique("titre7","coucou6",193,55,34,8,138)
tableaudobjets = [mus1,mus2,mus3,mus4,mus5]
"""
# Exemple : print tableaudobjets[1].titre

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


    return()
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

for nombre_generation in range(5000):
    # Evaluation de la qualité des solutions
    # Détermination de la somme des écarts bpm pour chaque solution
    def sommeecartBPM(matrice_solutionsBPM):
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
        return (tabl_BPMsoustrait)


    sommeecartBPM(matrice_solutionsBPM)


    # Détermination de la somme des écarts harmo pr chaque solution
    def sommeecartHARMO(matrice_solutionsHARMO):
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
                                result_soustrac2 += abs(
                                    matrice_pitchs.index(x - 12) - matrice_pitchs.index(x + y - 12 - 12))
                            else:
                                result_soustrac2 += abs(
                                    matrice_pitchs.index(y - 12) - matrice_pitchs.index(x + y - 12 - 12))
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
        return tabl_HARMOsoustrait


    # Création de nouveaux individus par mutation
    # Mutation arbitrairement choisie : inversion de deux musiques dans chaque ligne (ie) interversion de deux colonnes

    matrice_solutionsMutationBPM = np.copy(matrice_solutionsBPM)
    matrice_solutionsMutationHARMO = np.copy(matrice_solutionsHARMO)
    random1 = randint(0, len(tableaudobjets) - 1)
    random2 = randint(0, len(tableaudobjets) - 1)
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    j = 0

    while random2 == random1:  # on évite d'avoir deux fois le même nombre aléatoire
        random1 = randint(0, len(tableaudobjets) - 1)
        random2 = randint(0, len(tableaudobjets) - 1)

    for j in range(len(tableaudobjets)):  # on échange les colonnes et on obtient notre matrice mutée
        temp1 = matrice_solutionsBPM[j, random2]
        temp2 = matrice_solutionsBPM[j, random1]
        temp3 = matrice_solutionsHARMO[j, random2]
        temp4 = matrice_solutionsHARMO[j, random1]
        matrice_solutionsMutationBPM[j, random1] = temp1
        matrice_solutionsMutationBPM[j, random2] = temp2
        matrice_solutionsMutationHARMO[j, random1] = temp3
        matrice_solutionsMutationHARMO[j, random2] = temp4
        j += 1

    # Calcule des écarts sur les matrices mutées

    tabl_BPMsoustraitMUT = sommeecartBPM(matrice_solutionsMutationBPM)
    tabl_HARMOsoustraitMUT = sommeecartHARMO(matrice_solutionsMutationHARMO)

    # On choisit les 2 meilleurs solutions des solutions initiales et les deux meilleurs des solutions mutées


    # PONDERATION

    tabl_BPMsoustrait = sommeecartBPM(matrice_solutionsBPM)
    tabl_HARMOsoustrait = sommeecartHARMO(matrice_solutionsHARMO)


    def ponderation(tabl_BPMsoustrait, tabl_HARMOsoustrait):
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
        return tabl_BPMHARMOpondeesoustrait


    # Création  de la nouvelle solution

    tabl_BPMHARMOpondeesoustrait = ponderation(tabl_BPMsoustrait, tabl_HARMOsoustrait)
    i = 0
    j = 0
    k = 0
    matrice_nouvellesolutionBPM = np.zeros((nbre_solution, len(tableaudobjets)))
    matrice_nouvellessolutionHARMO = np.zeros((nbre_solution, len(tableaudobjets)))

    for k in range(nbre_solution // 2):
        for i in range(len(tabl_BPMHARMOpondeesoustrait)):
            if tabl_BPMHARMOpondeesoustrait[i] == min(tabl_BPMHARMOpondeesoustrait):
                for j in range(len(tabl_BPMHARMOpondeesoustrait)):
                    matrice_nouvellesolutionBPM[k, j] = matrice_solutionsBPM[i, j]
                    matrice_nouvellessolutionHARMO[k, j] = matrice_solutionsHARMO[i, j]
                    j += 1
                    tabl_BPMHARMOpondeesoustrait[i] = 999999
                j = 0
                i += 1
            else:
                i += 1
                j = 0
        k += 1

    k = 0
    j = 0
    i = 0
    half = nbre_solution // 2
    tabl_BPMHARMOpondeesoustraitMUT = ponderation(tabl_BPMsoustraitMUT, tabl_HARMOsoustraitMUT)

    if nbre_solution % 2 == 0:  # si le nbre_solution est pair on
        for k in [half, nbre_solution]:  # verif qu'on a bien Moitié moitié de solution
            for i in range(len(tabl_BPMHARMOpondeesoustraitMUT)):
                if tabl_BPMHARMOpondeesoustraitMUT[i] == min(tabl_BPMHARMOpondeesoustraitMUT):
                    for j in range(len(tabl_BPMHARMOpondeesoustrait)):
                        matrice_nouvellesolutionBPM[k, j] = matrice_solutionsMutationBPM[i, j]
                        matrice_nouvellessolutionHARMO[k, j] = matrice_solutionsMutationHARMO[i, j]
                        j += 1
                        tabl_BPMHARMOpondeesoustraitMUT[i] = 999999
                    i += 1
                    j = 0
                else:
                    i += 1
                    j = 0
            k += 1

    else:
        for k in [half, nbre_solution - 2]:  # verif qu'on a bien Moitié moitié de solution
            for i in range(len(tabl_BPMHARMOpondeesoustraitMUT)):
                if tabl_BPMHARMOpondeesoustraitMUT[i] == min(tabl_BPMHARMOpondeesoustraitMUT):
                    for j in range(len(tabl_BPMHARMOpondeesoustrait)):
                        matrice_nouvellesolutionBPM[k, j] = matrice_solutionsMutationBPM[i, j]
                        matrice_nouvellessolutionHARMO[k, j] = matrice_solutionsMutationHARMO[i, j]
                        j += 1
                        tabl_BPMHARMOpondeesoustraitMUT[i] = 999999
                    i += 1
                    j = 0
                else:
                    i += 1
                    j = 0
            k += 1
            # SI nombre de musiques impair, on remplit moitié/moitié par les vieilles solutions et les solutions mutées
            # et on rajoute une des solutions parmi les "vieilles solutions" au hasard (procédé arbitraire)
            j = 0
            random3 = randint(0, len(tableaudobjets) - 1)
            for j in range(len(tabl_BPMHARMOpondeesoustrait)):
                matrice_nouvellesolutionBPM[-1, j] = matrice_solutionsBPM[random3, j]
                matrice_nouvellessolutionHARMO[-1, j] = matrice_solutionsHARMO[random3, j]
                j += 1

    matrice_solutionsBPM = matrice_nouvellesolutionBPM
    matrice_solutionsHARMO = matrice_nouvellessolutionHARMO
    nombre_generation += 1

print
matrice_solutionsBPM
print
matrice_solutionsHARMO
tabl_BPMsoustrait = sommeecartBPM(matrice_solutionsBPM)
tabl_HARMOsoustrait = sommeecartHARMO(matrice_solutionsHARMO)
tabl_final = ponderation(tabl_BPMsoustrait, tabl_HARMOsoustrait)
solution_finaleBPM = []
solution_finaleHARMO = []  # Le mauvais jeu de mot n'est pas voulu ...
print
tabl_final
for i in range(len(tabl_final)):
    if tabl_final[i] == min(tabl_final):
        if solution_finaleBPM != []:
            break
        for j in range(len(tableaudobjets)):
            solution_finaleBPM.append(matrice_solutionsBPM[i, j])
            solution_finaleHARMO.append(matrice_solutionsHARMO[i, j])
            j += 1
    i += 1

print
solution_finaleBPM
print
solution_finaleHARMO
""" PROBLEME FINAL  A REGLER
# Reste à retourner la liste d'objet "tableaudobjets" qui sera triée !
# Il suffit de refaire la liaison entre les nombres des listes solution_finaleBPM,solution_finaleHARMO et
# le tableau d'objets initial.
tableaudobjets_final = []
i = 0
k = 0

while (len(solution_finaleBPM)) != 0:
    for i in range (len(tableaudobjets)):
        if (len(tableaudobjets_final)) == (len(tableaudobjets)):
            break
        if tableaudobjets[i].BPM_moy == solution_finaleBPM[k] and tableaudobjets[i].pitch == solution_finaleHARMO[k]:
            tableaudobjets_final.append(tableaudobjets[i])
            del solution_finaleBPM[k]
        i += 1

print tableaudobjets_final[2].BPM_moy
i = 0
for i in range (len(tableaudobjets_final)):
    print tableaudobjets_final[i].BPM_moy, tableaudobjets_final[i].pitch
    i += 1
"""
# ------------------------------------------------------------------------
# Transformation objet résultat en matrice résultat pour tintin
matrice_export = np.zeros(5, len(tableaudobjets))
for i in range(len(tableaudobjets_final)):
    matrice_export[i, 0] = tableaudobjets_final[i].emplacement
    matrice_export[i, 1] = tableaudobjets_final[i].titre
    matrice_export[i, 2] = tableaudobjets_final[i].duree
    matrice_export[i, 3] = tableaudobjets_final[i].BPM_moy
    matrice_export[i, 4] = tableaudobjets_final[i].pitch
    i += 1
print
matrice_export
