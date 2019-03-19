import pyaudio
import wave
import sys
import numpy as np
import librosa
#from pydub import AudioSegment


class Play:
    CHUNK = 1024

    def __init__(self):
        #try:
        #self.audio_file = wave.open(urllib.request.urlopen(url))
        self.audio_file = wave.open("low.wav", 'rb')
        #self.audio_file = wave.open(url, 'rb')
        '''
        except Exception as e:
            print("Something went wrong!", e, "exiting.....")
            exit()
        '''
        
        self.p = pyaudio.PyAudio()

        self.rate = self.audio_file.getframerate()
        print(self.rate)
        self.pitch = 0

        self.stream = self.p.open(
                        format=self.p.get_format_from_width(
                            self.audio_file.getsampwidth()),
                        channels=self.audio_file.getnchannels(),
                        rate=self.rate,
                        output=True)

        print("done")

    def start_stream(self):
        #try:
        data = self.shift(self.audio_file.readframes(Play.CHUNK), self.rate)
        '''
        except Exception as e:
            print("Could not play song!", e, "Exiting....")
            exit()
        '''
        print("Started Playing")

        while len(data) <= Play.CHUNK:
            print("listen")
            self.stream.write(data)
            data = self.shift(self.audio_file.readframes(Play.CHUNK), self.rate)

        print("Stopped Playing")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def shift(self, data, sample_rate):
        print("in")
        np_data = np.frombuffer(data)
        transposed = librosa.effects.pitch_shift(
                        np_data, sample_rate, n_steps=5)
        return transposed

'''
import librosa
f = wave.open("low.wav", 'rb')
data = f.readframes(1024*3)
y = np.frombuffer(data, dtype=np.float32)
print(y)
#y, sr = librosa.load(librosa.util.example_audio_file(), sr=None)
#y, sr = librosa.load('low.wav', sr=48000) # y is a numpy array of the wav file, sr = sample rate
y_shifted = librosa.effects.pitch_shift(y, 44100, n_steps=5) # shifted by 4 half steps
'''

new = Play()
new.start_stream()

