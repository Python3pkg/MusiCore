import scipy, pylab
import os
import librosa

def extraire_path(path):
    """
    :param path: chemin absolue d'une fichier audio
    :return: list =[nom fichier, chemin du repertoire du dossier contenant le fichier audio]
    Comment: permet d'extraire d'un chemin absolu le nom du fichier une list:

    """
    path1=path[::-1]
    k=0
    while path[len(path)-k-1]!="/":
        k=k+1
    return [path[len(path)-k:], path[:len(path)-k-1] ]

def stft(x, fs, framesz, hop):
    framesamp = int(framesz*fs)
    hopsamp = int(hop*fs)
    w = scipy.hanning(framesamp)
    X = scipy.array([scipy.fft(w*x[i:i+framesamp])
                     for i in range(0, len(x)-framesamp, hopsamp)])
    return X

def istft(X, fs, T, hop):
    x = scipy.zeros(T*fs)
    framesamp = X.shape[1]
    hopsamp = int(hop*fs)
    for n,i in enumerate(range(0, len(x)-framesamp, hopsamp)):
        x[i:i+framesamp] += scipy.real(scipy.ifft(X[n]))
    return x

if __name__ == '__main__':
    #f0 = 440         # Compute the STFT of a 440 Hz sinusoid
    fs = 1000       # sampled at 8 kHz
    T = 2            # lasting 5 seconds
    framesz = 0.050  # with a frame size of 50 milliseconds
    hop = 0.025      # and hop size of 25 milliseconds.

    # Create test signal and STFT.
    t = scipy.linspace(0, T, T*fs, endpoint=False)
    os.chdir("/home/bettini/Musique/")
    filename = "Deorro.wav"
    y, sr = librosa.load(filename)
    #x = scipy.sin(2*scipy.pi*f0*t)
    X = stft(y, fs, framesz, hop)

    # Plot the magnitude spectrogram.
    pylab.figure()
    pylab.imshow(scipy.absolute(X.T), origin='lower', aspect='auto',
                 interpolation='nearest')
    pylab.xlabel('Time')
    pylab.ylabel('Frequency')
    pylab.show()

    # Compute the ISTFT.
    xhat = istft(X, fs, T, hop)

    # Plot the input and output signals over 0.1 seconds.
    T1 = int(0.1*fs)

    pylab.figure()
    pylab.plot(t[:T1], y[:T1], y[:T1], xhat[:T1])
    pylab.xlabel('Time (seconds)')

    pylab.figure()
    pylab.plot(t[-T1:], y[-T1:], t[-T1:], xhat[-T1:])
    pylab.xlabel('Time (seconds)')