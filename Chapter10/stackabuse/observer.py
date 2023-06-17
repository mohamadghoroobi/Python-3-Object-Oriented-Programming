class Observer:
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)

