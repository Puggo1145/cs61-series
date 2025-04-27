def make_withdraw_list(balance: int = 100):
    my_balance = balance

    def withdraw(amount: int):
        nonlocal my_balance
        my_balance -= amount
        return my_balance

    return withdraw

def make_withdraw_list_2(balance: int = 100):
    my_balance = [balance]

    def withdraw(amount: int):
        if amount > my_balance[0]:
            return "insufficient balance"
        
        my_balance[0] -= amount
        return my_balance[0]

    return withdraw
