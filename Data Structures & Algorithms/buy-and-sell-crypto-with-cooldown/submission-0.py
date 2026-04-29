class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def best(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = best(i + 1, buying)
            if buying:
                buy = best(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = best(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
            
        return best(0, True)