import numpy as np
from pylab import *
from scipy.io.wavfile import write

# tone synthesis
def note(freq, len, amp=1, rate=44100):
    t = np.linspace(0,len,len*rate)
    data = np.sin(2*np.pi*freq*t)*amp
    return data.astype(np.int16) # two byte integers


# A tone, 2 seconds, 44100 samples per second
a = note(440, 2, amp=10000)
b = note(494, 2, amp=10000)
g = note(784, 2, amp=10000)
write('a.wav', 44100, a) # writing the sound to a file
write('b.wav', 44100, b) # writing the sound to a file
write('g.wav', 44100, g) # writing the sound to a file
