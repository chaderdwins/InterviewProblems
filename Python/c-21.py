# Write a function called nth, which accepts a list and a
# number and returns the element at whatever index is the number in the list. If
# the number is negative, the nth element from the end is returned.
'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b'
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(li, num):
    return li[num]
