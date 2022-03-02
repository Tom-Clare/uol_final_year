from pyo import *

s = Server().boot()

# Amplitude envelope
env = LinTable([(0,0), (100,1), (500,0.5), (4096,0.5), (8191,0)])

# The Metro object output triggers at the rate of two successive taps.
# It also handles the number of voices of polyphony.
met = Metro(.125, poly=2).play()

# Initial list of amplitudes for each tap.
seq = DataTable(16, init=[1,0,0.5,0,1,0.5,0,0.5,1,0,0.5,0,1,0.5,0,0.5])
# Graph editor.
seq.graph()

# Tap number counter, the metronome is mixed down to one channel to avoid
# dupplication of the counter. No matter how many voices of polyphony, we
# want the tap count to move forward for every trig of the metro.
tap = Counter(met.mix(1), max=16)

# Retrieve the amplitude of the current tap.
tapamp = TableIndex(seq, tap)

# This trigger is the one who start the sound for a tap to play.
# "tapamp > 0.0" returns 1 (as an audio stream) if the condition
# is true, 0 otherwise,
trig = met * (tapamp > 0.0)

# Read the envelope. Because "trig" is created from "met", a 2-streams
# object, it produces two alternating trigger signals.
amp = TrigEnv(trig, table=env, dur=.2, mul=tapamp)

# Simple frequency-modulation synthesizer.
fm = FM(carrier=250, ratio=0.254, index=amp*20, mul=amp*0.3)

# Mix the two channels in one and output the sound.
out = fm.mix(1).out()

s.gui(locals())