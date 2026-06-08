# You are given an integer n.
# Return true if its binary representation contains exactly one pair
#  of consecutive set bits, and false otherwise.
# --- --- --- ---
# 0 <= n <= 10 ** 5


def consecutive_set_bits(n: int) -> bool:
    # working_solution: (100%, 100%) -> (4ms, 19.35mb)  Time: O(n) Space: O(n)
    bin_n: str = bin(n)
    out: int = 0
    for index in range(1, len(bin_n)):
        if '1' == bin_n[index] and bin_n[index] == bin_n[index - 1]:
            out += 1
    return 1 == out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: int = 6
test_out: bool = True
assert test_out == consecutive_set_bits(test)

test = 3
test_out = False
assert test_out == consecutive_set_bits(test)
