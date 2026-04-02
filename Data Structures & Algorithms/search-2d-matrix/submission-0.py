class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        # first we find the row we want to search in
        row_to_search = -1
        while l < r:
            m = (l+r) // 2
            lrow = matrix[l]
            rrow = matrix[r]
            mrow = matrix[m]
            # check if we are between l row
            if target >= lrow[0] and target <= lrow[-1]:
                row_to_search = l
                l = r
            elif target >= rrow[0] and target <= rrow[-1]:
                row_to_search = r
                l = r
            else:
                # now we have to shift l or r
                if target < mrow[0]:
                    r = m
                elif target > mrow[-1]:
                    l = m+1
                else:
                    row_to_search = m
                    l = r

        row = matrix[row_to_search]
        l, r = 0, len(row) - 1
        while l < r:
            m = (l+r) // 2
            if target == row[m]:
                return True
            if target < row[m]:
                r = m
            elif target > row[m]:
                l = m + 1


        return row[l] == target

