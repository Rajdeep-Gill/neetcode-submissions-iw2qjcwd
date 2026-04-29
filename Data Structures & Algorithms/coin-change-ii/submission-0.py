class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, need):
            if i == len(coins):
                return 0
            if need < 0 :
                return 0
            if need == 0:
                return 1
            if (i, need) in dp:
                return dp[(i, need)]

            # so we can tak ethe current coin or skip it
            ways = dfs(i, need - coins[i]) + dfs(i+1, need)
            dp[(i, need)] = ways
            return ways
            
        return dfs(0, amount)