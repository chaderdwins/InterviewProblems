# Write a function called same_frequency which accepts two numbers and returns
# True if they contain the same frequency of digits. Otherwise, it returns False.

'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    d1 , d2 = {}, {}

    for item in num1:
        if item in d1:
            d1[item] += 1
        else:
            d1[item] = 0

    for item in num2:
        if item in d2:
            d2[item] += 1
        else:
            d2[item] = 0

    return d1 == d2
