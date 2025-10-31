# In a mystic dungeon, n magicians are standing in a line.
# Each magician has an attribute that gives you energy.
# Some magicians can give you negative energy, which means taking energy from you.
# You have been cursed in such a way that after absorbing energy from magician i,
#  you will be instantly transported to magician (i + k).
# This process will be repeated until you reach
#  the magician where (i + k) does not exist.
# In other words, you will choose a starting point
#  and then teleport with k jumps until you reach the end of the magicians' sequence,
#  absorbing all the energy during the journey.
# You are given an array energy and an integer k.
# Return the maximum possible energy you can gain.
# Note that when you are reach a magician, you must take energy from them,
#  whether it is negative or positive energy.
# --- --- --- ---
# 1 <= energy.length <= 10 ** 5
# -1000 <= energy[i] <= 1000
# 1 <= k <= energy.length - 1


def maximum_energy(energy: list[int], k: int) -> int:
    # working_solution: (68.13%, 55.00%) -> (1142ms, 31.29mb)  Time: O(n) Space: O(1)
    # We either get out of bounds when we start from some index.
    # Or we will end up in the range ( len(energy) - k, len(energy) ).
    # So, we have to check a backwards path from these landing indexes.
    out: int = -10000 * 10 ** 5
    for index in range(len(energy) - k, len(energy)):
        rev_sum: int = 0
        while 0 <= index:
            rev_sum += energy[index]
            out = max(out, rev_sum)
            index -= k
    
    return out


# Time complexity: O(n ** 2) <- n - length of the input array `energy`.
# In the worst case `k` == `n`.
# So, we will check start from every index of the `energy`.
# And we traverse the whole array => O(n ** 2).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [5, 2, -10, -5, 1]
test_k: int = 3
test_out: int = 3
assert test_out == maximum_energy(test, test_k)

test = [-2, -3, -1]
test_k = 2
test_out = -1
assert test_out == maximum_energy(test, test_k)
