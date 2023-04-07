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
def max_area(height: list[int]) -> int:
    volume = 0
    for x in range(len(height)):
        line_num = x
        line_height = height[x]
        for y in range(x + 1, len(height)):
            check_num = y
            check_height = height[y]
            rect_len = check_num - line_num
            rect_height = min(line_height, check_height)
            new_volume = rect_len * rect_height
            if new_volume > volume:
                volume = new_volume
    return volume


test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test2 = [1, 1]
test3 = []
test4 = [0, 0, 2, 1]
test5 = [1, 2, 1]
print(max_area(test1))
print(max_area(test2))
print(max_area(test3))
print(max_area(test4))
print(max_area(test5))
