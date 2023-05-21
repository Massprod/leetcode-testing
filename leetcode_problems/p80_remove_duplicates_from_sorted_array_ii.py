# Given an integer array nums sorted in non-decreasing order,
# remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
# -----------------------
# 1 <= nums.length <= 3 * 104  ,  -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


def remove_duplicates(nums: list[int]) -> int:
    # working_sol: (12.21%, 24.61%) -> (78ms, 16.4mb)  time: O(m + (n * k)) | space: O(1)
    pointer: int = len(nums)
    index: int = 1
    count: int = 1
    tempo: int = nums[0]
    shift: int = 1
    while index < pointer:
        if count == 2 and nums[index] == tempo:
            for y in range(index + shift, pointer):
                if nums[y] == tempo:
                    shift += 1
                if nums[y] != tempo:
                    break
            for x in range(index + shift, pointer):
                nums[x - shift], nums[x] = nums[x], nums[x - shift]
            pointer -= shift
            shift = 1
            continue
        if nums[index] != tempo:
            count = 1
            tempo = nums[index]
            index += 1
            continue
        if nums[index] == tempo:
            count += 1
            index += 1
            continue
    return index


# Time complexity: O(m + (n * k)) -> worst case, every time we encounter duplicate, looping slice n
#                                     and shifting values for every index => O(n * k) ->
#                                     -> checking every index in input to start shifting => O(m) -> O(m + (n * k))
#                  Ω(m) -> best case no duplicates, just looping once through whole input =>  Ω(m)
# n - slice in range(index to pointer) ^^
# k - number of duplicate encounters ^^
# m - length of input_nums ^^
# Space complexity: O(1) -> only extra constants => O(1)
# ! can be done with lesser constants, but will be harder to read and slower, and still using count,
#   otherwise we can't check duplicates. At least I don't know how. !
# ------------------
# Correct solution but slow, tried to speed this up with *shift* and failed, forgot about changing start_index.
# Failed 2 commits for that...well don't do tasks at 2am :)


test1 = [1, 1, 1, 2, 2, 3]
test1_k = 5
test1_out = [1, 1, 2, 2, 3, "_"]
print(remove_duplicates(test1))
print(test1)
for _ in range(test1_k):
    assert test1_out[_] == test1[_]

test2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
test2_k = 7
test2_out = [0, 0, 1, 1, 2, 3, 3, "_", "_"]
print(remove_duplicates(test2))
print(test2)
for _ in range(test2_k):
    assert test2_out[_] == test2[_]

# test3 - failed -> added shit to make it a little bit faster, and forgot about resetting after every shift_phase
test3 = [0, 0, 1, 1, 1, 1, 2, 2, 2, 4]
test3_k = 7
test3_out = [0, 0, 1, 1, 2, 2, 4, "_", "_", "_"]
print(remove_duplicates(test3))
print(test3)
for _ in range(test3_k):
    assert test3_out[_] == test3[_]

test4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test4_k = remove_duplicates(test4)
test4_out = [1, 1]
print(test4)
for _ in range(test4_k):
    assert test3_out[_] == test3[_]
