import abc
import uuid


class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the right methods."
            )

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id


class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls in Assignment:
            attrs = set(dir(C))
            if set(cls.__abstactmethods__) <= attrs:
                return True

        return NotImplemented


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1
        return result

    def lesson(self):
        return self.assignment.lesson()
