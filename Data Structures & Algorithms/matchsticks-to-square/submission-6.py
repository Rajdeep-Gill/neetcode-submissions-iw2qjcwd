class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target = total // 4
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)

        def dfs(i, n, s, e, w):
            if n > target or s > target or e > target or w > target:
                return False
            if n == s == e == w and i == len(matchsticks):
                return True

            if i == len(matchsticks):
                return False

            curr = matchsticks[i]
            ans = (
                dfs(i+1, n+curr, s, e, w) or
                dfs(i+1, n, s + curr, e, w) or
                dfs(i+1, n, s, e + curr, w) or
                dfs(i+1, n, s, e, w + curr)
            )
            return ans

        return dfs(0, 0, 0, 0, 0)
        