from Sequencer import Sequencer
import time

sequencer = Sequencer(4)
sequencer.setSequence(1, 34)
sequencer.setSequence(2, 22)
sequencer.setSequence(3, 56)
sequencer.setSequence(4, 99)

print(sequencer._out)
time.sleep(0.2)
sequencer.next()
print(sequencer._out)
time.sleep(0.2)
sequencer.next()
print(sequencer._out)
time.sleep(0.2)
sequencer.next()
print(sequencer._out)
