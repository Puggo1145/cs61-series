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
            

print(luhn_sum(5105105105105100))
