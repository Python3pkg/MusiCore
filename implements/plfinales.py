'''creation de fichier mp3 playlist
'''

from pydub import AudioSegment

def Playlist_mp3(resultat):
    '''
    fonction de creation du fichier mp3 contenant la playlist
    
    :param resultat: les objects musique une fois qu'ils sont tries
    :return: un fichier mp3 de toutes les chansons tries avec un crossfade entre chaques
    
    '''
    
    song = AudioSegment.from_mp3(resultat[0].emplacement)
    playlist = song
    
    for i in range (1,len(resultat)):
        song = AudioSegment.from_mp3(resultat[i].emplacement)
        playlist = playlist.append(song, crossfade=(10 * 1000))
        
        
    playlist = playlist.fade_out(10)
    out_f = open("entrezlenomici.mp3",'wb')#faire une jointure avec l'UI ici pour que l'utilisateur nomme sa playlist
    playlist.export(out_f, format='mp3')
