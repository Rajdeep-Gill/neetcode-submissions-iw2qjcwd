class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sorted_words = ["".join(sorted(i)) for i in strs]
        print(sorted_words)
        grouped = {}

        for i, word in enumerate(sorted_words):
            if word not in grouped:
                grouped[word] = []
            grouped[word].append(strs[i])

        for i in grouped:
            ans.append(grouped[i])

        return ans