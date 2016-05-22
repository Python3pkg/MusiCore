# -*- coding: utf-8 -*-
# fonction de test des fichiers csv
import implements.analyseaudio
import implements.parse_audio_2

# test 1
# ouverture d'un fichier csv

# On instancie l'objet csv
csv1 = implements.analyseaudio.csv_musicore('test')
print('test1: ok')

# test 2
# ajouter un éléments à un fichier csv
try:
    csv1.add_list(csv1.path_to_csv_file, ['nom', 'premon', 'date'])
except:
    print("l'élément n'a pas pu être rajouté")
print("test 2: ok")

# test 3
# On essaye de rajouter un élément qui n'est pas une list
try:
    csv1.add_list(csv1.path_to_csv_file, 'coucou')
except:
    print("l'objet n'est pas une liste")
print('test 3 ok')

# test 4
# test is_file
# cas correct
assert (csv1.is_file(csv1.path_to_database) == True)




# csv1.add_column(csv1.path_to_csv_file,['a','a','coucou','toto'])
# print(csv1.get_column_database(1))
# print(csv1.get_row_database(2))
# csv1.delete_row(1)
# csv1.delete_column(1)
# implements.parseaudio.parseaudio('bob', True, True)
