class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        groups = {}

        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i) - ord('a')] += 1

            hash_val = tuple(count)
            if hash_val not in groups:
                groups[hash_val] = []

            groups[hash_val].append(s)

        print(groups)
        for i in groups:
            ans.append(groups[i])
        return ans