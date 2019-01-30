import unittest

#write a method to substitute all spaces ' ' in a string with %20.
#you may assume the string has sufficient space at the end to hold additional characters
#and we are given the 'true' length of the string initiallyself.
#ex:
#    input: "Mr John Smith    " 13 characters
#    output: "Mr%20John%20Smith"

def urlify(st):
    li = st.split()
    new_string = ''
    i = 0
    while i < len(li):
        if i == len(li) - 1:
            new_string += li[i]
        else:
            new_string += li[i] + '%20'
        i += 1
    return new_string

#unit testing
ans = urlify('much ado about nothing      ')
print(ans)
ans = urlify('Mr John Smith    ')
print(ans)
