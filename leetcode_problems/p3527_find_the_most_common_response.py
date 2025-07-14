# You are given a 2D string array responses where each responses[i]
#  is an array of strings representing survey responses from the ith day.
# Return the most common response across all days after removing duplicate responses
#  within each responses[i]. If there is a tie, return the lexicographically smallest response.
# ---------------------------
# 1 <= responses.length <= 1000
# 1 <= responses[i].length <= 1000
# 1 <= responses[i][j].length <= 10
# responses[i][j] consists of only lowercase English letters
from collections import defaultdict


def find_common_response(responses: list[list[str]]) -> str:
    # working_sol: (77.47%, 59.62%) -> (415ms, 165.84mb)  time: O(m * n) | space: O(m * n)
    # { response: occurs }
    all_occurs: dict[str, int] = defaultdict(int)
    for row in responses:
        uniques: set[str] = set(row)
        for key in uniques:
            all_occurs[key] += 1
    # ! 1 <= responses[i][j].length <= 10 ! <- using maximum possible string.
    out: str = 'z' * 10
    max_occurrences: int = max(all_occurs.values())
    for response, occurs in all_occurs.items():
        if max_occurrences == occurs:
            out = min(out, response)
    
    return out


# Time complexity: O(m * n) <- m - length of the input matrix `responses`,
#                              n - height of the input matrix `responses`.
# In the worst case, every value in the matrix is unique.
# Traversing every value of the matrix, twice:
# First to get all the unique values on the row.
# Second to count their occurrences => O(m * n * 2).
# Traversing every value of the matrix again, to get the max().
# Extra in the worst case, they all appear once.
# Traversing every value again to get the minimum string => O(m * n * 4).
# ---------------------------
# Auxiliary space: O(m * n).
# `all_occurs` <- allocates space for each unique value from `responses`.


test: list[list[str]] = [
    ["good", "ok", "good", "ok"], ["ok", "bad", "good", "ok", "ok"], ["good"], ["bad"]
]
test_out: str = 'good'
assert test_out == find_common_response(test)

test = [
    ["good", "ok", "good"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]
]
test_out = 'bad'
assert test_out == find_common_response(test)
