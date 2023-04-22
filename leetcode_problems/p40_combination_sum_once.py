# Given a collection of candidate numbers (candidates) and a target
# number (target), find all unique combinations in candidates where
# the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

# As always they want to return list, but in reality it can be set...
# w.e speed not a goal here

def comb_sums(candidates: list[int], target: int) -> list[list[int]]:
    combos = []
    tempo = []

    def combinations(sliced: list[int], temp: list) -> None:
        if sum(temp) == target:
            to_add = temp.copy()
            to_add.sort()
            if to_add not in combos:
                combos.append(to_add)
                return
        if sum(temp) > target:
            return
        for y in range(len(sliced)):
            temp.append(sliced[y])
            combinations(sliced[y+1:], temp)
            temp.pop()
    for x in range(len(candidates)):
        tempo.append(candidates[x])
        combinations(candidates[x + 1:], tempo)
        tempo.pop()
    return combos


test1 = [10, 1, 2, 7, 6, 1, 5]
test1_target = 8
test1_out = [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]
print(comb_sums(test1, test1_target))
answer1 = comb_sums(test1, test1_target)
assert len(answer1) == len(test1_out)
for _ in answer1:
    assert _ in test1_out

test2 = [2, 5, 2, 1, 2]
test2_target = 5
test2_out = [
    [1, 2, 2],
    [5],
]
print(comb_sums(test2, test2_target))
answer2 = comb_sums(test2, test2_target)
assert len(answer2) == len(test2_out)
for _ in answer2:
    assert _ in test2_out
