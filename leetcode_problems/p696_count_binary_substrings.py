# Given a binary string s, return the number of non-empty substrings
#  that have the same number of 0's and 1's,
#  and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s[i] is either '0' or '1'.


def count_binary_substrings(s: str) -> int:
    # working_solution: (23.04%, 16.04%) -> (82ms, 19.89mb)  Time: O(s) Space: O(s)
    # Gather all consecutive groups.
    groups: list[int] = [1]
    for index in range(1, len(s)):
        if s[index - 1] == s[index]:
            groups[-1] += 1
        else:
            groups.append(1)
    # We have all consecutive `0` and `1` in groups.
    # And we can easily build from it the mannner:
    # '1110000' -> '_1100__' -> `__10___` -> `_______`
    out: int = 0
    for index in range(1, len(groups)):
        out += min(groups[index], groups[index - 1])

    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "00110011"
test_out: int = 6
assert test_out == count_binary_substrings(test)

test = "10101"
test_out = 4
assert test_out == count_binary_substrings(test)
