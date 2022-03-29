from pyo import *
s = Server().boot()
s.amp = 0.1
## adsr'ed sine wave. Plays once
# f = Adsr(attack=1, decay=.2, sustain=.5, release=4, dur=5, mul=.5)
# a = Sine(mul=f).out()
# f.play()
# s.gui(locals())

## experiment with sending single audio source to multiple effects
# a = Sine()
# hr1 = Harmonizer(a).out()
# ch = Chorus(a).out()
# sh = FreqShift(a).out()

## passing single source through chain of effects
# a = Sine()
# h1 = Harmonizer(a).out()
# h2 = Harmonizer(h1).out()
# h3 = Harmonizer(h2).out()
# h4 = Harmonizer(h3).out()

## multi-channelling outputs
# n = Noise()
# lp = ButLP(n).out()
# hp = ButHP(n).out(1)

## mul and add attributes
a = Sine(freq=200)
b = Sine(freq=200, mul=0.5, add=0.5).mix(2).out()
#c = Sine(freq=100).range(-0.25, 0.5)
sc = Scope([a, b])

## Keep this, will allow you to start/stop signal
s.gui(locals())
