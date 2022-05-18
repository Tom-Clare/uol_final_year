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
        freq : array(float)
            Array of frequency values that will be mapped to sequence.
            Defaults to array of 1hz.
        envelope : ASDR object, optional
            Envelope to be retriggered at the start of each note.
            Defaults to Adsr(attack=.0018, decay=0, sustain=1, release=.04, dur=0.1, mul=mul)
        mul : float, optional
            Volume of notes.
            Defaults to 1.0


    >>> s = Server().boot()
    >>> s.start()
    >>> bpm = Sine(2)
    >>> seq = Sequencer(bpm, 4, [0.5, 1, 1, 2])
    >>> a = Sine(freq=100, mul=0.2, add=seq).out()
    """

    def __init__(self, freq, envelope=None, mul=1.0):
        # Initialise PyoObject's basic attributes
        PyoObject.__init__(self)

        # Keep references of all raw arguements
        #self._step_duration = step_duration
        self._freq = freq
        if envelope is None: # if no ASDR evelope provided
            self._envelope = Adsr(attack=.0018, decay=0, sustain=1, release=.04, dur=0.1, mul=mul) # default envelope
        else:
            self._envelope = envelope

        # # Create exposed var
        # self._volt = 0

        # Setup required vars
        #self.resetStep()
        self._index = 0

        # Convert all arguements to lists for "multichannel expansion"
        freq, envelope, lmax = convertArgsToLists(freq, envelope)

        # Processing
        #self._asdr = Adsr(attack=.05, decay=0, sustain=1, release=.05, dur=0.15, mul=.5)
        self._seq_out = Sine(freq=self._freq[self._index], mul=self._envelope)

        # Begin module's internal clock on a seperate thread
        #self._internal_clock = threading.Thread(name="clock", target=self.clock, daemon=True)
        #self._internal_clock.start()

        # self._base_objs is the audio output seen by the outside world
        self._base_objs = self._seq_out.getBaseObjects()

    def next(self):
        """
        Triggers the next step in the sequence
        """
        next_index = self._index + 1
        if next_index > len(self._freq) - 1:
            next_index = 0  # back to the start
        self._index = next_index
        if self._freq[self._index] != 0:
            #self._seq_out.out()
            self._seq_out.freq = self._freq[self._index]
            self._envelope.play()
        
    def setFreq(self, x):
        """
        Set frequency list
        
        :Args:
        
            x : List
                List of new frequency values
        
        """
        self._freq = x

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
        return PyoObject.stop(self, wait)

    def out(self, chnl=0, inc=1, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.out(self, chnl, inc, dur, delay)

# if __name__ == "__main__":
#     from notes import notes

#     plus_tot = [notes["D4"], notes["Fs4"], notes["A4"], notes["D4"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["B3"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"], notes["Cs4"], notes["Fs4"], notes["A4"]]
#     basic = [notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["A4"],notes["G4"],notes["G4"]]

#     s = Server().boot()
#     seq = Sequencer(60/220, plus_tot).out()
#     s.gui(locals())