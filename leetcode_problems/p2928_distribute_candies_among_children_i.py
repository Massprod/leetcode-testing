# You are given two positive integers n and limit.
# Return the total number of ways to distribute n candies among 3 children
#  such that no child gets more than limit candies.
# ------------------
# 1 <= n <= 50
# 1 <= limit <= 50


def distribute_candies(n: int, limit: int) -> int:
    # working_sol (35.47%, 40.80%) -> (143ms, 17.90mb)  time: O(n ** 3) | space: O(1)
    # 100% some math problem, but I don't want to bother
    #  and will just brute force it :)
    out: int = 0
    for first_candies in range(n + 1):
        if limit < first_candies:
            break
        after_first: int = n - first_candies
        for second_candies in range(after_first + 1):
            if limit < second_candies:
                break
            after_second: int = after_first - second_candies
            for third_candies in range(after_second + 1):
                if limit < third_candies:
                    break
                if n == (first_candies + second_candies + third_candies):
                    out += 1
    
    return out


# Time complexity: O(n ** 3)
# Three nested loops, which checks all combinations => O(n ** 3).
# ------------------
# Auxiliary space: O(1)


test_n: int = 5
test_limit: int = 2
test_out: int = 3
assert test_out == distribute_candies(test_n, test_limit)

test_n = 3
test_limit = 3
test_out = 10
assert test_out == distribute_candies(test_n, test_limit)
