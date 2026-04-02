class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # we append the i'th value
            # dfs (i + 1)
            # then we remove the i'th value
            # then increment i until we are at a new value
            # that is curr != last
            # then build from there

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            # then we remove the i'th value
            # then increment i until we are at a new value
            new_start = i + 1
            while new_start < len(nums) and nums[new_start] == nums[i]:
                new_start += 1
            
            dfs(new_start)

        dfs(0)
        return res
