class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0] # the lowest price so far: the best day to buy
        for sell_day in range(1, len(prices)):
            buy = min(buy, prices[sell_day])
            profit = max(profit, prices[sell_day] - buy) # the best profit so far

        return profit