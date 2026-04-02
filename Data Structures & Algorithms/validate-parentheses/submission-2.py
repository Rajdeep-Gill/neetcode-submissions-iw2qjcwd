class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = set(["(", "{", "["])
        closed_set = set([']', '}', ')'])
        mapping = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for i in s:
            if i in open_set:
                stack.append(i)
            if i in closed_set:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if mapping[last] != i:
                    return False

        return len(stack) == 0