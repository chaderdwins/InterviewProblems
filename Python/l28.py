# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        x, y = len(haystack), len(needle)
        if x == 0 and y == 0:
            return 0
        if y == 0:
            return 0
        for i in reversed(range(len(haystack))):
            for p in range(len(haystack) - i):
                x = haystack[p: i + p + 1]
                if ''.join(x) == needle:
                    return p
        return -1
        


s = Solution()
print(s.strStr('hello', 'll'))
