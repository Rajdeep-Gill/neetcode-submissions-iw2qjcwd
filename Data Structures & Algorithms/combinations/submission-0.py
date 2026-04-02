class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        combo = []

        def dfs(start):
            if len(combo) == k:
                ans.append(combo.copy())
                return

            
            # we add the number from start
            for i in range(start, n+1):
                combo.append(i)
                dfs(i+1)
                combo.pop()

        dfs(1)
        return ans