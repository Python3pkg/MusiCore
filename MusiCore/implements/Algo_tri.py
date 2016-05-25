# coding: utf-8
#test orienté_objet
#classe Musique déf par titre, BPM_debut, BPM_fin, pitch

#------------------------------
#import des librairies nécessaires

import csv
from random import randint
import numpy as np

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
    duree = ""
    """
    def __init__(self, titre, emplacement, BPM_moy, BPM_debut, BPM_fin, pitch, duree):#methode constructeur
       self.titre = titre #il faut extraire les données du csv
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

#-------------------------
#Importation de la matrice avec les infos et conversion en objet

#matrice_import = ??? à recevoir de tintin
# définir la variable "tableaudobjets"

#-----------------------------------------
#Implémentation d'un algorithme génétique pour aboutir au tri final
"""
mus1 = Musique("titre1","coucou",125,80,130,1,200)
mus2 = Musique("titre2","coucou2",110,78,130,12,300)
mus3 = Musique("titre3","coucou3",102,90,129,13,400)
mus4 = Musique("titre4","coucou4",105,28,85,24,200)
mus5 = Musique("titre5","coucou5",139,38,58,6,400)
mus6 = Musique("titre6","coucou5",194,48,45,3,405)
mus7 = Musique("titre7","coucou6",193,55,34,8,138)
#tableaudobjets = [mus1,mus2,mus3,mus4,mus5]"""

exemple = [['titre1', 'durée1', 123, 12], ['titre2', 'durée2', 80, 20],
           ['titre3', 'durée3', 140, 18], ['titre4', 'durée4', 130, 19],
           ['titre5','durée5',169,6],['titre6','duree6',184,5],
           ['titre7','duree7',100,14]]
# Exemple : print tableaudobets[1].titre
def determination_nbre_sol(tableaudobjets):
    if len(tableaudobjets)<=100:
        nbre_solution = len(tableaudobjets)
    else:
        nbre_solution = 100
    return(nbre_solution)

def creationtabl_BPM(tableaudobjets):
    i=0
    tabl_BPM = []
    for i in range (len(tableaudobjets)):
        tabl_BPM.append(tableaudobjets[i].BPM_moy)
        i += 1
    return(tabl_BPM)


def creationtabl_HARMO(tableaudobjets):
    i=0
    tabl_HARMO = []
    for i in range (len(tableaudobjets)):
        tabl_HARMO.append(tableaudobjets[i].pitch)
        i +=1
    return(tabl_HARMO)

def sommeecartBPM(tableaudobjets,matrice_solutionsBPM):
        nbre_solution = determination_nbre_sol(tableaudobjets)
        A = creationtabl_HARMO(tableaudobjets)
        B = creationtabl_BPM(tableaudobjets)
        tabl_BPMsoustrait = []  #contient l'écart entre chaque musique pr chaque solution
        result_soustrac = 0
        j=0
        i=0
        for i in range (nbre_solution):
            for j in range (1):
                 while j+1 <= (len(A)-1) :
                    result_soustrac += abs(matrice_solutionsBPM[i,j] - matrice_solutionsBPM[i,j+1])
                    j += 1
                 tabl_BPMsoustrait.append(result_soustrac)
                 result_soustrac = 0
            i = i+1
        return(tabl_BPMsoustrait)

def sommeecartHARMO(tableaudobjets, matrice_solutionsHARMO):
            tabl_HARMOsoustrait = [] #contient l'écart harmo entre chaque musique pr chaque solution
            result_soustrac2 = 0
            matrice_pitchs = range(25)
            nbre_solution = determination_nbre_sol(tableaudobjets)
            A = creationtabl_HARMO(tableaudobjets)
            B = creationtabl_BPM(tableaudobjets)
            x = 0
            y = 0
            i = 0
            j = 0
            for i in range (nbre_solution):
                for j in range (1):
                    while j+1 <= (len(B)-1) :
                        x = matrice_solutionsHARMO[i,j]
                        y = matrice_solutionsHARMO[i,j+1]
                        if x <= 12 and y <=12 : #cas des harmos majeures
                            if abs(matrice_solutionsHARMO[i,j] - matrice_solutionsHARMO[i,j+1]) <= 7:
                                result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y))
                            else:
                                if x > y :
                                    result_soustrac2 += abs(matrice_pitchs.index(x)-matrice_pitchs.index(x+y))
                                else :
                                    result_soustrac2 += abs(matrice_pitchs.index(y)-matrice_pitchs.index(x+y))
                            j += 1
                        elif x > 12 and y > 12: #cas des harmos mineures
                            if abs(matrice_solutionsHARMO[i,j] - matrice_solutionsHARMO[i,j+1]) <= 7:
                                result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y))
                            else:
                                if x > y :
                                    result_soustrac2 += abs(matrice_pitchs.index(x-12)-matrice_pitchs.index(x+y-12-12))
                                else :
                                    result_soustrac2 += abs(matrice_pitchs.index(y-12)-matrice_pitchs.index(x+y-12-12))
                            j += 1
                        else: #cas où on a une différence mineur/majeur
                            if x > 12 :
                                x = x-12
                            else:
                                y = y-12
                            if abs(x-y) <= 7:
                                result_soustrac2 += abs(matrice_pitchs.index(x) - matrice_pitchs.index(y))+1
                            else:
                                if x > y:
                                    result_soustrac2 += abs(matrice_pitchs.index(x)-matrice_pitchs.index(x+y))+1
                                else:
                                    result_soustrac2 += abs(matrice_pitchs.index(y)-matrice_pitchs.index(x+y))+1
                            j += 1
                    tabl_HARMOsoustrait.append(result_soustrac2)
                    result_soustrac2 = 0
                i = i+1
            return tabl_HARMOsoustrait

