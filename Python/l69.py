class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        # if x == 0:
        #     return 0
        # if x <= 2:
        #     return 1
        # for i in range(1,x):
        #     if i * i > x:
        #         return i - 1
        return int(x**0.5)
        