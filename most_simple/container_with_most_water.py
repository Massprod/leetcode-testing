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
    lines = {}
    for x, y in enumerate(height):
        line_num = x
        line_height = height[x]
        lines[] =

    return volume


test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test2 = [1, 1]
test3 = []
test4 = [0, 0, 2, 1]
test5 = [1, 2, 1]
# print(max_area(test1))
# print(max_area(test2))
# print(max_area(test3))
print(max_area(test4))
print(max_area(test5))
