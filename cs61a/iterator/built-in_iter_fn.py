# There's some utility function in python that can be used to compute or generate an iterator lazily
# which means the elements in the iterator will only be computed when accessed
ls1 = [1, 2, 3]
ls2 = [2, 3, 4]

print("-"*20, "MAP ITERATOR", "-"*20)
map_iter = map(lambda x: x*3, ls1)
print(next(map_iter))
print(next(map_iter))

print("-"*20, "FILTER ITERATOR", "-"*20)
filter_iter = filter(lambda x: x >= 2, ls1)
print(next(filter_iter))
print(next(filter_iter))

print("-"*20, "ZIP ITERATOR", "-"*20)
zip_iter = zip(ls1, ls2)
print(next(zip_iter))
print(next(zip_iter))

print("-"*20, "REVERSED ITERATOR", "-"*20)
reversed_iter = reversed(ls1)
print(next(reversed_iter))
print(next(reversed_iter))
