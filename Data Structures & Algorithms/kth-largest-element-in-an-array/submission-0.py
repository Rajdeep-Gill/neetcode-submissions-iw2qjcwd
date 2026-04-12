class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        for i in range(k - 1):
            a = heapq.heappop_max(nums)

        return heapq.heappop_max(nums)