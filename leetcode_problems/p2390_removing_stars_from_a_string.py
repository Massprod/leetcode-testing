# You are given a string s, which contains stars *.
# In one operation, you can:
#   Choose a star in s.
#   Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
#   The input will be generated such that the operation is always possible.
#   It can be shown that the resulting string will always be unique.
# ------------------
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.


def remove_stars(s: str) -> str:
    # working_sol (97.72%, 71.47%) -> (171ms, 17.9mb)  time: O(n) | space: O(n)
    list_stack: list[str] = []
    # Store everything, delete only when '*' encountered.
    for _ in s:
        if _ == '*':
            list_stack.pop()
            continue
        list_stack.append(_)
    return ''.join(list_stack)


# Time complexity: O(n) -> traversing whole input_string, once => O(n) ->
# n - len of input_string^^| -> worst case should be like == 'aaaaa....aaaa',
#                               then ''.join() will extra use every index => O(2n).
# Auxiliary space: O(n) -> same worst case, everything will be stored => O(n).
# ------------------
# Default stack I guess. Append and remove last element when '*' encountered.


test: str = "leet**cod*e"
test_out: str = "lecoe"
assert test_out == remove_stars(test)

test = "erase*****"
test_out = ""
assert test_out == remove_stars(test)
