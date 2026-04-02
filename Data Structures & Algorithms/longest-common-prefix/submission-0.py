class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs:
            if len(s) > len(longest):
                i = 0
                while i < len(longest) and longest[i] == s[i]:
                    i+=1
                longest = s[:i]
            else:
                i = 0
                while i < len(s) and longest[i] == s[i]:
                    i+=1
                longest = s[:i]

        return longest