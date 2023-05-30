# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# !
# You must write an algorithm that runs in O(n) time.!
# -----------------------
# 0 <= nums.length <= 105  ,  -109 <= nums[i] <= 109


def longest_consecutive(nums: list[int]) -> int:
    pass


# Yeah. That's it, we use HASH operations which always take O(1) time,
# and just checking every value as I wanted but not from an original list.
# Ok. Guess for the future use => if we use some HASH table we can call searching in it O(1).
# -----------------------
# Time -> O(n) -> How?
# Obvious basic solution is to check every number left_right sides for values of num-1, num+1, but it's (n * n).
# With while or recursion for like I did in word_search_matrix, encounter some num-1 and start search from it with
# lowest_value - 1, highest_value + 1.
# Way I see to speed this, is sort, than we could just walk from lowest_highest and record only -+1 changes.
# But sorting is at least O(n * (log n)).
# Either I don't know some method for this like bit_stuff, or it's same as p148.
# Where's recursion without saving a result was counted as O(1) space, when it shouldn't.
# No reasons to waste time for trying to solve it on my own. Because it's can't be done in O(n) without some rules,
# like in p148, or it's task with bit operations which I have so little experience and don't see it.


test1 = [100, 4, 200, 1, 3, 2]
test1_out = 4

test2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
test2_out = 9
