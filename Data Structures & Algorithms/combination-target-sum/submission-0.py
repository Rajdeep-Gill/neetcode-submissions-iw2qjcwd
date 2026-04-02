class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        combo = []
        total = 0

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(nums) or total > target:
                return

            # use the current number
            combo.append(nums[i]) 
            total += nums[i]
            dfs(i, combo, total) # we do not do i+1 because we can reuse this number

            combo.pop() # remove the current number
            total -= nums[i]
            # we must now skip this number as all combinations with this number have been found
            dfs(i+1, combo, total)

        dfs(0, [], 0)
        return res