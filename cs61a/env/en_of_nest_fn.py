# Environments for nested function
# When a function is called, 
# a data structure: "frame" will be created
# to record its variable binding and execution status
# Frame is a representation of Scope

# A frame usually has:
# 1. parameters
# 2. local variables
# 3. return address
# 4. parent frame / enclosing frame


# e.g.

# Global Frame
# f1: make_adder
# var: adder(f1)

# f1 [parent=Global]
    # parameters: x
    # local variable: adder
    # return value: adder
def make_adder(x: int): 
    # f2 [parent=f1(make_adder)]
        # parameter: y
        # return value: x + y
    def adder(y):
        return x + y
    
    return adder

adder = make_adder(1) # initial value: 1
print(adder(1)) # 2

# Sum Up: When a function is called
# 1. add a local frame, and bind the name of the called function to this frame
# 2. copy parent of the function frame to this local frame
# 3. bind formal parameters（形参）to the arguments in the local frame
# 4. execute the body of the function in the environment that starts with the local frame
