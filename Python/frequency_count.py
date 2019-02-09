# write a fxn called same which accepts two arrays
# the function should return true if every value in
# the array has it's corresponding value squared
# in the second array. frequency must match.
#

def frequency(x,y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        x[i] = x[i]**2
    x.sort()
    y.sort()
    if x == y:
        return True
    else:
        return False



li = [1,2,4,4,5]
zi = [25,16,9,4,1]
print(frequency(li, zi))
