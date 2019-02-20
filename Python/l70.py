class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        for i in self.helper(n):
            k = i
        return k
    
    def helper(self, n):
        x = 1
        y = 1
        count = 0
        while count < n:
            x, y = y, x + y
            yield x
            count += 1
        