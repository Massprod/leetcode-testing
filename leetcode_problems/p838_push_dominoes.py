# There are n dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either
#  to the left or to the right.
# After each second, each domino that is falling to the left pushes
#  the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent
#  dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides,
#  it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends
#  no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
#  - dominoes[i] = 'L', if the ith domino has been pushed to the left,
#  - dominoes[i] = 'R', if the ith domino has been pushed to the right, and
#  - dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
# ----------------------
# n == dominoes.length
# 1 <= n <= 10 ** 5
# dominoes[i] is either 'L', 'R', or '.'.


def push_dominoes(dominoes: str) -> str:
    # working_sol (44.74%, 59.87%) -> (234ms, 22.32mb)  time: O(n) | space: O(n)
    r_dom: str = 'R'
    l_dom: str = 'L'
    push_force: int = 0
    # Push strength from left to right state.
    left_right: list[int] = []
    for domino in dominoes:
        # Any `R` starts with full force.
        if r_dom == domino:
            push_force = len(dominoes)
        # `L` stops any `R`
        elif l_dom == domino:
            push_force = 0
        # Idle == absorbs 1 hit.
        else:
            push_force = max(push_force - 1, 0)
        left_right.append(push_force)

    push_force = 0
    for index in range(len(dominoes) - 1, -1, -1):
        if l_dom == dominoes[index]:
            push_force = len(dominoes)
        elif r_dom == dominoes[index]:
            push_force = 0
        else:
            push_force = max(push_force - 1, 0)
        left_right[index] -= push_force
    
    out: list[str] = []
    for collide_val in left_right:
        if 0 < collide_val:
            out.append(r_dom)
        elif 0 > collide_val:
            out.append(l_dom)
        else:
            out.append('.')
    
    return ''.join(out)


# Time complexity: O(n) <- n - length of the input string `dominoes`.
# Always using every char of the input string `dominoes`, three times => O(3 * n).
# ----------------------
# Auxiliary space: O(n)
# `left_right` <- allocates space for each char from `dominoes` => O(n).
# `out` <- allocates space for each chat from `dominoes` => O(2 * n).


test: str = "RR.L"
test_out: str = "RR.L"
assert test_out == push_dominoes(test)

test = ".L.R...LR..L.."
test_out = "LL.RR.LLRRLL.."
assert test_out == push_dominoes(test)
