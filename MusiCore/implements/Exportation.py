import os
from pydub import AudioSegment


def m3u(loc, mat):
    '''
    permet d'exporter la playlist sous le format m3u
    
    :param loc: location du dossier destination, choisi par l'utilisateur, du fichier m3u
    :param mat: liste contenant les emplacements des différentes chansons ordonnées
    :return: None
    '''
    
    if loc != " ":
        pl = open(loc, "w")#on créé le document .m3u
        pl.write("#EXTM3U")
        resultat = mat
        for i in resultat:#écriture du document
            pl.write("\n")
            pl.write(i)
        pl.close()
        os.system("touch save")#on enregistre le document
        os.system("echo " + loc + ">save")


def mp3(loc, mat):
     '''
    permet d'exporter la playlist sous le format mp3
    
    :param loc: location du dossier destination, choisi par l'utilisateur, du fichier mp3
    :param mat: liste contenant les emplacements des différentes chansons ordonnées
    :return: None
    '''
    
    if loc != " ":
        resultat = mat
        song = AudioSegment.from_mp3(resultat[0])#on crée la playlist
        playlist = song
        for i in range(1, len(resultat)):
            song = AudioSegment.from_mp3(resultat[i])
            playlist = playlist.append(song, crossfade=(10 * 1000))#on rajoute la chanson suivant en faisant un crossfade avec la précédente
        playlist = playlist.fade_out(10)#on fini le m3p par un fade out
        out_f = open(loc, 'wb')
        playlist.export(out_f, format='mp3')#on exporte la playlist au dossier destination spécifié par l'utilisateur
        os.system("touch save")
        os.system("echo " + loc + ">save")
