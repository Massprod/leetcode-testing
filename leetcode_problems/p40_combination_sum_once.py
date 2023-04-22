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
    avail = {}
    if len(candidates) == 1:
        if candidates[0] == target:
            combos.append([candidates[0]])
            return combos
        if candidates[0] != target:
            return combos
    for _ in candidates:
        if _ not in avail.keys():
            avail[_] = candidates.count(_)
    if len(avail) == 1:
        for key, value in avail.items():
            if value >= target:
                combos.append([key for g in range((int(target / key)))])
                return combos
            if value <= target:
                return combos

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
            combinations(sliced[y + 1:], temp)
            temp.pop()

    if sum(candidates) < target:
        return combos
    if min(candidates) > target:
        return combos
    combinations(candidates, tempo)
    return combos


# I don't get how can we speed up a search.
#   - we can't stop on encountering same value - True
#   - we can stop if the same value used 30 times and still 70 left -> leads us to same combos, how can I check this?
# Creating dictionary with available usages of same number. Only allowing me to skip same_values tests.
# But what if there's 11111111121111111???
# Don't get it. We can't skip values even if it's repeating 10000times, after this 10000time can be another value,
# and we should count this as a summ.
# But if there's only ONE value in a list 10000times im skipping it with a dictionary usage. Google time?

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

# test3 - failed -> time_limit | apparently I need speed :) but I can't ignore that 1 can be used every time.
test3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test3_target = 27
test3_out = []
print(comb_sums(test3, test3_target))
answer3 = comb_sums(test3, test3_target)
assert len(answer3) == len(test3_out)
for _ in answer3:
    assert _ in test3_out

# test4 - failed -> time_limit | combos = list(30x1), how can I stop iteration?
test4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test4_target = 30
test4_out = [[1 for _ in range(30)]]
answer4 = comb_sums(test4, test4_target)
print(answer4)
assert len(answer4) == len(test4_out)
for _ in answer4:
    assert _ in test4_out

test5 = [3, 1, 3, 5, 1, 5, 2, 3, 2, 5, 4]
test5_target = 1
test_5_out = [[1]]
print(comb_sums(test5, test5_target))
