# You are given an array of digits called digits.
# Your task is to determine the number of distinct three-digit even numbers
#  that can be formed using these digits.
# Note: Each copy of a digit can only be used once per number,
#  and there may not be leading zeros.
# ----------------------
# 3 <= digits.length <= 10
# 0 <= digits[i] <= 9


def total_numbers(digits: list[int]) -> int:
    # working_sol (19.21%, 88.03%) -> (38ms, 17.76mb)  time: O(n ** 3) | space: O(n ** 3)
    # 100% some math voodo, but im just triple looping this :)
    build: set[int] = set()
    for index1 in range(len(digits)):
        dig1: int = digits[index1]
        # No leading zeroes:
        if 0 == dig1:
            continue
        for index2 in range(len(digits)):
            if index1 == index2:
                continue
            dig2: int = digits[index2]
            for index3 in range(len(digits)):
                if index1 == index3 or index2 == index3:
                    continue
                dig3: int = digits[index3]
                value: int = int(f'{dig1}{dig2}{dig3}')
                if value % 2:
                    continue
                build.add(value)
    
    return len(build)



# Time complexity: O(n ** 3) <- n - length of the input array `digits`.
# Always looping the input array `digits`, three times => O(n ** 3).
# ----------------------
# Auxiliary space: O(n ** 3)
# In the worst case, every digit can be used and gives even number => O(n ** 3).


test: list[int] = [1, 2, 3, 4]
test_out: int = 12
assert test_out == total_numbers(test)

test = [0, 2, 2]
test_out = 2
assert test_out == total_numbers(test)

test = [6, 6, 6]
test_out = 1
assert test_out == total_numbers(test)

test = [1, 3, 5]
test_out = 0
assert test_out == total_numbers(test)
