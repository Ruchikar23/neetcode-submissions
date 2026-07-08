class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = len(prices)
        profit =0
        for i in range(k):
            buy = prices[i]
            for j in range(i+1,k):
                sell = prices[j]
                profit = max(profit,sell-buy)
        return profit

