# Imports
from research_guideline import *
from university_a import UniversityA
from university_b import UniversityB


# Auxiliary function
def client_call(research_guideline: ResearchGuideline):
    research_guideline.templateMethod();


# Entry point
if __name__ == '__main__':
    # Calling the Template Method using the University A class as parameter
    print("University A:")
    client_call(UniversityA())

    # Calling the Template Method using the University A class as parameter
    print("University B:")
    client_call(UniversityB())