# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.


def permute_unique(nums: list[int]) -> list[list[int]] | set:
    # working_sol (9.18%, 44.71%) -> (1085ms, 14.4mb)  time: O(n*n!) | space: O(n!)
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
# Space complexity: O(n!) -> creating list with n! lists in it, n! <- all combinations of input list.

# Still slow, and obviously I shouldn't check indexes with same values, how do we skip it?

# Well. Most simple trick to speed things up is to use SET() instead of a LIST(),
# but as always there's no mentioning of sets. But there's list[list[int]] as return by default.

# Surprisingly didn't hit time_limit :)

# I guess there's a speed catch. Going to try commit same solution, checking every possible permute.
# But just ignoring which have been already added.


def sp_permute_unique(nums: list[int]) -> list[list[int]] | set:
    # working_sol (32.18%, 44.71%) -> (103ms, 14.4mb)  time: O(n*n!) | space: O(n!)
    permutes = set()
    origin = nums

    def rec_permute(to_check: list[int], start_ind: int = 0):
        if start_ind == len(to_check):
            permutes.add(tuple(to_check.copy()))
            return
        for x in range(start_ind, len(to_check)):
            if to_check[x] == to_check[start_ind] and start_ind != x:
                continue
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
            rec_permute(to_check, start_ind + 1)
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
    rec_permute(origin, start_ind=0)
    return permutes

# Time complexity: O(n*n!) -> before we used n! rec_permute() calls, now we're skipping some calls with same values,
#                             but worst case is still the same -> every value is unique, and we're using -> n! calls.
# Space complexity: O(n!) -> creating list with n! lists in it, n! <- all combinations of input list.

# Welp it worked. Using set(tuple) gives us 1085ms -> 261ms | skipping same values gives us 261ms -> 103ms
# x10 improvement, not so bad! Obviously there's more ways to solve this.
# But I don't want to google and commit for speed, leaving it like this.


test1 = [1, 1, 2]
test1_out = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1]
]
test = permute_unique(test1)
test_sp = sp_permute_unique(test1)
# print(test)
print(test_sp)
for _ in test:
    assert len(test1_out) == len(test)
    assert list(_) in test1_out
for _ in test_sp:
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
test_sp = sp_permute_unique(test2)
# print(test)
print(test_sp)
for _ in test:
    assert len(test2_out) == len(test)
    assert list(_) in test2_out
for _ in test_sp:
    assert len(test2_out) == len(test)
    assert list(_) in test2_out
