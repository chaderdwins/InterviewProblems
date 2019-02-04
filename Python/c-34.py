# <p>Write a function called&nbsp;<strong>once.&nbsp;</strong>This function accepts
# a function and returns a new function that can only be invoked once. If the
# function is invoked more than once, it should return None.
# Hint you will need to define a new function inside of your
# once function and return that function. You can add properties to your inner function
# to see if it has run already.</p>

def once(fun):
    count = 0
    def fun(a,b):
        nonlocal count
        if count == 0:
            count += 1
            return a + b
        return None
    return fun
