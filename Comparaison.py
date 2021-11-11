
from python_speech_features import mfcc
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import wave
import DTW
class comparaison:
    def __init__(self, audio1="null", audio2="null"):
        self.audio1= audio1
        self.audio2= audio2

    def Comparer2Mot(self):
        if self.audio1 == "null" or self.audio2 == "null":
            result = "Erreur dans l'insertion des audio essayer autre fois "
            return result
        else:
            (rate, sig) = wav.read(self.audio1)
            mfcc_feat = mfcc(sig, rate)
            (rate, sig) = wav.read(self.audio2)
            mfcc_feat1 = mfcc(sig, rate)
            x = np.array(mfcc_feat).reshape(-1, 1)
            y = np.array(mfcc_feat1).reshape(-1, 1)
            print(x)
            print(y)
            a = DTW.dtw(x, y)
            if a <= 6000:
                result = "les Deux audios sont identique , la distance entre les deux audio est  " + str(a)
                return result
            else:
                result = "les Deux audios ne sont pas identique , la distance entre les deux audio est : " + str(a)
                return result

