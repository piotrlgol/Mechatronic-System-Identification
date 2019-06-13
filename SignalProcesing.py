import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pywt

class Function:
    def __init__(self, t, a, Fs):
        self.time = t
        self.amplitude = a
        self.Fs = Fs

class Data3d:
    def __init__(self, x, y, z, lx, ly, lz):
        self.x = x
        self.y = y
        self.z = z
        self.label_x = lx
        self.label_y = ly
        self.label_z = lz
    
    def get_data(self):
        return self.x, self. y, self. z

    def get_labels(self):
        return self.label_x, self.label_y, self.label_z

    
class Math: 
    @staticmethod   
    def time_domain(sig):
       return sig.time, sig.amplitude

    @staticmethod
    def frequency_domain(sig, cut_0 = False):
        if cut_0:
            signal_frequencies = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(len(signal_frequencies), 1/sig.Fs)
            if len(frequency)%2 != 0:
                fq_len = len(frequency)+1
            else:
                fq_len = len(frequency)
            signal_frequencies = signal_frequencies[:int(-fq_len/2)]
            frequency = frequency[:int(len(frequency)/2)]
        else:
            signal_frequencies = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(len(signal_frequencies), 1/sig.Fs)
        return frequency, abs(signal_frequencies)

    @staticmethod
    def stft(sig, win, persek, overlap, _nfft):
        f, t, Zxx = signal.stft(sig.amplitude, sig.Fs, window=win, nperseg=persek, noverlap=overlap, nfft=_nfft)
        return t, f, np.abs(Zxx)
        

    @staticmethod
    def cwt(sig, scMin, scMax, wavelet):
        coef, freqs = pywt.cwt(sig.amplitude, np.arange(scMin,scMax), wavelet, sampling_period=sig.Fs)
        return sig.time, np.arange(scMin,scMax), coef.real


