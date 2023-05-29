# There are n children standing in a line.
# Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
#   1) Each child must have at least one candy.
#   2) Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
# ---------------------
# n == ratings.length  ,  1 <= n <= 2 * 104  ,  0 <= ratings[i] <= 2 * 104


def candy(ratings: list[int]) -> int:
    # working_sol (47.62%, 47.31%) -> (174ms, 19.2mb)  time: O(2n) | space: O(n)
    if len(ratings) == 0:
        return 1
    candies: int = 0
    all_candies: list[int] = [1 for _ in range(len(ratings))]
    for x in range(len(ratings) - 1):
        if ratings[x + 1] > ratings[x]:
            left_candies: int = all_candies[x] + 1
            all_candies[x + 1] = left_candies
    candies += all_candies[-1]
    for y in range(len(ratings) - 2, -1, -1):
        if ratings[y] > ratings[y + 1]:
            current_candies: int = all_candies[y]
            right_candies: int = all_candies[y + 1] + 1
            all_candies[y] = max(current_candies, right_candies)
        candies += all_candies[y]
    return candies


# Time complexity: O(2n) -> traversing input_list twice to count candies from left_neighbor and right_neighbor => O(2n)
# n - len of input_list^^  ! can be changed to O(n) -> because input doesn't change number of loops,
#                            but I prefer to show number of loops. !
# Space complexity: O(n) -> extra list of input_list size to store all candy values for individual child => O(n)
# ---------------------
# Flow:
#   1) -> adding every child 1 candy by default ->
#   2) -> adding every child their (left neighbors candies + 1) if they have higher rating than this left neighbor ->
#   3) -> adding last child candies into a candies, because we're checking right neighbors next,
#                                                            and he doesn't have right neighbor ->
#   4) -> adding every child their right neighbor candies if they have higher rating than this right neighbor ->
#         -> but, ignoring child's who's already have more candies than their (right neighbor candies + 1).
#   !) -> candies, can be replaced with just sum of all_candies.
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


test1 = [1, 0, 2]
test1_out = 5
print(candy(test1))
assert test1_out == candy(test1)

test2 = [1, 2, 2]
test2_out = 4
print(candy(test2))
assert test2_out == candy(test2)

test3 = [1, 2, 3, 4, 5, 2, 2, 9, 3, 9, 2, 1, 6, 2, 4, 0, 1, 0]
test3_out = 35
print(candy(test3))
assert test3_out == candy(test3)
