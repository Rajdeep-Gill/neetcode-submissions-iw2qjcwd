class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            stack.append(c)
            # if curr letter is repeated
            i = len(stack) - 1
            repeats = 0
            while stack and i > - 1 and stack[i] == c and repeats < k:
                repeats += 1
                i -= 1
            if repeats == k:
                while stack and repeats != 0:
                    stack.pop()
                    repeats -= 1

        return "".join(stack)