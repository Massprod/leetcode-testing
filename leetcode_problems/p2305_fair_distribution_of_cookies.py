# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag.
# You are also given an integer k that denotes the number of children to distribute all the bags of cookies to.
# All the cookies in the same bag must go to the same child and cannot be split up.
# The unfairness of a distribution is defined as the maximum total cookies obtained
#  by a single child in the distribution.
# Return the minimum unfairness of all distributions.
# -----------------------
# 2 <= cookies.length <= 8
# 1 <= cookies[i] <= 10 ** 5
# 2 <= k <= cookies.length
from random import randint


def distribute_cookies(cookies: list[int], k: int) -> int:
    # working_sol (52.97%, 97.90%) -> (930ms, 16.2mb)  time: O(k ** n) | space: O(k + n)
    # Keep track of cookies given per child.
    per_child: list[int] = [0 for _ in range(k)]
    min_unfair: list[int | float] = [float('inf')]

    def check(bag_index: int) -> None:
        # If all bags are used, we get maximum distribution.
        # max_dist == max_cookies at one child.
        if bag_index == len(cookies):
            # We need minimum of all maximum distributions
            min_unfair[0] = min(min_unfair[0], max(per_child))
            return
        # We can cull calls when number of childs with 0 bags(cookies),
        #  exceeding number of bags left. Because it will always give as HIGHEST.
        # And there's always can be an option with at least 1 bag per child.
        # Which is always going to be lower option than this. No reasons to calc it.
        if per_child.count(0) > len(cookies) - bag_index:
            return
        # Giving current BAG to every child possible.
        for x in range(k):
            # Give.
            per_child[x] += cookies[bag_index]
            # Check.
            check(bag_index + 1)
            # Reset.
            per_child[x] -= cookies[bag_index]
        return

    check(0)
    return min_unfair[0]


# Time complexity: O(k ** n) -> recursion with k options and depths of n, for every bag we can distribute it for k
# n - len of cookies_array^^| children => O(k ** n).
# k - number of child^^|
# Auxiliary space: O(k + n) -> creating list with all children as indexes => O(k) -> and recursion stack can be at max
#                              of n calls, when every bag is used => O(n).
# -----------------------
# Nah. Even with 2nd test case its already TLE. What can we cull or rebuild?
# Ok. Instead of trying to give all bags to every child, I can just give every bag once to all the childs with
#  tracking of bag_index. And extra cull calls when childs who doesn't have any bags given is more than bags left.
# Because we will always get HIGHEST result when bags are given to the One child. And it will always be overwritten by
# any other lower option, and we need LOWEST. So we need to always give at least 1 bag to a child.
# -----------------------
# Ok. It should be easy recursion with using every possible bag for every child once.
# And when last bag used, just find maximum value we have and then minimum value from all of these maximums.
# But it's O(8 ** 8) for max constraint, which I think is TLE or close to it.
# And I don't see how we can memorize this calls, cuz I want to store cookies per child in a list.
# It can't be arg of recursion, cuz it's always different number.
# Or it's need to be arg == list with cookies itself, but then how do we store it?
# Rebuild and save as tuple for every iteration? Dunno let's try 8 ** 8 at first.


test: list[int] = [8, 15, 10, 20, 8]
test_k: int = 2
test_out: int = 31
assert test_out == distribute_cookies(test, test_k)

test = [6, 1, 3, 2, 2, 4, 1, 2]
test_k = 3
test_out = 7
assert test_out == distribute_cookies(test, test_k)

test = [randint(1, 10 ** 5) for _ in range(8)]
test_k = 8
print(test)
# Passing max constraints.
print(distribute_cookies(test, test_k))
