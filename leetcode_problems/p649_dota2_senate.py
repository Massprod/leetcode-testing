# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties.
# Now the Senate wants to decide on a change in the Dota2 game.
# The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
#   Ban one senator's right:
#     A senator can make another senator lose all his rights in this and all the following rounds.
#   Announce the victory:
#     If this senator found the senators who still have rights to vote are all from the same party,
#       he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging.
# The character 'R' and 'D' represent the Radiant party and the Dire party.
# Then, if there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator in the given order.
# This procedure will last until the end of voting.
# All the senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his own party.
# Predict which party will finally announce the victory and change the Dota2 game.
# The output should be "Radiant" or "Dire".
# -------------------
# n == senate.length  ,  1 <= n <= 10 ** 4
# senate[i] is either 'R' or 'D'.
from collections import deque


def predict_party_victory(senate: str) -> str:
    # working_sol (89.71%, 51.4%) -> (53ms, 16.6mb)  time: O(n) | space: O(n + (log n))
    if not senate:
        return senate
    radiant_que: deque = deque()
    dire_que: deque = deque()
    # Store indexes and faction of every senator.
    for index, value in enumerate(senate):
        if value == "R":
            radiant_que.append(index)
        if value == "D":
            dire_que.append(index)
    # Repeat while there's still senators capable to vote.
    while radiant_que and dire_que:
        radiant_active: deque = deque()
        dire_active: deque = deque()
        # Every senator always blocks first opposite_faction voter.
        while radiant_que and dire_que:
            # Dire|Radian que -> indexes|number when they can vote.
            # If dire is higher_index, he will be blocked by radiant.
            if dire_que[0] > radiant_que[0]:
                radiant_active.append(radiant_que[0])
            # Same for radiant, always blocked if it's index higher.
            elif dire_que[0] < radiant_que[0]:
                dire_active.append(dire_que[0])
            # Both of them voted, and can't do anything,
            # so delete from a vote que.
            radiant_que.popleft()
            dire_que.popleft()
        # If one side is exhausted.
        # Other side will block everyone who could vote in the next round.
        # Because all of their indexes are higher, and we vote in circular manner.
        # So last voters, can block anyone who could vote in the next round.
        while radiant_que:
            # They can't be blocked until next round,
            # so instantly active == still present in the next round.
            radiant_active.append(radiant_que[0])
            radiant_que.popleft()
            # If someone on opposite side is still not blocked from
            # next round vote, it will be blocked by this last_voters.
            if len(dire_active) != 0:
                dire_active.popleft()
        # Same approach.
        while dire_que:
            dire_active.append(dire_que[0])
            dire_que.popleft()
            if len(radiant_active) != 0:
                radiant_active.popleft()
        # Reset active senators.
        radiant_que = radiant_active
        dire_que = dire_active
    # One side will be always fully blocked.
    if radiant_que:
        return "Radiant"
    elif dire_que:
        return "Dire"


# Time complexity: O(n) -> creating two deque() lists with summarized size of n => O(n) -> banning senators
# n - len of input_string^^| for every value in both lists, there n indexes => O(n) -> O(n + n) -> O(n)
# !
# Don't see options where's we cannot do this in 1 round, so I'm counting them.
# Because there's always faction with higher senators, and we're banning active senators with these extras. !
# -------------------
# Auxiliary space: O(n + (log n)) -> two deque() lists with summarized size of n => O(n) ->
#                       -> extra two deque() lists with number of senators left after each round => O(log n) ->
#                       -> O(n + (log n)) <- don't count number of rounds because we're overriding them.
# -------------------
# For a future use -> If I want to delete from a list with O(1) not just from right_side, use deque() ->
#                     -> insert, delete from both ends in O(1).
# -------------------
# Failed to do:
#   1) I was thinking about deleting consuls one by one depending on their input,
#      but I didn't know about lists with O(1) popleft(), so I used dictionary to store indexes
#      and was scrolling input_string. If I tried to remove from this list not just scroll it could cost me even more
#      because it's always O(n)=> O(j * (n * (log n) * n)
#   2) Failed to actually see better solution without extra checks and repeating, not just deque() miss.
# So after peaking at top_tiers with <100ms, I learnt about deque() and rebuild solution.
# Now we're just creating 2 deque() lists with radiant, dire senators in them ->
# -> after than we're creating 2 extra deque() lists to store senators who's not going to be banned in this round ->
# -> if we have senators in both ques we can simply check their indexes to get idea who is forward and who can ban them
#   (because we're always going in left_right order), one who's forward is going to be banned, banning opposites
#   and saving those who did the banning -> repeating until we run out of senators from one faction,
#   because now there's no opposite faction in right_side(forward) and we can check if there's any senators left,
#   who can ban one's behind (who_did_the_banning) -> every index of senators who's still left in some faction,
#   after we run out of 1 faction, is always higher than anyone in saved active_senators ->
# -> simply deleting everyone behind until we run out of senators in que -> and if there's still someone left active
#   on both sides, we're going to repeat round.
# ^^Stolen(peaked) solution, but I didn't know about deque() at all, so even if I wanted to make index_check
#   and remove banned senators, it would be even slower than my solution with dictionary.
# -------------------
# Ok. Time to learn how to use deque(), cuz 3800 diff is not ok.
# !
# Deque is preferred over a list in the cases where we need quicker append and pop operations
# from both the ends of the container! https://www.geeksforgeeks.org/deque-in-python/
# -------------------
# !
# Suppose every senator is smart enough and will play the best strategy for his own party. !
# ^^Guess it's only voting against opposite faction? Then we can just make dictionary to hold all indexes,
# for both parties and every round left_to_right walk with checking their ability to ban opposite.


test: str = "RD"
test_out: str = "Radiant"
assert test_out == predict_party_victory(test)

test = "RDD"
test_out = "Dire"
assert test_out == predict_party_victory(test)

test = "RRRDDDDDDR"
test_out = "Dire"
assert test_out == predict_party_victory(test)

# test4 - failed -> Ok. I was deleting senators in most basic way, just first one from start.
#                   But we need to delete them before they can vote, so it's extra check from point to end.
test = "DRRDRDRDRDDRDRDR"
test_out = "Radiant"
assert test_out == predict_party_victory(test)

# test5 - failed -> forgot to check if senator we want to block is already blocked or not...
#                   And extra typo with checking Radiant, guess I need to be doublecheck, on +38c days.
test = "DDRRR"
test_out = "Dire"
assert test_out == predict_party_victory(test)
