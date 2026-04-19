class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for i in range(1, len(prices)):
            cur = prices[i] - prices[buy]
            if cur < 0:
                buy = i 
            profit = max(profit, cur)

        return profit