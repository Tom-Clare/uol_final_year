Project paper can be read [here](https://github.com/Tom-Clare/uol_final_year/blob/main/Project%20Report.pdf).

# Final Year Project
Final year project for my Computer Science Undergraduate Degree at the University of Lincoln

This project aims to provide an easy to use musical synthesis program. The music can be made in such a way that it can integrate with other programmatic events, responding to and triggering code from other sources.

This project is built on Pyo, an audio synthesis toolkit which leverages C-binding techniques to achieve the speed necessary for multi-channel audio synthesis. This readme file will take a look at a few code examples for this project and break them down, explaining both Pyo concepts and some of the classes introduced in this project. It is recommended that you have at least a casual understanding of Pyo before working with this project. The Pyo documentation can be found [here](http://ajaxsoundstudio.com/pyodoc/).

# Classes

Here the reader will find the docstrings for each class introduced with this project. Some examples are included as part of the docstring, but clearer and perhaps more usable examples are included in the examples section.

## SoundSequencer

A sound file sequencer with modifyable step count.
This module is externally clocked.

Parent: `PyoObject`

Args:
```
file  : string
    Filename of sound file to be played. Can be relative or absolute filepath.
activation_grid : list<bool>
    List of bools corresponding to when the wav file should play.
mul : float, optional
    How loudy to play the file.
```
Example:
```
s = Server().boot()

kicks = SoundSequencer("kick.wav", [1,0,1,0], 0.5).out()
bpm = BPM(120, [kick.next])

s.gui(locals())
```

## Sequencer

A sequencer with modifyable step count and step frequency.
This module is externally clocked. Output is a sine wave,
but this class could be further modified to output other
types of wave.

Parent: `PyoObject`

Args:
```
freq : array<float>
    Array of frequency values that will be mapped to sequence.
envelope : ASDR object, optional
    Envelope to be retriggered at the start of each note.
    Defaults to Adsr(attack=.0018, decay=0, sustain=1, release=.04, dur=0.1, mul=mul)
mul : float, optional
    Volume of notes.
    Defaults to 1.0
```
Example:
```
s = Server().boot()

envelope = Adsr(attack=.01, decay=0, sustain=1, release=.5, dur=0.2)
seq = Sequencer([0.5, 1, 1, 2], envelope, 0.3)
bpm = BPM(120, [seq.next])

s.gui(locals())
```

## BPM

This class creates an internal "tick" and will call supplied
functions on each tick. This class could be further modified
to accept a list of modulo's and only call each specific
callback function when the corresponding modulo operator is 
equal to zero.

Parent: `PyoObject`

Args:
```
rate : int or float
    Number of ticks per minute
func_next : list<callback functions>
    List of functions to call on each new tick.
```
Example:
```
s = Server().boot()

seq = Sequencer([440, 440, 440, 440])
bpm = BPM(120, [seq.next])

s.gui(locals())
```

# Examples

The following example shows a relatively simple drum pattern. The first and last lines are related to the Pyo toolkit. The first line of the example boots the Pyo server so that output can be heard. The final line creates a small interactive window. This window enables the user to start and stop audio, record audio to an output file, and to change the overall volume level of the script.

```
s = Server().boot()

kicks = SoundSequencer("sounds/kick.wav", [1,0,1,0]).out()
snares = SoundSequencer("sounds/snare.wav", [0,1,0,1], 0.5).out()
bpm = BPM(120, [kicks.next, snares.next])

s.gui(locals())
```

It’s possible to think of the `SoundSequencer` class as a drum sequencer. The first parameter specifies a sound file to be played every time the sequencer is activated. The second parameter specifies when the sequencer should activate. The optional third parameter for the SoundSequencer is a normalised volume value between 0 and 1.

The `BPM` class’s first parameter creates a “tick” with some time constant interval between each tick. This time interval is the first parameter, divided by 60. On each tick, the `BPM` class will call each and every function supplied to it via its second parameter.

The `BPM` class doesn’t strictly have to be thought of only as a BPM counter. For example, let’s say we wished to add hihats. Hihats usually occur more than every beat, perhaps they need to occur every half beat. In its current state, the first example is unable to do that because there is not enough fidelity in the patterns. To fix this, the BPMs rate can be doubled, and the length of the patterns can be doubled, adding a zero in every other element. The below example will sound identical to the pattern before, only there will now be a hihat on every beat and offbeat.

```
s = Server().boot()

kicks = SoundSequencer("sounds/kick.wav", [1,0,0,0,1,0,0,0]).out()
snares = SoundSequencer("sounds/snare.wav", [0,0,1,0,0,0,1,0], 0.5).out()
hihats= SoundSequencer("sounds/hat2.wav", [1,1,1,1,1,1,1,1]).out()
bpm = BPM(240, [kicks.next, snares.next, hihats.next])

s.gui(locals())
```

The next example will show the `Sequencer` class. This class is very similar to the `SoundSequencer` class, but instead plays a sine wave. Instead of the pattern parameter being a boolean list, it takes a list of floats which it will use as a list of frequencies to play the sine wave at. Here, the `notes` dictionary has been imported, allowing the user to simply specify a note on the western scales, instead of needing to remember the value of each note and typing each one in.

```
s = Server().boot()

kicks = SoundSequencer("sounds/kick.wav", [1,0,1,0,1,0,1,0], 0.4)
snares = SoundSequencer("sounds/snare.wav", [0,0,1,0,0,0,1,0], 0.4)
ohats = SoundSequencer("sounds/ohat.wav", [0,1,0,1,0,1,0,1], 0.3)
bass = Sequencer([0,notes['D2'],0,notes['D2'],0,notes['D2'],0,notes['D2']], mul=0.3)
bass_mix = bass.mix(2).out()
bpm = BPM(240, [kicks.next, snares.next, ohats.next, bass.next])

s.gui(locals())
```

The example above plays a house-type loop - a four-to-the-floor drum pattern with offbeat open hihats and bass notes. The `bass_mix` variable is instantiated with a call to `.mix(2)`. This is to spread the audio out over two channels, left and right. The SoundSequencer is mixed internally for easier use with sample files, which are usually single-channeled. However, the Sequencer may go through reverb, chorus, or other spread effects before being output to the speakers, so internal mixing will more than likely get in the way here.

To use Pyo effects with code from this project, it is possible to treat the outputs of the Sequencer as you would handle any other output in Pyo. The next example is a breakbeat pattern with a reverb-ed lead synth. The higher fidelity to achieve the style necessitates a tickrate of 570 ticks per minute.

```
s = Server().boot()
kicks = SoundSequencer("sounds/kick.wav", [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0], 0.4)
snares = SoundSequencer("sounds/snare.wav", [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0], 0.4)
ohats = SoundSequencer("sounds/hat.wav", [1,1,1,1,1,1,1,1], 0.05)
bass = Sequencer([notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['D4'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0,notes['G3'],0,0,0,0,0,0,0], mul=0.3)
bass_mix = bass.mix(2).out()

reverb = Freeverb(bass, size=0.9).mix(2).out()
bpm = BPM(570, [kicks.next, snares.next, ohats.next, bass.next])

s.gui(locals())
```
