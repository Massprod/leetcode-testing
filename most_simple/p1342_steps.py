
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.

def numberOfSteps(num: int) -> int:
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        elif num % 2 != 0:
            num -= 1
            steps += 1
    return steps


test = numberOfSteps(15)
print(test)