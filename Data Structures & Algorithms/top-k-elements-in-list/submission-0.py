class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for i in range(len(nums) + 1)] # we can have atmost n repeated numbers
        # buckets will track bucket[count] = all numbers with that count

        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        for i in counts:
            buckets[counts[i]].append(i)


        ans = []
        l = len(nums) - 1
        while k > 0:
            curr = buckets[l]
            for i in curr:
                ans.append(i)
                k -= 1
            l -= 1
            
        return ans