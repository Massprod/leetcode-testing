# The value of an alphanumeric string can be defined as:
#  - The numeric representation of the string in base 10, if it comprises of digits only.
#  - The length of the string, otherwise.
# Given an array strs of alphanumeric strings,
#  return the maximum value of any string in strs.
# -------------------------
# 1 <= strs.length <= 100
# 1 <= strs[i].length <= 9
# strs[i] consists of only lowercase English letters and digits.


def maximum_value(strs: list[str]) -> int:
    # working_sol (85.86%, 25.06%) -> (32ms, 16.54mb)  time: O(s * k) | space: O(1)
    out: int = 0
    for word in strs:
        if word.isnumeric():
            out = max(out, int(word))
        else:
            out = max(out, len(word))
    return out


# Time complexity: O(s * k) <- s - length of the input array `strs`, k - average length of word inside `strs`.
# In the worst case, there's only digits in every word of `strs`.
# Always traversing all words from `strs`, and every char in them => O(s * k).
# -------------------------
# Auxiliary space: O(1)


test: list[str] = ["alic3", "bob", "3", "4", "00000"]
test_out: int = 5
assert test_out == maximum_value(test)

test = ["1", "01", "001", "0001"]
test_out = 1
assert test_out == maximum_value(test)
