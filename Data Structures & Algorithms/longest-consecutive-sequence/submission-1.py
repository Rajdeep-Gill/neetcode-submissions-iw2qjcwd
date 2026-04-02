class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        ans = 0

        for i in nums:
            if i-1 not in nums:
                temp = i
                count = 1
                while temp + 1 in nums:
                    temp += 1
                    count += 1

                ans = max(count, ans)

        return ans