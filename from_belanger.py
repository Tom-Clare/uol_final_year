from pyo import *
s = Server().boot()
f = Adsr(attack=1, decay=.2, sustain=.5, release=4, dur=5, mul=.5)
a = Sine(mul=f).out()
f.play()
s.gui(locals())
