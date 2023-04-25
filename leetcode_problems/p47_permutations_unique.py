# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.


def permute_unique(nums: list[int]) -> list[list[int]] | set:
    # working_sol (9.18%, 44.71%) -> (1085ms, 14.4mb)  time: O(n!) | space: O(n!)
    # working_sol (28.16%, 44.71%) -> (261ms, 14.5mb) -> with set(tuple) instead of a list[list[int]] as return
    permutes = set()
    origin = nums

    def rec_permute(to_check: list[int], start_ind: int = 0):
        if start_ind == len(to_check):
            permutes.add(tuple(to_check.copy()))
            return
        for x in range(start_ind, len(to_check)):
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
            rec_permute(to_check, start_ind + 1)
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]

    rec_permute(origin)
    return permutes

# Time complexity: O(n*n!) -> calling recursion for n elements in given input,
#                             and for each element recursion for n! times.
# Space complexity: O(n!) -> creating lists with n! lists in it, n! <- all combinations of input list.

# Well. Most simple trick to speed things up is to use SET() instead of a LIST(),
# but as always there's no mentioning of sets. But there's list[list[int]] as return by default.

# Surprisingly didn't hit time_limit :)

# I guess there's a speed catch. Going to try commit same solution, checking every possible permute.
# But just ignoring which have been already added.


test1 = [1, 1, 2]
test1_out = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
]
test = permute_unique(test1)
print(test)
for _ in test:
    assert len(test1_out) == len(test)
    assert list(_) in test1_out

test2 = [1, 2, 3]
test2_out = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
test = permute_unique(test2)
print(test)
for _ in test:
    assert len(test2_out) == len(test)
    assert list(_) in test2_out
