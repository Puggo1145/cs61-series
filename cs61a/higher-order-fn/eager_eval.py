# Differences of eval behavior between function and control statements

# When using function for control purpose
# we have to pay attention to its different behavior on evaluation
# When using normal control syntax:
    # eval happens only when the program reaches one of the branches
# When using function:
    # eval happens when passing parameters!!!


import math
from typing import Callable, Any

def my_if(a: bool, b: float, c: float) -> float:
    if a:
        return b
    else:
        return c

def my_if_eval_later(a: bool, b: Callable[[], float], c: float) -> float:
    if a:
        return b() # call the sqrt() later at this point
    else:
        return c

def real_sqrt(x: int):
    # if we eval later by passing a callback function. Call the sqrt() inside the function. Things will work
    eval_later_result = my_if_eval_later(x >= 0, lambda: math.sqrt(x), 0)
    print(f"eval later succeed!: {eval_later_result}\n")
    
    # An error will be raised if x < 0 
    # since the math.sqrt() evaled when passing params before going into the function
    eval_immediately_result = my_if(x >= 0, math.sqrt(x), 0)
    print(eval_immediately_result)
    
real_sqrt(-2)
    