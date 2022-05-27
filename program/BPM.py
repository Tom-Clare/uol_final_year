from time import sleep
import threading

class BPM:
    """
    BPM
    
    This class creates an internal "tick" and will call supplied
    functions on each tick. This class could be further modified
    to accept a list of modulo's and only call each specific
    callback function when the corresponding modulo operator is 
    equal to zero.

    :Parent: :py:class:`PyoObject`

    :Args:
        rate : int or float
            Number of ticks per minute
        func_next : list<callback functions>
            List of functions to call on each new tick.


    >>> s = Server().boot()

    >>> seq = Sequencer([440, 440, 440, 440])
    >>> bpm = BPM(120, [seq.next])

    >>> s.gui(locals())
    """

    def __init__(self, rate, func_next):
        self._rate = rate
        self._duration = 60 / self._rate 
        self._func_next = func_next # this must be given as a list

        self.heartrate = threading.Thread(name="heartbeat", target=self.go, daemon=True)
        self.heartrate.start()
        

    def go(self):
        threshold = 1
        while(True):
            
            if threshold:
                # make callbacks
                for func_next in self._func_next:
                    func_next() # call callback
                threshold = 0
            else:
                sleep(self._duration) # pause for tick interval
                threshold = 1