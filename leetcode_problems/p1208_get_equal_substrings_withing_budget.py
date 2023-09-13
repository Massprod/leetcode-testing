# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t.
# Changing the ith character of s to ith character of t costs |s[i] - t[i]|
# (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same
#  as the corresponding substring of t with a cost less than or equal to maxCost.
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.
# -------------------------
# 1 <= s.length <= 10 ** 5
# t.length == s.length
# 0 <= maxCost <= 10 ** 6
# s and t consist of only lowercase English letters.
from collections import deque
from random import choice
from string import ascii_lowercase


def equal_substring(s: str, t: str, maxCost: int) -> int:
    # working_sol (98.58%, 57.45%) -> (55ms, 17.1mb)  time: O(n) | space: O(n)
    # Standard sliding_window.
    max_len: int = 0
    cur_len: int = 0
    used_costs: deque[int] = deque()
    index: int = 0
    cur_cost: int = 0
    # ! t.length == s.length !
    # Expand while we can, and shrink when cost is over limit.
    while index != len(s):
        change_cost: int = abs(ord(s[index]) - ord(t[index]))
        used_costs.append(change_cost)
        cur_cost += change_cost
        index += 1
        cur_len += 1
        if cur_cost <= maxCost:
            max_len = max(max_len, cur_len)
            continue
        while cur_cost > maxCost:
            cur_cost -= used_costs.popleft()
            cur_len -= 1
    return max_len


# Time complexity: O(n) -> worst case == every symbol exceeds maxCost, so we will extra popleft() for every index ->
# n - len of any input_string^^| -> every index will be used twice => O(2n).
# Auxiliary space: O(n) -> worst case == maxCost > than price to change everything -> then for every index(symbol)
#                          we wil store it's change_cost => O(n).


test_s: str = "abcd"
test_t: str = "bcdf"
test_max_cost: int = 3
test_out: int = 3
assert test_out == equal_substring(test_s, test_t, test_max_cost)

test_s = "abcd"
test_t = "cdef"
test_max_cost = 3
test_out = 1
assert test_out == equal_substring(test_s, test_t, test_max_cost)

test_s = "abcd"
test_t = "acde"
test_max_cost = 0
test_out = 1
assert test_out == equal_substring(test_s, test_t, test_max_cost)

test_s = "fdjbatpfupfbjsydcehnhewpiuwhdhgxafnpghvyfrxoibqxkvhxayikknionkxolfibduiykcyejzfytlsxzdnpfpalxnrrtwev"
test_t = "kbvrqvlixbscwfeghpkuecwbxyzuzsojdfyuorcglzfvhbtpbvuhgeeenmsxzenddrmzgkrisksqnlnbbypuqvvirgxmufpicrwe"
test_max_cost = 11
test_out = 4
assert test_out == equal_substring(test_s, test_t, test_max_cost)

test_s = "gzpayfagtgejplvzwzdpdgxvb"
test_t = "reairbzliapyvplkjityvctol"
test_max_cost = 25
test_out = 4
assert test_out == equal_substring(test_s, test_t, test_max_cost)

test_s = ''.join([choice(ascii_lowercase) for _ in range(1000)])
test_t = ''.join([choice(ascii_lowercase) for _ in range(1000)])
print(test_s)
print(test_t)
