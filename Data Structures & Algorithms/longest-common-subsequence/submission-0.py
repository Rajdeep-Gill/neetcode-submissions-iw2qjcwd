class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            ans = 0
            if text1[i] == text2[j]:
                ans = 1 + lcs(i + 1, j + 1)
            else:
                ans = max(lcs(i, j+1), lcs(i+1, j))
            
            dp[(i, j)] = ans
            return ans

        return lcs(0, 0)