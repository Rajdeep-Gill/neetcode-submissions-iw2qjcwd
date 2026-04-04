class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {} # steps left -> ways to end

        def dfs(curr):
            if curr > n :
                return 0
            if curr == n:
                return 1
            if curr in dp:
                return dp[curr]
                
            dp[curr] = dfs(curr+1) + dfs(curr+2)
            return dp[curr]

        return dfs(0)