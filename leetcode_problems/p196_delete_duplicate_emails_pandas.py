import pandas as pd


# Write a solution to delete all duplicate emails,
#   keeping only one unique email with the smallest id.
# For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
# For Pandas users, please note that you are supposed to modify Person in place.
# After running your script, the answer shown is the Person table.
# The driver will first compile and run your piece of code and then show the Person table.
# The final order of the Person table does not matter.
# +----+------------------+
# | id | email            |
# +----+------------------+
# | 1  | john@example.com |
# | 2  | bob@example.com  |
# | 3  | john@example.com |
# +----+------------------+


def delete_duplicate_email(person: pd.DataFrame) -> None:
    # No idea how to compare ID's of rows correct when deleting, so it's extra sorting before it.
    # And every first occurrence will have lowest_id.
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email',  keep='first', inplace=True)
