# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# 1 <= heights.length <= 105  ,  0 <= heights[i] <= 104

def largest_rectangle(heights: list[int]) -> int:
    # working_sol (43.51%, 32.19%) -> (989ms, 31mb)  time: O(n) | space: O(n)
    heights.append(0)
    indexes: list[int] = [-1]
    max_area: int = 0
    for x in range(len(heights)):
        while heights[x] < heights[indexes[-1]]:
            height: int = heights[indexes.pop()]
            length: int = x - indexes[-1] - 1
            max_area = max(max_area, height * length)
        if len(indexes) == 0 or heights[x] >= heights[indexes[-1]]:
            indexes.append(x)
    heights.pop()
    return max_area

# Time complexity: O(n) -> worst case, 1..2.3..n -> only ascending values ->
#                          -> iterate once to create indexes of input_n size => O(n) ->
#                          -> iterate indexes once to calc all index areas => O(n) -> leaving us with O(n)
# Space complexity: O(n) -> extra list with size of input_n => O(n)
# -----------------------------
# Flow:
#   left_limit = indexes[-1] after removing last element -> removing last element and getting ascending_point ->
#   we need 2 break_points: first is point of ascending and second is point of descending.
#   ! failed to make this before ! ascending_point == left_limit ! descending_point = right_limit !
#   in this solution ascending_point is always last element of indexes after removing,
#   even from the start [-1] == 0 - lowest possible
#   right_limit = heights[x] => descending_point or first time we encounter something smaller ->
#   distance between them is equal to length of rectangle which can be placed here ->
#   allowing us to calc areas of all rectangles inside with heights of removed indexes.
# -----------------------------
# Failed with making my own solution without googling:
#   1) Failed to count descending bard, everything worked for ascending part or equal part.
#   2) Failed to make breakpoints, such I could count some slice with height in it.
#   3) Failed - TimeLimit with working simple solution while counting every possible area.
#      ! btw this solution is 1000ms, and it's after googling !


test1 = [2, 1, 5, 6, 2, 3]
test1_out = 10
print(largest_rectangle(test1))
assert test1_out == largest_rectangle(test1)

test2 = [2, 4]
test2_out = 4
print(largest_rectangle(test2))
assert test2_out == largest_rectangle(test2)

test3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]
test3_out = 5
print(largest_rectangle(test3))
assert test3_out == largest_rectangle(test3)

test4 = [1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 0, 100]
test4_out = 100
print(largest_rectangle(test4))
assert test4_out == largest_rectangle(test4)

test5 = [0, 0, 0, 0, 0, 6, 0]
test5_out = 6
print(largest_rectangle(test5))
assert test5_out == largest_rectangle(test5)

test6 = [9, 8, 7, 0, 9, 8, 7, 5]
test6_out = 21
print(largest_rectangle(test6))
assert test6_out == largest_rectangle(test6)

test7 = [1, 2, 2]
test7_out = 4
print(largest_rectangle(test7))
assert test7_out == largest_rectangle(test7)

test8 = [5, 4, 1, 2]
test8_out = 8
print(largest_rectangle(test8))
assert test8_out == largest_rectangle(test8)

test9 = [0, 1, 2, 3]
print(largest_rectangle(test9))