# You are given a binary string s.
# You can perform the following operation on the string any number of times:
# Choose any index i from the string where i + 1 < s.length such that s[i] == '1'
#  and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string
#  or another '1'. For example, for s = "010010", if we choose i = 1,
#  the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s[i] is either '0' or '1'.


def max_operations(s: str) -> int:
    # working_solution: (22.75%, 81.44%) -> (87ms, 18.08mb)  Time: O(s) Space: O(1)
    # We always should move `1` from the leftmost position first.
    # Because it will be stuck on another `1` and we would need to use two moves.
    # Or even more, to finally push it to the end.
    out: int = 0
    sum: int = 0
    b_point: bool = False
    # We stack all the `1` on the left. And once we have a free space to move == `0`,
    #  we should move all the `1` on the left, one by one starting from the rightmost.
    # In this case, we either hit the `1` or end of the array.
    for char in s:
        if int(char):
            sum += 1
            b_point = True
            continue
        if not b_point:
            continue
        out += sum
        b_point = False
    
    return out


# Time complexity: O(s)
# Always traversing the whole input string `s`, once => O(s).
# --- --- --- ---
# Space complexity: O(1)


test: str = "1001101"
test_out: int = 4
assert test_out == max_operations(test)

test = "00111"
test_out = 0
assert test_out == max_operations(test)
