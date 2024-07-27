# You are given a string s consisting of lowercase English letters, and an integer k.
# First, convert s into an integer by replacing each letter with its position
#  in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
# Then, transform the integer by replacing it with the sum of its digits.
# Repeat the transform operation k times in total.
# For example, if s = "zbax" and k = 2, then the resulting integer
#  would be 8 by the following operations:
#  - Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
#  - Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
#  - Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.
# ---------------------
# 1 <= s.length <= 100
# 1 <= k <= 10
# s consists of lowercase English letters.


def get_lucky(s: str, k: int) -> int:
    # working_sol (99.80%, 90.91%) -> (23ms, 16.38mb)  time: O(s * k)  | space: O(s)
    nums: list[str] = []
    for char in s:
        nums.append(str(ord(char) - 96))  # 96 <- cuz we need 1-indexed
    value: str = ''.join(nums)
    while k:
        cur_sum: int = 0
        for digit in value:
            cur_sum += int(digit)
        value = str(cur_sum)
        k -= 1
    return int(value)


# Time complexity: O(s * k)
# Always traversing whole `s` to get all `num` values of chars => O(s).
# We can every `num` become (2 * char) like z -> 26,
#  so we extra `join` `2 * s` and traverse it for `k` times => O(s * k).
# ---------------------
# Auxiliary space; O(s).
# `nums` <- will be x2 of `s` => O(2 * s).
# `value` <- joined `nums` => O(4 * s).


test: str = "iiii"
test_k: int = 1
test_out: int = 36
assert test_out == get_lucky(test, test_k)

test = "leetcode"
test_k = 2
test_out = 6
assert test_out == get_lucky(test, test_k)

test = "zbax"
test_k = 2
test_out = 8
assert test_out == get_lucky(test, test_k)
