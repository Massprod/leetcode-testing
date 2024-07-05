# A critical point in a linked list is defined as either a local maxima or a local minima.
# A node is a local maxima if the current node has
#  a value strictly greater than the previous node and the next node.
# A node is a local minima if the current node has
#  a value strictly smaller than the previous node and the next node.
# Note that a node can only be a local maxima/minima
#  if there exists both a previous node and a next node.
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance]
#  where minDistance is the minimum distance between any two distinct critical points
#  and maxDistance is the maximum distance between any two distinct critical points.
# If there are fewer than two critical points, return [-1, -1].
# -----------------------
# The number of nodes in the list is in the range [2, 10 ** 5].
# 1 <= Node.val <= 10 ** 5
from random import randint
from utils.linked_list import create_linked, ListNode


def nodes_between_critical_points(head: ListNode) -> list[int]:
    # working_sol (53.61%, 82.89%) -> (355ms, 44.28mb)  time: O(n) | space: O(1)
    base_state: list[int | float] = [float('inf'), -1]
    out: list[int | float] = [float('inf'), -1]
    first_crit: int = -1
    prev_crit: int = -1
    cur_crit: int = -1
    cur_node: ListNode = head
    cur_index: int = 1
    while cur_node.next.next:
        # Local maximum
        if cur_node.val < cur_node.next.val > cur_node.next.next.val:
            cur_crit = cur_index + 1
            if 0 > first_crit:
                first_crit = cur_crit
            elif -1 < prev_crit:
                out[0] = min(out[0], cur_crit - prev_crit)
                # Always going from left -> right.
                # So, it's always the furthest point from the `first_crit`.
                out[1] = cur_crit - first_crit
            prev_crit = cur_crit
        # Local minimum
        if cur_node.val > cur_node.next.val < cur_node.next.next.val:
            cur_crit = cur_index + 1
            if 0 > first_crit:
                first_crit = cur_crit
            elif -1 < prev_crit:
                out[0] = min(out[0], cur_crit - prev_crit)
                out[1] = cur_crit - first_crit
            prev_crit = cur_crit
        cur_node = cur_node.next
        cur_index += 1
    if base_state == out:
        return [-1, -1]
    return out


# Time complexity: O(n) <- n - number of Nodes inside input LinkedList `head`.
# Always traversing whole `head`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only constant values used, none of them depends on input `head` => O(1).


test: ListNode = create_linked([3, 1])
test_out: list[int] = [-1, -1]
assert test_out == nodes_between_critical_points(test)

test = create_linked([5, 3, 1, 2, 5, 1, 2])
test_out = [1, 3]
assert test_out == nodes_between_critical_points(test)

test = create_linked([1, 3, 2, 2, 3, 2, 2, 2, 7])
test_out = [3, 3]
assert test_out == nodes_between_critical_points(test)

test_list: list[int] = [randint(1, 10 ** 5) for _ in range(10 ** 4)]
print(test_list)
