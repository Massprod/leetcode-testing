# You have n boxes labeled from 0 to n - 1.
# You are given four arrays: status, candies, keys,
#  and containedBoxes where:
#  - status[i] is 1 if the ith box is open and 0 if the ith box is closed,
#  - candies[i] is the number of candies in the ith box,
#  - keys[i] is a list of the labels of the boxes you can open after opening the ith box.
#  - containedBoxes[i] is a list of the boxes you found inside the ith box.
# You are given an integer array initialBoxes that contains the labels of the boxes
#  you initially have.
# You can take all the candies in any open box and you can use the keys
#  in it to open new boxes and you also can use the boxes you find in it.
# Return the maximum number of candies you can get following the rules above.
# ----------------------------
# n == status.length == candies.length == keys.length == containedBoxes.length
# 1 <= n <= 1000
# status[i] is either 0 or 1.
# 1 <= candies[i] <= 1000
# 0 <= keys[i].length <= n
# 0 <= keys[i][j] < n
# All values of keys[i] are unique.
# 0 <= containedBoxes[i].length <= n
# 0 <= containedBoxes[i][j] < n
# All values of containedBoxes[i] are unique.
# Each box is contained in one box at most.
# 0 <= initialBoxes.length <= n
# 0 <= initialBoxes[i] < n
from collections import deque


def max_candies(
    status: list[int],
    candies: list[int],
    keys: list[list[int]],
    containedBoxes: list[list[int]],
    initialBoxes: list[int],
) -> int:
    # working_sol (77.78%, 86.97%) -> (15ms, 28.06mb)  time: O(n) | space: O(n)
    # [ opened boxes ]
    can_open: list[int] = [1 == status[i] for i in range(len(status))]
    # [ box status ] <- index == box
    has_box: list[bool] = [False for _ in status]
    # [ key status ] <- index == key
    used: list[bool] = [False for _ in status]
    out: int = 0
    
    que: deque[int] = deque([])
    for box in initialBoxes:
        has_box[box] = True
        if can_open[box]:
            que.append(box)
            used[box] = True
            out += candies[box]
    
    while que:
        cur_box: int = que.popleft()
        for key in keys[cur_box]:
            can_open[key] = True
            # key == box <- because key is opening certain box, by index.
            if not used[key] and has_box[key]:
                que.append(key)
                used[key] = True
                out += candies[key]
        for box in containedBoxes[cur_box]:
            has_box[box] = True
            if not used[box] and can_open[box]:
                que.append(box)
                used[box] = True
                out += candies[box]
    
    return out


# Time complexity: O(n) <- n - length of the input array `keys`.
# We always use BFS to check every key == box => O(n).
# ----------------------------
# Auxiliary space: O(n)
# `que` <- allocates space for each key == box => O(n).
# Other arrays are of the same length == n => O(n).


test_status: list[int] = [1, 0, 1, 0]
test_candies: list[int] = [7, 5, 4, 100]
test_keys: list[list[int]] = [[], [], [1], []]
test_contained_boxes: list[list[int]] = [[1, 2], [3], [], []]
test_initial_boxes: list[int] = [0]
test_out: int = 16
assert test_out == max_candies(
    test_status, test_candies, test_keys, test_contained_boxes, test_initial_boxes
)

test_status = [1, 0, 0, 0, 0, 0]
test_candies = [1, 1, 1, 1, 1, 1]
test_keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
test_contained_boxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
test_initial_boxes = [0]
test_out = 6
assert test_out == max_candies(
    test_status, test_candies, test_keys, test_contained_boxes, test_initial_boxes
)
