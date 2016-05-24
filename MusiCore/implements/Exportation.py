import os
from pydub import AudioSegment


def m3u(loc, mat):
    if loc != " ":
        pl = open(loc, "w")
        pl.write("#EXTM3U")
        resultat = mat
        for i in resultat:
            pl.write("\n")
            pl.write(i)
        pl.close()
        os.system("touch save")
        os.system("echo " + loc + ">save")


def mp3(loc, mat):
    if loc != " ":
        resultat = mat
        song = AudioSegment.from_mp3(resultat[0])
        playlist = song
        for i in range(1, len(resultat)):
            song = AudioSegment.from_mp3(resultat[i])
            playlist = playlist.append(song, crossfade=(10 * 1000))
        playlist = playlist.fade_out(10)
        out_f = open(loc, 'wb')
        playlist.export(out_f, format='mp3')
        os.system("touch save")
        os.system("echo " + loc + ">save")
