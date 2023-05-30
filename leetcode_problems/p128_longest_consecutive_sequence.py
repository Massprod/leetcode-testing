# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# !
# You must write an algorithm that runs in O(n) time.!
# -----------------------
# 0 <= nums.length <= 105  ,  -109 <= nums[i] <= 109


def longest_consecutive(nums: list[int]) -> int:
    # working_sol (53.27%, 11,1%) -> (458ms, 34mb)  time: O(n) | space: O(n)
    original: dict[int] = {}
    for num in nums:
        original[num] = False
    consecutive: int = 0
    for key in original.keys():
        if original[key] is False:
            original[key] = True
            value: int = key - 1
            current_streak: int = 1
            while (value in original) and (original[value] is False):
                original[value] = True
                current_streak += 1
                value -= 1
            value = key + 1
            while (value in original) and (original[value] is False):
                original[value] = True
                current_streak += 1
                value += 1
            consecutive = max(consecutive, current_streak)
    return consecutive


# Time complexity: O(n) -> traversing once to create dictionary with all values from original list => O(n) ->
# n - len of input_list^^ -> assuming that every search in dictionary is hash operation, and we can call that => O(1) ->
#                         -> leading us to O(n)
# Space complexity: O(n) -> extra space to store dictionary with same values as original list => O(n)
# -----------------------
# Still don't think that is correct to call dict_search as O(1) if we're searching multiple values,
# because we're still doing N - operations just with O(1) time for every single one of them,
# but all I could see is either HASH searching or sorting and counting after that.
# So I was correct on thinking about solution that we can't solve it in O(n) without some extra rule,
# like this HASH search. But w.e still correct idea just need to know this rule for a future use.
# -----------------------
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
print(longest_consecutive(test1))
assert test1_out == longest_consecutive(test1)

test2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
test2_out = 9
print(longest_consecutive(test2))
assert test2_out == longest_consecutive(test2)
