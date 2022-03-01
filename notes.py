import pandas

data = pandas.read_csv("notes.csv", sep=",")

name = data.note_sharp.values
hertz = data.hertz.values
octave = data.octave.values

notes = {}
for i in range(0, len(name)):
    note_name = name[i].replace("#", "s", 1)
    key = f"{note_name}{octave[i]}"
    notes.update( { key : hertz[i] } )

## copy/paste from console, create constants file. Go you!!
print(notes)