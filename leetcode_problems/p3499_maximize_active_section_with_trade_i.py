# You are given a binary string s of length n, where:
#  - '1' represents an active section.
#  - '0' represents an inactive section.
# You can perform at most one trade to maximize the number of active sections in s.
# In a trade, you:
#  - Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
#  - Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
# Return the maximum number of active sections in s after making the optimal trade.
# Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'.
# The augmented '1's do not contribute to the final count.
# --- --- --- ---
# 1 <= n == s.length <= 10 ** 5
# s[i] is either '0' or '1'


def max_active_sections_after_trade(s: str) -> int:
    # working_solution: (48.60%, 100%) -> (729ms, 20.25mb)  Time: O(s) Space: O(s)
    basic: int = s.count('1')
    out: int = basic
    # Extra breaker
    s_e: str = s + '1'
    # Basically suffix.
    count: int = 0
    prefix: int = 0
    
    ind_cur: int = 0

    while ind_cur < len(s_e):
        cur_char: str = s_e[ind_cur]
        if '1' == cur_char:
            if 0 != prefix and 0 != count:
                out = max(
                    out,
                    basic + prefix + count
                )
                prefix, count = count, 0
            elif 0 == prefix:
                prefix, count = count, 0
        else:
            count += 1
    
        ind_cur += 1
    
    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "01"
test_out: int = 1
assert test_out == max_active_sections_after_trade(test)

test = "0100"
test_out = 4
assert test_out == max_active_sections_after_trade(test)

test = "1000100"
test_out = 7
assert test_out == max_active_sections_after_trade(test)

test = "01010"
test_out = 4
assert test_out == max_active_sections_after_trade(test)

test = "10110"
test_out = 5
assert test_out == max_active_sections_after_trade(test)