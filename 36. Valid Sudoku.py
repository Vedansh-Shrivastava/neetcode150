class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        row = [[] for _ in range(n)]
        col = [[] for _ in range(n)]
        box = [[] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == ".":
                    continue

                if val in row[r]:
                    return False
                row[r].append(val)

                if val in col[c]:
                    return False
                col[c].append(val)

                idx = (r//3) * 3 + (c//3)
                if val in box[idx]:
                    return False
                box[idx].append(val)

        return True

