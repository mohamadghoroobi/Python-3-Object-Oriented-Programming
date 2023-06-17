# Importing the ABC library
from abc import ABC, abstractmethod


# Creating our abstract class:
class ResearchGuideline(ABC):

    # Template Method definition:
    def templateMethod(self):
        # Calling all the steps
        self.step1()
        self.step2()
        self.step3()
        self.step4()

    # Defining the Template Method Steps
    def step1(self):
        pass

    def step2(self):
        pass

    @abstractmethod
    def step3(self):
        pass

    def step4(self):
        pass