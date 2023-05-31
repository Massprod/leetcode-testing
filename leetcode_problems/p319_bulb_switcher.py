# There are n bulbs that are initially off. You first turn on all the bulbs,
# then you turn off every second bulb.
#
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
# For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
#
# Return the number of bulbs that are on after n rounds.
# -----------------------
# 0 <= n <= 109


def bulb_switch(n: int) -> int:
    bulbs_on: int = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    bulbs: dict[int] = {}
    for _ in range(1, n + 1):
        if _ % 2 == 0:
            bulbs[_] = False
            continue
        bulbs[_] = True
    round_num: int = 3
    while round_num < n:
        for x in range(round_num, n + 1, round_num):
            bulbs[x] = not bulbs[x]
        round_num += 1
    bulbs[round_num] = not bulbs[round_num]
    for bulb in bulbs:
        if bulbs[bulb] is True:
            bulbs_on += 1
    return bulbs_on


test1 = 3
test1_out = 1
print(bulb_switch(test1))

test2 = 0
test2_out = 0
print(bulb_switch(test2))

test3 = 1
test3_out = 1
print(bulb_switch(test3))

test4 = 13
print(bulb_switch(test4))

test5 = 2
print(bulb_switch(test5))
