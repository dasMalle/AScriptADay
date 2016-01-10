import wave
import struct
import math

SAMPLE_LEN = 15000
noise_output = wave.open('noise.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))


for i in range(0, SAMPLE_LEN):
        value = int(math.sin(i)*400)
        packed_value = struct.pack('h', value)
        noise_output.writeframes(packed_value)
        noise_output.writeframes(packed_value)

noise_output.close()
