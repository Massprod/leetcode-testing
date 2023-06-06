# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties.
# Now the Senate wants to decide on a change in the Dota2 game.
# The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
#       Ban one senator's right:
#           A senator can make another senator lose all his rights in this and all the following rounds.
#       Announce the victory:
#           If this senator found the senators who still have rights to vote are all from the same party,
#           he can announce the victory and decide on the change in the game.
#
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


def predict_party_victory(senate: str) -> str:
    if not senate:
        return senate
    active_senators: dict[int] = {}
    dire_rights: int = 0
    radiant_rights: int = 0
    for x in range(len(senate)):
        if senate[x] == "D":
            dire_rights += 1
            active_senators[x] = True
        elif senate[x] == "R":
            radiant_rights += 1
            active_senators[x] = True
    if radiant_rights == 0:
        return "Dire"
    if dire_rights == 0:
        return "Radiant"
    while radiant_rights != 0 and dire_rights != 0:
        for y in range(len(senate)):
            right_used: bool = False
            if senate[y] == "R" and active_senators[y]:
                for z in range(y + 1, len(senate)):
                    if senate[z] == "D":
                        active_senators[z] = False
                        dire_rights -= 1
                        right_used = True
                        break
                if not right_used:
                    for z in range(y):
                        if senate[z] == "D":
                            active_senators[z] = False
                            dire_rights -= 1
                            break
                if dire_rights == 0 and radiant_rights > 0:
                    return "Radiant"
            if senate[y] == "D" and active_senators[y]:
                for z in range(y + 1, len(senate)):
                    if senate[z] == "R":
                        active_senators[z] = False
                        radiant_rights -= 1
                        right_used = True
                        break
                if not right_used:
                    for z in range(y):
                        if senate[z] == "D":
                            active_senators[z] = False
                            radiant_rights -= 1
                            break
                if radiant_rights == 0 and dire_rights > 0:
                    return "Dire"
    if radiant_rights == 0:
        return "Dire"
    if dire_rights == 0:
        return "Radiant"


# !
# Suppose every senator is smart enough and will play the best strategy for his own party. !
# ^^Guess it's only voting against opposite faction? Then we can just make dictionary to hold all indexes,
# for both parties and every round left_to_right walk with checking their ability to ban opposite.


test1 = "RD"
test1_out = "Radiant"
print(predict_party_victory(test1))

test2 = "RDD"
test2_out = "Dire"
print(predict_party_victory(test2))

test3 = "RRRDDDDDDR"
test3_out = "Dire"
print(predict_party_victory(test3))

# test4 - failed -> Ok. I was deleting senators in most basic way, just first one from start.
#                   But we need to delete them before they can vote, so it's extra check from point to end.
test4 = "DRRDRDRDRDDRDRDR"
print(predict_party_victory(test4))

# test5 - failed -> forgot to check if senator we want to block is already blocked or not...
test5 = "DDRRR"
print(predict_party_victory(test5))
