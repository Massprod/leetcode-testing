# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# ----------------------
# 1 <= n <= 8


def gen_parentheses(n: int) -> list[str]:
    # working_sol (67.8%, 37.38%) -> (40ms, 16.7mb)  time: O(Cn * n) | space: O(Cn * n)
    combos: list[str] = []

    def backtrack(cur_seq: list[str], opened: int, closed: int) -> None:
        # Everything correctly closed => correct sequence.
        if closed == n:
            combos.append(''.join(cur_seq))
            return
        # We can place open_bracket's until != 'n'.
        if opened < n:
            backtrack(cur_seq + ['('], opened + 1, closed)
        # Every open_bracket should be closed.
        if closed < opened:
            backtrack(cur_seq + [')'], opened, closed + 1)

    backtrack([], 0, 0)
    return combos


# Time complexity: O(Cn * n) -> ! https://en.wikipedia.org/wiki/Catalan_number ! for all combinations ->
# n - input value 'n'^^|        -> Catalan(n) gives all combinations and every combination is size == n => O(Cn * n).
#                             ! Asymptotically, the Catalan numbers grow as:
#                               (4 ** n) / (n ** (3 / 2)) * (3.14 ** 0.5)   !
# Auxiliary space: O(Cn * n) -> every combination stored and size of each == n => O(Cn * n).


test: int = 3
test_out: list[str] = ["((()))", "(()())", "(())()", "()(())", "()()()"]
assert test_out == gen_parentheses(test)

test = 1
test_out = ["()"]
assert test_out == gen_parentheses(test)
