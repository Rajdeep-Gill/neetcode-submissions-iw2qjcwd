class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = nums.copy()
        for i in nums:
            new.append(i)

        return new