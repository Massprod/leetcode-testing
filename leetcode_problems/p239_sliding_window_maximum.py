# You are given an array of integers nums, there is a sliding window of size k which is moving
#   from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Return the max sliding window.
# ----------------
# 1 <= nums.length <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4
# 1 <= k <= nums.length
from random import randint
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # working_sol (32.63%, 44.73%) -> (1743ms, 33.2mb)  time: O(n) | space: O(n + k)
    max_windows: list[int] = []
    que: deque = deque()
    # Storing maximum value at the start of a que.
    # First window:
    for _ in range(k):
        # Delete everything that's lower than new_value.
        while len(que) != 0 and nums[que[-1]] <= nums[_]:
            que.pop()
        que.append(_)
    # Maximum of the first_window.
    max_windows.append(nums[que[0]])
    # Any other windows is the same, except part with expired.
    # We need to delete expired indexes, cuz they're not in a current window:
    # current window left limit == x - (k - 1) <- -1 for 0 indexed
    #                right limit == x
    for x in range(k, len(nums)):
        while len(que) != 0 and x - (k - 1) > que[0]:
            que.popleft()
        while len(que) != 0 and nums[que[-1]] <= nums[x]:
            que.pop()
        que.append(x)
        max_windows.append(nums[que[0]])
    return max_windows


# Time complexity: O(n) -> in the worst case with array being only descending we're going to add every index
# n - len of input_array^^| into a que once => O(n) -> extra to that we're going to pop only part of this elements
#                           while their expired => O(log n) -> but on median we're going to delete these elements
#                           for at least once when there's some new_value which is higher ->
#                           -> like [1,2,3,4,5] k == 1, we just add and delete every index, if k is higher
#                           we're still deleting everything from a que when last index checked => O(n) + O(n - 1).
#                           But if last element isn't highest, like [5, 4, 3, 2, 1] k == 3 ->
#                           -> again everything except last 3 elements deleted once => O(n - 3) => O(log n) ->
#                           -> depending on k only part of the input_array will be deleted from a que.
#                           But no matter the k, every index will be added once => O(n).
# Auxiliary space: O(n + k) -> in the worst case k == 1, so every possible index of input_array will be added in
#                           max_windows => O(n).
#                           On median, it's going to be only a part of input_array => O(log n).
#                           Extra to this we're storing a que of size k = O(k).
# ----------------
# Ok. List with insertion is failing as well.
# Guess I don't know some theory about deque.
# We can use deque to store everything, but if we found something bigger we can delete all lower
# elements. From right -> left deleting everything lower than new_element.
# Extra to this we need to delete EXPIRED elements, which isn't in range(x - (k - 1), x).
# Because they're not in a current window range  == (x - (k - 1), x).
# ----------------
# Heap failed, dictionary failed. Worked for cases with 10 ** 4, but wit normal dispersion.
# With case when every new value is just lower by 1, we're extra checking for a new max_value,
# and it's too slow.
# Taking hints -> ! How about using a data structure such as deque (double-ended queue)?
# Remove redundant elements and the queue should store only elements that need to be considered. !
# ! only elements that need to be considered ! <- what these elements?
# If we use just deque without extra sorting elements it gives nothing.
# But if we sort it's still at least (log n) for insertion of every element.


test1 = [1, 3, -1, -3, 5, 3, 6, 7]
test1_k = 3
test1_out = [3, 3, 5, 5, 6, 7]
assert test1_out == max_sliding_window(test1, test1_k)

test2 = [1]
test2_k = 1
test2_out = [1]
assert test2_out == max_sliding_window(test2, test2_k)

