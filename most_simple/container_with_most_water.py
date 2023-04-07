# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

#     end_point1 = (i, 0)
#     end_point2 = (i, height[i])
# Hint 2:
# Try to use two-pointers.
# Set one pointer to the left and one to the right of the array.
# Always move the pointer that points to the lower line.
def max_area(height: list[int]) -> int:
    volume = 0
    min_x = 0
    max_x = len(height) - 1
    while max_x >= min_x:
        right_column = height[max_x]
        left_column = height[min_x]
        new_volume = min(right_column, left_column) * (max_x - min_x)
        volume = max(new_volume, volume)
        if right_column > left_column:
            min_x += 1
        elif left_column > right_column:
            max_x -= 1
        elif left_column == right_column:
            max_x -= 1
    return volume





test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test2 = [1, 1]
test4 = [0, 0, 2, 1]
test5 = [1, 2, 1]
print(max_area(test1))
print(max_area(test2))
print(max_area(test4))
print(max_area(test5))
