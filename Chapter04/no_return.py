def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned."


def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception was raised")
    print("...so theses lines don't run")
