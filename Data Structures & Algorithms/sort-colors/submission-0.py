class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0
        for i in nums:
            if i == 0:
                r+=1
            if i == 1:
                w += 1
            if i == 2:
                b += 1
        print(r, w, b)
        for i in range(r):
            nums[i] = 0
        for i in range(r, r+w):
            nums[i] = 1
        for i in range(r+w, r+w+b):
            nums[i] = 2

        