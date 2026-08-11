def solve_sudoku(board):
    """
    Solves a 9x9 Sudoku puzzle represented by a 2D array.
    Modifies the board in-place. Returns True if solved, False otherwise.
    """
    # 1. Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 0 represents an empty cell

                # 2. Try placing digits from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Tentatively place the number

                        # 3. Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # 4. Backtrack if the choice doesn't lead to a solution
                        board[row][col] = 0

                return False  # Trigger backtracking to the previous cell
    return True  # Entire board is filled successfully


def is_valid(board, row, col, num):
    """
    Checks if placing 'num' at board[row][col] is valid according to Sudoku rules.
    """
    # Check the row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check the column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True


def print_board(board):
    """
    Helper function to print the 2D grid beautifully.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j], end=" ")
        print()


# --- Example Usage ---
if __name__ == "__main__":
    # 0 represents blank cells
    sudoku_grid = [
        [0,0,8,0,0,2,0,0,0],
        [3,0,0,0,9,0,0,6,4],
        [6,0,0,0,7,0,2,0,1],

        [0,0,0,3,2,0,0,0,0],
        [4,0,0,0,0,0,0,0,9],
        [0,0,0,0,5,1,0,0,0],

        [9,0,5,0,4,0,0,0,3],
        [7,8,0,0,1,0,0,0,5],
        [0,0,0,5,0,0,4,0,0]
    ]
    # Tarun Bharat SuDuKu 3957

    print("Initial Sudoku Grid:")
    print_board(sudoku_grid)
    print("\nSolving...\n")

    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku Grid:")
        print_board(sudoku_grid)
    else:
        print("No solution exists for this Sudoku configuration.")
