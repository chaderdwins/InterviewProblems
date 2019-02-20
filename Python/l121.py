class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        loc = glo = 0
        for i in range(len(prices)-1, 0, -1):
            loc = max(loc + prices[i] - prices[i-1], 0)
            print(loc)
            glo = max(glo, loc)
        return glo
        