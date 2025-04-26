# A return expression completes the evaluation of a call expression and provide its value
# A user-defined f(x) is called: 1. switch to a new environment 2. execute the f's body
# return statement within the f: switch back to the previous environment; f(x) has a value


def search(f):
    x = 0
    while not f(x):
        x += 1
    return x


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


print(search(positive))
