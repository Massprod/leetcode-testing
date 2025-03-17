# You are given a positive integer n.
# A binary string x is valid if all substrings of x
#  of length 2 contain at least one "1".
# Return all valid strings with length n, in any order.
# -----------------------
# 1 <= n <= 18


def valid_strings(n: int) -> list[str]:
    # working_sol (97.97%, 52.03%) -> (43ms, 19.20mb)  time: O(2 ** n) | space: O(2 ** n)

    def construct(bstr: str, target: int, bstr_bank: list[str]) -> None:
        if len(bstr) > target:
            return
        if len(bstr) == target:
            bstr_bank.append(bstr)
            return
        if '0' == bstr[-1]:
            construct(bstr + '1', target, bstr_bank)
        if '1' == bstr[-1]:
            construct(bstr + '1', target, bstr_bank)
            construct(bstr + '0', target, bstr_bank)

    
    out: list[str] = []
    starts: list[str] = ['0', '1']
    for start in starts:
        construct(start, n, out)

    return out


# Time complexity: O(2 ** n)
# Recursion with depth == `n` and 2 options => O(2 ** n).
# -----------------------
# Auxiliary space: O(2 ** n)
# `out` <- allocates space for each binaryString we built => O(2 ** n).


test: int = 3
test_out: list[str] = ["010", "011", "101", "110", "111"]
assert set(test_out) == set(valid_strings(test))

test = 1
test_out = ["0", "1"]
assert set(test_out) == set(valid_strings(test))
