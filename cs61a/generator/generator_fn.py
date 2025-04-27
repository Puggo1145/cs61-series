# A generator function is a function that yields value instead of returning them
# A normal function returns once; A generator function yields multiple times
# A generator is an iterator created automatically when you call a generator function 

def plus_n_minus(x):
    yield x
    yield -x
    
# when you call a generator function, it returns a iterator
f = plus_n_minus(3)
# every time you call next on the iterator, it yields value in sequence
print(next(f))
print(next(f))


def evens(start, end):
    even = start + (start % 2) # make sure starts from a even number
    while start < end:
        yield even
        even += 2

# When we call the generator function, we just get the generator of the fn
# the body of the function will only be executed every time the next() is called
# so every time we call next, the generator will yield the value in sequence        
t = evens(2, 10)
print(list(t))

