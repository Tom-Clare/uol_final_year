from pyo import *
from Sequencer_ext import Sequencer as Sequencer2
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

#basic = [notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["G4"],notes["G4"]]
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

# s = Server().boot()
# kicks = SoundSequencer("sounds/kick.wav", [1,0,1,0,1,0,1,0])
# hihats = SoundSequencer("sounds/hat2.wav", [1,1,1,1,1,1,1,1], 0.5)
# bpm = BPM(248, [kicks.next, hihats.next])

# s.gui(locals())

########################################
## simple offbeat with hihat
s = Server().boot()
kicks = SoundSequencer("./sounds/kick.wav", [1,0,1,0,1,0,1,0], 0.4)
snares = SoundSequencer("./sounds/snare.wav", [0,0,1,0,0,0,1,0], 0.4)
ohats = SoundSequencer("./sounds/ohat.wav", [0,1,0,1,0,1,0,1], 0.3)
bass = Sequencer2([0,notes['D2'],0,notes['D2'],0,notes['D2'],0,notes['D2']], mul=0.3)
bass_mix = bass.mix(2).out()
bpm = BPM(252, [kicks.next, snares.next, ohats.next, bass.next])

s.gui(locals())

########################################
## 

########################################
## breakbeat with reverb lead
# s = Server().boot()
# kicks = SoundSequencer("sounds/kick.wav", [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0], 0.6)
# snares = SoundSequencer("sounds/snare.wav", [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], 0.6)
# ohats = SoundSequencer("sounds/hat.wav", [1,1,1,1,1,1,1,1], 0.15)
# bass = Sequencer2([notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0], mul=0.3)
# bass_mix = bass.mix(2).out()

# reverb = Freeverb(bass, size=0.9).mix(2).out()
# bpm = BPM(570, [kicks.next, snares.next, ohats.next, bass.next])

# s.gui(locals())