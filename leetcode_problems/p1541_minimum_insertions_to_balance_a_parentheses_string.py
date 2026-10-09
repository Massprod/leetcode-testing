# Given a parentheses string s containing only the characters '(' and ')'.
# A parentheses string is balanced if:
#  - Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
#  - Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
#  - For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s consists of '(' and ')' only.


def min_insertions(s: str) -> int:
    # working_solution: (38.60%, 28.42%) -> (83ms, 20.32mb)  Time: O(s) Space: O(s)
    out: int = 0
    index: int = 0
    stack: list[int] = []
    opener: str = '('
    closer: str = ')'
    while index < len(s):
        if opener == s[index]:
            stack.append(opener)
            index += 1
        else:
            if stack:
                stack.pop()
            # Insert if nothing to close
            else:
                out += 1
            # double closer == skip
            if index < (len(s) - 1) and closer == s[index + 1]:
                index += 2
            # single closer == insert
            else:
                index += 1
                out += 1

    return out + len(stack) * 2


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = '(()))'
test_out: int = 1
assert test_out == min_insertions(test)

test = '())'
test_out = 0
assert test_out == min_insertions(test)

test = '))())('
test_out = 3
assert test_out == min_insertions(test)

test = ')()'
test_out = 3
assert test_out == min_insertions(test)
