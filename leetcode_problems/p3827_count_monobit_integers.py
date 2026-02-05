# You are given an integer n.
# An integer is called Monobit if all bits in its binary representation are the same.
# Return the count of Monobit integers in the range [0, n] (inclusive).
# --- --- --- ---
# 0 <= n <= 1000


def count_monobit(n: int) -> int:
    # working_solution: (9.77%, 66.29%) -> (139ms, 19.40mb)  Time: O(n * k) Space: O(1)
    # 0 - is always there.
    out: int = 1
    uniques: set[str] = set()
    for val in range(1, n + 1):
        bin_rep: str = bin(val)[2:]
        for char in bin_rep:
            if 1 < len(uniques):
                break
            uniques.add(char)
        if 1 == len(uniques):
            out += 1
        uniques.clear()

    return out


# Time complexity: O(n * k)
# k - length of the binary representations
# --- --- --- ---
# Space complexity: O(1)


test: int = 1
test_out: int = 2
assert test_out == count_monobit(test)

test = 4
test_out = 3
assert test_out == count_monobit(test)
