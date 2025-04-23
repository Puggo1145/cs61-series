from typing import Callable

# A higher-order function is a function 
# that 1. takes a function as an argument or 2. returns a function
# Currying is a kind of application of HoC

# 1. take a function as an argument
def event_listener(x: str, fn: Callable) -> None:
    # Let's pretend there is an event listener;
    if (x == 'my_event'):
        fn()

event_listener('my_event', lambda: print("oh my god!"))

# 2. return a function
def make_adder(n: int) -> Callable[[int], int]:
    def adder(k):
        return n + k

    return adder

res = make_adder(2)(3)
print(res)


# Crazy currying
def a(x):
    def b(y):
        def c(z):
            return x + y + z
        return c
    return b

print(a(1)(2)(3))
