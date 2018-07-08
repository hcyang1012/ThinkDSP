# My excercise code for Think DSP Chapter 1
# Codes from http://nbviewer.jupyter.org/github/AllenDowney/ThinkDSP/blob/master/code/chap01.ipynb

from __future__ import print_function, division

# We don't need this link. Comment Out
# %matplotlib inline

import thinkdsp
import thinkplot

import numpy as np

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

# Excercise 1 : Plotting Signals

# Generate COS and SINE signals
cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

# Mix them
mix = sin_sig + cos_sig

# Plot
mix.plot()
#thinkplot.show()

# Excercise 2 : Wave

# Convert signal into Wave
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
period = mix.period
segment = wave.segment(start=0, duration=period*3)

#Plot
segment.plot()
#thinkplot.show()

# Excercise 3 : Spectrum

# Read wave from wav file
wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)

# Convert segment into spectrum
spectrum = segment.make_spectrum()


# Low Pass
spectrum.low_pass(3000)

# Plot
spectrum.plot()
# thinkplot.show()

# Excercise 1.2
wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)

segment.make_spectrum()
segment.make_audio()
segment.write("unfiltered.wav")

spectrum = segment.make_spectrum()
spectrum.low_pass(3000)
spectrum.plot()
#thinkplot.show()

filtered = spectrum.make_wave()
filtered.make_audio()
filtered.write("filtered.wav")

# Excercise 1.3
# Generate Two COS SIgnals
cos_sig1 = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
cos_sig2 = thinkdsp.SinSignal(freq=440*2, amp=1.0, offset=0)
cos_sig3 = thinkdsp.SinSignal(freq=440*3, amp=1.0, offset=0)

# Mix them
mix2 = cos_sig1 + cos_sig2 + cos_sig3

# Plot
wave2 = mix2.make_wave(duration=5, start=0, framerate=11025)
period = mix2.period
segment2 = wave2.segment(start=0, duration=5)
segment2.plot()
#thinkplot.show()
segment2.make_audio()
segment2.write("Excercise1_3_Harmonic.wav")



cos_sig1 = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
cos_sig2 = thinkdsp.SinSignal(freq=440*2+50, amp=1.0, offset=0)
cos_sig3 = thinkdsp.SinSignal(freq=440*3+50, amp=1.0, offset=0)

# Mix them
mix2 = cos_sig1 + cos_sig2 + cos_sig3

# Plot
wave2 = mix2.make_wave(duration=5, start=0, framerate=11025)
period = mix2.period
segment2 = wave2.segment(start=0, duration=5)
segment2.plot()
#thinkplot.show()
segment2.make_audio()
segment2.write("Excercise1_3_NonHarmonic.wav")