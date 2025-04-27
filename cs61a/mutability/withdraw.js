function makeWithdrawList(balance) {
    let my_balance = balance

    return function withdraw(amount) {
        if (amount > my_balance) {
            return "Insufficient Balance!"
        }
        my_balance -= amount
        return my_balance
    }
}

withdraw = makeWithdrawList(100)
console.log(withdraw(25))
console.log(withdraw(25))
console.log(withdraw(25))
console.log(withdraw(25))
console.log(withdraw(25))
