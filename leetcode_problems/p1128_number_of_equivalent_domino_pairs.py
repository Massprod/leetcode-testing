# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d]
# if and only if either (a == c and b == d), or (a == d and b == c) - that is,
# one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
#  and dominoes[i] is equivalent to dominoes[j].
# ----------------------
# 1 <= dominoes.length <= 4 * 10 ** 4
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9


def num_equ_domino_pairs(dominoes: list[list[int]]) -> int:
    # working_sol (60.37%, 80.25%) -> (199ms, 25.97mb)  time: O(n) | space: O(n)
    pairs: dict[tuple[int, int], int] = {}
    for dom1, dom2 in dominoes:
        pair1: tuple[int, int] = (dom1, dom2)
        pair2: tuple[int, int] = (dom2, dom1)
        if pair1 in pairs:
            pairs[pair1] += 1
        elif pair2 in pairs:
            pairs[pair2] += 1
        else:
            pairs[pair1] = 1
    out: int = 0
    for val in pairs.values():
        if 1 != val:
            # n * (n - 1) / 2 <- all unique permutations for 2 elements from `n` elements.
            out += val * (val - 1) // 2
    return out


# Time complexity: O(n) <- n - length of the input array `dominoes`.
# In the worst case, every dominoes pair is unique.
# We're going to traverse whole input array `dominoes`, once => O(n).
# And extra traverse every value in `pairs` => O(2n).
# ----------------------
# Auxiliary space: O(n)
# Every unique pair from `dominoes` stored in `pairs` => O(n).


test: list[list[int]] = [[1,2],[2,1],[3,4],[5,6]]
test_out: int = 1
assert test_out == num_equ_domino_pairs(test)

test = [[1,2],[1,2],[1,1],[1,2],[2,2]]
test_out = 3
assert test_out == num_equ_domino_pairs(test)
