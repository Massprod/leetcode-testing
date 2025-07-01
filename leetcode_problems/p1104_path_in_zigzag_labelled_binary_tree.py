# In an infinite binary tree where every node has two children,
#  the nodes are labelled in row order.
# In the odd numbered rows (ie., the first, third, fifth,...),
#  the labelling is left to right, while in the even numbered rows
#  (second, fourth, sixth,...), the labelling is right to left.
# Given the label of a node in this tree,
#  return the labels in the path from the root of the tree to the node with that label.
# ----------------------
# 1 <= label <= 10 ** 6


def path_in_zig_zag_tree(label: int) -> list[int]:
    # working_sol (100.00%, 61.71%) -> (0ms, 17.76mb)  time: O(log n) | space: O(log n)
    out: list[int] = []
    level: int = 1
    level_nodes: int = 1
    while label >= (level_nodes := level_nodes * 2):
        level += 1
    while 0 != label:
        out.append(label)
        level_max_node: int = 2 ** level - 1
        level_min_node: int = 2 ** (level - 1)
        label = int(
            (level_max_node + level_min_node - label) / 2
        )
        level -= 1

    return out[::-1]


# Time complexity: O(log n) <- n - input value `label`.
# Getting level of the `label` => O(log n).
# Getting all the parent nodes from this level => O(2 * log n).
# Reversing result, because we were traversing backwards => O(n + 2 * log n).
# ----------------------
# Auxiliary space: O(log n)
# `out` <- allocates space only for the parent nodes => O(log n).


test_label: int = 14
test_out: list[int] = [1, 3, 4, 14]
assert test_out == path_in_zig_zag_tree(test_label)

test_label = 26
test_out = [1, 2, 6, 10, 26]
assert test_out == path_in_zig_zag_tree(test_label)
