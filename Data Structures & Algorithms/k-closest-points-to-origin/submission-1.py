class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i in range(len(points)):
            x, y = points[i]

            dist = x**2 + y**2

            heapq.heappush(heap, (dist, i))

        ans = []
        for i in range(k):
            _, index = heapq.heappop(heap)
            ans.append(points[index])

        return ans