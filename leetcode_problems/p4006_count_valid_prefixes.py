# You are given a binary string s.
# A prefix of s is considered valid if its characters
#  can be rearranged to form an alternating string.
# Return the number of valid prefixes of s.
# A string is considered alternating if no two adjacent characters are equal.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists only of '0' and '1'.


def count_valid_prefixes(s: str) -> int:
    # working_solution: (100%, 40%) -> (0ms, 19.27mb)  Time: O(s) Space: O(1)
    out: int = 0
    pref_o: int = 0
    pref_i: int = 0

    for char in s:
        if '1' == char:
            pref_i += 1
        else:
            pref_o += 1
        out += 1 if abs(pref_i - pref_o) <= 1 else 0

    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = "00101"
test_out: int = 3
assert test_out == count_valid_prefixes(test)

test = "101"
test_ouut = 3
assert test_out == count_valid_prefixes(test)
