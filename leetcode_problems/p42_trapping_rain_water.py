# Given n non-negative integers representing an elevation
# map where the width of each bar is 1,
# compute how much water it can trap after raining.

def rain_water(height: list[int]) -> int:
    # working_sol (5.3%, 35.77%) -> (3790ms, 16.1mb)  time: O(n**n) | space: O(n)
    volumes = []
    left = 0
    length = len(height)
    while left < (length - 1):
        if height[left + 1] < height[left]:
            busy_boxes = 0
            for x in range(left + 1, length):
                if x == length - 1 and height[x] > height[x - 1]:
                    right = x
                    rect_height = min(height[left], height[x])
                    rect_length = right - left - 1
                    tempo_vol = rect_height * rect_length
                    volumes.append(tempo_vol - busy_boxes)
                    left = right
                    break
                if x == length - 1 and height[x] < height[x - 1]:
                    left += 1
                    break
                if height[x] >= height[x + 1] and (height[x] >= height[left] or height[x] >= max(height[left + 1:])):
                    right = x
                    rect_height = min(height[left], height[x])
                    rect_length = right - left - 1
                    tempo_vol = rect_height * rect_length
                    volumes.append(tempo_vol - busy_boxes)
                    left = right
                    break
                if height[x] <= height[x + 1] and (height[x] >= height[left] or height[x] >= max(height[left + 1:])):
                    right = x
                    rect_height = min(height[left], height[x])
                    rect_length = right - left - 1
                    tempo_vol = rect_height * rect_length
                    volumes.append(tempo_vol - busy_boxes)
                    left = right
                    break
                busy_boxes += height[x]
        elif height[left + 1] >= height[left]:
            left += 1
    return sum(volumes)

# Time complexity: O(n**n) -> looping through whole input, and for every value looping through left values slice.
#                             worst case -> looping through every index
# Space complexity: O(n) -> volumes and slice sizes all depends on input_size, we're not storing slices for max(height)
#                           there's always one n - size slice and volumes of n - size depending on input.
#                           Extra 2 arrays of n - size.

# 100% sure I needed to use two_pointer's and scroll from left and right, but I wanted to solve it in one way first,
# and didn't get how can we skip walls from going right->left. Google time


def rain_water_next(height: list[int]) -> int:
    # working_sol (93.64%, 35.69%) -> (112ms, 16mb)  time: O(n) | space: O(1)
    volume = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                volume += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                volume += right_max - height[right]
            right -= 1
    return volume

# Time complexity: O(n) -> going once through whole input array.
# Space complexity: O(1) -> only extra constants, not changing with input.

# Googled solution. But I never encountered this problem before, there was something similar,
# but we were allowed to calc just left_right walls no matter what between.
# Btw my solution is slow af but working, which is already Ok.
# Maybe if I spend more time on it, I could see pattern like this solution.
# Cuz everytime we take wall on the right or left side ->
# there's always going to be a wall at least min(wall1, wall2) size ->
# if there's no such wall, water won't be trapped at all.
# And I was calculating every wall we encounter where water could be trapped.


test1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test1_out = 6
print(rain_water(test1))
print(rain_water_next(test1))
assert rain_water(test1) == test1_out
assert rain_water_next(test1) == test1_out

test2 = [4, 2, 0, 3, 2, 5]
test2_out = 9
print(rain_water(test2))
print(rain_water_next(test2))
assert rain_water(test2) == test2_out
assert rain_water_next(test2) == test2_out

test3 = [10, 11, 12, 8, 0, 4, 1, 0]
test3_out = 4
print(rain_water(test3))
print(rain_water_next(test3))
assert rain_water(test3) == test3_out
assert rain_water_next(test3) == test3_out

test4 = [10, 11, 12, 8, 0, 4, 4, 4]
test4_out = 4
print(rain_water(test4))
print(rain_water_next(test4))
assert rain_water(test4) == test4_out
assert rain_water_next(test4) == test4_out

# test5 - failed -> cuz I wasn't taking in credit that we can encounter right_wall, without diff point ->
#                   height[x] < height[x + 1] but height[x + 1] > height[left] and height[left] < height[x]
#                   (diff point -> point where water can stack on both sides of this point)
test5 = [5, 5, 4, 7, 8, 2, 6, 9, 4, 5]
test5_out = 10
print(rain_water(test5))
print(rain_water_next(test5))
assert rain_water(test5) == test5_out
assert rain_water_next(test5) == test5_out

test6 = [5, 5, 4, 7, 7, 8, 2, 6, 9, 4, 5]
test6_out = 10
print(rain_water(test6))
print(rain_water_next(test6))
assert rain_water(test6) == test6_out
assert rain_water_next(test6) == test6_out
