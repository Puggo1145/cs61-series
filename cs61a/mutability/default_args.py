def f(arr=[]):
    arr.append(1)
    return len(arr)


# In python, the default argument is part of the function's value
# It is not created when the function is called
print(f())
print(f())
print(f())
