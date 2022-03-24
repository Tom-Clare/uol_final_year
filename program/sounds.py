from pyo import *
from SoundSequencer import SoundSequencer
from notes import notes

# s = Server().boot()
# bpm = 60/120
# kicks = SoundSequencer(bpm, "sounds/kick.wav", [1,1,1,1])
# snares = SoundSequencer(bpm, "sounds/snare.wav", [0,1,0,1])
# kicks.out()
# snares.out()
# #sound = Sine(freq=seq.out()).out()
# s.gui(locals())



from notes import notes

s = Server().boot()
clock = Sine(freq=0.01)
bpm = 60/120
seq = SoundSequencer(bpm, "sounds/kick.wav", [1,1,1,1]).out()
snares = SoundSequencer(bpm, "sounds/snare.wav", [0,1,0,1]).out()
#sound = Sine(freq=seq.out()).out()
s.gui(locals())