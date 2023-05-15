# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= n <= 45

def climb_stairs(n: int) -> int:
    def climbing(step: int = 0) -> int | None:
        if step == n:
            return 1
        if step > n:
            return 0
        return climbing(step + 1) + climbing(step + 2)
    return climbing()


test1 = 2
test1_out = 2
print(climb_stairs(test1))

test2 = 3
test2_out = 3
print(climb_stairs(test2))

test3 = 10
test3_out = 89
print(climb_stairs(test3))
