import numpy as np
from scipy.io.wavfile import write
from noteconv import *

# tone synthesis
def note(freq, len, amp=1, rate=44100):
    t = np.linspace(0,len,len*rate)
    data = np.sin(2*np.pi*freq*t)*amp
    return data.astype(np.int16) # two byte integers

# combine notes for a chord
# I think amplitude caps at intMax... so put it at 32k / len(chord)
def doChord( chord, filename ):
    output = 0
    for i in range(0,len(chord)):
        output += note(getFreq(chord[i]), 2, amp=(32000/len(chord)))
    write( filename + '.wav', 44100, output )

doChord( [ "c3", "e3", "g3", "bb4", "c4" ], 'chord' )
