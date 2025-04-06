from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Modifies board in-place to solve the Sudoku puzzle."""
        rows = [0] * 9  # Bitmask for rows
        cols = [0] * 9  # Bitmask for columns
        boxes = [0] * 9  # Bitmask for 3x3 boxes
        empty_cells = []

        # Initialize bitmasks and collect empty cell positions
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = int(board[i][j])
                    bit = 1 << (num - 1)
                    box_index = (i // 3) * 3 + (j // 3)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[box_index] |= bit

        def backtrack(index):
            """Recursive backtracking function to solve Sudoku."""
            if index == len(empty_cells):
                return True  # Solved
            
            i, j = empty_cells[index]
            box_index = (i // 3) * 3 + (j // 3)

            for num in range(1, 10):
                bit = 1 << (num - 1)

                if (rows[i] & bit) or (cols[j] & bit) or (boxes[box_index] & bit):
                    continue  # Number is already used

                # Place number and update bitmasks
                board[i][j] = str(num)
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_index] |= bit

                if backtrack(index + 1):
                    return True  # Solution found

                # Undo changes (backtrack)
                board[i][j] = '.'
                rows[i] &= ~bit
                cols[j] &= ~bit
                boxes[box_index] &= ~bit

            return False  # No valid number found

        backtrack(0)
