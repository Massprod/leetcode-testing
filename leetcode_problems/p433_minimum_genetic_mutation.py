# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene
#  to a gene string endGene where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations.
# A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank,
#  return the minimum number of mutations needed to mutate from startGene to endGene.
# If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.
# --------------------------
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
from collections import deque


def min_mutation(startGene: str, endGene: str, bank: list[str]) -> int:
    # working_sol (99.03%, 98.20%) -> (26ms, 16.09mb)  time: O(n) | space: O(n)
    # We don't need duplicates, and we're not guaranteed that endGene in the 'bank'.
    bank: set[str] = set(bank)
    if endGene not in bank:
        return -1
    # Genes with 1 symbol difference.
    # Like: ('AACCGG_*_T' : ['AACCGG_A_T', 'AACCGG_B_T', 'AACCGG_C_T' etc.])
    graph: dict[str, list[str]] = {}
    for gene in bank:
        for x in range(len(gene)):
            option: str = f'{gene[:x]}*{gene[x + 1:]}'
            if option in graph:
                graph[option].append(gene)
            else:
                graph[option] = [gene]
    # Standard BFS with delimiter.
    que: deque[str | None] = deque([startGene, None])
    mutations: int = 0
    visited: set[str] = set()
    while que:
        cur_gen: str = que.popleft()
        if not cur_gen:
            if que:
                que.append(None)
            mutations += 1
            continue
        if cur_gen in visited:
            continue
        visited.add(cur_gen)
        # Check every other Gene with only 1 symbol difference.
        for x in range(len(cur_gen)):
            option = f'{cur_gen[:x]}*{cur_gen[x + 1:]}'
            if option in graph:
                for gene in graph[option]:
                    if gene == endGene:
                        mutations += 1
                        return mutations
                    que.append(gene)
    return -1


# Time complexity: O(n) -> creating graph with all 'bank' genes options, worst case they all different => O(8 * n) ->
# n - len of input array 'bank'^^| -> BFS starts from 'startGene', worst case == every gene in 'bank' differs by 1 ->
#                                  -> so, we will use every gene and for every gene we check 1 symbol diff options =>
#                                  => O(16 * n) <- ! startGene.length == endGene.length == bank[i].length == 8 !.
# Auxiliary space: O(n) -> worst case == every gene is different -> dictionary with all 1 symbol diff options for
#                          every gene => O(8 * n) -> 'que' with all genes allocated => O(n).
# --------------------------
# ! Note that the starting point is assumed to be valid, so it might not be included in the bank. !
# What about endGene?
# Should we extra check bank to hold it? Yep, tested with no endGene, insta -1.
# And there's no info about duplicates, so we need to delete duplicates as well.
# Should be same approach as word_ladder task with graph like: (1sym_dif: [all_options])


test_start: str = "AACCGGTT"
test_end: str = "AACCGGTA"
test_bank: list[str] = ["AACCGGTA"]
test_out: int = 1
assert test_out == min_mutation(test_start, test_end, test_bank)

test_start = "AACCGGTT"
test_end = "AAACGGTA"
test_bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
test_out = 2
assert test_out == min_mutation(test_start, test_end, test_bank)
