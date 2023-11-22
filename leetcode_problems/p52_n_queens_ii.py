# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
#  such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
# -------------------------
# 1 <= n <= 9


def total_n_queens(n: int) -> int:
    # working_sol (89.54%, 57.84%) -> (43ms, 16.28mb)  time: O(n!) | space: O(n)

    def place(queens: int, cols_taken: set[int], asc_taken: set[int], desc_taken: set[int]) -> int:
        """
        Backtracking for Queens safe placements.
        :param queens: number of rows with already placed Queens OR current row we're trying to place on.
        :param cols_taken: all columns on which we already placed Queens.
        :param asc_taken: all ascending diagonals on which we already placed Queens.
        :param desc_taken: all descending diagonals on which we already placed Queens.
        :return: Number of ways we can place Queens safely.
        """
        if queens == n:
            return 1
        out: int = 0
        # On every row|col we can place only 1 queen, so queens == rows used.
        for col in range(n):
            if col not in cols_taken:
                # Every ascending diagonal in matrix have same (row + col) values.
                ascending: int = queens + col
                # Every descending have same (row - col) values.
                descending: int = queens - col
                # Queens can move on columns + rows + diagonals.
                if ascending not in asc_taken and descending not in desc_taken:
                    cols_taken.add(col)
                    asc_taken.add(ascending)
                    desc_taken.add(descending)
                    out += place(queens + 1, cols_taken, asc_taken, desc_taken)
                    cols_taken.remove(col)
                    asc_taken.remove(ascending)
                    desc_taken.remove(descending)
        return out

    return place(0, set(), set(), set())


# Time complexity: O(n!) -> no idea, it's easy to do but complexity is overwhelming ->
#                         -> maybe, O(n!)? like we're not calling for every column but still calculating
#                         diagonals and check them for every not taken column, and because at max we can do 'n' calls
#                         with every call we will have -1 column option ->
#                         -> so, it's like (n-1, n-2, n-3 ... 0).
#                         But for (n == 9) there's only 8394 recursion calls and 72378 column checks.
#                         When 9! is actually 362880.
# Auxiliary space: O(n) -> 'cols_taken' with all columns taken (n) -> both ascending and descending sets
#                          will store 2 * (2 * n - 1) diagonals stored => O(n + 2 * (2 * n - 1)).
#                          Or without recursion diving, we can just say O(n), because depth == n.


test: int = 4
test_out: int = 2
assert test_out == total_n_queens(test)

test = 1
test_out = 1
assert test_out == total_n_queens(test)

test = 9
test_out = 352
assert test_out == total_n_queens(test)
