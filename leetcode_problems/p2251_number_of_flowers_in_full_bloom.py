# You are given a 0-indexed 2D integer array flowers,
#  where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive).
# You are also given a 0-indexed integer array people of size n,
#  where people[i] is the time that the ith person will arrive to see the flowers.
# Return an integer array answer of size n,
#  where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
# --------------------------
# 1 <= flowers.length <= 5 * 10 ** 4
# flowers[i].length == 2
# 1 <= starti <= endi <= 10 ** 9
# 1 <= people.length <= 5 * 10 ** 4
# 1 <= people[i] <= 10 ** 9
from random import randint


def full_bloom_flowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    # working_sol (16.37%, 99.09%) -> (1179ms, 41.46mb)  time: O((n * 2log m) + 2(m * log m)) | space: O(2m + n)
    starts: list[int] = sorted([inter[0] for inter in flowers])
    ends: list[int] = sorted([inter[1] for inter in flowers])

    def bs(array: list[int], target: int, start: bool) -> int:
        left: int = 0
        right: int = len(array) - 1
        if start:
            # We need flowers which started blooming before and ON target day.
            # First value > target.
            while left < right:
                middle: int = (left + right) // 2
                if array[middle] <= target:
                    left = middle + 1
                else:
                    right = middle
            # Nothing higher, so it's whole array == last_index + 1.
            if array[left] <= target:
                return left + 1
            else:
                return left
        else:
            # We need flowers which STILL blooming ON target day.
            # First value >= target.
            while left < right:
                middle = (left + right) // 2
                if array[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
            # Nothing higher, so it's whole array == last_index + 1.
            if array[left] < target:
                return left + 1
            else:
                return left

    day_cache: dict[int, int] = {}
    for x in range(len(people)):
        day: int = people[x]
        # We can have duplicates, no reasons to rerun.
        if day in day_cache:
            people[x] = day_cache[day]
            continue
        # We need to know how many flowers started blooming
        #  before and ON this day.
        blooming: int = bs(starts, day, True)
        # And how many flowers already gone.
        gone: int = bs(ends, day, False)
        # (blooming - gone) == still blooming, and ppl can see them.
        people[x] = blooming - gone
        day_cache[day] = people[x]
    return people


# Time complexity: O((n * 2log m) + 2(m * log m)) -> creating array with all starts and sorting it => O(m + m * log m)
# m - len of input array: 'flowers'^^| -> creating array with all ends and sorting it => O(m + m * log m) ->
# n - len of input array: 'people'^^|  -> worst case == every day in people is unique -> we will BS on same size
#                                      arrays twice, to get started blooming and gone flowers => O(n * 2log m).
# Auxiliary space: O(2m + n) -> creating two new arrays with starts and ends from flowers with same size => O(2m) ->
#                            -> same worst case -> dictionary with all days included => O(n) ->
#                            -> repopulating input array with new values, and it will not change it's size.
# --------------------------
# Hints:
# !
# Notice that for any given time t, the number of flowers blooming at time t is equal
#  to the number of flowers that have started blooming minus the number of flowers
#  that have already stopped blooming.
# We can store the starting times in sorted order, which then allows us to binary search
#  to find how many flowers have started blooming for a given time t.
# We do the same for the ending times to find how many flowers have stopped blooming at time t.
# We can obtain these values efficiently using binary search.
# !
# So, essentially we want to know how many flowers is started blooming until AND on some day in ppl.
# And then we can find how many flowers already NOT blooming at this day, but this day should be included.
# Sort starts and ends separately to get them correctly.
# And for every day in ppl, just find this numbers with BS. Let's try.


test_flo: list[list[int]] = [[1, 6], [3, 7], [9, 12], [4, 13]]
test_ppl: list[int] = [2, 3, 7, 11]
test_out: list[int] = [1, 2, 2, 2]
assert test_out == full_bloom_flowers(test_flo, test_ppl)

test_flo = [[1, 10], [3, 3]]
test_ppl = [3, 3, 2]
test_out = [2, 2, 1]
assert test_out == full_bloom_flowers(test_flo, test_ppl)

test_flo = [[randint(1, 10 ** 4), randint(10 ** 4, 10 ** 9)] for _ in range(10 ** 3)]
test_ppl = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
print(test_flo)
print('!=========================!')
print(test_ppl)
