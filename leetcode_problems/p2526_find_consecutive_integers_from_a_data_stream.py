# For a stream of integers, implement a data structure that checks
#  if the last k integers parsed in the stream are equal to value.
# Implement the DataStream class:
#   DataStream(int value, int k) - Initializes the object with an empty integer
#                                   stream and the two integers value and k.
#   boolean consec(int num) - Adds num to the stream of integers. Returns true if the last k integers are equal
#                              to value, and false otherwise.
#                             If there are less than k integers, the condition does not hold true, so returns false.
# ---------------------
# 1 <= value, num <= 10 ** 9
# 1 <= k <= 10 ** 5
# At most 10 ** 5 calls will be made to consec.
from collections import deque


class DataStream:
    # working_sol (66.79%, 31.43%) -> (431ms, 44mb)
    def __init__(self, value: int, k: int):
        # All stored, deque to take most_left in constant.
        self.last_values: deque = deque()
        # Correct value counter.
        self.value_count: int = 0
        # Correct value set.
        self.value: int = value
        # Limit of values to store.
        self.limit: int = k

    def consec(self, num: int) -> bool:
        # Add everything and count only correct,
        #  when limit isn't reached.
        if len(self.last_values) != self.limit:
            self.last_values.append(num)
            if num == self.value:
                self.value_count += 1
        # When limit reached, we need to replace.
        else:
            # And maintain number of correct ones.
            if self.last_values.popleft() == self.value:
                self.value_count -= 1
            if num == self.value:
                self.value_count += 1
            self.last_values.append(num)
        # № of correct values == k.
        if self.value_count == self.limit:
            return True
        return False


# Time complexity:
#   initiation: O(1) -> always constant.
#   conses: O(1) -> appending and count is always constant, deque.popleft() is also constant => O(1).
# Auxiliary space:
#   DataStream: O(k) -> maximum size of deque() stored in object is equal to init_input k => O(k).
