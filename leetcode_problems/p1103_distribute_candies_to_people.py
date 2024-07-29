# We distribute some number of candies,
#  to a row of n = num_people people in the following way:
# We then give 1 candy to the first person, 2 candies to the second person,
#  and so on until we give n candies to the last person.
# Then, we go back to the start of the row, giving n + 1 candies to the first person,
#  n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
# This process repeats (with us giving one more candy each time,
#  and moving to the start of the row after we reach the end) until we run out of candies.
# The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
# Return an array (of length num_people and sum candies)
#  that represents the final distribution of candies.
# ---------------------
# 1 <= candies <= 10 ** 9
# 1 <= num_people <= 1000


def distribute_candies(candies: int, num_people: int) -> list[int]:
    # working_sol (35.92%, 74.47%) -> (43ms, 16.58mb)  time: O(n + k) | space: O(k)
    out: list[int] = [0 for _ in range(num_people)]
    cur_turn: int = 0
    cur_val: int = 1
    while 0 < candies:
        if cur_val <= candies:
            out[cur_turn % num_people] += cur_val
            candies -= cur_val
        else:
            out[cur_turn % num_people] += candies
            break
        cur_turn += 1
        cur_val += 1
    return out


# Time complexity: O(n + k) <- n - input value `candies`, k - input value `num_people`
# We're using simulation, and just distribute all the candies 1 by 1 => O(n).
# Extra building `out` of size `num_people` => O(k).
# ---------------------
# Auxiliary space: O(k).
# `out` <- always of the size `num_people` => O(k)


test_candies: int = 7
test_people: int = 4
test_out: list[int] = [1, 2, 3, 1]
assert test_out == distribute_candies(test_candies, test_people)

test_candies = 10
test_people = 3
test_out = [5, 2, 3]
assert test_out == distribute_candies(test_candies, test_people)
