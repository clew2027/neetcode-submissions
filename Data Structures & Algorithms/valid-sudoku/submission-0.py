class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                elm = board[r][c]

                if elm == ".":
                    continue

                # Check row
                if elm in rows[r]:
                    return False
                rows[r].add(elm)

                # Check column
                if elm in cols[c]:
                    return False
                cols[c].add(elm)

                # Check 3x3 box
                box = (r // 3) * 3 + (c // 3)

                if elm in boxes[box]:
                    return False
                boxes[box].add(elm)

        return True