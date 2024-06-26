# A linked list of length n is given such that each node contains an additional random pointer,
#  which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand-new nodes,
#  where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list
#  such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.
# ------------------
# For example, if there are two nodes X and Y in the original list, where X.random --> Y,
#  then for the corresponding two nodes x and y in the copied list, x.random --> y.
# ------------------
# Return the head of the copied linked list.
#   - The linked list is represented in the input/output as a list of n nodes.
#   - Each node is represented as a pair of [val, random_index] where:
#       - val: an integer representing Node.val
#       - random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
#          or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
# ------------------
# 0 <= n <= 1000  ,  -10 ** 4 <= Node.val <= 10 ** 4
# Node.random is null or is pointing to some node in the linked list.


class Node:
    """
    Creating single Node for a linked list with random links inside.
      self.val -> value this node holds.
      self.next -> next node this node links to.
      self.random -> link to any random node inside linked list.
    """

    def __init__(self, x: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[list[int, int]]) -> Node:
    """
    Creating linked list with random links inside.
      to_link -> should have value to put inside and index of a random_node to link with.
    """
    tempo = link = Node()
    all_nodes: list[Node] = []
    for index in range(len(to_link)):
        tempo.val = to_link[index][0]
        all_nodes.append(tempo)
        if index != (len(to_link) - 1):
            tempo.next = Node()
            tempo = tempo.next
    tempo = link
    for x in range(len(to_link)):
        random_index: int = to_link[x][1]
        if random_index is None:
            tempo = tempo.next
            continue
        tempo.random = all_nodes[random_index]
        tempo = tempo.next
    return link


def show_all_nodes(linked: Node, show_all: bool = True) -> None:
    """
    Showing all linked list with random links.
      linked -> correctly linked list with random links inside the nodes.
      show_all -> shows every node one by one with random nodes when True, without random nodes when False.
    """
    print("\nAll nodes:", linked)
    if not show_all:
        return
    node_num: int = 0
    one_node: Node = linked
    while one_node:
        print("Node index:", node_num)
        print("Node.val:", one_node.val)
        print("Node.random:", one_node.random)
        print("----")
        one_node = one_node.next
        if one_node:
            node_num += 1


def t_two_lists_with_random(list1: Node, list2: Node, check_random: bool = False) -> None:
    """
    Testing all Nodes being different.
    And all values (.val) for all nodes in lists passed being the same == copied.

    :param:

    list1 Node: Linked list with random links inside.

    list2 Node: Linked list with random links inside.

    check_random bool:
        True -> to check only random Node's from list1 and list2.

        False -> to check all Nodes from both given lists.
    """
    if not list1 or not list2:
        raise AttributeError('Empty inputs. Use linked lists.')
    while list1 and list2:
        assert id(list1) != id(list2)
        assert list1.val == list2.val
        if check_random:
            return
        if list1.random is not None:
            t_two_lists_with_random(list1.random, list2.random, True)
        list1 = list1.next
        list2 = list2.next


def copy_random_list(head: Node) -> Node:
    # working_sol (80.67%, 70.41%) -> (41ms, 17.2mb)  time: O(n) | space: O(n)
    if not head:
        return head
    # Save every original Node and it's index.
    # And recreate new linked list with same values.
    orig_nodes: dict[Node, int] = {}
    copied_nodes: list[Node] = []
    tempo: Node = head
    index: int = 0
    while tempo:
        orig_nodes[tempo] = index
        new_head: Node = Node(tempo.val)
        if copied_nodes:
            copied_nodes[-1].next = new_head
        copied_nodes.append(new_head)
        tempo = tempo.next
        index += 1
    # Link stored Nodes to correct .random places from original indexing.
    new_head = copied_nodes[0]
    tempo = head
    while tempo:
        # Standard random == None.
        if tempo.random:
            # Only care about Nodes which points to something.
            new_head.random = copied_nodes[orig_nodes[tempo.random]]
        new_head = new_head.next
        tempo = tempo.next
    return copied_nodes[0]


# Time complexity O(n) -> traversing once through input linked list to get all Nodes and index them, also recreate
# n - number of nodes in original list^^| original nodes as copies => O(n) -> traversing all original node one more
#                                         time to get assign random places by saved indexes => O(n).
# Auxiliary space: O(n) -> saving all nodes and their indexes into a dictionary => O(n) -> saving all original nodes
#                          into a list for correct index assignment => O(n).
# ------------------
# !
# Node.random is null or is pointing to some node in the linked list.
# !
# ^^Don't need to check for negative values, or check if it's correct link.
# ------------------
# Ok. All working. Time to make test function and fail commit, because there's either time_limit or
# some tricky part I have missed.
# ------------------
# Well while making all this basics to see what's going on in this task. I'm already made part of what we needed.
# Hardest part is to get indexes of random_nodes, because we're just given these nodes.
# Their not unique and have no indexes, so only way I see to get where we need to place them,
# is to change every value in given list to 0...n, than read this list again, and get first .val of random_link.
# But it's changing original input_list, so we're going to traverse TWICE just to get random indexes,
# is there a better way?
# First task with this type of linked_lists, and I won't google until I hit time_limit, so let's try to
# make something like O(4) -> 1 to get indexes,
#                          -> 2 to return original values,
#                          -> 3 build new with values,
#                          -> 4 put random_links
# I could leave original changed, but it's not correct, and maybe it's allowed because there's no condition for that.
# But we're dealing DEEPCOPY, so we're obliged to return COPY and leave original as it is.
# I don't even know if we're allowed to change original in first place, but how else can we get random_indexes to put?
# Extra time to traverse, but it's 99% more correct to return the original state.
# ------------------
# Ok. Rebuild creating of linked list from before, and dunder for __str__.
# But can't make it show random, because it's trying to loop for itself and ending in a max_recursion.
# Tho it's working correct, and checking with just print, is bad.
# But it's first time I encounter something more than single_linked list, so it's fine for now.


test: list[list[int]] = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
test_linked: Node = create_linked(test)
# show_all_nodes(test_linked, False)
test_out: Node = copy_random_list(test_linked)
# show_all_nodes(test_out)
t_two_lists_with_random(test_linked, test_out)

test = [[1, 1], [2, 1]]
test_linked: Node = create_linked(test)
# show_all_nodes(test_linked, False)
test_out: Node = copy_random_list(test_linked)
# show_all_nodes(test_out)
t_two_lists_with_random(test_linked, test_out)

test = [[3, None], [3, 0], [3, None]]
test_linked: Node = create_linked(test)
# show_all_nodes(test_linked, False)
test_out: Node = copy_random_list(test_linked)
# show_all_nodes(test_out)
t_two_lists_with_random(test_linked, test_out)

# test -> Failed -> Most silly mistake I could make after nailing all of this, is to check if VALUE in a node is None
#                   I did this like if VAL => proceed, but 0 is False...
#                   So we need to check implicitly for None, now it if VAL is not None => proceed.
test = [
    [3, None], [5, 17], [4, None], [-9, 6], [-10, 3], [5, 15], [0, 11],
    [6, None], [-6, 16], [3, 16], [-6, 11], [9, 12], [-2, 1], [-3, 11],
    [-1, 10], [2, 11], [-3, None], [-9, 7], [-2, 4], [-8, None], [5, None]
]
test_linked: Node = create_linked(test)
show_all_nodes(test_linked, False)
test_out: Node = copy_random_list(test_linked)
show_all_nodes(test_out)
t_two_lists_with_random(test_linked, test_out)
