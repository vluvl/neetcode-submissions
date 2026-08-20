class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 999
        profit = 0
        for price in prices:
            if minP > price:
                minP = price
            if price - minP > profit:
                profit = price - minP
        return profit