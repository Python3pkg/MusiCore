#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Ce module est un lecteur audio utilisant l'api de vlc pour python et en
l'adaptant aux effets audio précisée dans le cahier des charges
'''

import vlc.vlc

###############################################################################
# class `lecteur audio`
###############################################################################

import vlc

'''
p=vlc.MediaPlayer('file:///tmp/foo.avi')
p.play()'''


class lecteur_audio():
    def __init__(self):
        self.nomlecteur = 'lecteur_vlc'

    def lecture(self, path_to_file, nom_instance=None):
        if nom_instance is None:
            print("il manque le nom de l'instance")
        print('lecture: la musique est instanciée')
        nom_instance = vlc.MediaPlayer(path_to_file)
        nom_instance.play()

    def pause(self):

    def stop(self):

    def
