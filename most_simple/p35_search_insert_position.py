# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

def search_insert(nums: list[int], target: int) -> int:
    length = len(nums)
    if length == 0:
        return 0
    if nums[-1] < target:
        return length
    if nums[0] > target:
        return 0
    x, y = 0, (length - 1)
    while x < y:
        if nums[x] == target:
            return x
        if nums[y] == target:
            return y
        if target > nums[x]:
            if target < nums[x + 1] and target != nums[x +1]:
                return x + 1
        if target < nums[y]:
            if target > nums[y - 1] and target != nums[y - 1]:
                return y
        if nums[x] < target < nums[y]:
            x += 1
            y -= 1


test1 = [1, 3, 5, 6]
test1_target = 5
test1_out = 2
print(search_insert(test1, test1_target))

test2 = [1, 3, 5, 6]
test2_target = 2
test2_out = 1
print(search_insert(test2, test2_target))

test3 = [1, 3, 5, 6]
test3_target = 7
test3_out = 4
print(search_insert(test3, test3_target))
