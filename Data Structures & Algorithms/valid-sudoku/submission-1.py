class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[i][j]
                if curr in seen and curr != ".":
                    return False
                seen.add(curr)
        # check all cols
        for i in range(9):
            seen = set()
            for j in range(9):
                curr = board[j][i]
                if curr in seen and curr != ".":
                    return False
                seen.add(curr)

        seen_box = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()],
        ] # holds sets for each of the 9 boxes
        for i in range(9):
            for j in range(9):
                box_i, box_j = i // 3, j // 3
                curr = board[j][i]
                if curr in seen_box[box_i][box_j] and curr != ".":
                    print('returning false')
                    return False
                seen_box[box_i][box_j].add(curr)

        
        return True