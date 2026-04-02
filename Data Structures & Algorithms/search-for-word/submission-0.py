class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, j, x):
            if x == len(word):
                return True

            if i < 0 or i >= rows:
                return False
            if j < 0 or j >= cols:
                return False
            if board[i][j] != word[x]:
                return False
            if (i, j) in visited:
                return False

            visited.add((i, j))
            res = (
                dfs(i+1, j, x+1) or
                dfs(i, j+1, x+1) or
                dfs(i-1, j, x+1) or
                dfs(i, j-1, x+1)
            )
            visited.remove((i, j))
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False