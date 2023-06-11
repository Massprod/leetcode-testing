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
        self.snap_array: list[int] = [0 for _ in range(length)]
        self.snaps: dict[int] = {}
        self.snap_id: int = -1

    def set(self, index: int, val: int) -> None:
        if index in range(len(self.snap_array)):
            self.snap_array[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snaps[self.snap_id] = self.snap_array.copy()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snaps:
            return self.snaps[snap_id][index]


# No info about what we return on incorrect calls, on no info about if there's incorrect calls in tests.
# Because if we call with index > len(snap_array) it's error, but we better let people know about this,
# not just return None. No info so I will leave it like None, maybe this is what expected in tests.
# Same goes for dictionary(snaps), and SNAP() should I consider duplicates and ignore them?
# Or we don't care about duplicates and allowing to SNAP() w.e times same lists.
# In my opinion it should be blocked, to not waste space, but in this task there's no info on that.
# So I can't ignore them without knowing the test_cases. Only way is to fail and see what they want us to do.


def t(test_case: list[str], test_val: list[list[int]], test_out: list[int | None]) -> None:
    test: SnapshotArray | None = None
    for x in range(len(test_case)):
        if test_case[x] == "SnapshotArray":
            test = SnapshotArray(test_val[x][0])
        elif test_case[x] == "set":
            test.set(test_val[x][0], test_val[x][1])
        elif test_case[x] == "snap":
            assert test_out[x] == test.snap()
        elif test_case[x] == "get":
            assert test_out[x] == test.get(test_val[x][0], test_val[x][1])


test1 = ["SnapshotArray", "set", "snap", "set", "get"]
test1_vals = [[3], [0, 5], [], [0, 6], [0, 0]]
test1_out = [None, None, 0, None, 5]
t(test1, test1_vals, test1_out)

test2 = ["SnapshotArray", "set", "snap", "set", "snap", "get", "set", "snap", "set", "set", "snap", "get", "get"]
test2_vals = [[5], [0, 12], [], [0, 14], [], [0, 0], [4, 14], [], [4, 28], [5, 11], [], [4, 2], [4, 3]]
test2_out = [None, None, 0, None, 1, 12, None, 2, None, None, 3, 14, 28]
t(test2, test2_vals, test2_out)
