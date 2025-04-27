# iterator can be used in for statement
r = range(5)
for i in r:
    print(i)
    
# for statement will move the marker of a iterator
ri = iter(r)
for i in ri:
    print(i)
    
# so when all the elements in an iterator is iterated by a for statement
# you cannot call next since the marker has been moved to the last element
next(ri)
