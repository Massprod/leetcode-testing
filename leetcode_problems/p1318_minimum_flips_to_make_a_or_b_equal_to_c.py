# Given 3 positives numbers a, b and c. Return the minimum flips required
#   in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0
#   or change the bit 0 to 1 in their binary representation.
# ------------------
# 1 <= a <= 10 ** 9
# 1 <= b <= 10 ** 9
# 1 <= c <= 10 ** 9


def min_flips(a: int, b: int, c: int) -> int:
    # working_sol (81.97%, 74.81%) -> (37ms, 16.2mb)  time: O(n) | space: O(1)
    mask: int = 1
    flips: int = 0
    while a or b or c:
        # Reset for every new check.
        # Extra if any number is exhausted == 0.
        # Then every bit is 0, and we need them False anyway.
        a_one: bool = False
        b_one: bool = False
        c_one: bool = False
        # If LSB is 1, marking True.
        if mask & a:
            a_one = True
        # Shifting this bit.
        a = a >> 1
        # Same approach for b, c.
        if mask & b:
            b_one = True
        b = b >> 1
        if mask & c:
            c_one = True
        c = c >> 1
        # If LSB of 'c' is 1, only one of the 'a' or 'b'
        # should have LSB == 1.
        if c_one:
            if not a_one and not b_one:
                flips += 1
            continue
        # Otherwise both of them.
        if a_one:
            flips += 1
        if b_one:
            flips += 1
    return flips


# Time complexity: O(n) -> trying to take LSB of a, b or c until all of them are exhausted ->
# n - max of a,b,c^^|  -> so it's max(a, b, c) => O(max(a, b, c)) => O(n).
# Auxiliary space: O(1) -> only constants used, none of them depends on input => O(1).
# ------------------
# No idea about fast approach if there is some. But we can just save a bit representation of 'a', 'b' and 'c'.
# And check what bits needs to be switching for correct OR on 'a' and 'b'.
# Wait, can we just check if LSB is 1 on all 3 of them, and if 'a', 'b' and 'c' are 1 then we don't need to flip.
# If LSB -> 'a' == 0, 'b' == 1 and 'c' == 1, switch == 1.
# If LSB -> 'a' == 0, 'b' == 1 and 'c' == 0, switch == 0.
# And when 'a' or 'b' exhausted there's only 0 bits left, and we can treat them as 0.
# This should be better. But if 'c' is shorted than 'a' or 'b'?
# Then I would need to flip all 'a' and 'b' bits left to 0. Switch +2 for every pair(a==1, b==1) left?
# Should be correct.


test_a: int = 2
test_b: int = 6
test_c: int = 5
test_out: int = 3
assert test_out == min_flips(test_a, test_b, test_c)

test_a = 4
test_b = 2
test_c = 7
test_out = 1
assert test_out == min_flips(test_a, test_b, test_c)

test_a = 1
test_b = 2
test_c = 3
test_out = 0
assert test_out == min_flips(test_a, test_b, test_c)
