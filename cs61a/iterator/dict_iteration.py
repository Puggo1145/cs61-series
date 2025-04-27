dict = {
    "one": 1,
    "two": 2,
    "three": 3
}
dict["zero"] = 0

i = iter(dict.items())
print(next(i))
print(next(i))
# if a iterable value is changed, the last iterator be no longer usable
dict["four"] = 4
print(next(i)) # we will get an error here
# we have to recreate a iterator on that iterable value
