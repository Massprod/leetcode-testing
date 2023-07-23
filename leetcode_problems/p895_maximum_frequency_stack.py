# Design a stack-like data structure to push elements to the stack
#   and pop the most frequent element from the stack.
# Implement the FreqStack class:
#   FreqStack() constructs an empty frequency stack.
#   void push(int val) pushes an integer val onto the top of the stack.
#   int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element,
#   the element closest to the stack's top is removed and returned.
# ----------------------
# 0 <= val <= 10 ** 9
# At most 2 * 10 ** 4 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before calling pop.


class FreqStack:
    # working_sol (66.31%, 29.62%) -> (318ms, 25.1mb)

    def __init__(self):
        # All added keys and times they pushed(used) == usage.
        self.keys: dict[int, int] = {}
        # Keys -> time of USAGE for any KEY^^
        # Values -> keys itself, which was used Keys amount of times.
        # Because we're adding keys one_by_one their usage is always,
        # just increased by 1. And we can delete them 1 by 1 in correct order.
        self.usage: dict[int, list[int]] = {}
        # Most usage of all KEYS.
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        # If KEY not present, add and set its usage to 1.
        # First encounter.
        if val not in self.keys:
            self.keys[val] = 1
            # Every KEY pushed just once, can be placed
            # with usage == 1.
            if 1 not in self.usage:
                self.usage[1] = [val]
            else:
                self.usage[1].append(val)
            # Can be first_encounter for cur_KEY, but not first KEY.
            self.max_freq = max(self.max_freq, 1)
            return
        # If KEY present, increment its usage by 1 and add into
        # corresponding usage list.
        self.keys[val] += 1
        if self.keys[val] not in self.usage:
            self.usage[self.keys[val]] = [val]
        else:
            self.usage[self.keys[val]].append(val)
        # Always update max_freq value.
        self.max_freq = max(self.max_freq, self.keys[val])

    def pop(self) -> int:
        # We're adding KEYS one by one, so it's always the most recent KEY at [-1].
        # And if his usage same as max_freq, we can be sure it last_added KEY with
        # most frequent usage.
        last_added: int = self.usage[self.max_freq].pop()
        # Lower KEY usage.
        self.keys[last_added] -= 1
        # If there's no keys with current usage left,
        # there's 2 options:
        #  1) All KEYS deleted <- ignoring this, cuz =>
        #   => It is guaranteed that there will be at least one element
        #      in the stack before calling pop.
        #  2) Only KEYS within frequency_range(0, max_freq) left,
        #     and we just need to lower it (1 by 1 added, always step of 1).
        if len(self.usage[self.max_freq]) == 0:
            self.max_freq -= 1
        return last_added

# Time complexity:
#       initiation: O(1) -> doesn't depend on input, always same 2 dicts and INT created => O(1).
#       push: O(1) -> doesn't depend on input, KEY will be either added as new or its usage incremented by 1,
#                     same for USAGE it's going to be added as new list or just appended into existed,
#                     extra max_freq checked => O(1).
#       pop: O(1) -> doesn't depend on input => O(1).
# ----------------------
# ! It is guaranteed that there will be at least one element in the stack before calling pop. ! ->
# -> No need to extra checks.
# Surprisingly working, at not even bad results.
# ----------------------
# With p146 it was least_recently_used, so we could just store it as pre_last node in double_linked list,
# and delete/replace/change based on it. Here we need only to delete MOST used and if there's multiple KEYS,
# with the same usage we need to delete last added.
# So just store usage of everything and increment it and extra store USAGES itself to decide what was added in it.
# Like 1, 2, 3 -> we add 1, 2, 3, all 3 of them will have USAGE == 1, and if we store USAGE as well.
# It's going to be USAGE[1] == [1, 2, 3] -> we can just delete last of them because we added them one by one.
# And now KEYS[3] = 1 - 1 = 0.
# 1, 2, 3, 3, 3 -> USAGE[3] == [3], most usage is 3, so we're deleting 3 and decreasing its frequency by 1 as well.
# KEYS[3] = 3 - 1 = 2, next pop() is for USAGE[2] == [3] same.
# Extra to that we need to store Frequency of ALL, so it's should be the same as max_key in USAGE but how we maintain.
# IF len(USAGE[value]) == 0, decrease Frequency by 1?
# And maintain max_value of added, like we add 3, 2 times then it's max(cur_max, new_max) and USAGE[new_max].append(3).
# Strange, it's HARD when it easier than LRU. Guess I just don't understand it correctly, let's test.
