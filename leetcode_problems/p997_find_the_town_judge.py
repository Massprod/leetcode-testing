# In a town, there are n people labeled from 1 to n.
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
#   1. The town judge trusts nobody.
#   2. Everybody (except for the town judge) trusts the town judge.
#   3. There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi]
#  representing that the person labeled ai trusts the person labeled bi.
# If a trust relationship does not exist in trust array,
#  then such a trust relationship does not exist.
# Return the label of the town judge if the town judge exists and can be identified,
#  or return -1 otherwise.
# ----------------------
# 1 <= n <= 1000
# 0 <= trust.length <= 10 ** 4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
from collections import defaultdict


def find_judge(n: int, trust: list[list[int]]) -> int:
    out: int = -1
    ppl_all: set[int] = set([_ for _ in range(1, n + 1)])
    # All we care is Trust existence.
    # If some1 trusts somebody == not a Judge.
    ppl_who_trust: set[int] = set()
    trusted: dict[int, int] = defaultdict(int)
    for who, who_trust in trust:
        ppl_who_trust.add(who)
        trusted[who_trust] += 1
    res: list[int] = list(ppl_all - ppl_who_trust)
    if res and trusted[res[0]] == (n - 1):
        out = res[0]
    return out


test: int = 2
test_trust: list[list[int]] = [[1, 2]]
test_out: int = 2
assert test_out == find_judge(test, test_trust)

test = 3
test_trust = [[1, 3], [2, 3]]
test_out = 3
assert test_out == find_judge(test, test_trust)


test = 3
test_trust = [[1, 3], [2, 3], [3, 1]]
test_out = -1
assert test_out == find_judge(test, test_trust)
