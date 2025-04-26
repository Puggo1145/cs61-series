def split(number):
    return number // 10, number % 10


def sum_digit(number):
    # Conditional statements check for base cases
    # It is evaluated without recursive calls
    # similar to an end condition in recursion
    if number < 10:
        return number
    else:
        # split numbers to digist less than 10
        all_but_last, last = split(number)
        return sum_digit(all_but_last) + last
    
print(sum_digit(2020))


def fact(number):
    if number == 0:
        return 1
    else:
        # Every time when a recursion happens, a new frame is created
        # Every frame keeps track of its own data
        # until a recursive function starts to return
        # then the frames return again and again to its top
        return number * fact(number - 1)
    
    
print(fact(3))
