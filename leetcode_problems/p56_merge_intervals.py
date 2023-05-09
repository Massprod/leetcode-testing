# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals: list[list[int]]) -> list[list[int]]:
    def can_be_merged(merges: list[list[int]], start: int, end: int, start_index: int) -> dict:
        merge_indexes = []
        for y in range(start_index, len(merges)):
            check_start = merges[y][0]
            check_end = merges[y][1]
            if start <= check_start <= end <= check_end:
                merge_indexes.append(y)
                start = min(start, check_start)
                end = max(end, check_end)
            elif check_start <= start <= check_end <= end:
                merge_indexes.append(y)
                start = min(start, check_start)
                end = max(end, check_end)
        merge_data = {
            "indexes": merge_indexes,
            "new_limits": [start, end]
        }
        return merge_data

    for x in range(len(intervals)):
        try:
            start_val = intervals[x][0]
            end_val = intervals[x][1]
            if result := can_be_merged(intervals, start_val, end_val, x + 1):
                for index in result["indexes"]:
                    intervals.pop(index)
                intervals[x] = result["new_limits"]
        except IndexError:
            pass
    return intervals

# [1, 3] [2, 6]
# start1 = 1, end1 = 3, start2 = 2, end2 = 6
# start2 should be in range of (start1 - end1) -> start2 >= start1 and start2 <= end1
# end2 should be more than end1 -> end2 >= end1
# if reversed [2, 6] [1, 3]
# start1 = 2, end1 = 3, start2 = 1, end2 = 3
# start2 <= start1 and start2 <= end1
# end2 >= start1 and end2 <= end1


test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
test1_out = [[1, 6], [8, 10], [15, 18]]
print(merge(test1))

test2 = [[1, 4], [4, 5]]
test2_out = [[1, 5]]
print(merge(test2))
