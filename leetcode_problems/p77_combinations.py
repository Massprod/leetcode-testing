# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# 1 <= n <= 20  ,  1 <= k <= n
# You may return the answer in any order.


def combine(n: int, k: int) -> set:
    # working_sol (39.07%, 97.59%) -> (410ms, 17.51mb)  time: O(n ** k) | space: O(nCk * k)
    k_numbers: set = set()
    # Temporary storage for combination.
    tempo: list[int] = []

    def new_combine(start: int = 1, end: int = n + 1, left_to_use: int = k) -> None:
        if left_to_use == 0:
            k_numbers.add(tuple(sorted(tempo)))
            return
        # Creating combinations, by taking values from start -> end,
        # one by one until we hit usage limit == k.
        for num in range(start, end):
            # We don't need duplicates, so there's no reason
            # to recall same values.
            if num in tempo:
                break
            tempo.append(num)
            new_combine(start + 1, end, left_to_use - 1)
            tempo.pop()

    new_combine()
    return k_numbers


# Time complexity: O(n ** k) -> recursion tree with n branches and k depths => O(n ** k).
# Auxiliary space: O((n! / k! * (n-k)!) * k) or O(nCk * k) -> storing all combinations => O(nCk) ->
#                   and size of combinations is k, for every combination we create tempo_list of k size ->
#                   -> leaving us with a list or set with size of => O(nCk * k).
#   !
#   The number of combinations of n distinct objects, taken r at a time is:
#                          nCr = n! / r! (n - r)!
#   !
# --------------------------
# Counting all permutations, with 4585ms solution not a great idea, but working.
# Ok...77ms just for breaking from loop after we try to use already used num.
# We shouldn't have duplicates inside, it was obvious (cuz range 1...n),
# and we should break instantly if we meet it,
# and there's no reason to check any values after it for this recursion call.


test1_n = 4
test1_k = 2
test1_out = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
test = list(combine(test1_n, test1_k))
for _ in test1_out:
    assert len(test1_out) == len(test)
    assert tuple(_) in test
del test

test2_n = 1
test2_k = 1
test2_out = [[1]]
test = list(combine(test2_n, test2_k))
for _ in test2_out:
    assert len(test2_out) == len(test)
    assert tuple(_) in test
del test

test3_n = 5
test3_k = 3
test3_out = [
    [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5],
    [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5],
]
test = list(combine(test3_n, test3_k))
for _ in test3_out:
    assert len(test3_out) == len(test)
    assert tuple(_) in test
del test

# test4 - failed -> Made a lot of useless checks and used creating of a list,
#                   when we can just use a range for values not indexing them for a list.
test4_n = 13
test4_k = 10
test = list(combine(test4_n, test4_k))
# correct test, I just don't want to store 1000values here or made some file for it.
