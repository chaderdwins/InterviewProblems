# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
# Input: [2, 2, 1]
# Output: 1

# Example 2:
# Input: [4, 1, 2, 1, 2]
# Output: 4

class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        return [key for key, value in d.items() if value == 1][0]

s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
