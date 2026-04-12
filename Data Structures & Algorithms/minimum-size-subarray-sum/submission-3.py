class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        minLen = float('inf')

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                left = nums[l]
                if currSum - left >= target:
                    currSum -= left
                    l += 1
                else:
                    break
            if currSum >= target:
                minLen = min(minLen, (r - l + 1))

        return minLen if currSum >= target else 0