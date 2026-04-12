class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            elif s[r] in seen:
                while s[r] in seen and l < r:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1

            longest = max(longest, len(seen))
        
        return longest