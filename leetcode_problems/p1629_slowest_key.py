# A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.
# You are given a string keysPressed of length n, where keysPressed[i]
#  was the ith key pressed in the testing sequence,
#  and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released.
# Both arrays are 0-indexed. The 0th key was pressed at the time 0,
#  and every subsequent key was pressed at the exact time the previous key was released.
# The tester wants to know the key of the keypress that had the longest duration.
# The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1],
#  and the 0th keypress had a duration of releaseTimes[0].
# Note that the same key could have been pressed multiple times during the test,
#  and these multiple presses of the same key may not have had the same duration.
# Return the key of the keypress that had the longest duration.
# If there are multiple such keypresses,
#  return the lexicographically largest key of the keypresses.
# ------------------------------
# releaseTimes.length == n
# keysPressed.length == n
# 2 <= n <= 1000
# 1 <= releaseTimes[i] <= 10 ** 9
# releaseTimes[i] < releaseTimes[i+1]
# keysPressed contains only lowercase English letters.


def slowest_key(release_times: list[int], keys_pressed: str) -> str:
    # working_sol (89.54%, 73.86%) -> (48ms, 16.61mb)  time: O(n) | space: O(1)
    slowest: str = keys_pressed[0]
    cur_max: int = release_times[0]
    for index in range(1, len(release_times)):
        cur_time: int = release_times[index] - release_times[index - 1]
        if cur_time > cur_max:
            slowest, cur_max = keys_pressed[index], cur_time
        elif cur_time == cur_max and slowest < keys_pressed[index]:
            slowest = keys_pressed[index]
    return slowest


# Time complexity: O(n) <- n - length of the input array `release_times` or string `keys_pressed`.
# Always traversing every index from input array and string, once => O(n).
# ------------------------------
# Auxiliary space: O(1)
# Only two constant variables used, none of them depends on input => O(1).


test_times: list[int] = [9, 29, 49, 50]
test_keys: str = "cbcd"
test_out: str = "c"
assert test_out == slowest_key(test_times, test_keys)

test_times = [12, 23, 36, 46, 62]
test_keys = "spuda"
test_out = "a"
assert test_out == slowest_key(test_times, test_keys)
