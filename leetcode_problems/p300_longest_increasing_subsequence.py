# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# -------------------
# 1 <= nums.length <= 2500
# -10 ** 4 <= nums[i] <= 10 ** 4
from random import randint


def length_of_list(nums: list[int]) -> int:
    # working_sol (72.57%, 93.58%) -> (2141ms, 16.6mb)  time: O(n * log n) | space: O(n)
    # unique case, no reasons to bother
    if len(nums) == 1:
        return 1
    # All values can be counted as SUBSEQ by themselves.
    # seq_lens, stores => LEN of SUBSEQ to some index.
    seq_lens: list[int] = [1] + [1 for _ in nums[1:]]
    # Starting from 1, cuz first value is always SUBSEQ by itself and there's only 1 PATH to it.
    for x in range(1, len(nums)):
        # Setting defaults.
        # max_seq will always be updated in a loops,
        # if it's not then there's no correct SUBSEQ leading to this index.
        max_seq: int = 0
        # If values are equal, then every PATH leading to it
        # can be used to lead for the same value.
        # Same goes for a SUBSEQ 1, 2, 3, 3 -> 1, 2, 3 | 1, 2, 3
        # So it can be copied.
        if nums[x] == nums[x - 1]:
            seq_lens[x] = seq_lens[x - 1]
        # If value is higher than previous, then we need to find
        # the longest SUBSEQ and increment by it.
        if nums[x] > nums[x - 1]:
            # Starting from previous element, cuz it's first index
            # from who we can build correct SUBSEQ.
            y: int = x - 1
            # No reasons to check Y after (-1 + max_seq) == INDEX,
            # because we already found max_seq and there's nothing
            # higher can be constructed after this INDEX.
            # Like -> 1,2,3,4 => on 4 we already know that max_seq is 3
            # and anything before INDEX == (-1 + 3) == 2 is going to be LOWER than max_seq.
            while y > (-1 + max_seq):
                # Ignore everything that's higher or equal.
                # Higher can't correctly lead us to X.
                # Equal can't either.
                if nums[x] > nums[y]:
                    # Everytime we found SUBSEQ with bigger size, update.
                    if max_seq < seq_lens[y]:
                        max_seq = seq_lens[y]
                y -= 1
            # Increment by maximum size SUBSEQ.
            seq_lens[x] += max_seq
        # Actual repeat of previous part, but with start from
        # x - 2, cuz we already now that's nums[x - 1] > nums[x].
        # So we can't start any correct SUBSEQ from it.
        if nums[x] < nums[x - 1]:
            y = x - 2
            # Same limit approach, as before.
            while y > (-1 + max_seq):
                if nums[x] > nums[y]:
                    if max_seq < seq_lens[y]:
                        max_seq = seq_lens[y]
                y -= 1
            seq_lens[x] += max_seq
    # Could be done while we're searching.
    # But then we could call it for every index update,
    # and it's O(n) either way.
    return max(seq_lens)


# Time complexity: O(n * log n) -> creating array with size of n => O(n) -> traversing whole input_array once ->
# n - len of input_array^^|      -> but for every index in the array we're doing backwards path(walk/traverse)
#                                from this index to the limit(-1 + max_seq) -> so it should be O(n * log n) =>
#                                => where (log n) is always changing from 1 to (n - 1).
# Auxiliary space: O(n) -> creating extra array with size of n, always => O(n) -> extra 2 constant INTs used => O(1).
# -------------------
# Deleted part with counting paths, and made a little improvement for a Y loop.
# Already been thinking to change it, but after failing commits and rushing forgot to add.
# We can drop Y loop once we get to INDEX == MAX_SEQ, because there's no way something after this index
# will have more LENGTH than MAX_SEQ we already found.
# Like 1,2,3,4,5 -> no reasons to check Y after 3 for 4 because we already know that MAX_SEQ == 3.
# -------------------
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
# Same as p673, but now we don't need to find anything except max_length.
# And I'm already solved it with O(n * log n).


test1 = [10, 9, 2, 5, 3, 7, 101, 18]
test1_out = 4
assert test1_out == length_of_list(test1)

test2 = [0, 1, 0, 3, 2, 3]
test2_out = 4
assert test2_out == length_of_list(test2)

test3 = [7, 7, 7, 7, 7, 7, 7]
test3_out = 1
assert test3_out == length_of_list(test3)

test: list[int] = []
for _ in range(1, 2500):
    test.append(randint(-10 ** 4, 10 ** 4))
print(test)
print(length_of_list(test))
