# You are given a string s consisting only of uppercase English letters.
# You can apply some operations to this string where, in one operation,
#  you can remove any occurrence of one of the substrings "AB" or "CD" from s.
# Return the minimum possible length of the resulting string that you can obtain.
# Note that the string concatenates after removing the substring and could produce
#  new "AB" or "CD" substrings.
# ---------------------
# 1 <= s.length <= 100
# s consists only of uppercase English letters.


def min_length(s: str) -> int:
    # working_sol (89.23%, 34.74%) -> (37ms, 16.52mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    # { endChar: startChar }
    deletes: dict[str, str] = {
        'B': 'A',
        'D': 'C',
    }
    for char in s:
        if char in deletes:
            if stack and stack[-1] == deletes[char]:
                stack.pop()
                continue
        stack.append(char)
    return len(stack)


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# ---------------------
# Auxiliary space: O(s)
# In the worst case there's no chars to delete.
# `stack` <- allocates space for each char from `s` => O(s).


test: str = "ABFCACDB"
test_out: int = 2
assert test_out == min_length(test)

test = "ACBBD"
test_out = 5
assert test_out == min_length(test)
