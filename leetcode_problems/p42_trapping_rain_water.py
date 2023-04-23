# Given n non-negative integers representing an elevation
# map where the width of each bar is 1,
# compute how much water it can trap after raining.

def rain_water(height: list[int]) -> int:
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
                busy_boxes += height[x]
                if x == length - 1:
                    left += 1
        elif height[left + 1] >= height[left]:
            left += 1
    return sum(volumes)



test1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test1_out = 6
print(rain_water(test1))

test2 = [4, 2, 0, 3, 2, 5]
test2_out = 9
print(rain_water(test2))

test3 = [10, 11, 12, 8, 0, 4, 1, 0]
test3_out = 4
print(rain_water(test3))

test4 = [10, 11, 12, 8, 0, 4, 4, 4]
test4_out = 4
print(rain_water(test4))
