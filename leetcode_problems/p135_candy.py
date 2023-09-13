# There are n children standing in a line.
# Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
#   1) Each child must have at least one candy.
#   2) Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
# ---------------------
# n == ratings.length
# 1 <= n <= 2 * 10 ** 4
# 0 <= ratings[i] <= 2 * 10 ** 4


def candy(ratings: list[int]) -> int:
    # working_sol (77.68%, 91.55%) -> (140ms, 19.17mb)  time: O(n) | space: O(n)
    # Greedy approach.
    # ! Each child must have at least one candy. !
    # Give every child at least 1 candy.
    all_childs: list[int] = [1 for _ in ratings]
    # LEFT neighbours.
    for x in range(1, len(ratings)):
        # Higher rating -> more candies than LEFT neighbour.
        if ratings[x] > ratings[x - 1]:
            all_childs[x] = all_childs[x - 1] + 1
    # RIGHT neighbours.
    for y in range(len(ratings) - 2, -1, -1):
        if ratings[y] > ratings[y + 1]:
            all_childs[y] = max(       # Already:
                all_childs[y],         # Have more than RIGHT neighbour.
                all_childs[y + 1] + 1  # Have less than RIGHT neighbour.
            )
    return sum(all_childs)


# Time complexity: O(n) -> traversing input_list twice to count candies from left_neighbor and right_neighbor => O(2n).
# n - len of input_list^^|
# Space complexity: O(n) -> extra list of input_list size to store all candy values for individual child => O(n).
# ---------------------
# !
# Children with a higher rating get more candies than their neighbors. !
# ^^Again this book stuff. Already met this, and still have no idea why they cant normally evaluate this.
#   Like !get more candies than their neighbors ! -> is it more than LEFT neighbor, or more than RIGHT neighbor,
#   or both of them? Because if it's both of them we can't give anyone more than 2 candies:
#    1 2 2 1 1 => only 1 neighbor is less on rating why would I consider to give more candies to the middle child?
#    1 2 3 2 1 => only middle(3) child can have 2 candies, if we consider both of neighbors together.
#   But for the task, we actually need to consider both neighbors but not together,
#   like -> every neighbor with lower rating gives (his candies + 1), no matter what side he is.
#   Tricky description with no intuitive way to understand this, at least they could use
#   ! get more candies than their NEIGHBOR ! not neighbors. Because of that, HARD task not because it's hard to solve.
#   But HARD to see this tricky_part.


test: list[int] = [1, 0, 2]
test_out: int = 5
assert test_out == candy(test)

test = [1, 2, 2]
test_out = 4
assert test_out == candy(test)

test = [1, 2, 3, 4, 5, 2, 2, 9, 3, 9, 2, 1, 6, 2, 4, 0, 1, 0]
test_out = 35
assert test_out == candy(test)
