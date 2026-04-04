class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}

        def dfs(curr):
            if curr == 0:
                return 0
            if curr == 1:
                return 1
            if curr == 2:
                return 1

            if curr in dp:
                return dp[curr]

            new = dfs(curr-3) + dfs(curr-2) + dfs(curr-1)
            dp[curr] = new
            return new

        return dfs(n)