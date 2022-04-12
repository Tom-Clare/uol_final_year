from SoundSequencer import SoundSequencer
from pyo import *
import os

path = os.path.join(os.path.expanduser("~"), "Desktop")
lname = os.path.join(path, "left.wav")
rname = os.path.join(path, "right.wav")
allname = os.path.join(path, "all.wav")

s = Server().boot()
s.recordOptions(dur=60.1, filename=allname, fileformat=0, sampletype=1)
s.setAmp(0.4)
bpm1 = 60/100
bpm2 = 60/200
kicks = SoundSequencer(bpm2, "sounds/lofi1.wav", [1,0,1,0,1,0,1,0], 0).out() # left
hihats = SoundSequencer(bpm2, "sounds/hihat.wav", [1,1,1,1,1,1,1,1], 1).out() # right

#kickrec = Record(kicks, filename=lname, chnls=2, fileformat=0, sampletype=0)
#hihatrec = Record(hihats, filename=rname, chnls=2, fileformat=0, sampletype=0)

#clean = Clean_objects(60.1, kickrec, hihatrec)

#clean.start()
s.recstart()
s.start()

## record this into wav file and overlay left and right with different colour values. Could use matplotlib maybe idk

## uh, problem...the hihat and kick are becoming out of time, after like 7 or 8 bars. No clue why, but it isn't the length of the sample
## hopefully it's something to do with the bpm?
s.gui(locals())