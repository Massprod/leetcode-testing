# You are given an integer array digits, where each element is a digit.
# The array may contain duplicates.
# You need to find all the unique integers that follow the given requirements:
#  - The integer consists of the concatenation of three elements
#    from digits in any arbitrary order.
#  - The integer does not have leading zeros.
#  - The integer is even.
# For example, if the given digits were [1, 2, 3],
#  integers 132 and 312 follow the requirements.
# Return a sorted array of the unique integers.
# ------------------------
# 3 <= digits.length <= 100
# 0 <= digits[i] <= 9
from collections import Counter


def find_even_numbers(digits: list[int]) -> list[int]:
    # working_sol (63.18%, 65.57%) -> (55ms, 17.80mb)  time: O(n) | space: O(n)
    out: list[int] = []
    # { digit: occurrences }
    usable: dict[int, int] = Counter(digits)
    # 3 digits => 100 - 999 options.
    for value in range(100, 1000):
        if value % 2:
            continue
        # { digit: occurrences }
        current: dict[int, int] = Counter(str(value))
        can_be_used: bool = True
        for key in current:
            usable_val: int = usable.get(int(key), 0)
            if usable_val and usable_val >= current[key]:
                continue
            can_be_used = False
        if can_be_used:
            out.append(value)
            
    return out


# Time complexity: O(n) <- n - length of the input array `digits`.
# Always traversing whole input array `digits`, to get digit occurrences => O(n).
# ------------------------
# Auxiliary space: O(n).
# In the worst case every digit is unique.
# `usable` <- allocates space for each of them => O(n).


test: list[int] = [2, 1, 3, 0]
test_out: list[int] = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
assert test_out == find_even_numbers(test)

test = [2, 2, 8, 8, 2]
test_out = [222, 228, 282, 288, 822, 828, 882]
assert test_out == find_even_numbers(test)

test = [3, 7, 5]
test_out = []
assert test_out == find_even_numbers(test)
