class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1

        while r >=0 and nums[r] == val:
            r -= 1

        l = 0
        while l < r:
            print(l, r, nums)
            while nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            while nums[r] == val:
                r -= 1
            print(l, r, nums)
            l += 1

        return r+1