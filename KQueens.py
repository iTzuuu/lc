def can_place_k_queens(k):
    """
    Returns a solution (list of column positions) if k queens can be placed on a k x k chessboard so that no two queens attack each other using backtracking.
    Returns None if not possible.
    """
    def is_safe(row, col, queens):
        for r, c in enumerate(queens):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(row, queens):
        if row == k:
            return queens  # Return the solution
        for col in range(k):
            if is_safe(row, col, queens):
                result = solve(row + 1, queens + [col])
                if result:
                    return result
        return None

    return solve(0, [])

if __name__ == "__main__":
    k = int(input("Enter the value of k: "))
    solution = can_place_k_queens(k)
    if solution:
        print(f"Yes, {k} queens can be placed on a {k}x{k} board without attacking each other.")
        print("Positions (row, col):")
        for row, col in enumerate(solution):
            print(f"({row}, {col})")
        # Optional: print the board
        print("\nBoard:")
        for row in range(k):
            line = ['Q' if solution[row] == col else '.' for col in range(k)]
            print(' '.join(line))
    else:
        print(f"No, {k} queens cannot be placed on a {k}x{k} board without attacking each other.")
