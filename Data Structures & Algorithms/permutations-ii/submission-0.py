class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        perm = []
        ans = []

        def dfs():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    perm.append(num)
                    dfs()
                    perm.pop()
                    count[num] += 1

        dfs()
        return ans