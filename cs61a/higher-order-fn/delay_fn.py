def delay(val):
    print("delayed")
    def g():
        return val
    return g

print(delay(delay)()(6)())

# 1. delay(delay)
# print: delayed
# delay(delay) == g -> delay

# 2. delay(delay)()
# == g()
# == delay

# 3. delay(delay)()(6)
# == delay(6)
# print: delayed
# == g -> 6

# 4. delay(delay)()(6)()
# == g()
# == 6

# exec result:
# delayed
# delayed
# 6

# I would kick the guy's ass if they write program like this!
