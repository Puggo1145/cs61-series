def split(number):
    return number // 10, number % 10


def sum_digits(number):
    if number < 10:
        return number
    else:
        number_but_last, last = split(number)
        return sum_digits(number_but_last) + last


# luhn_sum focus on adding odd number
def luhn_sum(number):
    if number < 10:
        return number
    else:
        all_but_last, last = split(number)
        return luhn_sum_double(all_but_last) + last
    

# luhn_sum_double focus on adding even number
def luhn_sum_double(number):
    all_but_last, last = split(number)
    luhn_digit = sum_digits(last * 2)
    if number < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
            

def luhn_sum_everything(number: int):
    """A more readable and maintable luhn sum example I believe"""
    if number < 10:
        return number
    
    total = 0
    number_sequence: list[int] = []
    
    while number > 0:
        last_digit = number % 10
        number_sequence.append(last_digit)
        number = number // 10
        
    for i, n in enumerate(number_sequence):
        if (i + 1) % 2 == 0:
            doubled_digit = n * 2
            if doubled_digit >= 10:
                first_doubled_digit = doubled_digit // 10
                last_doubled_digit = doubled_digit % 10
                luhn_digit = first_doubled_digit + last_doubled_digit
            else:
                luhn_digit = doubled_digit
                
            total += luhn_digit
        else:
            total += n
            
    return total
        

print(luhn_sum(5105105105105100))
print(luhn_sum_everything(5105105105105100))
