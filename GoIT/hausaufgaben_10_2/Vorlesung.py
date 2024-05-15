def func_decorator (func):
    def wrapper():
        print ('----etwas machen wir vor den Aufrufen')
        func()
        print('---etwas machen wir nach dem Aufrufen')
    return wrapper

def some_funk():
    print('Es wird funktion some_funk aufgerufen')


some_funk= func_decorator(some_funk)


some_funk()
