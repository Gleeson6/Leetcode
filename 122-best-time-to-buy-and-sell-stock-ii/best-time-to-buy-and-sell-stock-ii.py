class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # Loop up to second-to-last index
        for i in range(len(prices) - 1):
            # If tomorrow's price is higher than today's
            if prices[i] < prices[i + 1]:
                # Capture that profit
                profit += prices[i + 1] - prices[i]
        
        return profit
        