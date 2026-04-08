class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):

            if i == len(s1) and j == len(s2):
                return True

            if i + j >= len(s3):
                return False

            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = False

            if i < len(s1) and s1[i] == s3[i+j]:
                ans = dfs(i+1, j)
            
            if j < len(s2) and s2[j] == s3[i+j]:
                ans = ans or dfs(i, j+1)
            
            dp[(i, j)] = ans
            return ans
        
        return dfs(0, 0)
