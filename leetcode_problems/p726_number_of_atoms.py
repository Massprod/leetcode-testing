# Given a string formula representing a chemical formula,
#  return the count of each atom.
# The atomic element always starts with an uppercase character,
#  then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1.
# If the count is 1, no digits will follow.
#  - For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
#  - For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
#  - For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order),
#  followed by its count (if that count is more than 1),
#  followed by the second name (in sorted order),
#  followed by its count (if that count is more than 1), and so on.
# The test cases are generated so that all the values in the output fit in a 32-bit integer.
# --------------------------
# 1 <= formula.length <= 1000
# formula consists of English letters, digits, '(', and ')'.
# formula is always valid.
from collections import defaultdict


def count_of_atoms(formula: str) -> str:
    # working_sol (79.34%, 28.74%) -> (33ms, 16.63mb)  time: O(n * log n) | space: O(n)

    def gather_digits() -> int:
        # Always gathering the whole `number` we get after some `element`
        #  or closed parentheses ')'.
        nonlocal index
        cur_count: str = ''
        while index < len(formula) and formula[index].isdigit():
            cur_count += formula[index]
            index += 1
        return int(cur_count)

    def gather_element() -> str:
        # We're always getting an element in style `UPPER` + `w.e lowers`.
        # So, we're always gathering a full element when we encounter any `UPPER`.
        nonlocal index
        index += 1
        element_lowers: str = ''
        while index < len(formula) and formula[index].islower():
            element_lowers += formula[index]
            index += 1
        return element_lowers

    # { element: occurrences }
    out: dict[str, int] = defaultdict(int)
    # [`element`, `count`] <- style for every element we get from the `formula`.
    # Always `element` and count of it after.
    # The Only exception is mark for the `(`,
    #  because we need to close parentheses before we start a new.
    stack: list[str | int] = []
    index: int = 0
    while index < len(formula):
        if formula[index].isdigit():
            stack[-1] *= gather_digits()
        elif formula[index].isupper():
            stack.append(formula[index] + gather_element())
            stack.append(1)  # Every element is `1` by itself.
        elif '(' == formula[index]:
            stack.append(formula[index])
            index += 1
        elif ')' == formula[index]:
            # Current multiplier for the elements inside parentheses.
            new_stack_multiplier: int = 1
            index += 1
            if index < len(formula) and formula[index].isdigit():
                new_stack_multiplier = gather_digits()
            # Original stack, but in reverse.
            # For a slice of elements inside `(` and `)`.
            new_stack: list[str | int] = []
            while '(' != stack[-1]:
                if isinstance(stack[-1], int):
                    new_stack.append(stack.pop() * new_stack_multiplier)
                else:
                    new_stack.append(stack.pop())
            stack.pop()
            stack = stack + new_stack[::-1]
    # With our `stack` style, we can just go and take every `element` + it's `occurrences`.
    for index in range(0, len(stack) - 1, 2):
        out[stack[index]] += stack[index + 1]
    # Sorting as requested => ascending order of `element` names.
    order: list[str] = sorted([element for element in out])
    return ''.join([element + str(out[element]) if out[element] > 1 else element for element in order])


# Time complexity: O(n * log n) <- n - length of the input string `formula`.
# We're always traversing the whole input string `formula`, once => O(n).
# And in the worst case, we're going to have a whole string in 1 pair of parentheses.
# So, we're going to use every index of the `formula` to add in `stack`
#  and using `n - 2` indexes to build a `new_stack` and reversing it => O(n + 2 * n)
# Also, in the worst case, every `element` and `count` should be of size `1`.
# Because, we will traverse every `element` after as every unique symbol in `out`.
# Extra traversing every element in `stack` to get our `element`'s and their occurrences => O(n + 2 * n + n).
# Sorting every element, which is unique index of the `formula` => O(4n + n * log n).
# Because all `element`s are unique, we're going to traverse `n` elements again
#  to build our `output` array => O(5n + n * log n)
# --------------------------
# Auxiliary space: O(n)
# Worst case every symbol in `formula` is unique, and no `count` values.
# `out` is going to allocate `n` keys and `int` for every of them => O(n).
# `stacks` is also, going to store every symbol from `formula`, but with style like: `element` + `count`.
# And because we always add at least `count` == 1, stack is allocating `2n` => O(n + 2n).
# `new_stack` is also going to be of size `n - 2` because we're only going to ignore '(' and ')' => O(3n + (n - 2).
# `order` is also allocating every symbol from `formula` => O(5n).
# And finally `output` string will store every symbol of `formula` but in correct order => O(6n).


test: str = "H2O"
test_out: str = "H2O"
assert test_out == count_of_atoms(test)

test = "Mg(OH)2"
test_out = "H2MgO2"
assert test_out == count_of_atoms(test)

test = "K4(ON(SO3)2)2"
test_out = "K4N2O14S4"
assert test_out == count_of_atoms(test)

test = "((((H2SO4)50(NaCl)30)10(Cu(NO3)2)40)20(Mg(OH)2)60)5"
test_out = "Cl30000Cu4000H100600Mg300N8000Na30000O224600S50000"
assert test_out == count_of_atoms(test)
