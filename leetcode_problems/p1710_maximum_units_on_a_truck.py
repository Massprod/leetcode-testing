# You are assigned to put some amount of boxes onto one truck.
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#  - numberOfBoxesi is the number of boxes of type i.
#  - numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize,
#  which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.
# -----------------------
# 1 <= boxTypes.length <= 1000
# 1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
# 1 <= truckSize <= 10 ** 6


def maximum_units(box_types: list[list[int]], truck_size: int) -> int:
    # working_sol (80.97%, 92.40%) -> (132ms, 16.89mb)  time: O(n * log n) | space: O(n)
    box_types.sort(reverse=True, key=lambda x: x[1])
    out: int = 0
    for box_type in box_types:
        if not truck_size:
            break
        can_take: int = min(box_type[0], truck_size)
        out += can_take * box_type[1]
        truck_size -= can_take
    return out


# Time complexity: O(n * log n) <- n - length of the input array `box_types`
# Always sorting `box_types`, once => O(n * log n).
# Extra traversing it after sorting, once => O(n + n * log n).
# -----------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) => O(n).


test_types: list[list[int]] = [[1, 3], [2, 2], [3, 1]]
test_size: int = 4
test_out: int = 8
assert test_out == maximum_units(test_types, test_size)

test_types = [[5, 10], [2, 5], [4, 7], [3, 9]]
test_size = 10
test_out = 91
assert test_out == maximum_units(test_types, test_size)
