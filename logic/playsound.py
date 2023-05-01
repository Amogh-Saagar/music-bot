import audio2numpy as a2n
import sounddevice as sd
import threading


class Player(threading.Thread):
    def __init__(self):
        super().__init__()
        self.song_path = None

    def set(self, song_path):
        if self.song_path is None:
            self.song_path = song_path
            print(self.song_path)
            self.run()
        else:
            self.change_song(song_path)

    def run(self):
        self.data, self.fs = a2n.audio_from_file(self.song_path)
        print(self.fs)
        print(len(self.data))
        sd.play(self.data, self.fs, blocking = False)

    def change_time(self, new_time):
        sd.stop()
        sd.play(self.data[new_time:], self.fs, blocking = False)
    
    def change_song(self, new_song_path):
        self.song_path = new_song_path
        sd.stop()
        self.run()

    @property
    def song_length(self) -> int:
        return len(self.data)
    
    @property
    def freq(self):
        return self.fs

    