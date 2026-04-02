class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort()

        stack = []

        for i in range(len(pairs)-1,-1,-1):
            pos, sp = pairs[i]
            time = (target - pos) / sp
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


