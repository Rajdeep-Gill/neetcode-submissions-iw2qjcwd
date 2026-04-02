class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            bucket[idx] += 1
        
        for i in t:
            idx = ord(i) - ord('a')
            if bucket[idx] == 0:
                return False
            bucket[idx] -= 1

        for i in bucket:
            if i != 0:
                return False

        return True
        
