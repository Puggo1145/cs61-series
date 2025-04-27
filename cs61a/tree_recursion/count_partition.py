# Tree-shaped processes arise whenever executing the body of recursive function
# makes more than one call to that function


def count_partition(n: int, m: int):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partition(n - m, m)
        without_m = count_partition(n, m - 1)
        return with_m + without_m
    
print(count_partition(6, 4))

