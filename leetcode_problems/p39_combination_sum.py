# Given an array of distinct integers candidates and a target integer target,
#  return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target
#  is less than 150 combinations for the given input.
# -------------------
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # working_sol (98.57%, 60.69%) -> (43ms, 16.3mb)  time: O(target * 2 ** n) | space: O(target)
    combos: list[list[int]] = []
    if len(candidates) == 1:
        if candidates[0] == target:
            combos.append([candidates[0]])
            return combos
        if candidates[0] != target:
            return combos
    # To ignore already used values, we need to move lowest -> highest.
    candidates.sort()
    if candidates[0] > target:
        return combos

    def combinations(options: list[int], path: list[int], summ: int = 0) -> None:
        if summ == target:
            combos.append(path)
            return
        for x in range(len(options)):
            next_sum: int = options[x] + summ
            if next_sum > target:
                break
            combinations(
                options[x:],  # no reasons to recheck used values, because we only care about unique combs.
                path + [options[x]],
                next_sum,
            )

    combinations(candidates, [], 0)
    return combos


# Time complexity: O(target * 2 ** n) <- n - len of input array 'candidates'.
# Worst case == like: [1, 2, 4, 8, 16], target == 16.
# First we will sort == (n * log n).
# Then we have a recursion with 2 options => include current options[x] or not => 2 ** n.
# But, because we're allowed to reuse ! The same number may be chosen from candidates an unlimited number of times !.
# Our initial calls will be recalled, like for '1' it will be (1 * target) times to get 16.
# So, it should be something like O((n * log n) + target * 2 ** n)
# -------------------
# Auxiliary space: O(target).
# 'path' in case with '1' will be of length == target, and because we're building it from (0 -> length).
# We will have at max One array with length == target, and w.e '1' calls arrays with length == (part of target).
# So, for '1' we will make target calls and => path == (target * log target).
# And options, which for every call is copy of original 'candidates' for every '1' call => (target * n)?
# Extra for every call we have INT('summ').
# How many combinations and sizes? No idea.
#           'path'              'options'    'summ'  'output'
#   O((target * log target) + (target * n) + target +  N.A)
# Or if we ignore recursion deep diving we can just call it: O(target).
# Because worst case is still '1' repeated for a target times, which is actually a number of calls.


test: list[int] = [2, 3, 6, 7]
test_target: int = 7
test_out: list[list[int]] = [[2, 2, 3], [7]]
assert test_out == combination_sum(test, test_target)

test = [2, 3, 5]
test_target = 8
test_out = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
assert test_out == combination_sum(test, test_target)

test = [2]
test_target = 1
test_out = []
assert test_out == combination_sum(test, test_target)
