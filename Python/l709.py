# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
#
# Example 1:
#
# Input: "Hello"
# Output: "hello"
# Example 2:
#
# Input: "here"
# Output: "here"
# Example 3:
#
# Input: "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, str: 'str') -> 'str':
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        new_string = ''

        for char in str:
            if char in upper_alphabet:
                new_string += lower_alphabet[upper_alphabet.index(char)]
            else:
                new_string += char
        return new_string
