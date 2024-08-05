# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o",
#  and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.
# ------------------------
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.
from random import choice


def interpret(command: str) -> str:
    # working_sol (49.21%, 55.63%) -> (36ms, 16.41mb)  time: O(n) | space: O(n)
    out: list[str] = []
    current: list[str] = []
    for char in command:
        if "G" == char:
            out.append(char)
        elif ")" == char:
            if current[-1] == "l":
                out.append("al")
            else:
                out.append("o")
            current = []
        else:
            current.append(char)
    return ''.join(out)


# Time complexity: O(n) <- n - length of the input string `command`.
# We're always traversing every index of `command`, once => O(n).
# ------------------------
# Auxiliary space: O(n)
# In the worst case every char in `command` is `G`.
# So, every char will be used 1 by 1 in `out`, and joined into the same string after => O(2 * n).


test: str = "G()(al)"
test_out: str = "Goal"
assert test_out == interpret(test)

test = "G()()()()(al)"
test_out = "Gooooal"
assert test_out == interpret(test)

test = "(al)G(al)()()G"
test_out = "alGalooG"
assert test_out == interpret(test)

test_combs: list[str] = ["G", "()", "(al)"]
test = ''.join([choice(test_combs) for _ in range(30)])
print(test)
