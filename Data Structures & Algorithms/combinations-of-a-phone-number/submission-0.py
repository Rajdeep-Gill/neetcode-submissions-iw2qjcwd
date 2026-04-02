class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        char_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        def dfs(i, curr_str):
            if i == len(digits):
                res.append(curr_str)
                return

            combos = char_map[digits[i]]
            for c in combos:
                dfs(i+1, curr_str + c)

        if digits == "":
            return []
        dfs(0, "")
        return res