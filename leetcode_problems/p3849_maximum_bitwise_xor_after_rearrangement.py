# You are given two binary strings s and t​​​​​​​, each of length n.
# You may rearrange the characters of t in any order, but s must remain unchanged.
# Return a binary string of length n representing the maximum integer value obtainable
#  by taking the bitwise XOR of s and rearranged t.
# --- --- --- ---
# 1 <= n == s.length == t.length <= 2 * 10 ** 5
# s[i] and t[i] are either '0' or '1'.


def maximum_xor(s: str, t: str) -> str:
    # working_solution: (9.07%, 11.03%) -> (974ms, 24.55mb)  Time: O(s) Space: O(s)
    cur_val: int
    # [zeroes, onex]
    count: list[int] = [0, 0]
    for value in t:
        cur_val = int(value)
        if 0 == int(value):
            count[0] += 1
        else:
            count[1] += 1
    # More left sided -> higher the INT
    out: list[str] = []
    for value in s:
        cur_val = int(value)
        if 0 < count[1] and 0 == cur_val:
            out.append('1')
            count[1] -= 1
        elif 0 < count[0] and 1 == cur_val:
            out.append('1')
            count[0] -= 1
        else:
            out.append('0')
    
    str_out: str = ''.join(out)
    return str_out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test_s: str = "101"
test_t: str = "011"
test_out: str = "110"
assert test_out == maximum_xor(test_s, test_t)

test_s = "0110"
test_t = "1110"
test_out = "1101"
assert test_out == maximum_xor(test_s, test_t)

test_s = "0101"
test_t = "1001"
test_out = "1111"
assert test_out == maximum_xor(test_s, test_t)
