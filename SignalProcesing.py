import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class Function():
    def __init__(self, t, a, Fs):
        self.time = t
        self.amplitude = a
        self.Fs = Fs

    
class Math(): 
    @staticmethod   
    def time_domain(sig):
       plt.plot(sig.time, sig.amplitude) 
       plt.show()

    @staticmethod
    def frequency_domain(sig, cut_0 = False):
        if cut_0:
            signal_frequency = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(sig.time.size, 1/sig.Fs)
            signal_frequency = signal_frequency[:int(-len(frequency)/2)]
            frequency = frequency[:int(len(frequency)/2)]
        else:
            signal_frequency = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(sig.time.size, 1/sig.Fs)
        plt.plot(frequency, abs(signal_frequency))
        plt.show()

    @staticmethod
    def stft(sig):
        f, t, Zxx = signal.stft(sig.amplitude, sig.Fs, nperseg=50)
        plt.pcolormesh(t, f, np.abs(Zxx), vmin=0)
        plt.show()

    # @staticmethod
    # def cwt(sig):
    #     plt.show()
if __name__ == "__main__":
    fs =400
    t = np.linspace(0,2*np.pi,fs)
    a = np.sin(t*50)
    f1 = Function(t,a,fs)
    Math.stft(f1)

