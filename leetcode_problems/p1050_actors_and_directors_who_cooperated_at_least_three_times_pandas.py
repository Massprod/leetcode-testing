import pandas as pd


# Write a solution to find all the pairs (actor_id, director_id)
#   where the actor has cooperated with the director at least three times.
# Return the result table in any order.
# --------------------
# ActorDirector table:
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+
# Output:
# +-------------+-------------+
# | actor_id    | director_id |
# +-------------+-------------+
# | 1           | 1           |
# +-------------+-------------+


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Count every unique pair of (actor_id, director_id) ->
    actor_director['count'] = actor_director.groupby(by=['actor_id', 'director_id']).transform('count')
    # -> delete everything, except >= 3 occurrences.
    actor_director = actor_director[actor_director['count'] >= 3]
    # Delete duplicates.
    actor_director.drop_duplicates(subset=['actor_id', 'director_id'], inplace=True)
    return actor_director[['actor_id', 'director_id']]
