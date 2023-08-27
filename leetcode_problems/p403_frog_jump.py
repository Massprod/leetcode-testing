# A frog is crossing a river. The river is divided into some number of units,
#  and at each unit, there may or may not exist a stone.
# The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order,
#  determine if the frog can cross the river by landing on the last stone.
# Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.
# The frog can only jump in the forward direction.
# ------------------
# 2 <= stones.length <= 2000
# 0 <= stones[i] <= 2 ** 31 - 1
# stones[0] == 0
# stones is sorted in a strictly increasing order.


def can_cross(stones: list[int]) -> bool:
    # working_sol (95.93%, 37.80%) -> (108ms, 26mb)  time: O(n) | space: O(n)
    recur_cache: dict[tuple[int, int]: bool] = {}
    # ! stones is sorted in a strictly increasing order. !
    # Assume there's no duplicates.
    fast_stones: set[int] = set(stones)

    def jump(pos: int, dist: int) -> bool:
        if (pos, dist) in recur_cache:
            return recur_cache[pos, dist]
        # Position we needed to reach.
        # Insta return, cuz we only care about its reachability.
        if pos == stones[-1]:
            return True
        # 3 options to consider for making a jump:
        # k + 1, k - 1, k.
        # K -> distance we jumped before.
        # First.
        option: int = dist - 1
        # ! frog can only jump in the forward direction !
        # All options should be > 0.
        if option > 0 and pos + option in fast_stones:
            # If path found, insta return.
            if jump(pos + option, option):
                return True
        option = dist + 1
        # Always taking positive values, so +1 can't go negative or 0.
        if pos + option in fast_stones:
            if jump(pos + option, option):
                return True
        option = dist
        if option > 0 and pos + option in fast_stones:
            if jump(pos + option, option):
                return True
        # Reusing Failed paths, with cache.
        recur_cache[pos, dist] = False
        return recur_cache[pos, dist]

    return jump(0, 0)


# Time complexity: O(n) -> standard recursion time complexity is O(3 ** n), but I still can't get how to calc
# n - len of input array^^| caching correctly, like we're reusing most of the calls but how to calc it? ->
#                           -> in case like: [0, 1, 2, 3 .. s + 1] it's just O(n), but we can visit every index with
#                           3 options, how? Can't find any normal data on that, sticking to O(n) <- cuz when im
#                           counting every call of the recursion with max_constraints, it's always in range of length.
#                           Might be x2, x3 but not like it's exponential or logarithmic, stick to linear.
# Auxiliary space: O(n) -> saving every recursion call, should be linear as well => O(n).
# ------------------
# Should be standard DP problem. We can just make 3 options K, K + 1, K - 1.
# Insta return if last index found, otherwise save and reuse.
# Dunno about bot -> top, but top -> down should be correct. Let's try.


test: list[int] = [0, 1, 3, 5, 6, 8, 12, 17]
test_out: bool = True
assert test_out == can_cross(test)

test = [0, 1, 2, 3, 4, 8, 9, 11]
test_out = False
assert test_out == can_cross(test)

test = [0, 2]
test_out = False
assert test_out == can_cross(test)

test = [0, 1, 3, 6, 10, 13, 15, 18]
test_out = True
assert test_out == can_cross(test)
