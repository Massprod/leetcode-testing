# You are given a binary array rain of length n, where rain[i] == 1
#  means it rains on day i, and rain[i] == 0 means it does not.
# Alice and Bob share a single umbrella over these n days. On each day i:
#  - Alice needs the umbrella on day i if rain[i] == rain[i + 1] == 1 for 0 <= i < n - 1.
#  - Bob needs the umbrella if rain[i] == 1.
#  - At most one of them can receive the umbrella.
#  - If only one person needs it, that person receives it.
#  - If both need it, it goes to whoever has received it fewer times so far.
#    If they are tied, it goes to Alice.
#  - If neither needs it, no one receives it.
# A person's count increases only on a day they receive the umbrella.
# Initially, both counts are 0.
# Return a string array answer of length n, where answer[i] is "Alice", "Bob", or "None",
#  denoting who receives the umbrella on day i.
# A binary array is an array that contains only 0 and 1.
# --- --- --- ---
# 1 <= n == rain.length <= 100
# rain[i] is either 0 or 1.


def assign_umbrella(rain: list[int]) -> list[str]:
    # working_solution: (75%, 75%) -> (2ms, 19.24mb)  Time: O(n) Space: O(1)
    s_a: str = 'Alice'
    s_b: str = 'Bob'
    s_none: str = 'None'

    first: bool = False
    second: bool = False
    
    count_a: int = 0
    count_b: int = 0
    out: list[str] = []
    for index, day in enumerate(rain):
        first, second = False, False
        c_sym: str = s_none
        if 1 != day:
            out.append(c_sym)
            continue
        if (index < (len(rain) - 1)
            and 1 == day
            and 1 == rain[index + 1]):
            first = True
        if 1 == day:
            second = True
        if first and second:
            if count_a == count_b:
                count_a += 1
                c_sym = s_a
            elif count_a < count_b:
                count_a += 1
                c_sym = s_a
            elif count_a > count_b:
                count_b += 1
                c_sym = s_b
        elif first:
            count_a += 1
            c_sym = s_a
        elif second:
            count_b += 1
            c_sym = s_b
        out.append(c_sym)
    
    return out


# Time complexity: O(n)
# n  - length of the input array `rain`
# --- --- --- ---
# Space complexity: O(1)


t_a: str = "Alice"
t_b: str = "Bob"
t_none: str = "None"

test: list[int] = [1, 1, 0, 1, 1]
test_out: list[str] = [t_a, t_b, t_none, t_a, t_b]
assert test_out == assign_umbrella(test)

test = [0, 1, 0, 1]
test_out = [t_none, t_b, t_none, t_b]
assert test_out == assign_umbrella(test)
