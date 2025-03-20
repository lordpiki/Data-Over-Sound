import numpy as np
import sounddevice as sd

def play_frequency(frequency, duration=1.0, sample_rate=44100):
    # Create a time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate a sine wave for the given frequency
    audio_signal = np.sin(2 * np.pi * frequency * t)
    # Play the audio signal
    sd.play(audio_signal, samplerate=sample_rate)
    sd.wait()  # Wait until the sound is finished

# Example: Play a 440 Hz tone for 2 seconds
play_frequency(440, 2)

