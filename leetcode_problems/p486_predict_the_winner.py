# You are given an integer array nums.
# Two players are playing a game with this array: player 1 and player 2.
# Player 1 and player 2 take turns, with player 1 starting first.
# Both players start the game with a score of 0. At each turn, the player takes one of the numbers
#   from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1.
#   The player adds the chosen number to their score. The game ends when there are no more elements in the array.
# Return true if Player 1 can win the game.
# If the scores of both players are equal, then player 1 is still the winner, and you should also return true.
# You may assume that both players are playing optimally.
# ------------------
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 10 ** 7
from random import randint


def predict_winner(nums: list[int]) -> bool:
    # working_sol (91.2%, 43.57%) -> (45ms, 16.5mb)  time: O(n ** 2) | space: O(n ** 2)
    # all possible score of the input_array
    summ_scores: int = sum(nums)
    # rec cache with (left_l, right_l)
    rec_cache: dict[tuple[int, int], int] = {}

    def take_turn(left_l: int, right_l: int) -> int:
        # if cached:
        if (left_l, right_l) in rec_cache:
            return rec_cache[left_l, right_l]
        # Out of bounds, no values possible.
        if left_l > right_l:
            return 0
        # Last option:
        if left_l == right_l:
            return nums[left_l]
        # Player2 is mastermind and w.e we do he's always taking BEST option,
        # so we can take all turns possible and still only get SMALLEST amount.
        # Take left -> w.e p2 takes we still have 2 options after his turn.
        take_left: int = nums[left_l] + min(take_turn(left_l + 2, right_l), take_turn(left_l + 1, right_l - 1))
        # Take right -> same, w.e p2 picks we still have 2 options on our(p1) turn.
        take_right: int = nums[right_l] + min(take_turn(left_l + 1, right_l - 1), take_turn(left_l, right_l - 2))
        # We're still need to check if we capable of winning, even if he's overplayed us on every step.
        # So it's MAXIMUM of all our options.
        max_path: int = max(take_left, take_right)
        rec_cache[left_l, right_l] = max_path
        return max_path

    player1_max = take_turn(0, len(nums) - 1)
    # We know all possible points we can take on each turn for every player.
    # We can just check Player2 score by taking Player1 from WHOLE.
    return player1_max >= (summ_scores - player1_max)


# Time complexity: O(n ** 2) -> standard recursion tree with height n would take O(2 ** n), but we're using cache ->
# n - len of input_array^^| -> so in the worst case we're calculating all possible permutations of input_array,
#                           and if check_index is repeating we're just reusing it in constant_time => O(n ** 2).
#                           Extra sum(nums) => O(n), but it's too small to consider.
# Auxiliary space: O(n ** 2) -> recursion stack is at max of depth n => O(n) -> extra to this we're storing every
#                           limit combinations in a dictionary for every call => O(n ** 2) <- (n ** 2) number of calls.
# ------------------
# We can take another approach, what if we consider only player1?
# And player2 is master mind who is always a step ahead and takes all best options no matter what?
# Then we can just take player1 turns with ALL_OPTIONS, and just choose smallest of them ->
# -> greedy approach, but we don't need to calculate player2.
# Because no matter what steps we're taking he is overplaying us, and we're getting the smallest amount possible.
# ------------------
# Ok. I was trying to calculate scores of 2 players and first player was just choosing all_options while
# second player was culling it to take Best for him. I only made it for like 1 step ahead ->
# nums[right_l] + nums[left_l + 1] >= nums[right_l - 1] + nums[left_l]
# or
# nums[right_l] + nums[left_l + 1] <= nums[right_l - 1] + nums[left_l]
# So we take step depending on what will be higher after player1 turn.
# 58/62 passed, but I guess it's not enough, and either I made calc for all ARRAY for every step which isn't optimal.
# Or it's better to take a hint.
# ------------------
# ! You may assume that both players are playing optimally. ! -> Always best option.
# Well after playing with recursion I understand that we need to take BEST option for a second player,
# but we can take w.e option for the first player -> to get all options.
# Cuz if we take best options for both, then we can't check every path.
# Tested with 3, 13, 20 sizes working fine and fast. Let's try to fail.
# I need more tricky_test_cases, cuz random ones are all correct.


test1 = [1, 5, 2]
test1_out = False
assert test1_out == predict_winner(test1)

test2 = [1, 5, 233, 7]
test2_out = True
assert test2_out == predict_winner(test2)

# test3 -> failed -> I was taking all options, but we need only OPTIMAL, so player2 is always
#                    taking steps to undercut player1 and get most value in the future.
test3 = [2, 4, 55, 6, 8]
test3_out = False
assert test3_out == predict_winner(test3)

# test4 -> failed -> 58/62. Rebuild.
test4 = [3606449, 6, 5, 9, 452429, 7, 9580316, 9857582, 8514433, 9, 6, 6614512, 753594, 5474165, 4, 2697293, 8, 7, 1]
test4_out = False
assert test4_out == predict_winner(test4)

test: list[int] = []
for _ in range(20):
    test.append(randint(0, 10 ** 7))
print(test)
print(predict_winner(test))