test3 = [
    3867, -7657, 4795, -300, -5471, 1530, 9353, 3679, 2237, 8612, -3682, -3063, 7235, -4599, 1513, 5448,
    -6593, -4033, 1933, 3191, 5552, -7442, 3827, 7766, -4982, -3385, -2968, -3309, 6272, -4061, -7193,
    4598, 5705, 1844, -8664, 1452, 7808, 9737, -999, -8206, 990, -9181, 2485, -7048, -4276, -2217, -9168,
    7673, 9607, 535, -839, -6168, -3221, 208, 9890, 6434, 4341, 4518, 7944, -9669, -439, -9101, 4517, -183,
    -8904, 3448
]
test3_k = 9
test3_out = [
    9353, 9353, 9353, 9353, 9353, 9353, 9353, 8612, 8612, 8612, 7235, 7235, 7235, 5552, 5552, 7766, 7766, 7766, 7766,
    7766, 7766, 7766, 7766, 7766, 6272, 6272, 6272, 6272, 7808, 9737, 9737, 9737, 9737, 9737, 9737, 9737, 9737, 9737,
    2485, 7673, 9607, 9607, 9607, 9607, 9607, 9607, 9890, 9890, 9890, 9890, 9890, 9890, 9890, 9890, 9890, 7944, 7944,
    7944
]
assert test3_out == max_sliding_window(test3, test3_k)

test4 = [
    -1955, -1781, 367, -1624, -8654, -3696, 7188, -4752, -5004, 964, 6845, -2442, -219, 970, 392, 1398, 571,
    -4478, -9186, 868, -208, -9638, 3952, 9374, 9383, 8558, -8622, 620, -7870, 5568, 2261, -7824, 5305, -3578,
    5148, 7364, -2976, -356, -8136, -4241, -8994, 172, 688, -6590, -6691, -1469, 8152, 9304, -5343, -7612, -6871,
    7921, 6071, -1446, 1800, -8515, 8418, -7444, 1652, -614, 4243, 3301, 2541, 7138, 8634, -2006, 6826, 1322, -6419,
    2957, 2836, -1021, 795, -75, -7510, 758, 6186, -5494, 593, 6929, 2201, -4225, -9960, -8016, 5951, -5564, -2379,
    9712, 6178, 2351, 7824, 7814, -6348, 4313, 897, -4790, 5310, 6564, 5289, -9221, -7910, -3421, -9895, 4318, 846,
    -3827, -1033, -4746, -1529, -7578, -3106, -3204, -5791, -6004, -9346, -8691, -9458, -4948, -2648, 2374, -7499, 7001,
    -2116, 9479, -1579, 6209, 1148, -3653, 8153, 8813, -8265, 5819, 6311, -5633, -5331, -3275, -4001, -4780, 2113,
    -2445, -7730, -5286, -8927, 819, 6052, -2179, 7231, 7650, -64, -8975, -566, 3969, 1908, 9204, 5059, 8903, 9454
]
test4_k = 15
test4_out = [
    7188, 7188, 7188, 7188, 7188, 7188, 7188, 6845, 6845, 9374, 9383, 9383, 9383, 9383, 9383, 9383, 9383, 9383,
    9383, 9383, 9383, 9383, 9383, 9383, 9383, 8558, 7364, 7364, 7364, 7364, 7364, 7364, 8152, 9304, 9304, 9304,
    9304, 9304, 9304, 9304, 9304, 9304, 9304, 9304, 9304, 9304, 9304, 9304, 8418, 8418, 8634, 8634, 8634, 8634,
    8634, 8634, 8634, 8634, 8634, 8634, 8634, 8634, 8634, 8634, 8634, 6929, 6929, 6929, 6929, 6929, 6929, 6929,
    6929, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 9712, 7824, 7824,
    7824, 7814, 6564, 6564, 6564, 6564, 6564, 6564, 5289, 4318, 4318, 4318, 4318, 4318, 846, 2374, 2374, 7001,
    7001, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 9479, 8813, 8813,
    8813, 8813, 8813, 8813, 6311, 6311, 7231, 7650, 7650, 7650, 7650, 7650, 7650, 9204, 9204, 9204, 9454
]
assert test4_out == max_sliding_window(test4, test4_k)

test: list[int] = []
for _ in range(10 ** 3):
    test.append(randint(-10 ** 4, 10 ** 4))
test_k: int = randint(1, len(test))
print(test)
print(test_k)
