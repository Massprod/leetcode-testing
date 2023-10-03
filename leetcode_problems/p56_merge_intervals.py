# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input.
# --------------------
# 1 <= intervals.length <= 10 ** 4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10 ** 4


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # working_sol (13.81%, 97.95%) -> (148ms, 20.7mb)  time: O(n * log n) | space: O(1)
    intervals.sort()
    # Inplace.
    for x in range(len(intervals)):
        try:
            # Starting values of interval.
            start: int = intervals[x][0]
            end: int = intervals[x][1]
            y: int = x + 1
            # Combine it with all intervals we can.
            while True:
                check_start: int = intervals[y][0]
                check_end: int = intervals[y][1]
                # New starts inside old.
                if start <= check_start <= end <= check_end:
                    end = check_end
                    intervals.pop(y)
                    intervals[x] = [start, end]
                # Old start inside new.
                elif check_start <= start <= check_end <= end:
                    start = check_start
                    intervals.pop(y)
                    intervals[x] = [start, end]
                # New fully inside old.
                elif start <= check_start <= check_end <= end:
                    intervals.pop(y)
                    intervals[x] = [start, end]
                # Old fully inside new.
                elif check_start <= start <= end <= check_end:
                    start = check_start
                    end = check_end
                    intervals.pop(y)
                    intervals[x] = [start, end]
                else:
                    break
        except IndexError:
            break
    return intervals


# Time complexity O(n * log n) -> sorting -> (n * log n) -> and only looping ONCE through whole input O(n),
# n - len of input array^^|       don't repeat any checks and single left_to_right path.
# Space complexity O(1) -> only constant's and changing input array inplace => O(1).
# --------------------
# Committed solution without additional function, cuz we can put everything inside for_loop.
# But there's no speed or memory win here, so leaving it like this is fine.
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


test: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
test_out: list[list[int]] = [[1, 6], [8, 10], [15, 18]]
test_t: list[list[int]] = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[1, 4], [4, 5]]
test_out = [[1, 5]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[1, 5], [4, 9], [9, 18], [5, 6], [2, 3], [4, 4], [0, 0]]
test_out = [[1, 18], [0, 0]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[0, 0], [0, 5], [4, 9], [4, 4], [100, 100], [5, 100]]
test_out = [[0, 100]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[1, 4], [0, 5]]
test_out = [[0, 5]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[0, 0], [1, 2], [5, 5], [2, 4], [3, 3], [5, 6], [5, 6], [4, 6], [0, 0], [1, 2], [0, 2], [4, 5]]
test_out = [[0, 6]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t

test = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
test_out = [[1, 10]]
test_t = merge(test)
assert len(test_t) == len(test_out)
for _ in test_out:
    assert _ in test_t
