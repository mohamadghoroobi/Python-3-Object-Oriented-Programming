from observer import Observer, Observable

subject = Observable()

observer1 = Observer(subject)
observer2 = Observer(subject)

subject.notify_observers('This is the 1st broadcast', kw='From the Observer')
subject.unsubscribe(observer2)

subject.notify_observers('This is the 2nd broadcast',
                         kw='From the Observer')