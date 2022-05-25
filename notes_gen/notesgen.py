import pandas
import os
current_dir = os.path.dirname(os.path.abspath(__file__)) # get current file
filepath = os.path.join(current_dir, "notes.csv") # add filename onto current dir path
data = pandas.read_csv(filepath, sep=",") # read notes csv

# get values
name = data.note_sharp.values
hertz = data.hertz.values
octave = data.octave.values

notes = {} # this dict will hold the names and values of freqs
for i in range(0, len(name)):
    note_name = name[i].replace("#", "s", 1) # replace sharp symbols for a character that won't be confused as a python comment
    key = f"{note_name}{octave[i]}" # programmatically assign note name
    notes.update( { key : hertz[i] } ) # add note

## copy/paste from console and create the constants file. Go you!!
print(notes)