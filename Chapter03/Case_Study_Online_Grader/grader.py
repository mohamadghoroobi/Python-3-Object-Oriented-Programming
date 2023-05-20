import abc


class Assignments(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls in Assignments:
            attrs = set(dir(C))
            if set(cls.__abstactmethods__) <= attrs:
                return True

        return NotImplemented
