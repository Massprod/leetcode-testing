# Every valid email consists of a local name and a domain name,
#  separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#  - For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address,
#  mail sent there will be forwarded to the same address without dots in the local name.
# Note that this rule does not apply to domain names.
#  - For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#  - For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# Given an array of strings emails where we send one email to each emails[i],
#  return the number of different addresses that actually receive mails.
# ------------------
# 1 <= emails.length <= 100
# 1 <= emails[i].length <= 100
# emails[i] consist of lowercase English letters, '+', '.' and '@'.
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.
# Domain names end with the ".com" suffix.


def num_unique_emails(emails: list[str]) -> int:
    # working_sol (5.84%, 85.45%) -> (79ms, 16.54mb)  time:O(n * k) | space: O(n * k)
    uniques: set[str] = set()
    for email in emails:
        cor_email: str = ''
        sign_met: bool = False
        for index in range(len(email)):
            if '@' == email[index]:
                cor_email += email[index:]
                break
            if sign_met:
                continue
            elif '+' == email[index]:
                sign_met = True
            elif '.' != email[index]:
                cor_email += email[index]
        if cor_email not in uniques:
            uniques.add(cor_email)
    return len(uniques)


# Time complexity: O(n * k) <- n - length of the input array `emails`, k - average length of the emails in `emails`.
# Always traversing whole input array `email`, once and every word in it => O(n * k)
# ------------------
# Auxiliary space: O(n * k)
# In the worst case, every string is going to have only correct symbols and we store all of them in `uniques`.


test: list[str] = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
                   "testemail+david@lee.tcode.com"]
test_out: int = 2
assert test_out == num_unique_emails(test)

test = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
test_out = 3
assert test_out == num_unique_emails(test)
