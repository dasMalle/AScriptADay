__author__ = 'aoostdijk'

# function for calculating frequency offset
# fn = f0 * (x)n
# x = pow( 2, ( 1.0 / 12.0 ) )
global x
x = pow( 2, ( 1.0 / 12.0 ) )
# f0 = A4 = 440 Hz

def getFreq( note ):
    return freqForSteps( calcHalfSteps( note ) )

# freq relative to A4 from given half step distance
def freqForSteps( halfStepsFromA4 ):
    return 440 * pow( x, halfStepsFromA4 )

# calculates half steps from A4 for a given note
def calcHalfSteps( note ):
    # valid notes are things like C1, A4, G#5, Gb5
    # so they are either 2 or 3 chars
    if len(note) < 2 or len(note) > 3: return 0

    base = note.lower()[0]
    offset = 0
    octaveSteps = 0
    if len(note) == 3:
        if note[1] == '#':
            offset = 1
        elif note[1] == 'b':
            offset = -1
        octaveSteps = ( int(note[2]) - 4 ) * 12
    else:
        octaveSteps = ( int(note[1]) - 4 ) * 12

    return distanceFromA(base) + offset + octaveSteps

# maybe there's some way to calculate this, but this is pretty simple...
def distanceFromA( note ):
    if note == 'a': return 0
    elif note == 'b': return 2
    elif note == 'c': return 3
    elif note == 'd': return 5
    elif note == 'e': return 7
    elif note == 'f': return 8
    elif note == 'g': return 10
    else: return 0
