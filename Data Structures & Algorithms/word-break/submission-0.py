class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(start):
            if start == len(s):
                return True

            if start in dp:
                return dp[start]

            for i in range(start, len(s)):
                sub = s[start:i+1]
                if sub in wordDict and dfs(i+1):
                    dp[start] = True
                    return True

            dp[start] = False
            return False
        return dfs(0)