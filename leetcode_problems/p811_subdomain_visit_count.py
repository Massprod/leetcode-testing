# A website domain "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com" and at the lowest level,
#  "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
#  we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3"
#  or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain
#  that indicates that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains,
#  return an array of the count-paired domains of each subdomain in the input.
# You may return the answer in any order.
# ------------------------
# 1 <= cpdomain.length <= 100
# 1 <= cpdomain[i].length <= 100
# cpdomain[i] follows either the "repi d1i.d2i.d3i" format or the "repi d1i.d2i" format.
# repi is an integer in the range [1, 10 ** 4].
# d1i, d2i, and d3i consist of lowercase English letters.


def subdomain_visits(cpdomains: list[str]) -> list[str]:
    # working_sol (94.33%, 63.45%) -> (50ms, 16.32mb)  time: O(n * k + n) | space: O(n)
    # (key, value) => (domain_name, visits)
    all_visits: dict[str, int] = {}
    for cpdomain in cpdomains:
        # all domains|subdomains
        domains: list[str] = []
        visits: int = 0
        domain: str = ''
        for sym in cpdomain:
            if sym == ' ':
                visits = int(domain)
                domain = ''
            elif sym == '.':
                domains.append(domain)
                domain = ''
            else:
                domain += sym
        # Last index != '.' or ' ' by constraints.
        domains.append(domain)
        # We need to add names from right -> left.
        # Every one of them have same visits, but counted separately.
        full: str = domains[-1]
        if full not in all_visits:
            all_visits[full] = visits
        else:
            all_visits[full] += visits
        full = domains[-2] + '.' + domains[-1]
        if full not in all_visits:
            all_visits[full] = visits
        else:
            all_visits[full] += visits
        if len(domains) == 3:
            full = domains[-3] + '.' + domains[-2] + '.' + domains[-1]
            if full not in all_visits:
                all_visits[full] = visits
            else:
                all_visits[full] += visits
    # Reverse with new counted visits for every subdomain.
    out: list[str] = []
    for key, value in all_visits.items():
        out_string: str = f'{value} {key}'
        out.append(out_string)
    return out


# Time complexity: O(n * k + n) -> for every count_paired string in input_array traversing this string to get visits
# k - len of count_paired string^^| and subdomains => O(n * k) -> worst case, all count_paired strings have 3 subs ->
# n - len of input_array^^| -> we will get (3 * n) keys to traverse after, for creating of out_string => O(n * k + 3n).
# Auxiliary space: O(n) -> same worst case, we're going to have 3 extra strings for every count_paired of input =>
#                       => O(3n) -> and extra list with all of these strings: (d1.d2.d3) and (d1.d2) and (d1) ->
#                       -> if all of count_paired string were unique then it's size == 3n. => O(6n) <- linear anyway.
# ------------------------
# So it should be just dict with all domains from right -> left, and incrementing similar ones.


test: list[str] = ["9001 discuss.leetcode.com"]
test_out: list[str] = ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]
t_test: list[str] = subdomain_visits(test)
assert len(t_test) == len(test_out)
for _ in t_test:
    assert _ in test_out

test = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
test_out = [
    "901 mail.com", "50 yahoo.com", "900 google.mail.com",
    "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"
]
t_test: list[str] = subdomain_visits(test)
assert len(t_test) == len(test_out)
for _ in t_test:
    assert _ in test_out
