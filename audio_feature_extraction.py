import matplotlib.pyplot as plt
import numpy as np
import librosa, librosa.display
import sklearn

x, sr = librosa.load('output.wav')

def audiowaveform():
    global x,sr
    plt.style.use('ggplot')
    plt.figure(figsize=(14,5))
    librosa.display.waveplot(x, sr=sr)

def zcr(): 
    global x,sr
    zcrs = librosa.feature.zero_crossing_rate(x)
    plt.figure(figsize = (14,5))
    plt.title('Zero crossing rate')
    plt.plot(zcrs[0])

def spectrogram():
    global x,sr
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    plt.title('Spectrogram')
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
    
def spectralcentroid():
    global x,sr
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)
    def normalize(x, axis=0):
        return sklearn.preprocessing.minmax_scale(x, axis=axis)
    plt.figure(figsize=(14,5))
    plt.title('Spectral Centroid')
    librosa.display.waveplot(x, sr=sr, alpha=0.4)
    plt.plot(t, normalize(spectral_centroids), color='r')

def chromafrequencies():
    global x,sr
    hop_length = 512
    chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=hop_length)
    plt.figure(figsize=(14, 5))
    plt.title('Chroma frequencies')
    librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=hop_length, cmap='coolwarm')