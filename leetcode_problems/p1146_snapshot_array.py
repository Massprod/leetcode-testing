# Implement a SnapshotArray that supports the following interface:
#       SnapshotArray(int length) initializes an array-like data structure with the given length.
#           Initially, each element equals 0.
#       void set(index, val) sets the element at the given index to be equal to val.
#       int snap() takes a snapshot of the array and returns the snap_id:
#           the total number of times we called snap() minus 1.
#       int get(index, snap_id) returns the value at the given index,
#           at the time we took the snapshot with the given snap_id.
# -------------------
# 1 <= length <= 5 * 10 ** 4  ,  0 <= index < length
# 0 <= val <= 10 ** 9  ,  0 <= snap_id < (the total number of times we call snap())
# At most 5 * 10 ** 4 calls will be made to set, snap, and get.


class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass

    def snap(self) -> int:
        pass

    def get(self, index: int, snap_id: int) -> int:
        pass


test1 = ["SnapshotArray", "set", "snap", "set", "get"]
test1_vals = [[3], [0, 5], [], [0, 6], [0, 0]]
test1_out = [None, None, 0, None, 5]
