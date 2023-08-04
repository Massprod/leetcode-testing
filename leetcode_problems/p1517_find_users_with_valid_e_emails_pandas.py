import pandas as pd


# Write a solution to find the users who have valid emails.
# A valid e-mail has a prefix name and a domain where:
#   The prefix name is a string that may contain letters (upper or lower case),
#     digits, underscore '_', period '.', and/or dash '-'.
#   The prefix name must start with a letter.
#   The domain is '@leetcode.com'.
# Return the result table in any order.
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Standard regex:
    # ^ -> start with.
    # * -> any repeats
    # . -> matches anything by default, so we need to use escape \\. or [.]
    # $ -> END.
    users = users[users['mail'].str.match(pat='^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$')]
    return users
