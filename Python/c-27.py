# <p>Write a function called <strong>is_odd_string</strong>&nbsp;which returns true
# if sum of each character's position in the alphabet is odd. For example, "a" is
# in the first position, "b" is in the second position, and so on. If the sum is
# even, return false.&nbsp; NOTE:&nbsp;INDEXING&nbsp;STARTS AT&nbsp;1.&nbsp; A is
# position 1, NOT&nbsp;POSITION&nbsp;0.</p>
#
'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(string):
    alphabet = "0abcdefghijklmnopqrstuvwxyz"
    sum = 0
    for char in string:
        sum += alphabet.index(char)
    return sum % 2 != 0

print(is_odd_string('aaaa'))
