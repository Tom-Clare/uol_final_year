import pyaudio
import numpy as np
import math
import keyboard
import sys

np.set_printoptions(threshold=sys.maxsize)

p = pyaudio.PyAudio()

fs = 44100       # sampling rate, Hz, must be integer

def square(self):
    output = self
    for i in range(0, len(self)):
        if self[i] > 0:
            output[i] = 1
        else:
            output[i] = -1
    return output

def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

def gen_wave(key):
    volume = 0.3       # range [0.0, 1.0]
    duration = 0.2   # in seconds, may be float
    f = 1000.0        # wave frequency, Hz, may be float

    f3_freq = 174.61
    c4_freq = 261.63
    f4_freq = 349.23


    if key == "h":
        freq = f3_freq
    if key == "j":
        freq = c4_freq
    if key == "k":
        freq = f4_freq

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)
    wave = square(samples)

    #### FILTER
    cutOffFrequency = 400

    freqRatio = (cutOffFrequency/fs)
    N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

    # Use moviung average (only on first channel)
    filtered = running_mean(wave, N).astype(wave.dtype)

    return filtered*volume

def clean_wave_tail(wave):
    rev_wave = wave[::-1]
    output = ""
    for i in wave:
        output += ", "
        output += str(i)
    # so now, go through array, value by value, and find the first value that is close to zero
    #for index in rev_wave:
    #    amplitude = rev_wave[index]
    #    if -0.1 <= amplitude <= 0.1 :
    #        wave_cut_point = len(wave) - index
    #del wave[wave_cut_point:]
    print(output)
    return wave

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play via keyboard input
while True:
    try:
        if keyboard.is_pressed("h"):
            stream.write(gen_wave("h").tobytes())
        if keyboard.is_pressed("j"):
            #stream.write(clean_wave_tail(gen_wave("j")).tobytes())
            stream.write(gen_wave("j").tobytes())
        if keyboard.is_pressed("k"):
            #stream.write(clean_wave_tail(gen_wave("k")).tobytes())
            stream.write(gen_wave("k").tobytes())
    except:
        break
#stream.write(clean_wave_tail(gen_wave("k")).tobytes())

stream.stop_stream()
stream.close()

p.terminate()