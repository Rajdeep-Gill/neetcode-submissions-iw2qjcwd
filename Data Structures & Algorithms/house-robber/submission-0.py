class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {} # money from robbing ith house

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in dp:
                return dp[i]

            new = max(nums[i] + dfs(i+2), dfs(i+1))
            dp[i] = new
            return new

        return dfs(0)

