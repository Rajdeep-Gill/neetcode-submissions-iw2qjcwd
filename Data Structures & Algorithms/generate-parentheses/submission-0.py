class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        pattern = []

        def dfs(open_b, closed_b):
            if len(pattern) == 2 * n:
                res.append("".join(pattern))
                return
            
            # if we have equal open and closed
            #we can only add an open char
            if open_b <= closed_b and open_b < n:
                pattern.append("(")
                dfs(open_b + 1, closed_b)
                pattern.pop()
            else:
                # we can add both open and closed
                if open_b < n:
                    pattern.append("(")
                    dfs(open_b+1, closed_b)
                    pattern.pop()
                if closed_b < n:
                    pattern.append(")")
                    dfs(open_b, closed_b+1)
                    pattern.pop()

        dfs(0, 0)
        return res
