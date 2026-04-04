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

            # take 1 step
            step1 = dfs(curr+1)
            step2 = dfs(curr+2)
            dp[curr] = step1 + step2
            return dp[curr]

        return dfs(0)