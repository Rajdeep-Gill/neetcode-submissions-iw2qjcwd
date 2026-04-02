class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            need = target - nums[i]
            print(pairs)

            if need in pairs:
                return [pairs[need], i]
            pairs[nums[i]] = i

        