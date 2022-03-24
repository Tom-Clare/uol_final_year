from pyo import *
from Sequencer import Sequencer
from SoundSequencer import SoundSequencer
from notes import notes

plus_tot = [notes["D4"], notes["Fs4"], notes["A4"], notes["D4"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"]]

s = Server().boot()
bpm = 60/220
seq = Sequencer(bpm, plus_tot).out()
s.gui(locals())

#####################################

# s = Server().boot()
# clock = Sine(freq=0.01)
# bpm = 60/120
# seq = SoundSequencer(bpm, "sounds/kick.wav", [1,1,1,1]).out()
# snares = SoundSequencer(bpm, "sounds/snare.wav", [0,1,0,1]).out()
# s.gui(locals())

######################################

# from notes import notes

# s = Server().boot()
# clock = Sine(freq=0.01)
# bpm = 60/120
# seq = SoundSequencer(bpm, "sounds/kick.wav", [1,1,1,1]).out()
# snares = SoundSequencer(bpm, "sounds/snare.wav", [0,1,0,1]).out()
# #sound = Sine(freq=seq.out()).out()
# s.gui(locals())

######################################


# basic = [notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["G4"],notes["G4"]]

# s = Server().boot()
# bpm = 60/120
# seq = Sequencer(bpm, basic).out()
# seq = SoundSequencer(bpm, "sounds/kick.wav", [1,1,1,1]).out()
# snares = SoundSequencer(bpm, "sounds/snare.wav", [0,1,0,1]).out()
# s.gui(locals())