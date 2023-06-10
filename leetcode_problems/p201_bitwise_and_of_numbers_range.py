# Given two integers left and right that represent the range [left, right],
#           return the bitwise AND of all numbers in this range, inclusive.
# -------------------
# 0 <= left <= right <= 2 ** 31 - 1


def range_bitwise_and(left: int, right: int) -> int:
    # working_sol (39.29%, 27.60%) -> (75ms, 16.4mb)  time: O(1)? | space: O(1)
    if left == right:
        return left
    shift_count: int = 0
    while left != right and left != 0:
        left = left >> 1
        right = right >> 1
        shift_count += 1
    return left << shift_count


# Time complexity: O(1) -> WHILE loop will be executing until we shift left to 0 or left == right ->
#                          -> so in case of left == right, right and left were shifted same times ->
#                          -> at max there's 30 shifts possible and they almost instant, so I guess
#                          we can call it constant time, always less than 91 shifts in total ->
#                          -> but it's still depends on input for some it will be 5 or even 1,
#                          how can we get number of shifts? No idea, leaving it as O(1) for now.
# Auxiliary space: O(1) -> one extra INT, doesn't depends on input => O(1).
# -------------------
# Doing this with simple loop to check every left, left +1 ... & right, is TLE, so I need extra_info on bit_methods,
# https://www.geeksforgeeks.org/bitwise-and-or-of-a-range/ <- this one to reference.
# -------------------
# Should we check every bit until we hit 0?
# Like take less_signi in right, check it to less_signi in left -> if it's correct save as counter,
# if it's not then every other number after that should give as 0, because like in 3 case below,
# after checking first less_signi bit in 1 and shifting we're getting 0. So every other number after that will be 0,
# and result of all AND operations after that is 0.
# Same for any other ranges, we either hit 0(run out of bits in left, but not in right)
# or hit equal bits_part in both numbers at the same time and every other AND operations will be the same.
# case 1:
print("\ncase 1\n", bin(2147483647),
      "\n", bin(1073741824),
      "\n", int(0b1111111111111111111111111111110),
      "\n", int(0b1000000000000000000000000000000),
      "! every AND check will annul everything except most_signi",
      "\n ! so they're sharing same position for a most_signi bit.",
      "\n", bin(2147483647 >> 30),
      "\n", bin(1073741824 >> 30),
      "\n", int((1073741824 >> 30) << 30),
      )
# Both of numbers equal to 0b00..001 -> so they're having same most_signi bit position,
# and we can call number with this bit placed to be a result of all AND operations.
# case 2:
print("\ncase2\n", bin(5), bin(6), bin(7),
      "\n", bin(7 >> 2),
      "\n", bin(5 >> 2),
      "! shared same most_signi bit position and now can be placed",
      "\n", bin((5 >> 2) << 2),
      "\n", int(0b100),
      )
# case 3:
print("\ncase3\n", bin(1), bin(2147483647),
      "\n", bin(1 >> 1), "! after this, every AND will result in 0",
      "\n", bin(2147483647 >> 1 and (1 >> 1)),
      )
# But all of this works on this ->
# -> We know that if a number num is a power of 2 then (num &(num – 1)) is equal to 0.
#   So if left is less than 2^k  and right is greater than or equal to 2^k, then the & of all values
#   in between left and right should be zero as (2^k & (2^k – 1)) is equal to 0.
#   So, if both left and right lies within the same number of bits then only answer won't be zero.


test1 = 5
test1_right = 7
test1_out = 4
assert test1_out == range_bitwise_and(test1, test1_right)

test2 = 0
test2_right = 0
test2_out = 0
assert test2_out == range_bitwise_and(test2, test2_right)

test3 = 1
test3_right = 2147483647
test3_out = 0
assert test3_out == range_bitwise_and(test3, test3_right)
