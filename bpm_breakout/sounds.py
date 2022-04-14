from pyo import *
from Sequencer_ext import Sequencer
from SoundSequencer_ext import SoundSequencer
from BPM import BPM
from notes import notes

# plus_tot = [notes["D4"], notes["Fs4"], notes["A4"], notes["D4"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"]]

# s = Server().boot()
# bpm = 60/220
# seq = Sequencer(bpm, plus_tot).mis(2).out()
# mix() will mix the signal into two channel, left and right.
# out() plays the sound to the audio output (speakers)
# These are both Pyo characteristics
# s.gui(locals())

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

basic = [notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["G4"],notes["G4"]]
# basic_bass = [notes["A2"],notes["A2"],notes["A2"],notes["A2"],notes["A2"],notes["A2"],notes["G2"],notes["G2"]]

# s = Server().boot()
# bpm1 = 60/120
# asdr = Adsr(attack=.05, decay=0, sustain=1, release=.05, dur=0.15, mul=.5)
# seq = Sequencer(bpm1, basic).mix(2).out() # can provide with or without envelope
# #bass = Sequencer(bpm1, basic_bass).mix(2).out()
# kick = SoundSequencer(bpm1, "sounds/kick.wav", [1,0,1,0]).out()
# snares = SoundSequencer(bpm1, "sounds/snare.wav", [0,1,0,1]).out()
# bpm2 = 60/240
# hihats = SoundSequencer(bpm2, "sounds/hihat.wav", [1,1,1,1,1,1,1,1]).out()
# bpm3 = 60/520
# #perc1 = SoundSequencer(bpm3, "sounds/perc1.wav", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).out()
# #perc2 = SoundSequencer(bpm3, "sounds/perc2.wav", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).out()
# #perc3 = SoundSequencer(bpm3, "sounds/perc3.wav", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).out()
# s.gui(locals())

########################################
## Simple Patch

s = Server().boot()
s.setAmp(0.4)
kicks = SoundSequencer("sounds/lofi1.wav", [1,1,1,1], 2).out()
hihats = SoundSequencer("sounds/hihat.wav", [1,1,1,1,1,1,1,1], 1).out()
synth = Sequencer(basic, 1).out()
bpm = BPM(250, [kicks, hihats, synth])

## uh, problem...the hihat and kick are becoming out of time, after like 7 or 8 bars. No clue why, but it isn't the length of the sample
## hopefully it's something to do with the bpm?
s.gui(locals())