import pyaudio
import numpy as np
import math

p = pyaudio.PyAudio()

volume = 0.3       # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 1000.0        # wave frequency, Hz, may be float

def square(self):
    print(self)
    output = self
    for i in range(0, len(self)):
        if self[i] > 0:
            output[i] = 1
        else:
            output[i] = -1
    print(output)
    return output

def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
wave = square(samples)

#### FILTER
cutOffFrequency = 400

freqRatio = (cutOffFrequency/fs)
N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

# Use moviung average (only on first channel)
filtered = running_mean(wave, N).astype(wave.dtype)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write((volume*filtered).tobytes())

stream.stop_stream()
stream.close()

p.terminate()