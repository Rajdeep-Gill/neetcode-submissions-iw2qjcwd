class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""

        stack = []

        for c in s:
            if c == "]":
                # now pop till we have "["
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                val = ""
                while stack and stack[-1].isnumeric():
                    val += stack.pop()

                val = int(val[::-1])

                stack.append(temp * val)
            else:
                stack.append(c)

        return "".join(stack)