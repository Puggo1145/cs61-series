# Function Composition is a way of combining different functin together

from typing import Callable


def square(x: int):
    return x * x


def triple(y: int):
    return 3 * y


def composer(f: Callable, g: Callable):
    def composed_fn(m: int):
        return g(f(m))

    return composed_fn


# square first and then triple the result
composed_fn = composer(square, triple)
result = composed_fn(4)
print(result)

# Execution Analysis
# 0. global frame initialization:
    # square
    # triple
    # composer
# 1. composer is called:
    # f1 <composer>(f, g) [parent=Global]
    # local variable: f, g, composed_fn
    # return value: composed_fn
# 2. execute the body of f1<composer>:
    # f2 <composed_fn>(x) [parent=f1]
    # local variable: x
    # variables from parent: f, g
    # return value: g(f(x))
# 3. f is called -> square
    # f3 <square>(x) [parent=f2]
    # local variable: x
    # return value: x * x -> (m * m)
# 4. g is called -> triple
    # f4 <triple>(y) [parent=f2]
    # local variable: y
    # return value: 3 * y -> (3 * f(m))