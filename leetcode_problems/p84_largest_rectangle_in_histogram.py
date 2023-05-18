# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# 1 <= heights.length <= 105  ,  0 <= heights[i] <= 104

def largest_rectangle(heights: list[int]) -> int:
    bars_on_route: dict[int] = {}
    min_height: int = 1
    length: int = 0
    max_area: int = 0
    break_point: int = 0
    for index in range(len(heights)):
        length += 1
        if heights[index] < min_height and heights[index] != 0:
            min_height = heights[index]
        if heights[index] == 0:
            min_plato = min_height * length
            max_area = max(max_area, min_plato)
            length = 0
        if index not in bars_on_route.keys():
            bars_on_route[index] = 1
        if (heights[index] < heights[index - 1] and index > 0) or (index == (len(heights) - 1)):
            for key in bars_on_route.keys():
                if key >= break_point:
                    bar_area: int = heights[key] * bars_on_route[key]
                    max_area = max(max_area, bar_area)
            break_point = index
            continue
        if heights[index] > heights[index - 1] and index > 0:
            for key in bars_on_route.keys():
                if break_point <= key < index:
                    bars_on_route[key] += 1

    min_plato: int = min_height * length
    return max(max_area, min_plato)


# I need more test cases, an either create them or fail. Is it worth it to create them?


test1 = [2, 1, 5, 6, 2, 3]
test1_out = 10
print(largest_rectangle(test1))

test2 = [2, 4]
test2_out = 4
print(largest_rectangle(test2))
