# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.
# --------------------
# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000


def find_longest_chain(pairs: list[list[int]]) -> int:
    # working_sol (96.85%, 65.76%) -> (190ms, 16.9mb)  time: O(n * log n) | space: O(1)
    # Essentially we need length of continuous sequence,
    #  where prevEND < newSTART.
    # So if we want to get maximum sequence with that rule,
    #  we need to take minEND from all and start building from it.
    # Which leads us to sorting by ENDs first.
    pairs.sort(key=lambda x_: x_[1])
    cur_count: int = 1
    # Then setting this minEND.
    cur_end: int = pairs[0][1]
    for x in range(len(pairs)):
        # We only care about newSTART > prevEND.
        if pairs[x][0] <= cur_end:
            continue
        # ! pairs[i] = [lefti, righti] and lefti < righti !
        # And maintaining this minEND, so we can greedy
        #  count all newSTARTs correctly.
        cur_end = pairs[x][1]
        cur_count += 1

    return cur_count


# Time complexity: O(n * log n) -> sorting by ENDs, in place => O(n * log n) -> extra traversing sorted pairs => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used, none of them depends on input => O(1).
# --------------------
# Ok. I was correct about counting non overlapping intervals, but I was sorting with STARTs when
#  actually we need to sort with ENDs. Seen it only after making correct recursion.
# With recursion, we're just building sequence from every possible index, and they're built with the same rule ->
# -> pair[x][0] > cur_end. And because cur_end is always minimum END from continuous sequence we're building.
# We can just sort it by ENDs and count these occurrences.
# With sorting by ENDs we will always use minimum correctly, like: [-7, -1] , [0, 10], [1, 2], [3, 10].
# When sorted by STARTs we will reset at [1] index cur_end to 10, and it's going to miss [1, 2] == incorrect.
# When sorted by ENDs it will be [-7, -1], [1, 2], [0, 10], [3, 10] <- and we can correctly build sequence when,
#  prevEND < newSTART.
# Don't actually need to consider cur_start either, cuz we will always use minEND anyway.


test: list[list[int]] = [[1, 2], [2, 3], [3, 4]]
test_out: int = 2
assert test_out == find_longest_chain(test)

test = [[1, 2], [7, 8], [4, 5]]
test_out = 3
assert test_out == find_longest_chain(test)

test = [[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]
test_out = 3
assert test_out == find_longest_chain(test)

test = [[7, 9], [4, 5], [7, 9], [-7, -1], [0, 10], [3, 10], [3, 6], [2, 3]]
test_out = 4
assert test_out == find_longest_chain(test)
