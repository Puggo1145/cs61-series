def cascade_print(number):
    # when implement recursive function
    # always put the base condition at first (highly recommended)
    if number < 10:
        print(number)
    else:
        print(number)
        cascade_print(number // 10)
        print(number)
        
cascade_print(12345)
