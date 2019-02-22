class Solution:
    def trailingZeroes(self, n: 'int') -> 'int':
        n = self.helper(n)
        k = 0
        n = str(n)
        n = n[::-1]
        nums = '123456789'
        for char in n:
            if char not in nums:
                k += 1
            else:
                return k
        
    def helper(self, x):
        if x == 0:
            return 1
        x = x * self.helper(x - 1)
        return x

s = Solution()
print(s.trailingZeroes(10))

