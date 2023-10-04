from threading import Thread
import pyaudio
import wave
import time

class Recorder(Thread):
    def __init__(self,
                 filename = 'temp/file.wav',
                 chunk = 1024, # Record in chunks of 1024 samples
                 chanels = 1, # Mono record
                 smpl_rt = 44100, # Record at 44400 samples per second
                 ):

        Thread.__init__(self)

        self.smpl_rt = smpl_rt
        self.chunk = chunk
        self.filename = filename
        self.chanels = chanels
        self.stat = True
        self.sample_format = pyaudio.paInt16
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format = self.sample_format, channels = self.chanels,
                                   rate = self.smpl_rt, input = True,
                                   frames_per_buffer = self.chunk)

    def run(self):
        print('Recording...')
        print('Press Control + c to stop recording')
        self.frames = []
        i = 0
        while self.stat:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
            i += 1

        print('Done !!! ')
        self.finish()

    def finish(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()

        sf = wave.open(self.filename, 'wb')
        sf.setnchannels(self.chanels)
        sf.setsampwidth(self.pa.get_sample_size(self.sample_format))
        sf.setframerate(self.smpl_rt)
        sf.writeframes(b''.join(self.frames))
        sf.close()
        print('Finished')

    def stop(self):
        self.stat = False


import scipy.io.wavfile as wavfile
import scipy.fftpack
import numpy as np

class Fourier:
    begin_file = 0.0

    def __init__(self, file):
        self.fichier = file

    def open(self):
        self.fs_rate, self.signal = wavfile.read(self.fichier)
        self.l_audio = len(self.signal.shape)
        if self.l_audio == 2:
            self.signal = self.signal.sum(axis = 1) / 2

        self.N = self.signal.shape[0] # Nombre d'éléments
        self.secs = self.N / float(self.fs_rate) # Durée e(n secondes) du fichier
        self.Ts = 1.0/self.fs_rate # Période d'échantillonage

        self.t = np.arange(0, self.secs, self.Ts) # Vecteur temps du signal

    def detect_begin(self):
        somme = 0.0
        for i in range(self.signal.size):
            if self.signal[i] >= 0:
                somme += self.signal[i]

        somme /= self.signal.size
        print('valeur moyenne du signal :', somme)

        i = 0
        couples = [{'high': 0.0, 'low': 0.0}]
        old = 'low'
        for i in range(self.signal.size):
            s = abs(self.signal[i])

            if s > somme:
                act = 'high'
            else:
                act = 'low'

            if act == 'high' and old == 'high':
                old = 'high'
                couples[-1]['high'] += 1

            elif act == 'low' and old == 'low':
                old = 'low'
                couples[-1]['low'] += 1

            elif act != old:
                couples.append({'high': 0.0, 'low': 0.0})

            if i % 1000 == 0:
                print(' + 1000')

        for i in range(len(couples)):
            if i % 1000 == 0:
                print(couples[i])


def Analyse(file = 'temp/tobetested.wav',
            source = 'temp/file.wav',
            record = True,
            command = lambda: input()):

    if record:
        r = Recorder(filename = 'temp/tobetested.wav')
        r.start()
        time.sleep(1)
        command()
        r.stop()

    f = Fourier(file = 'temp/tobetested.wav')
    f.open()
    f.detect_begin()


if __name__ == '__main__':
    a = Analyse(record = False)
    print(a)
