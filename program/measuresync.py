from SoundSequencer import SoundSequencer
from pyo import *

s = Server().boot()
bpm1 = 60/100
bpm2 = 60/200
kicks = SoundSequencer(bpm2, "sounds/lofi1.wav", [1,0,1,0,1,0,1,0], 0).out() # left
hihats = SoundSequencer(bpm2, "sounds/hihat.wav", [1,1,1,1,1,1,1,1], 1).out() # right

## record this into wav file and overlay left and right with different colour values. Could use matplotlib maybe idk

## uh, problem...the hihat and kick are becoming out of time, after like 7 or 8 bars. No clue why, but it isn't the length of the sample
## hopefully it's something to do with the bpm?
s.gui(locals())