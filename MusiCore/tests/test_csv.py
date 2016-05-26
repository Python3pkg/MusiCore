# -*- coding: utf-8 -*-
# # author: Aurélien BETTINI
# fonction de test des fichiers csv
import implements.Analyse
import implements.Parser

# test 1
# ouverture d'un fichier csv

# On instancie l'objet csv
csv1 = implements.Analyse.csv_musicore('test')
print('test1: ok')

# test 2
# ajouter un éléments à un fichier csv
try:
    csv1.add_list(csv1.path_to_csv_file, ['nom', 'premon', 'date'])
except:
    print("l'élément n'a pas pu être rajouté")
print("test 2 (objet is a list) : ok")
csv1.delete_row(3)

# test 3
# On essaye de rajouter un élément qui n'est pas une list
try:
    csv1.add_list(csv1.path_to_csv_file, 'coucou')
except:
    print("l'objet n'est pas une liste")
print('test 3 (objet is not the right object):ok')

# test 4
# test is_file
# cas correct
assert (csv1.is_file(csv1.path_to_database) == True), 'test 4 (is_file true) : problem'
print('test 4 (is_file true): ok')

# test 5
# test is_file dans le cas ou le fichier n'existe pas
assert (csv1.is_file('/home/gerox/fichierbidou') == False), 'test 5 (is_file): problem'
print('test 5 (is_file false): ok')

# test 6
# test find_title_in_database right test

assert (csv1.find_title_in_database("The Chainsmokers - Don't Let Me Down (Audio) ft. Daya.mp3")[
            0] == True), 'test 6 (find_title_in_database right test): problem'
print("test 6 (find_title_in_database right test) : ok")

# test 7
# test find_title_in_database wrong test
assert (csv1.find_title_in_database("The Chainsmokers - Don't Let Me Down (Audio) ft. Daya.mp3")[
            0] == True), 'test 6 (find_title_in_database wrong case): problem'
print("test 7 (find_title_in_database wrong test) : ok")

# test 8
# test find_title_in_database wrong object
try:
    csv1.find_title_in_database(Chainsmokers)
except:
    print("test 8 (test find_title_in_database wrong object): ok")

# test9
# test add_column (attention la liste doit avoir le meme nombre de colonne que la liste à ajouter)
try:
    csv1.add_column(csv1.path_to_csv_file, ['a', 'a', 'a'])
except:
    print("test 9 (test add_column): problem")
print('test 9 (test add_column): ok ')
csv1.delete_column(3)

# test 10
# test add_column wrong object(attention la liste doit avoir le meme nombre de colonne que la liste à ajouter)
try:
    csv1.add_column(csv1.path_to_csv_file, 'a')
except:
    print("test 10 (test add_column): ok")

# test 11
# test add_column (specific col)
try:
    csv1.add_column(csv1.path_to_csv_file, ['a', 'a', 'a'], 1)
except:
    print("test 11 (test add_column): problem")
csv1.delete_column(3)
print('test 11 (test add_column (specific col)): ok')

# test 12
# test get_column
csv1.get_column(2)
print('test 12 (get_column): ok')

# test 13
# test get_column (wrong int)
try:
    csv1.get_column('coucou')
except:
    print("test 13 (test add_column): ok")

# test 14
# test get_row
csv1.get_row(2)
print('test 14 (get_column): ok')

# test 15
# test get_row (wrong object)
try:
    csv1.get_row('coucou')
except:
    print("test 15 (test add_column): ok")

# test 16
# test get_column_database
csv1.get_row_database(1)
print('test 16 (get_column_database): ok')

# test 17
# test get_column (wrong int)
try:
    csv1.get_column('coucou')
except:
    print("test 17 (test add_column_database): ok")

# test 18
# test get_column_database
csv1.get_row_database(1)
print('test 18 (get_column_database): ok')

# test 19
# test get_column (wrong int)
try:
    csv1.get_row_database('coucou')
except:
    print("test 19 (test add_column_database): ok")

# test 20
# delete_row
csv1.delete_row(2)
print('test 20 (delete row): ok')
csv1.add_list(csv1.path_to_csv_file, ['a', 'a', 'a'])

# test 21
# delete_row (wrong object)
try:
    csv1.delete_row('test')
except:
    print("test 21 (delete_row): ok")

# test 22
# delete_column
csv1.delete_column(2)
print('test 20 (delete column): ok')
csv1.add_column(csv1.path_to_csv_file, ['a', 'a', 'a'])

# test 23
# delete_column (wrong object)
try:
    csv1.delete_column('test')
except:
    print("test 23 (delete_colum): ok")

# test 24
# nombre_ligne_csv
if isinstance(csv1.nombre_ligne_csv(), int) == False:
    raise ValueError('test 24: problem')
else:
    print('test 24: ok')

# test 25
# safe_state: supprime les lignes blanches
# csv1.safe_state()
