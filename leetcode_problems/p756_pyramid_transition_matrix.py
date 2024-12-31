# You are stacking blocks to form a pyramid.
# Each block has a color, which is represented by a single letter.
# Each row of blocks contains one less block than the row beneath it
#  and is centered on top.
# To make the pyramid aesthetically pleasing,
#  there are only specific triangular patterns that are allowed.
# A triangular pattern consists of a single block stacked on top of two blocks.
# The patterns are given as a list of three-letter strings allowed,
#  where the first two characters of a pattern represent the left
#  and right bottom blocks respectively, and the third character is the top block.
#  - For example, "ABC" represents a triangular pattern with a 'C' block stacked
#    on top of an 'A' (left) and 'B' (right) block. Note that this is different
#    from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
# You start with a bottom row of blocks bottom, given as a single string,
#  that you must use as the base of the pyramid.
# Given bottom and allowed, return true if you can build the pyramid
#  all the way to the top such that every triangular pattern in the pyramid
#  is in allowed, or false otherwise.
# ----------------------
# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
# All the values of allowed are unique.
from functools import cache


def pyramid_transition(bottom: str, allowed: list[str]) -> bool:
    # working_sol (42.17%, 5.41%) -> (4202ms, 199.75mb)  time: O(n ** 2 * k)
    #                                                  | space: O(n ** 2)
    _allowed: set[str] = set(allowed)
    top_blocks: list[str] = [tri_str[-1] for tri_str in allowed]

    @cache
    def check(index: int, level: str, prev_level: str) -> bool:
        # All done == last level builded.
        if 1 == len(prev_level):
            return True
        if len(level) == len(prev_level) - 1:
            return check(0, '', level)
        # We try to build from every index.
        left: int = index
        right: int = index + 1
        can_be_continued: bool = False
        while right < len(prev_level):
            prev_slice: str = prev_level[left: right + 1]
            for top_block in top_blocks:
                if (prev_slice + top_block) in _allowed:
                    can_be_continued = True
                    if check(index + 1, level + top_block, prev_level):
                        return True
                else:
                    can_be_continued = False
            left += 1
            right += 1
            if not can_be_continued:
                break
        return False
        
    return check(0, '', bottom)


# Time complexity: O(n ** 2 * k) <- n - length of the input array `bottom`,
#                                   k - length of the input array `allowed`.
# We start from bottom level == `n`.
# And building every row with checking all options from `allowed` for each index.
# O(n ** 2 * k).
# ----------------------
# Auxiliary space: O(n ** 2)
# Recursion stack is at max == `n - 1` levels.
# And for each level we're building `level` of size `prev_level - 1`.
# Starting from `n` => O(n ** 2).


test_bot: str = "BCD"
test_allowed: list[str] = ["BCC","CDE","CEA","FFF"]
test_out: bool = True
assert test_out == pyramid_transition(test_bot, test_allowed)

test_bot = "AAAA"
test_allowed = ["AAB","AAC","BCD","BBE","DEF"]
test_out = False
assert test_out == pyramid_transition(test_bot, test_allowed)

test_bot = "BDD"
test_allowed = [
    "ACC","AAD","ABB","DAB","DCD","ADA","BBC","CAB",
    "BCA","DDC","BAC","BAA","DDB","CCD","CAA","DBC"
]
test_out = False
assert test_out == pyramid_transition(test_bot, test_allowed)
