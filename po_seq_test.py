from time import sleep
from pyo import *
import threading

class Sequencer(PyoObject):
    """
    Step Sequencer
    
    A step sequencer with modifyable step count and step frequency.
    This module is externally clocked. The external clock must reach
    an amplitude of 1 before the next step is triggered, and must
    pass through 0 before a new step can be triggered again. Output
    can control oscillator pitch or other CV-controlled modules.

    :Parent: :py:class:`PyoObject`

    :Args:

        clock : PyoObject
            External clock source.
        steps : integer, optional
            Amount of steps in the sequence.
            Defaults to 8.
        freq : array(float), optional
            Array of frequency values that will be mapped to sequence.
            Defaults to array of 1hz.

    >>> s = Server().boot()
    >>> s.start()
    >>> bpm = Sine(2)
    >>> seq = Sequencer(bpm, 4, [0.5, 1, 1, 2])
    >>> a = Sine(freq=100, mul=0.2, add=seq).out()
    """

    def __init__(self, clock, steps=8, freq=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]):
        # Initialise PyoObject's basic attributes
        PyoObject.__init__(self)

        # Keep references of all raw arguements
        self._clock = clock
        self._steps = steps
        self._freq = freq

        # Setup required vars
        self.resetStep()

        # Use InputFader to allow cross-fading between inputs when changing sources
        self._in_fader = InputFader(clock)

        # Convert all arguements to lists for "multichannel expansion"
        in_fader, steps, freq, lmax = convertArgsToLists(self._in_fader, steps, freq)

        ## Input checks
        # If list of frequencies can't be mapped to steps, re-init values
        if len(self._freq) < self._steps:
            self._steps = 8
            self._freq = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

        # Processing
        self._seq_out = Sine(freq=freq[self._index])
        ## when clock == 1 call next()
        self._c = threading.Thread(name="clock_in", target=self.listenToClock, daemon=True)
        self._c.start()

        # self._base_objs is the audio output seen by the outside world
        self._base_objs = self._seq_out.getBaseObjects()

    def resetStep(self):
        """
        Resets step of sequencer
        """
        self._index = 0
        self._seq_out = Sine(freq=self._freq[0])

    def next(self):
        """
        Triggers the next step in the sequence
        """
        next_index = self._index + 1
        if next_index > len(self._freq) - 1:
            next_index = 0  # back to the start
        self._index = next_index
        self._seq_out.freq = self._freq[self._index]

    def setClock(self, x, fadetime=0.05):
        """
        Replace clock source with new source.
        
        :Args:
        
            x : PyoObject
                New source signal
            fadetime = float, optional
                Crossfade time between old and new input.
                Defaults to 0.05.
        
        """
        self._clock = x
        self._in_fader.setClock(x, fadetime)
    
    def setSteps(self, x):
        """
        Replace step count.
        
        :Args:
        
            x : Integer
                New step count
        
        """
        self._steps = x
        
    def setFreq(self, x):
        """
        Set frequency list
        
        :Args:
        
            x : List
                List of new frequency values
        
        """
        self._freq = x

    def listenToClock(self):
        """
        Listen to clock in. Intended for use on a seperate thread.
        """
        threshold = 1
        while(True):
            
            if threshold:
                self.next()
                threshold = 0
            else:
                sleep(0.2)
                threshold = 1

    @property # getter
    def clock(self):
        """PyoObject. Clock source"""
        return self._clock
    @clock.setter # setter
    def clock(self, x):
        self.setClock(x)

    @property # getter
    def freq(self):
        """PyoObject. Frequency list"""
        return self._freq
    @freq.setter # setter
    def freq(self, x):
        self.setFreq(x)

    def ctrl(self, map_list=None, title=None, wxnoserver=False):
        ## We may want to create a freq slider for each step (up to 8)
        #self._map_list = [SLMap(10, 2000, "log", "freq", self._freq), SLMapMul(self._mul)]
        PyoObject.ctrl(self, map_list, title, wxnoserver)

    ## following this tutorial:
    # http://ajaxsoundstudio.com/pyodoc/tutorials/pyoobject2.html

    # Best of luck, future me! :)

    def play(self, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.play(self, dur, delay)
    
    def stop(self, wait=0):
        self._seq_out.stop(wait)
        self._c.stop()
        return PyoObject.stop(self, wait)

    def out(self, chnl=0, inc=1, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.out(self, chnl, inc, dur, delay)

if __name__ == "__main__":
    s = Server().boot()
    clock = Sine(freq=0.2)
    seq = Sequencer(clock.out(), 24, [294, 370, 440, 294, 370.2, 440, 247, 370, 440, 247, 370, 440, 277, 370, 440, 277, 370, 440, 277, 370, 440, 277, 370, 440])
    sound = Sine(freq=seq.out()).out() # uninstall pandas
    s.gui(locals())