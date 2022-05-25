from time import sleep
from pyo import *
import threading

class Sequencer(PyoObject):
    """
    Sequencer
    
    A sequencer with modifyable step count and step frequency.
    This module is externally clocked. Output is a sine wave,
    but this class could be further modified to output other
    types of wave.

    :Parent: :py:class:`PyoObject`

    :Args:
        freq : array<float>
            Array of frequency values that will be mapped to sequence.
        envelope : ASDR object, optional
            Envelope to be retriggered at the start of each note.
            Defaults to Adsr(attack=.0018, decay=0, sustain=1, release=.04, dur=0.1, mul=mul)
        mul : float, optional
            Volume of notes.
            Defaults to 1.0


    >>> s = Server().boot()
    >>> envelope = Adsr(attack=.01, decay=0, sustain=1, release=.5, dur=0.2)
    >>> seq = Sequencer([0.5, 1, 1, 2], envelope, 0.3)
    >>> bpm = BPM(120, [seq.next])
    >>> s.gui(locals())
    """

    def __init__(self, freq, envelope=None, mul=1.0):
        # Initialise PyoObject's basic attributes
        PyoObject.__init__(self)

        # Keep references of all raw arguements
        self._freq = freq
        if envelope is None: # if no ASDR evelope provided
            self._envelope = Adsr(attack=.0018, decay=0, sustain=1, release=.04, dur=0.1, mul=mul) # default envelope
        else:
            self._envelope = envelope

        # Setup required vars
        self._index = 0

        # Convert all arguements to lists for "multichannel expansion"
        freq, envelope, lmax = convertArgsToLists(freq, envelope)

        # Processing
        self._seq_out = Sine(freq=self._freq[self._index], mul=self._envelope)

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
            self._seq_out.freq = self._freq[self._index]
            self._envelope.play()

    def ctrl(self, title=None, wxnoserver=False):
        PyoObject.ctrl(self, title, wxnoserver)

    def play(self, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.play(self, dur, delay)
    
    def stop(self, wait=0):
        self._seq_out.stop(wait)
        return PyoObject.stop(self, wait)

    def out(self, chnl=0, inc=1, dur=0, delay=0):
        self._seq_out.play(dur, delay)
        return PyoObject.out(self, chnl, inc, dur, delay)