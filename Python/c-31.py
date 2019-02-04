# <p>Write a function called mode. This function
# accepts a list of numbers and returns the most frequent number in the list of
# numbers. You can assume that the mode will be unique.</p>

def mode(li):
    count = 0
    for item in set(li):
        if li.count(item) > count:
            count = item
    return count

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
