# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i]
#  is the expected height of the ith student in line.
# You are given an integer array heights representing the current order
#  that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
# Return the number of indices where heights[i] != expected[i].
# ------------------------
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100


def height_checker(heights: list[int]) -> int:
    # working_sol (91.92%, 77.64%) -> (32ms, 16.46mb)  time: O(n * log n) | space: O(n)
    # Do we care about current `heights` value?
    # Or we can change them?
    # Because if we can change them, in case like:
    # 1 4 8 3 -> we could just change `3` -> 1 4 8 9 <= 1 value we need to change.
    # But if we can't, then it's a simple sort and check for changed values.
    # Expected answer for this == 3. So it's sorting.
    out: int = 0
    heights_sorted: list[int] = sorted(heights)
    for index in range(len(heights)):
        if heights[index] != heights_sorted[index]:
            out += 1
    return out


# Time complexity: O(n * log n) <- n - length of an input array `heights`
# Always sorting the input array `heights` and single traverse of it => O(n * log n + n)
# ------------------------
# Auxiliary space: O(n)
# Copying original array with `heights_sorted`, and also `sorted()` takes O(n) => O(2n).


test: list[int] = [1, 1, 4, 2, 1, 3]
test_out: int = 3
assert test_out == height_checker(test)

test = [5, 1, 2, 3, 4]
test_out = 5
assert test_out == height_checker(test)

test = [1, 2, 3, 4, 5]
test_out = 0
assert test_out == height_checker(test)
