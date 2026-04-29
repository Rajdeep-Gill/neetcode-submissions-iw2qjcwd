class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = [] # (start, end)
        intervals.sort()
        for i in range(len(intervals)):
            start, end = intervals[i]

            while stack and stack[-1][1] >= start:
                stackStart, stackEnd = stack.pop()
                start = min(start, stackStart)
                end = max(end, stackEnd)
            
            stack.append([start, end])

        return stack