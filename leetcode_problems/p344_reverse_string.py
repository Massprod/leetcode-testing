# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# ----------------------
# 1 <= s.length <= 10 ** 5
# s[i] is a printable ascii character.


def reverse_string(s: list[str]) -> None:
    # working_sol (91.20%, 80.05%) -> (164ms, 20.79mb)  time: O(n) | space: O(1)
    left: int = 0
    right: int = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Time complexity: O(n) <- n - length of input array `s`.
# Worst case: we have even length, so we will use all indexes.
# ----------------------
# Auxiliary space: O(1)


test: list[str] = ["h", "e", "l", "l", "o"]
test_out: list[str] = ["o", "l", "l", "e", "h"]
reverse_string(test)
assert test_out == test

test = ["H", "a", "n", "n", "a", "h"]
test_out = ["h", "a", "n", "n", "a", "H"]
reverse_string(test)
assert test_out == test
