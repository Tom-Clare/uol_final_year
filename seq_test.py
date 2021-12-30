from Sequencer import Sequencer
from Clock import Clock
import time

sequencer = Sequencer(4)
sequencer.setSequence(1, 34)
sequencer.setSequence(2, 22)
sequencer.setSequence(3, 56)
sequencer.setSequence(4, 99)

# print(sequencer._out)
# time.sleep(0.2)
# sequencer.next()
# print(sequencer._out)
# time.sleep(0.2)
# sequencer.next()
# print(sequencer._out)
# time.sleep(0.2)
# sequencer.next()
# print(sequencer._out)


clock = Clock(60)

clock.start()
print("ahhh")
sequencer.clock_in(clock._out)

## loop gets tuck in Clock - may need to look at subprocessing or multithreading https://stackoverflow.com/questions/2629680/deciding-among-subprocess-multiprocessing-and-thread-in-python

## the issue here is linking the output of the clock to the sequencer. 
## The method needs to be easy and quick. 
# sequencer.clock_in(clock._out)