def ponderation(tabl_BPMsoustrait,tabl_HARMOsoustrait):
            a = 0 #Coefficient de pondération si il vaut 0 alors on tient pas compte des écarts harmos
            b = 1 #si b vaut 0 et a = 1 alors on tient seulement compte du tri harmo
            i = 0
            valeur_ponderee = 0
            tabl_BPMHARMOpondeesoustrait = []
            a = 10 #cas où il y a la meme importance entre harmos et bpms
            for i in range (len(tabl_BPMsoustrait)):
                valeur_ponderee = b*tabl_BPMsoustrait[i] + a*tabl_HARMOsoustrait[i]  #REGLER COEFF A POUR PONDERATION
                tabl_BPMHARMOpondeesoustrait.append(valeur_ponderee)
            m = min(tabl_BPMHARMOpondeesoustrait)
            return tabl_BPMHARMOpondeesoustrait


def algorithme_genetique(playlist):
    # création de la population initiale de solutions
    # la solution doit passer par tous les points ET ne pas comporter de doublons

    #Détermination du nombre de solutions

    # arrangement de matrice playlist
    mat = []
    for row in playlist:
        mat.append(row[3])

    tableaudobjets = []
    for i in range(len(mat)):
        nummusic = str(i)
        music = "music" + nummusic
        music = Musique(playlist[i][0], playlist[i][-1], playlist[i][2], None, None, playlist[i][3], playlist[i][1])
        tableaudobjets.append(music)
        # mus1 = Musique("titre1","coucou",125,80,130,1,200)

    print(tableaudobjets[1].titre)
    print(tableaudobjets[1].emplacement)
    print(tableaudobjets[1].BPM_moy)
    print(tableaudobjets[1].pitch)


    nbre_solution = determination_nbre_sol(tableaudobjets)
        #Création de la matrice bpm avec 4 solutions initiales
    matrice_solutionsBPM = np.zeros((nbre_solution,len(tableaudobjets)))
    matrice_solutionsHARMO = np.zeros((nbre_solution,len(tableaudobjets)))

    A = creationtabl_BPM(tableaudobjets)
    B = creationtabl_HARMO(tableaudobjets)
    j=0
    i=0
    k=0
    l = 0
    valeur_random = 0
    tabl_valeurrandom = []
    for j in range (nbre_solution):
        #pour chaque ligne on ajoute toutes les musiques -> solution
        #il faut prendre un chiffre de tabl_bpm, le recopier et supprimer le bpm traité pr pas doublon)
        for i in range (len(tableaudobjets)):
            valeur_random = randint(0,len(A)-1)
            matrice_solutionsBPM[j,i] = A[valeur_random]
            matrice_solutionsHARMO[j,i] = B[valeur_random]
            del A[valeur_random]
            del B[valeur_random]
            i += 1
        A = creationtabl_BPM(tableaudobjets)
        B = creationtabl_HARMO(tableaudobjets)
        j += 1

    A = creationtabl_HARMO(tableaudobjets)
    B = creationtabl_BPM(tableaudobjets)


    for nombre_generation in range (500):
        #Evaluation de la qualité des solutions
        #Détermination de la somme des écarts bpm pour chaque solution


        sommeecartBPM(tableaudobjets, matrice_solutionsBPM)


        #Détermination de la somme des écarts harmo pr chaque solution


        # Création de nouveaux individus par mutation
        # Mutation arbitrairement choisie : inversion de deux musiques dans chaque ligne (ie) interversion de deux colonnes

        matrice_solutionsMutationBPM = np.copy(matrice_solutionsBPM)
        matrice_solutionsMutationHARMO = np.copy(matrice_solutionsHARMO)
        random1 = randint(0,len(tableaudobjets)-1)
        random2 = randint(0,len(tableaudobjets)-1)
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        j = 0

        while random2 == random1 :  #on évite d'avoir deux fois le même nombre aléatoire
            random1 = randint(0,len(tableaudobjets)-1)
            random2 = randint(0,len(tableaudobjets)-1)

        for j in range (len(tableaudobjets)):  #on échange les colonnes et on obtient notre matrice mutée
            temp1 = matrice_solutionsBPM[j,random2]
            temp2 = matrice_solutionsBPM[j,random1]
            temp3 = matrice_solutionsHARMO[j,random2]
            temp4 = matrice_solutionsHARMO[j,random1]
            matrice_solutionsMutationBPM[j,random1] = temp1
            matrice_solutionsMutationBPM[j,random2] = temp2
            matrice_solutionsMutationHARMO[j,random1] = temp3
            matrice_solutionsMutationHARMO[j,random2] = temp4
            j +=1


        #Calcule des écarts sur les matrices mutées

        tabl_BPMsoustraitMUT = sommeecartBPM(tableaudobjets, matrice_solutionsMutationBPM)
        tabl_HARMOsoustraitMUT = sommeecartHARMO(tableaudobjets, matrice_solutionsMutationHARMO)

        #On choisit les 2 meilleurs solutions des solutions initiales et les deux meilleurs des solutions mutées


        #PONDERATION

        tabl_BPMsoustrait = sommeecartBPM(tableaudobjets, matrice_solutionsBPM)
        tabl_HARMOsoustrait = sommeecartHARMO(tableaudobjets, matrice_solutionsHARMO)

        #Création  de la nouvelle solution

        tabl_BPMHARMOpondeesoustrait = ponderation(tabl_BPMsoustrait,tabl_HARMOsoustrait)
        i = 0
        j = 0
        k = 0
        matrice_nouvellesolutionBPM = np.zeros((nbre_solution,len(tableaudobjets)))
        matrice_nouvellessolutionHARMO = np.zeros((nbre_solution,len(tableaudobjets)))

        for k in range (0,nbre_solution//2):
            for i in range (len(tabl_BPMHARMOpondeesoustrait)):
                # if matrice_nouvellesolutionBPM[nbre_solution//2,3] != 0:
                # break
                if tabl_BPMHARMOpondeesoustrait[i] == min(tabl_BPMHARMOpondeesoustrait):
                    for j in range (len(tabl_BPMHARMOpondeesoustrait)):
                        matrice_nouvellesolutionBPM[k,j] = matrice_solutionsBPM[i,j]
                        matrice_nouvellessolutionHARMO[k,j] = matrice_solutionsHARMO[i,j]
                        j += 1
                        tabl_BPMHARMOpondeesoustrait[i] = 999999
                    j = 0
                else:
                    i += 1
                    j = 0
        k=0

        print(matrice_nouvellesolutionBPM)
        print("coucou1")
        #fonctionnel - pbm sur la suite
        k = 0
        j = 0
        i = 0
        half = nbre_solution//2
        tabl_BPMHARMOpondeesoustraitMUT = ponderation(tabl_BPMsoustraitMUT,tabl_HARMOsoustraitMUT)
        if nbre_solution%2 == 0 :  #si le nbre_solution est pair on fait moitié moitié
            for k in range (half, nbre_solution): #verif qu'on a bien Moitié moitié de solution
                for i in range (len(tabl_BPMHARMOpondeesoustraitMUT)):
                    if tabl_BPMHARMOpondeesoustraitMUT[i] == min(tabl_BPMHARMOpondeesoustraitMUT):
                        if min(tabl_BPMHARMOpondeesoustraitMUT) != 999999:
                            for j in range (len(tabl_BPMHARMOpondeesoustrait)):
                                matrice_nouvellesolutionBPM[k,j] = matrice_solutionsMutationBPM[i,j]
                                matrice_nouvellessolutionHARMO[k,j] = matrice_solutionsMutationHARMO[i,j]
                                j += 1
                                tabl_BPMHARMOpondeesoustraitMUT[i] = 999999
                            j = 0
                    else:
                        i += 1
                        j = 0
                k+= 1

        else:
            for k in range (half, nbre_solution):
                for i in range (len(tabl_BPMHARMOpondeesoustraitMUT)):
                    if tabl_BPMHARMOpondeesoustraitMUT[i] == min(tabl_BPMHARMOpondeesoustraitMUT):
                        for j in range (len(tabl_BPMHARMOpondeesoustrait)):
                            matrice_nouvellesolutionBPM[k ,j] = matrice_solutionsMutationBPM[i,j]
                            matrice_nouvellessolutionHARMO[k ,j] = matrice_solutionsMutationHARMO[i,j]
                            j += 1
                            tabl_BPMHARMOpondeesoustraitMUT[i] = 999999
                        j = 0
                        #print(matrice_nouvellesolutionBPM)
                    else:
                        i += 1
                        j = 0
                k+= 1
                 #SI nombre de musiques impair, on remplit moitié/moitié par les vieilles solutions et les solutions mutées
                 # et on rajoute une des solutions parmi les "vieilles solutions" au hasard (procédé arbitraire)
                j=0
                random3 = randint(0,len(tableaudobjets)-1)
                for j in range (len(tabl_BPMHARMOpondeesoustrait)):
                    matrice_nouvellesolutionBPM[-1,j] = matrice_solutionsBPM[random3,j]
                    matrice_nouvellessolutionHARMO[-1,j] = matrice_solutionsHARMO[random3,j]
                    j += 1
        print("coucou")
        print(matrice_nouvellesolutionBPM)


        matrice_solutionsBPM = matrice_nouvellesolutionBPM
        matrice_solutionsHARMO = matrice_nouvellessolutionHARMO
        nombre_generation += 1

   # print matrice_solutionsBPM
    #print matrice_solutionsHARMO
    tabl_BPMsoustrait = sommeecartBPM(tableaudobjets, matrice_solutionsBPM)
    tabl_HARMOsoustrait = sommeecartHARMO(tableaudobjets, matrice_solutionsHARMO)
    tabl_final = ponderation(tabl_BPMsoustrait, tabl_HARMOsoustrait)
    solution_finaleBPM = []
    solution_finaleHARMO = []  #Le mauvais jeu de mot n'est pas voulu ...
    for i in range (len(tabl_final)):
        if tabl_final[i] == min(tabl_final):
            if solution_finaleBPM != []:
                break
            for j in range (len(tableaudobjets)):
                solution_finaleBPM.append(matrice_solutionsBPM[i,j])
                solution_finaleHARMO.append(matrice_solutionsHARMO[i,j])
                j += 1
        i +=1

    # Solution finale
    print(solution_finaleBPM)
    print(solution_finaleHARMO)

    # on implemente les solutions dans la matrices playlist afin de l'exporter pour l'UI
    # partie qui ne fonctionne pas
    playlist_2 = []
    i = 0
    j = 0
    nb_ligne = len(solution_finaleBPM)
    while i < nb_ligne:
        while j < nb_ligne:
            # print(float(playlist[j][2]))
            # print(solution_finaleBPM[i])
            print(" i = %s" % i)
            print(" j = %d" % j)
            print('bpm solution: %s' % solution_finaleBPM[i])
            print('bpm solution: %s' % float(playlist[j][2]))
            print('bpm solution: %s' % solution_finaleHARMO[i])
            print('bpm solution: %s' % float(playlist[j][3]))
            if solution_finaleBPM[i] == float(playlist[j][2]) and solution_finaleHARMO[i] == float(playlist[j][3]):
                print('ca marche')
                list_output = []
                for w in range(5):
                    list_output.append(playlist[j][w])
                playlist_2.append(list_output)
            j += 1
        i += 1
        j = 0

    print(playlist_2)
    '''
            if solution_finaleBPM[i] == float(playlist[j][2]) and solution_finaleHARMO[i] == float(playlist[j][3]):
                print('ca marche')
                for w in range(5):
                    playlist_2[i][w] = playlist[j][w]
                solution_finaleBPM[i] = 9999
                # playlist_2[i] = playlist[j]'''

    # test
    print(playlist_2[0][0])
    print(playlist_2[1][0])
    print(playlist_2[2][0])

    return playlist_2

    ''' PROBLEME FINAL  A REGLER

     mat = []
    for row in playlist:
        mat.append(row[3])
    k=0
    for i in range(len(solution_finaleBPM)):
        for j in range(len(mat)):
            if solution_finaleBPM[i] == mat[j]:
                for w in range(5):
                    playlist[k][w], playlist[j,w] = playlist[j][w], playlist[k][w]
                    k += 1


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
    """
    #------------------------------------------------------------------------
    #Transformation objet résultat en matrice résultat pour tintin
    matrice_export = np.zeros(5,len(tableaudobjets))
    for i in range (len(tableaudobjets_final)):
        matrice_export[i,0]= tableaudobjets_final[i].emplacement
        matrice_export[i,1]= tableaudobjets_final[i].titre
        matrice_export[i,2]= tableaudobjets_final[i].duree
        matrice_export[i,3]= tableaudobjets_final[i].BPM_moy
        matrice_export[i,4]= tableaudobjets_final[i].pitch
        i +=1
    print matrice_export
    return matrice_export'''
