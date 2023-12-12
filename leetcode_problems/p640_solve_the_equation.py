# Solve a given equation and return the value of 'x' in the form of a string "x=#value".
# The equation contains only '+', '-' operation, the variable 'x' and its coefficient.
# You should return "No solution" if there is no solution for the equation,
#  or "Infinite solutions" if there are infinite solutions for the equation.
# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.
# ------------------------
# 3 <= equation.length <= 1000
# equation has exactly one '='.
# equation consists of integers with an absolute value in the range [0, 100]
#  without any leading zeros, and the variable 'x'.


def solve_equation(equation: str) -> str:
    # working_sol (95.81%, 70.6%) -> (30ms, 16.22mb)  time: O(n) | space: O(n)
    left: str
    right: str
    # All 'x' goes to left, all 'vals' goes to right.
    # Because we only have '-', '+' operations.
    left, right = equation.split('=')

    def rebuild_part(part: str) -> str:
        """
        Rebuild one part of the equation into: +-val*x+-vals
        :param part: part of the equation to change
        :return: rebuild version of the given part
        """
        part_x: int = 0
        part_else: int = 0
        cur_val: str = ''
        part += '+'  # we're always ignoring last value we built, so it's faster to add extra trigger.
        for x in range(len(part)):
            # Resets for new value.
            if part[x] == '-':
                if cur_val:
                    part_else += int(cur_val)
                cur_val = ''
                cur_val += '-'
            elif part[x] == '+':
                if cur_val:
                    part_else += int(cur_val)
                cur_val = ''
            # 'x' on current part.
            elif part[x] == 'x':
                if cur_val:
                    if cur_val == '-':
                        part_x += -1
                    else:
                        part_x += int(cur_val)
                else:
                    part_x += 1
                cur_val = ''
            # Everything else on this part.
            else:
                cur_val += part[x]
        return f'{part_x}x+{part_else}' if part_else >= 0 else f'{part_x}x{part_else}'

    new_left: str = rebuild_part(left)
    new_right: str = rebuild_part(right)
    # Both sides will lead to 0=0.
    if new_left == new_right:
        return 'Infinite solutions'
    # New parts are always in style: +-val*x+-vals
    # So, we care about value before 'x' and after.
    left_x_ind: int = new_left.index('x')
    right_x_ind: int = new_right.index('x')
    x_side: int = int(new_left[:left_x_ind]) - int(new_right[:right_x_ind])
    # Both sides will lead to 0*x=w.e.
    if x_side == 0:
        return 'No solution'
    # Transfer left_part -> right_part => (left_part values * -1).
    else_side: int = int(new_right[right_x_ind + 1:]) - int(new_left[left_x_ind + 1:])
    if x_side == 1:
        return f'x={else_side}'
    # ! If there is exactly one solution for the equation,
    #  we ensure that the value of 'x' is an integer. !
    # So, it's always floor, and ALL test cases bugs out if one of them results in => x=float.
    return f'x={else_side // x_side}'


# Time complexity: O(n) <- n - length of input string `equation`.
# Essentially we're traversing whole input string once while building `new_left` + `new_right` => O(n).
# But after that we only slice somewhat constant strings, because they both in style:
# +-val*x+-val, and val is always like:
#  len(equation) == 1000, and if we have only 1 side with max size 100 + 100 + 100 .. + 100 for (997) symbols.
#  Because 1 symbol for 'x' + 1 symbol for right part + '='.
#  ! (100 * 997) * x = 1 ! <- something like that.
#  And after check_part(left) => 99700x1 => len(new_left) == 7.
#  Maybe we can call it constant, and ignore. But if case like: 2x=2
#  We're going to have `new_left` == 2x0, which is still lower than len(equation) but close to it.
#  So, maybe it's better to just say O(log n) for slices and .index('x') searches.
# O(2n + 6 * log n)? <- 6 - 2 index searches + 4 slices.
# Forgot, about split(), extra traverse of full string to split in half's.
# Guess it's actually too much and in the worst case like (100 * 997), this traverse of 7 indexes will be
#  totally dominated. So I will stick to O(n).
# ------------------------
# Auxiliary space: O(n)
# Splitting original input string `equation` into 2 half's, essentially both will have size (n - 1),
#  because we ignore '=' sign => O(n - 1).
# Extra 2 strings: `new_left`, `new_right` with somewhat constant size, but let's call it part of original => O(log n).
# O((n - 1) + 2 * log n)?
# Well it can be called constant by the previous logic, but I guess it's just better to stick to (log n).
# Because it's still depends on input, higher the values we use => higher values we will have on sides of 'x'.
# But again, it's better to just call it O(n).
# Because splits `left`, `right` will dominate `new_left`, `new_right` by size.


test: str = "x+5-3+x=6+x-2"
test_out: str = "x=2"
assert test_out == solve_equation(test)

test = "x=x"
test_out = "Infinite solutions"
assert test_out == solve_equation(test)

test = "2x=x"
test_out = "x=0"
assert test_out == solve_equation(test)
