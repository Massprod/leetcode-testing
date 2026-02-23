# Given a binary string s and an integer k, return true if every binary code
#  of length k is a substring of s. Otherwise, return false.
# --- --- --- ---
# 1 <= s.length <= 5 * 10 ** 5
# s[i] is either '0' or '1'.
# 1 <= k <= 20


def has_all_codes(s: str, k: int) -> bool:
    # working_solution: (37.78%, 82.89%) -> (275ms, 44.10mb)  Time: O(s) Space: O(s ** 2)
    # All uniq subs should be equal to `2 ** k`.
    # Binary and we need uniques combos => 2 ** k.
    mask: int = (1 << k) - 1  # -1 <- shift all `0` to `1`.
    index: int = k
    sub: int = int(s[:k], base=2)
    uniques: set[int] = {sub}
    while index < len(s):
        sub = ((sub << 1) & mask) | (s[index] == "1")
        index += 1
        uniques.add(sub)

    return 2 ** k == len(uniques)


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s ** 2)
# In the worst case, only unique subs and we store all of them in the `uniques`.


test: str = "00110110"
test_k: int = 2
test_out: bool = True
assert test_out == has_all_codes(test, test_k)

test = "0110"
test_k = 1
test_out = True
assert test_out == has_all_codes(test, test_k)

test = "0110"
test_k = 2
test_out = False
assert test_out == has_all_codes(test, test_k)
