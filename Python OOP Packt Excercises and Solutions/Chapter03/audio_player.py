import abc


class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"playing {self.filename} as mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"playing {self.filename} as wav")


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"playing {self.filename} as ogg")


class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print(f"playing {self.filename} as flac")


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented
