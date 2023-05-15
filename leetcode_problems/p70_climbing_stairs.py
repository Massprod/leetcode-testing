# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= n <= 45

def climb_stairs(n: int) -> int:
    copy: int = n

    def climbing(step: int = copy) -> int | None:
        if step == 0:
            return 1
        if step < 0:
            return 0
        return climbing(step - 1) + climbing(step - 2)
    return climbing()

# From right_to_left, left_to_right leaving us with O(2 ** n) recursion, and both hits time_limit.


test1 = 2
test1_out = 2
print(climb_stairs(test1))

test2 = 3
test2_out = 3
print(climb_stairs(test2))

test3 = 10
test3_out = 89
print(climb_stairs(test3))

# test4 - failed -> time_limit, I did most simple wait and didn't think about task a lot, cuz it's easy.
#                   It's working, but too slow.
test4 = 38
test4_out = 63245986
print(climb_stairs(test4))
