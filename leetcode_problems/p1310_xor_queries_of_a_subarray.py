# You are given an array arr of positive integers.
# You are also given the array queries where queries[i] = [lefti, righti].
# For each query i compute the XOR of elements from lefti to righti
#  (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
# Return an array answer where answer[i] is the answer to the ith query.
# -------------------------
# 1 <= arr.length, queries.length <= 3 * 10 ** 4
# 1 <= arr[i] <= 10 ** 9
# queries[i].length == 2
# 0 <= lefti <= righti < arr.length


def xor_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    # working_sol (73.41%, 81.84%) -> (299ms, 31.18mb)  time: O(n + k) | space: O(n + k)
    xor_prefixes: list[int] = []
    xor_prefix: int = 0
    for num in arr:
        xor_prefix ^= num
        xor_prefixes.append(xor_prefix)
    out: list[int] = []
    # If we take every XOR prefix, we will see at they cancel each other.
    # Like [1, 2, 3, 4] <- prefix of 2 will contain all the XORs in [1, 2].
    # And if we use prefix of 4, it already contains all changes from [1, 2, 3, 4].
    # We can use it to get XOR of a range [3, 4].
    # Because the prefix of 2 will eliminate all the previous XORs from [1, 2] range.
    # And leave us with [3, 4].
    # Extra moment, if start of a range if `0` we don't have a prefix at all,
    #  so we can just use the end of the range (nothing to remove).
    for left, right in queries:
        if left:
            left -= 1
            out.append(xor_prefixes[left] ^ xor_prefixes[right])
            continue
        out.append(xor_prefixes[right])
    return out


# Time complexity: O(n + k) <- n - length of the input array `arr`, k - length of the input array `queries`.
# Always traversing `arr` to get all the prefixes, once => O(n).
# -------------------------
# Auxiliary space: O(n + k)
# `xor_prefixes` <- allocates space for each index of `arr` => O(n).
# `out` <- allocates space for each index of `queries` => O(n + k).


test_arr: list[int] = [1, 3, 4, 8]
test_queries: list[list[int]] = [[0, 1], [1, 2], [0, 3], [3, 3]]
test_out: list[int] = [2, 7, 14, 8]
assert test_out == xor_queries(test_arr, test_queries)

test_arr = [4, 8, 2, 10]
test_queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
test_out = [8, 0, 4, 4]
assert test_out == xor_queries(test_arr, test_queries)
