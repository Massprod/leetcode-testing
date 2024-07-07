# You're given strings jewels representing the types of stones that are jewels,
#  and stones representing the stones you have.
# Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# -----------------------
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    # working_sol (87.38%, 93.66%) -> (30ms, 16.38mb)  time: O(n + m) | space: O(n)
    pretty: set[str] = set(jewels)
    out: int = 0
    for stone in stones:
        if stone in pretty:
            out += 1
    return out


# Time complexity: O(n + m) <- n - length of the input string `jewels`, m - length of the input string `stores`.
# Always traversing both input arrays, once => O(n + m).
# -----------------------
# Auxiliary space: O(n)
# In the worst case, every char in `jewels` are unique => O(n).


test_jewels: str = "aA"
test_stones: str = "aAAbbbb"
test_out: int = 3
assert test_out == num_jewels_in_stones(test_jewels, test_stones)

test_jewels = "z"
test_stones = "ZZ"
test_out = 0
assert test_out == num_jewels_in_stones(test_jewels, test_stones)
