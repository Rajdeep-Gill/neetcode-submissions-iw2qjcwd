class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxSum = float("-inf")
        for i in range(len(nums)):
            curr += nums[i]
            maxSum = max(curr, maxSum)

            if curr < 0:
                curr = 0
        
        return maxSum