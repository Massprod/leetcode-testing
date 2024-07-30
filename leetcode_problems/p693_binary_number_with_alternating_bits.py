# Given a positive integer, check whether it has alternating bits:
#  namely, if two adjacent bits will always have different values.
# ----------------------
# 1 <= n <= 2 ** 31 - 1


def has_alternating_bits(n: int) -> bool:
    # working_sol (93.87%, 51.29%) -> (27ms, 16.43mb)  time: O(n) | space: O(1)
    start_bit: int = n & 1
    while n:
        cur_bit: int = n & 1
        if cur_bit == start_bit:
            start_bit = 0 if start_bit else 1
        else:
            return False
        n >>= 1
    return True


# Time complexity: O(n).
# Always depleting `n` and checking every digit it has => O(n).
# ----------------------
# Auxiliary space: O(1).
# Always using only 2 constant INT's, none of them depends on input => O(1).


test: int = 5
test_out: bool = True
assert test_out == has_alternating_bits(test)

test = 7
test_out = False
assert test_out == has_alternating_bits(test)

test = 11
test_out = False
assert test_out == has_alternating_bits(test)
