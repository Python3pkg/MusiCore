# -*- coding: utf-8 -*-
# fonction de test de l'analyse bpm

import implements.analyseaudio
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read, write
import numpy

Fs = 44100;  # sampling rate
rate, data = read('/home/gerox/Musique/Deorro.wav')
y = data[: 441000]
analyse1 = implements.analyseaudio.analyse("fichier_csv", 'bdd')
y = analyse1.extrairedatamusic()
Y = analyse1.analysefft(y, Fs)
print(Y)
