# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals: list[list[int]]) -> list[list[int]]:
    # working_sol (7.90%, 17.18%) -> (174ms, 20.4mb)  time: O(n) | space: O(1)
    intervals.sort()

    def can_merge(to_merge: list[list[int]], start_index: int) -> None:
        start: int = to_merge[start_index][0]
        end: int = to_merge[start_index][1]
        y: int = start_index + 1
        while True:
            check_start: int = to_merge[y][0]
            check_end: int = to_merge[y][1]
            if start <= check_start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif check_start <= start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif start <= check_start <= check_end <= end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            elif check_start <= start <= end <= check_end:
                start = min(start, check_start)
                end = max(end, check_end)
                to_merge.pop(y)
                to_merge[start_index] = [start, end]
                continue
            return
    for x in range(len(intervals)):
        try:
            can_merge(intervals, x)
        except IndexError:
            break
    return intervals

# Time complexity O(n) -> we're sorting (log n), and only looping ONCE through whole input,
#                         don't repeat any checks and single left_to_right path.
# Space complexity O(1) -> only constant's and changing input array inplace.

# ----------------------------
# Ok. First of all, I solved this on my first_commit, but it was too slow.
# Second I tried to delete, replace elements without sorting and stuck on this for a while.
# Actually it worked, but time_Limit.
# Next time, consider rebuilding if I can't make just ONE_PART to work, not whole IDEA.
# ----------------------------
# 167/170 <- again Time_limit, rebuild, but we're still scrolling over whole input.
#            Guess there's no way to make this work without sorting, cuz only with some ordering,
#            we can walk from left_to_right and collect everything until we hit some higher value,
#            and change our start, end on this value.


test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
test1_out = [[1, 6], [8, 10], [15, 18]]
for _ in merge(test1):
    assert _ in test1_out
print(merge(test1))

test2 = [[1, 4], [4, 5]]
test2_out = [[1, 5]]
for _ in merge(test2):
    assert _ in test2_out
print(merge(test2))

test3 = [[1, 5], [4, 9], [9, 18], [5, 6], [2, 3], [4, 4], [0, 0]]
test3_out = [[1, 18], [0, 0]]
for _ in merge(test3):
    assert _ in test3_out
print(merge(test3))

test4 = [[0, 0], [0, 5], [4, 9], [4, 4], [100, 100], [5, 100]]
test4_out = [[0, 100]]
for _ in merge(test4):
    assert _ in test4_out
print(merge(test4))

test5 = [[1, 4], [0, 5]]
test5_out = [[0, 5]]
for _ in merge(test5):
    assert _ in test5_out
print(merge(test5))

test6 = [[0, 0], [1, 2], [5, 5], [2, 4], [3, 3], [5, 6], [5, 6], [4, 6], [0, 0], [1, 2], [0, 2], [4, 5]]
test6_out = [[0, 6]]
for _ in merge(test6):
    assert _ in test6_out
print(merge(test6))

test7 = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
test7_out = [[1, 10]]
for _ in merge(test7):
    assert _ in test7_out
print(merge(test7))
