# <p>\Write a function called <strong>three_odd_numbers, </strong>which accepts a
#  list&nbsp;of numbers and returns <code>True</code>&nbsp; if any three consecutive
#   numbers sum to an odd number.</p>
'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

#try, except makes life o' so easy

def three_odd_numbers(li):
    try:
        for x in range(len(li)):
            if (li[x] + li[x+1] + li[x+2]) % 2 == 1:
                return True
    except IndexError:
        return False
