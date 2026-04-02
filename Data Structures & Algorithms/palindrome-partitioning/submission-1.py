class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        substring = []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(substring.copy())
                return

            # if our current substring is a palindrome
            # take it and dfs the rest
            if self.isPali(s, j, i):
                substring.append(s[j:i+1])
                dfs(i+1, i+1) # our new string should start after our current
                substring.pop() # restore state
            dfs(j, i+1)


        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1

        return True
