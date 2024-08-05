# There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
#  where idKey is an integer between 1 and n and value is a string.
# No two pairs have the same id.
# Design a stream that returns the values in increasing order of their IDs by returning
#  a chunk (list) of values after each insertion.
# The concatenation of all the chunks should result in a list of the sorted values.
# Implement the OrderedStream class:
#  - OrderedStream(int n) Constructs the stream to take n values.
#  - String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream,
#    then returns the largest possible chunk of currently inserted values that appear next in the order.
# -------------------------
# 1 <= n <= 1000
# 1 <= id <= n
# value.length == 5
# value consists only of lowercase letters.
# Each call to insert will have a unique id.
# Exactly n calls will be made to insert.


class OrderedStream:
    # working_sol (86.28%, 97.31%) -> (163ms, 17.18mb)

    def __init__(self, n: int):
        self.stream: list[str] = ['' for _ in range(n + 1)]
        # CHUNKS we return should be in order 1 -> n, always.
        # So, we should maintain order, starting from 1.
        self.chunk_sorted_point: int = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        out: list[str] = []
        if idKey == self.chunk_sorted_point:
            # If we have something after our current point, we should include it.
            for index in range(self.chunk_sorted_point, len(self.stream)):
                if not self.stream[index]:
                    self.chunk_sorted_point = index
                    break
                out.append(self.stream[index])
        return out


# Time complexity:
#   __init__: O(n) <- always building `1` indexed array `self.stream` => O(n).
#   insert:   O(n) <- in the worst case, we will traverse a whole array `self.stream`, once => O(n).
# -------------------------
# Auxiliary space:
#   __init__: O(n) <- `self.stream` always of the size `n + 1` => O(n + 1).
#   insert:   O(n) <- when we get last `insert` on `1` we will have `out` with size == `n` => O(n).
