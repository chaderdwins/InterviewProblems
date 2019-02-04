# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, i):
        """
        :type x: int
        :rtype: int
        """
        if i <= -2147483648 or i >= 2147483648:
            return 0
        if i < 0:
            o = int("-" + str(abs(i))[::-1])
            if o <= -2147483648 or o >= 2147483648:
                return 0
            return o
        k = int(str(i)[::-1])
        if k <= -2147483648 or k >= 2147483648:
            return 0
        return k



s = Solution()
print(s.reverse(123))
