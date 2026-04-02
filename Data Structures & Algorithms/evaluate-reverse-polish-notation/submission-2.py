class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = set(["+", "-", "*", "/"])

        stack = []

        for i in tokens:
            if i in operations:
                n = int(stack.pop())
                m = int(stack.pop())
                if i == "+":
                    stack.append(n + m)
                if i == "*":
                    stack.append(n*m)
                if i == "-":
                    stack.append(m-n)
                if i == "/":
                    stack.append(m/n)
            else:
                stack.append(i)

        return int(stack.pop())

    