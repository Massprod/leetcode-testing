# Given an array of integers arr, and three integers a, b and c.
# You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#   - 0 <= i < j < k < arr.length
#   - |arr[i] - arr[j]| <= a
#   - |arr[j] - arr[k]| <= b
#   - |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.
# -------------------
# 3 <= arr.length <= 100
# 0 <= arr[i] <= 1000
# 0 <= a, b, c <= 1000


def count_good_triplets(arr: list[int], a: int, b: int, c: int) -> int:
    # working_sol (33.30%, 42.78%) -> (295ms, 16.50mb)  time: O(n) | space: O(1)
    out: int = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if ((abs(arr[i] - arr[j]) <= a)
                        and (abs(arr[j] - arr[k]) <= b)
                        and (abs(arr[i] - arr[k]) <= c)):
                    out += 1
    return out


# Time complexity: O(n ** 3) <- n - length of the input array `arr`.
# Always 3 nested loops to search triplets => O(n ** 3).
# -------------------
# Auxiliary space: O(1)


test: list[int] = [3, 0, 1, 1, 9, 7]
test_a: int = 7
test_b: int = 2
test_c: int = 3
test_out: int = 4
assert test_out == count_good_triplets(test, test_a, test_b, test_c)

test = [1, 1, 2, 2, 3]
test_a = 0
test_b = 0
test_c = 1
test_out = 0
assert test_out == count_good_triplets(test, test_a, test_b, test_c)
