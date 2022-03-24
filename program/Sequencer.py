from time import sleep
from pyo import *
import threading

class Sequencer(PyoObject):
    """
    Sequencer
    
    A sequencer with modifyable step count and step frequency.
    This module is internally clocked. The external clock must reach
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

    def __init__(self, step_duration, freq=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]):
        # Initialise PyoObject's basic attributes
        PyoObject.__init__(self)

        # Keep references of all raw arguements
        self._step_duration = step_duration
        self._freq = freq

        # Create exposed var
        self._volt = 0

        # Setup required vars
        self.resetStep()

        # Convert all arguements to lists for "multichannel expansion"
        freq, lmax = convertArgsToLists( freq)

        # Processing
        self._seq_out = Sine(freq=freq[self._index])

        # Begin module's internal clock on a seperate thread
        self._internal_clock = threading.Thread(name="clock", target=self.clock, daemon=True)
        self._internal_clock.start()

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
        
    def setFreq(self, x):
        """
        Set frequency list
        
        :Args:
        
            x : List
                List of new frequency values
        
        """
        self._freq = x

    def clock(self):
        """
        Listen to clock in. Intended for use on a seperate thread.
        """
        threshold = 1
        while(True):
            
            if threshold:
                self.next()
                threshold = 0
            else:
                sleep(self._step_duration)
                threshold = 1

    @property # getter
    def step_duration(self):
        """PyoObject. Clock source"""
        return self._step_duration
    @step_duration.setter # setter
    def step_step_duration(self, x):
        self._set_step_step_duration(x)

    @property # getter
    def freq(self):
        """PyoObject. Frequency list"""
        return self._freq
    @freq.setter # setter
    def freq(self, x):
        self.setFreq(x)

    def ctrl(self, title=None, wxnoserver=False):
        PyoObject.ctrl(self, title, wxnoserver)

    ## following this tutorial:
    # http://ajaxsoundstudio.com/pyodoc/tutorials/pyoobject2.html

    # Best of luck, future me! :)

    def play(self, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.play(self, dur, delay)
    
    def stop(self, wait=0):
        self._seq_out.stop(wait)
        self._internal_clock.stop()
        return PyoObject.stop(self, wait)

    def out(self, chnl=0, inc=1, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.out(self, chnl, inc, dur, delay)

if __name__ == "__main__":
    from notes import notes

    plus_tot = [notes["D4"], notes["Fs4"], notes["A4"], notes["D4"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"]]
    basic = [notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["G4"],notes["G4"]]

    s = Server().boot()
    seq = Sequencer(60/220, plus_tot).out()
    s.gui(locals())