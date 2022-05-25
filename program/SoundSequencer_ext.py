from time import sleep
from pyo import *
import threading

class SoundSequencer(PyoObject):
    """
    Sound Sequencer
    
    A sound file sequencer with modifyable step count.
    This module is externally clocked.

    :Parent: :py:class:`PyoObject`

    :Args:

        file  : string
            Filename of sound file to be played.
        activation_grid : list<bool>
            List of bools corresponding to when the wav file should play.
        resolution : int
            How many BPM ticks are required to increment current position of the activation grid pointer.

    >>> s = Server().boot()
    >>> s.start()
    >>> bpm = Sine(60/120)
    >>> kicks = SoundSequencer("kick.wav", [1,0,1,0]).out()
    """

    def __init__(self, filename, activation_grid, mul=1.0):
        # Initialise PyoObject's basic attributes
        PyoObject.__init__(self)

        # Keep references of all raw arguements
        self._filename = filename
        self._activation_grid = activation_grid
        self._mul = mul

        # Setup required vars
        self.resetStep()

        # Convert all arguements to lists for "multichannel expansion"
        filename, activation_grid, lmax = convertArgsToLists(filename, activation_grid)

        ## Input checks
        ###### perform sanity checks here ###########################################################

        # Processing
        self._sound_out = SfPlayer(self._filename)

        # self._base_objs is the audio output seen by the outside world
        # This sets up all the correct outputs for the class to ensure it abides by PyoObject's rules.
        self._base_objs = self._sound_out.getBaseObjects()

    def resetStep(self):
        """
        Resets step of sequencer
        """
        self._index = 0

    def next(self):
        """
        Triggers the next step in the sequence
        """
        next_index = self._index + 1
        if next_index > len(self._activation_grid) - 1:
            next_index = 0  # back to the start
        self._index = next_index
        if self._activation_grid[self._index] == True:
            # play sound file
            self._sound_out = SfPlayer(self._filename, mul=self._mul).mix(2).out()
    
    def setSteps(self, x):
        """
        Replace step count.
        
        :Args:
        
            x : Integer
                New step count
        
        """
        self._steps = x

    def ctrl(self, map_list=None, title=None, wxnoserver=False):
        ## We may want to create a freq slider for each step (up to 8)
        #self._map_list = [SLMap(10, 2000, "log", "freq", self._freq), SLMapMul(self._mul)]
        PyoObject.ctrl(self, map_list, title, wxnoserver)

    ## following this tutorial:
    # http://ajaxsoundstudio.com/pyodoc/tutorials/pyoobject2.html

    # Best of luck, future me! :)

    def play(self, dur=0, delay=0):
        self._sound_out.play(dur, delay)
        return PyoObject.play(self, dur, delay)
    
    def stop(self, wait=0):
        return PyoObject.stop(self, wait)

    def out(self, chnl=0, inc=0, dur=0, delay=0):
        return PyoObject.out(self, chnl, inc, dur, delay)