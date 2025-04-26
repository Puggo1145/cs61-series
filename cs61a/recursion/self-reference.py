def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x + y)
    return next_sum
    

print_sum(1)(2)(3)


# Global:
#   print_sum: <print_sum>
# f1: <print_sum>(x) [parent=Global]
#   x: 1
#   next_sum: <next_sum>
#   return value: <next_sum>
# f2: <next_sum>(y) [parent=f1]
#   y: 2
# f3 <print_sum>(x) [parent=Global]
#   x: 3 (f1.x + f2.y)
#   return value: <next_sum>
# f4 <next_sum>(y) [parent=f3]
#   y: 3
#   return value: <print_sum>
# f5 <print_sum>(x) [parent=Global]
#   x: 6 (f3.x + f4.y)
#   retur value: <next_sum>
    