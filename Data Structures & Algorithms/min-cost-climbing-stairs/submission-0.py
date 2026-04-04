class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start at 0 or 1
        # each time we go 1 or 2 up
        # we pay that cost

        dp = {} # stair -> cost

        def dfs(i):
            # ith stair
            if i >= len(cost):
                return 0

            if i in dp:
                return dp[i]

            newcost = cost[i] + min(dfs(i+1), dfs(i+2))
            dp[i] = newcost
            return newcost

        return min(
            dfs(0),
            dfs(1)
        )