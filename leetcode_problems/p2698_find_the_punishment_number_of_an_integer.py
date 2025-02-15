# Given a positive integer n, return the punishment number of n.
# The punishment number of n is defined as the sum of the squares
#  of all integers i such that:
#  - 1 <= i <= n
#  - The decimal representation of i * i can be partitioned into contiguous substrings
#    such that the sum of the integer values of these substrings equals i.
# ----------------------
# 1 <= n <= 1000


def punishment_number(n: int) -> int:
    # working_sol (77.98%,  68.75%) -> (92ms, 17.78mb) time: O(n * 2 ** log_10_n)
    #                                                  space: O(log_10_n)
    
    def check(check_val: int, target: int) -> bool:
        # We can't take more from `target` => we have higher sum in `check_val`.
        # Or we don't have enough in `check_val` to buil `target`.
        if 0 > target or check_val < target:
            return False
        
        if check_val == target:
            return True
        
        # !
        # 1 <= n <= 1000
        # ! <- we can take digits from right -> left and summarize them,
        #      every digit we take, should be removed from the `target`.
        return (
            check(check_val // 10, target - (check_val % 10))
            or
            check(check_val // 100, target - (check_val % 100))
            or
            check(check_val // 1000, target - (check_val % 1000))
        )


    out: int = 0
    for value in range(1, n + 1):
        number: int = value * value
        if check(number, value):
            out += number

    return out


test: int = 10
test_out: int = 182
assert test_out == punishment_number(test)

test = 37
test_out = 1478
assert test_out == punishment_number(test)
