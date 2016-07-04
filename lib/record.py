import pyaudio
import wave
class Record:
    def __init__( self ):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.RECORD_SECONDS = 5
    def record(  self, filename ):
 
        self.audio = pyaudio.PyAudio()
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                    rate=self.RATE, input=True,
                    frames_per_buffer=self.CHUNK)
        print("recording...")
        self.frames = []
 
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)
        print("finished recording")
 
        stream.stop_stream()
        stream.close()
        self.audio.terminate()
        
    def save( self, filename ):
        waveFile = wave.open(filename, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()
      