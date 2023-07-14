# Given an integer array arr and an integer difference,
#   return the length of the longest subsequence in arr which
#   is an arithmetic sequence such that the difference between adjacent elements
#   in the subsequence equals difference.
# A subsequence is a sequence that can be derived from arr by deleting some
#   or no elements without changing the order of the remaining elements.
# --------------------------
# 1 <= arr.length <= 10 ** 5
# -10 ** 4 <= arr[i], difference <= 10 ** 4


def longest_subsequence_length(arr: list[int], difference: int) -> int:
    # working_sol (50.00%, 92.84%) -> (575ms, 30mb)  time: O(n) | space: O(n)
    stored: dict[int, int] = {}
    for x in range(len(arr) - 1, -1, -1):
        num: int = arr[x]
        # first encounter
        if num not in stored:
            stored[num] = 1
            # unique case with duplicates
            if difference == 0:
                continue
        if x < (len(arr) - 1):
            alr_met: int = num + difference
            # correct option we already met and stored its sequence_len,
            # NUM seq is NUM itself, so we can use it as continuation
            if alr_met in stored:
                stored[num] = stored[alr_met] + 1
    max_len: int = max(stored.values())
    return max_len


# Time complexity: O(n) -> traversing whole input_array, once => O(n) -> extra traverse for values stored,
# n - len of input_array^^|  size of it's equal to unique values in the input_array ->
#                          -> in the worst case there's only unique values => O(n) -> O(n) + O(n) => O(n).
# Auxiliary space: O(n) -> store every unique value in the input_array as dict_keys, and values are always constant =>
#                          => O(n).
# --------------------------
# Ok. There's space_limit, and I was actually too much focused on recording actual sequence.
# Like our task is asking about LEN(SEQ) and I was focused to find this seq and forgot that we need only LEN.
# Just increment from 1 for every correct option should be enough.
# Then we don't actually even need SET or LIST, cuz there's nothing to consider except +1 if correct.
# Extra to that, we can just record max_len and update from the start. But is it faster?
# Like we're going to check max_len for every index after we traverse, and if we do this on a way ->
# -> we would compare same indexes multiple times, so it's should be slower.
# But it's still can be changed to max.values(), cuz now we're having only INTs inside.
# --------------------------
# Ok. It's working, but I didn't consider difference can be 0.
# So arithmetic sequence can be correct even with difference 0.
# I was using set() to avoid duplicates, and we shouldn't.
# --------------------------
# Well order is matter, so we can't just sort.
# And if I use simple recursion it's 99% TLE.
# So it's DP problem and I need to find how we can cull recursion.
# Like 1, 5, 7, 8, 5, 3, 4, 2, 1, 2, 3 -> by default our recursion calls will be for every number,
# and we would check every combination with NUM + dif. And there's only 1 correct option on the way,
# so we're actually have only 1 correct turn for every call.
# If NUM = preNUM + diff than it's arithmetic seq and we continue.
# If there's multiple instances of this? We can ignore them, because arith seq is always UNIQUE values,
#   because every single one of them is prevNUM + dif.
# We can delete ANY amount of elements so, there's no difference if we met 1 at index == or 1 at index == 8,
# if after this index we meet anything that is correct for 1 + dif it's correct part of the seq.
# With recursion, it would be checked again, but if we record every correct encounter for this NUM
# we can just expand seq with it.
# In this case 1 -> 2, recorded => new encounter with 1 can be ignored. Same goes for every other NUM.
# Because we can just take seq for 2 cuz it's continuation of 1. Same goes for every other NUM.
# Recorded seq for 2 is == 1, 2 -> ignore duplicates until we hit something correct prevNUM + dif and only then,
# we can add this into a record.
# 1 -> 2 -> 3 => seq == 3 | So we can walk either way and collect correct options for every stored(met) NUM.


test1 = [1, 2, 3, 4]
test1_dif = 1
test1_out = 4
print(longest_subsequence_length(test1, test1_dif))
assert test1_out == longest_subsequence_length(test1, test1_dif)

test2 = [1, 3, 5, 7]
test2_dif = 1
test2_out = 1
print(longest_subsequence_length(test2, test2_dif))
assert test2_out == longest_subsequence_length(test2, test2_dif)

test3 = [1, 5, 7, 8, 5, 3, 4, 2, 1]
test3_dif = -2
test3_out = 4
print(longest_subsequence_length(test3, test3_dif))
assert test3_out == longest_subsequence_length(test3, test3_dif)

test4 = [1, 5, 7, 8, 5, 3, 4, 2, 1, 1, 1, 1, 2, 3, 4, 5, 6, 4, 2, 0, -2, -4, -6, 10]
test4_dif = -2
test4_out = 8
print(longest_subsequence_length(test4, test4_dif))
assert test4_out == longest_subsequence_length(test4, test4_dif)

# test5 -> failed -> because I was ignoring duplicates.
test5 = [4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8]
test5_dif = 0
test5_out = 2
print(longest_subsequence_length(test5, test5_dif))
assert test5_out == longest_subsequence_length(test5, test5_dif)


# Failed solution, due to recording of actual sequence,
# it is actually good to get all subsequences, so it's better to store it:
def all_correct_subsequences(arr: list[int], difference: int) -> dict[int, [set[int] | list[int]]]:
    """
    Finds all correct arithmetic sequences with set difference, RESULT is unsorted.
    :param arr: sequence of integers from what we need to find
    :param difference: dif of numbers in arithmetic sequence
    :return: all correct arithmetic subsequences with set difference, unsorted
    """
    stored: dict[int, [set[int] | list[int]]] = {}
    for x in range(len(arr) - 1, -1, -1):
        num: int = arr[x]
        # first encounter
        if num not in stored:
            if difference != 0:
                stored[num] = {num}
            # unique case with duplicates
            if difference == 0:
                stored[num] = [num]
                continue
        if x < (len(arr) - 1):
            # append duplicates
            if difference == 0:
                stored[num].append(num)
                continue
            alr_met: int = num + difference
            # correct option we already met and stored its sequence,
            # NUM seq is NUM itself, so we can use it as continuation
            if alr_met in stored:
                for _ in stored[alr_met]:
                    stored[num].add(_)
    return stored
