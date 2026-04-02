class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        # we have:
        # <length>#<string><length>#<string> ...

        ans = []

        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            count = int(s[l:r])

            l = r+1
            r = l+count

            string = s[l:r]
            ans.append(string)
            l = r
        return ans
