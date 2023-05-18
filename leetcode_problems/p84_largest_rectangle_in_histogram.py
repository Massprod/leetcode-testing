# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# 1 <= heights.length <= 105  ,  0 <= heights[i] <= 104

def largest_rectangle(heights: list[int]) -> int:
    max_area: int = 0
    for index in range(len(heights)):
        if heights[index] == heights[index - 1] and index != 0:
            continue
        if heights[index] == 0:
            continue
        length: int = 1
        height: int = heights[index]
        for x in range(index - 1, -1, -1):
            if heights[x] < height:
                break
            length += 1
        for y in range(index + 1, len(heights)):
            if heights[y] < height:
                break
            length += 1
        area: int = length * height
        max_area = max(max_area, area)
    return max_area


# ------------------------
# Yep. Failed with time_limit test of (1 * 10000000) indexes.
# This is why I wanted to use min_plato in a first solution.
# But here, I see only one way to skip this. If we encounter same value as before we just continue.
# And this won't work with case of (1* 100000, 0, 1*100000) cuz we will just calculate it again...
# ------------------------
# Ok. I'm done with trying to make this work, and will simply rebuild it in first_dump I thought about.
# Just count every bar one by one until I hit any value lower than bar, so we can't put this bar inside.
# Very slow, but still not burned enough to google.
# ------------------------
# No idea how to make prev_solution work with 2 ways, cuz I made it working with ascending or equal values,
# with no intervals with only descending like: test8.
# ------------------------
# min_plato => value of bottom rectangle with min_height and whole length of histogram,
#              breaking length only when encounter 0, and starting a new one.
# ------------------------
# I need more test cases, an either create them or fail. Is it worth it to create them?


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

# test7 - failed -> I made calculations of areas when we encounter break_point or last_index,
#                   but I failed to create test_case or see that -> we should add +1 length to all indexes,
#                   before calculating areas...
test7 = [1, 2, 2]
test7_out = 4
print(largest_rectangle(test7))
assert test7_out == largest_rectangle(test7)

# test8 - failed -> ok, failed with descending flow
test8 = [5, 4, 1, 2]
test8_out = 8
print(largest_rectangle(test8))
