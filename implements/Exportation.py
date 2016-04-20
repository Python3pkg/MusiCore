'''creation de playlist
'''

def CreationPlaylist(resultat):
    '''
    fonction de creation de playlist

    :param resultat: blabla
    :return: blabla

    '''

    pl = open("pl.m3u","w")
    pl.write("#EXTM3U")
    for i in range(len(resultat)):
        j=resultat[i]
        pl.write("\nEXTINF:")
        pl.write(str(i))
        pl.write(", ")
        pl.write(j.titre)
        pl.write("\n")
        pl.write(j.emplacement)
    pl.close()