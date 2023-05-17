# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# 1 <= n <= 20  ,  1 <= k <= n
# You may return the answer in any order.
from copy import deepcopy


def combine(n: int, k: int) -> list[list[int]] | set:
    k_numbers: set = set()
    tempo: list[int] = []

    def new_combine(start: int = 1, end: int = n + 1, left_to_use: int = k):
        if left_to_use == 0:
            copy: list[int] = deepcopy(tempo)
            copy.sort()
            k_numbers.add(tuple(copy))
            del copy
            return
        for num in range(start, end):
            if num in tempo:
                continue
            tempo.append(num)
            new_combine(start + 1, end, left_to_use - 1)
            tempo.pop()
    new_combine()
    return k_numbers


test1_n = 4
test1_k = 2
test1_out = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
test = list(combine(test1_n, test1_k))
print(test)
for _ in test1_out:
    assert tuple(_) in test
del test

test2_n = 1
test2_k = 1
test2_out = [[1]]
test = list(combine(test2_n, test2_k))
print(test)
for _ in test2_out:
    assert tuple(_) in test
del test

test3_n = 5
test3_k = 3
test3_out = [
    [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5],
    [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5],
]
test = list(combine(test3_n, test3_k))
print(test)
for _ in test3_out:
    assert tuple(_) in test
del test

# test4 - failed -> Made a lot of useless checks and used creating of a list,
#                   when we can just use a range for values not indexing them for a list.
test4_n = 13
test4_k = 10
test = list(combine(test4_n, test4_k))
print(test)
