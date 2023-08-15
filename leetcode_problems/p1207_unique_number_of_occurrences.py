# Given an array of integers arr, return true if the number of occurrences of each value
#   in the array is unique or false otherwise.
# ----------------------
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000


def unique_occur(arr: list[int]) -> bool:
    # working_sol (92.04%, 83.55%) -> (40ms, 16.4mb)  time: O(n) | space: O(n)
    values: dict[int, int] = {}
    # Count everything.
    for _ in arr:
        if _ in values:
            values[_] += 1
            continue
        values[_] = 1
    # set() == no_duplicates.
    # If length is changed, there were some duplicates deleted.
    if len(values.values()) != len(set(values.values())):
        return False
    return True


# Time complexity: O(n) -> traversing and counting all values and their occurrences => O(n) ->
# n - len of input_array^^| -> creating set of dict.values() => O(n).
# Auxiliary space: O(n) -> dictionary with all values and occurrences count => O(n) -> extra set, in the worst case
#                          there's no duplicates, and it's size == n => O(n).
# ----------------------
# Count everything and recheck for duplicates. Only question is how to check fast,
# cuz we can't escape counting everything in the array first.
# Change for set and compare len(dict.values) != len(set(dict_values))?
# Correct, but in some cases if I loop and just record values in a set, I could break on first values.
# And if I use len() then it's always creating of a full set().
# Actually w.e just don't want to build extra moves for Easy task when it's already 90%.


test: list[int] = [1, 2, 2, 1, 1, 3]
test_out: bool = True
assert test_out == unique_occur(test)

test = [1, 2]
test_out = False
assert test_out == unique_occur(test)

test = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
test_out = True
assert test_out == unique_occur(test)
