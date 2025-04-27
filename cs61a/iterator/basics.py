# A container can provide an iterator that provides access to its elements in some order
# In python: 
# iter(iterable): Returns an iterator over the elements of an iterable value
# next(iterator): Return the next element in an iterator

ls = [1, 2, 3] # -> this is an  iterable value
iterator_of_ls = iter(ls) # creates a iterator for ls and points to the first element
print(next(iterator_of_ls)) # get the next element of ls which is 1
print(next(iterator_of_ls)) # get the next element of ls which is 2
# At this point, we've used up the first two element in the list
# There's only the last element in the iterator
# we can see it by doing this:
print(list(iterator_of_ls)) # [3]