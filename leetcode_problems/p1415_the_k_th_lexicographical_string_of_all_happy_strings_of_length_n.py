# A happy string is a string that:
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
#  and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n
#  sorted in lexicographical order.
# Return the kth string of this list or return an empty string if there are less
#  than k happy strings of length n.
# ------------------------
# 1 <= n <= 10
# 1 <= k <= 100


def get_happy_string(n: int, k: int) -> str:
    # working_sol (73.52%, 94.09%) -> (5ms, 17.68mb)
    #            time: O(2 ** n + 2 ** n * log 2 ** n) | space: O(2 ** n)

    def build(
            cur_seq: list[str],
            t_len: int,
            built: list[str],
            built_limit: int,
        ) -> str:
        if t_len == len(cur_seq):
            return ''.join(cur_seq)

        for char in ['a', 'b', 'c']:
            if not cur_seq or cur_seq[-1] != char:
                cur_seq.append(char)
                cor_string: str = build(
                    cur_seq, t_len, built, built_limit
                )
                if cor_string:
                    built.append(cor_string)
                cur_seq.pop()
                if len(built) == k:
                    break
        return ''
    
    out: list[str] = []
    build([], n, out, k)
    if len(out) < k:
        return ''
    
    out.sort()
    return out[k - 1]  # 1-indexed


# Time complexity: O(2 ** n + 2 ** n * log 2 ** n)
# In the worst case, we will build all the `n` strings.
# And for each, we check 2 options to build from => O(3 * 2 ** n).
# We extra sort resulted array => O(2 ** n + (2 ** n * log 2 ** n)).
# ------------------------
# Auxiliary space: O(2 ** n)
# `out` <- allocates space for each build happy_string => O(3 * 2 ** n).
# `sort` <- takes O(m) by default `m` length of the sort array => O((2 ** n) *2).


test_n: int = 1
test_k: int = 3
test_out: str = 'c'
assert test_out == get_happy_string(test_n, test_k)

test_n = 1
test_k = 4
test_out = ''
assert test_out == get_happy_string(test_n, test_k)

test_n = 3 
test_k = 9
test_out = 'cab'
assert test_out == get_happy_string(test_n, test_k)
