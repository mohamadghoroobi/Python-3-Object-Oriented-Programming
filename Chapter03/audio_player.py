import abc


class AudioFile:
    def __init__(self, filename):
        # self.ext = None
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def play(self):
        pass

    @abc.abstractmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) << attrs:
                return True

        return NotImplemented
