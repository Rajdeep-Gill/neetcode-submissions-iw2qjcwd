class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (character, count)

        for c in s:
            count = 1

            if stack and stack[-1][0] == c:
                char, prevCount = stack.pop()
                if prevCount + 1 == k:
                    continue

                count = prevCount + 1                    

            stack.append((c, count))

        ans = ""
        while stack:
            c, times = stack.pop()
            ans = c * times + ans
        return ans