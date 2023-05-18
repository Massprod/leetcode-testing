# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# 1 <= heights.length <= 105  ,  0 <= heights[i] <= 104

def largest_rectangle(heights: list[int]) -> int:
    bars_on_route: dict[int] = {}
    min_height: int = heights[0]
    length: int = 0
    max_area: int = 0
    break_point: int = 0
    for index in range(len(heights)):
        if heights[index] != 0:
            bars_on_route[index] = 1
        else:
            bars_on_route[index] = 0
        if heights[index] != 0:
            length += 1
        if heights[index] < min_height and heights[index] != 0:
            min_height = heights[index]
        if heights[index] == 0:
            min_plato = min_height * length
            max_area = max(max_area, min_plato)
            if index != (len(heights) - 1):
                min_height = heights[index + 1]
            length = 0
        if heights[index] >= heights[index - 1] and index > 0 and heights[index] != 0:
            for key in bars_on_route.keys():
                if break_point <= key < index:
                    if heights[key] != 0:
                        bars_on_route[key] += 1
        if (heights[index] < heights[index - 1] and index > 0) or (index == (len(heights) - 1)):
            for key in bars_on_route.keys():
                if key >= break_point:
                    bar_area: int = heights[key] * bars_on_route[key]
                    max_area = max(max_area, bar_area)
            break_point = index
    min_plato: int = min_height * length
    return max(max_area, min_plato)

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

