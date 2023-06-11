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
        self.snap_dict: dict[int] = {}
        for _ in range(length):
            self.snap_dict[_] = [(0, 0)]
        self.snap_id: int = -1
        self.length: int = length

    def set(self, index: int, val: int) -> None:
        if index in range(self.length):
            if self.snap_id + 1 > 0:
                if len(self.snap_dict[index]) == (self.snap_id + 2):
                    if val != self.snap_dict[index][-1][0] and self.snap_dict[index][self.snap_id + 1]:
                        self.snap_dict[index][self.snap_id + 1] = (val, self.snap_id + 1)
                        return
                if val != self.snap_dict[index][-1][0]:
                    self.snap_dict[index].append((val, self.snap_id + 1))
            if self.snap_id + 1 == 0:
                if val != self.snap_dict[index][-1][0]:
                    self.snap_dict[index][0] = (val, 0)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int | None:
        if self.snap_id < snap_id < 0:
            return None
        array: list[tuple[int, int]] = self.snap_dict[index]
        if len(array) == 1:
            return array[0][0]
        snap_id = snap_id
        left: int = 0
        right: int = len(array) - 1
        # unique case for unchanged lists
        if array[right][1] < snap_id:
            return array[right][0]
        while left < right:
            if (right - left == 1) and array[left][1] < snap_id < array[right][1]:
                return array[left][0]
            if array[right][1] == snap_id:
                return array[right][0]
            if array[left][1] == snap_id:
                return array[left][0]
            middle: int = int((left + right) / 2)
            if array[middle][1] == snap_id:
                return array[middle][0]
            if array[middle][1] < snap_id < array[right][1]:
                left = middle
            if array[middle][1] > snap_id:
                right = middle
        return array[left][0]


# -------------------
# Still not enough, lists in list rebuild time.
# Lists in lists to save snaps is not working, last I consider might work is to store values in a list,
# and as I ignore snaps for same array calls, we can just return index from this list.
# -------------------
# Ok. Memory is limited, we can't save all snap_id's.
# But in a HINT they want us to use lists in list, I was thinking about that, but it's harder to read,
# and it's still will take an extra space. Need to check if we can ignore already taken snaps.
# -------------------
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

test3 = ["SnapshotArray", "snap", "snap", "get", "set", "snap", "set", "set", "get"]
test3_vals = [[4], [], [], [3, 1], [2, 4], [], [2, 6], [2, 8], [2, 2]]
test3_out = [None, 0, 1, 0, None, 2, None, None, 4]
t(test3, test3_vals, test3_out)

test4 = ["SnapshotArray", "set", "snap", "set", "snap", "get", "get", "set", "get", "set"]
test4_vals = [[2], [0, 4], [], [1, 13], [], [1, 1], [1, 0], [1, 3], [1, 0], [0, 5]]
test4_out = [None, None, 0, None, 1, 13, 0, None, 0, None]
t(test4, test4_vals, test4_out)

test5 = ["SnapshotArray", "set", "snap", "set", "snap", "set", "snap", "set", "get", "get", "snap"]
test5_vals = [[4], [1, 5], [], [0, 16], [], [2, 15], [], [2, 5], [1, 0], [0, 2], []]
test5_out = [None, None, 0, None, 1, None, 2, None, 5, 16, 3]
t(test5, test5_vals, test5_out)

test6 = ["SnapshotArray", "set", "snap", "snap", "set", "set", "get", "get", "get"]
test6_vals = [[3], [1, 6], [], [], [1, 19], [0, 4], [2, 1], [2, 0], [0, 1]]
test6_out = [None, None, 0, 1, None, None, 0, 0, 0]
t(test6, test6_vals, test6_out)

test7 = ["SnapshotArray", "set", "snap", "get", "set", "snap", "set", "get", "snap", "snap", "set", "snap", "set",
         "get", "get"]
test7_vals = [[2], [1, 16], [], [1, 0], [1, 15], [], [0, 2], [1, 0], [], [], [1, 6], [], [0, 12], [1, 4], [0, 4]]
test7_out = [None, None, 0, 16, None, 1, None, 16, 2, 3, None, 4, None, 6, 2]
t(test7, test7_vals, test7_out)

test8 = ["SnapshotArray", "snap", "set", "get", "set", "snap", "snap", "snap", "get", "set", "get", "get", "set", "get",
         "get", "get", "get", "snap"]
test8_vals = [[1], [], [0, 2], [0, 0], [0, 16], [], [], [], [0, 3], [0, 1], [0, 2], [0, 1], [0, 9], [0, 3], [0, 2],
              [0, 0], [0, 0], []]
test8_out = [None, 0, None, 0, None, 1, 2, 3, 16, None, 16, 16, None, 16, 16, 0, 0, 4]
t(test8, test8_vals, test8_out)
