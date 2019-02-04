# <p>Create a function running_average that returns a function.
# When the function returned is passed a value, the function returns the current
# average of all previous function calls. You will have to use closure to solve this.
# You should round all answers to the 2nd decimal place.</p>
'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

def running_average():
    total = 0
    called = 0
    def inner(value):
        nonlocal total
        nonlocal called
        called += 1
        total += value
        x = total / called
        return round(x, 2)
    return inner



rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
