# Given two integer arrays pushed and popped each with distinct values,
#  return true if this could have been the result of a sequence of push and pop
#  operations on an initially empty stack, or false otherwise.
# ------------------------
# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    # working_sol (60.85%, 74.74%) -> (1ms, 17.84mb)  time: O(n + k) | space: O(n)
    stack: list[int] = []
    # Values we can still have in the `stack`
    leftovers: set[int] = set(pushed)
    push_index: int = 0
    pop_index: int = 0
    # Either we can correctly pop() or we still can have value added into stack.
    while (
        push_index < len(pushed)
        or
        (
        pop_index < len(popped)
        and
        # We can correctly pop value or we potentially have a value,
        #  which can be correctly added into a stack.
        (
        (stack and stack[-1] == popped[pop_index])
            or popped[pop_index] in leftovers
        )
        )
        ):
        # Correctly pop() while we can.
        if stack and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1
            continue
        # Or add other values into the stack.
        stack.append(pushed[push_index])
        leftovers.remove(pushed[push_index])
        push_index += 1
    
    return pop_index == len(popped)


# Time complexity: O(n + k) <- n - length of the input array `pushed`,
#                              k - length of the input array `popped`.
# In the worst case, we have correct stack sequence.
# We will use every index of `pushed` and `popped` => O(n + k).
# ------------------------
# Auxiliary space: O(n)
# `stack` <- allocates space for each value from `pushed` => O(n).
# `leftovers` <- allocates space for each value from `pushed`, when it's correct => O(2 * n).


test_pushed: list[int] = [1, 2, 3, 4, 5]
test_popped: list[int] = [4, 5, 3, 2, 1]
test_out: bool = True
assert test_out == validate_stack_sequences(test_pushed, test_popped)

test_pushed = [1, 2, 3, 4, 5]
test_popped = [4, 3, 5, 1, 2]
test_out = False
assert test_out == validate_stack_sequences(test_pushed, test_popped)
