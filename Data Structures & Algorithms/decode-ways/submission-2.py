class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def dfs(curr):
            if curr == "":
                return 1
            if curr in dp:
                return dp[curr]
            
            if curr[0] == '0':
                return 0
            
            # Option 1: Take one digit
            ways = dfs(curr[1:])
            
            # Option 2: Take two digits
            if len(curr) >= 2 and int(curr[:2]) <= 26:
                ways += dfs(curr[2:])
            
            dp[curr] = ways
            return ways

        return dfs(s)