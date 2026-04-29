class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, need):
            if i == len(nums):
                return need == 0
            
            if (i, need) in dp:
                return dp[(i, need)]

            # we can add or subtract each number
            ways = dfs(i + 1, need - nums[i]) + dfs(i+1, need + nums[i])
            dp[(i, need)] = ways
            return ways
        return dfs(0, target)