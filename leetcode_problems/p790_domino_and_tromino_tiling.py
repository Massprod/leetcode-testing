# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large,
#   return it modulo 10 ** 9 + 7.
# In a tiling, every square must be covered by a tile.
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
#   such that exactly one of the tilings has both squares occupied by a tile.
# -------------------
# 1 <= n <= 1000


def num_tilings(n: int) -> int:
    # working_sol (27.24%, 9.18%) -> (56ms, 19.2mb)  time: O(n) | space: O(n)
    recur_cache: dict[tuple[int, bool]: int] = {}

    def place_tiles(index: int, gap: bool) -> int:
        if (index, gap) in recur_cache:
            return recur_cache[index, gap]
        # We stepped out of matrix limit and can't place anything here.
        # We're trying to place Horizontal or Tromino, and cuz we can't
        #  place anything after that index, Gap will never be closed.
        # So its incorrect Path.
        if index > n:
            return 0
        # Correct path.
        if index == n:
            # But if Tromino placed on (n - 1) we will have a Gap,
            #  which can't be closed. We don't have a tile with 1 square size.
            # And Horizontal or other Tromino will be out of limit.
            if gap:
                return 0
            return 1
        ways: int = 0
        if gap:
            # Place Tromino and fill the Gap from prev Index.
            ways += place_tiles(index + 1, False)
            # Place Horizontal and fill the Gap from prev Index,
            #  but create a new one to fill later.
            ways += place_tiles(index + 1, True)
        if not gap:
            # Place Vertical.
            # Only 1 Vertical per index at any time.
            ways += place_tiles(index + 1, False)
            # Place a pair of Horizontals.
            # We can't place 1 Horizontal at any time,
            #  cuz it will create a Gap on prev index.
            # And only way to close this Gap is other Horizontal.
            # So there's no reasons to make this call.
            ways += place_tiles(index + 2, False)
            # Place Tromino and create a Gap,
            #  either on top or bottom side.
            # There's 2 options to place Tromino,
            #  so we can multiply by 2 or make another call.
            ways += place_tiles(index + 2, True)
            ways += place_tiles(index + 2, True)
        # Standard cache.
        recur_cache[index, gap] = ways
        return recur_cache[index, gap]

    return place_tiles(0, False) % (10 ** 9 + 7)


# Time complexity: O(n) -> with memorization it's going to call every index for Vertical and Gap, once => O(2n).
# n - input value^^"|
# Auxiliary space: O(n) -> for every index from 0 to n inclusive at least one Vertical will be placed,
#                          which is equal to n calls and all of them saved => O(n) -> calls for other options
#                          with Gap is extra n => O(n) -> O(2n) => O(n).
#                          Tested with cache.keys() in almost all cases their x2 of n.
# -------------------
# We need to count all the ways to place dominos.
# Made visual to see it more clearly, but we have like 3 options without a Gap and extra 2 options with a Gap.
# Gap can be made only after placing Tromino, at least Gap which can be filled correctly.
# Incorrect Gap can be made with 1 Horizontal, and then there's only one way to fill it its place another Horizontal.
# So we never do this, and always placing 2 Horizontals at the same time.
# But Gaps from Tromino can be closed with another Tromino and leave no Gap after, or Horizontal and leave a Gap.
# Which needs to be closed later, so we always maintain trigger on Gap -> Closed or Opened.


test: int = 3
test_out = 5
assert test_out == num_tilings(test)

test = 1
test_out = 1
assert test_out == num_tilings(test)

test = 144
test_out = 732742205
assert test_out == num_tilings(test)
