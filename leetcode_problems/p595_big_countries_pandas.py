import pandas as pd
import pandas.testing

# A country is big if:
#   it has an area of at least three million (i.e., 3000000 km2), or
#   it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.
# Return the result table in any order.
# The result format is in the following example.


# First experience with pandas, so it's better to populate and check everything.
World: pd.DataFrame = pd.DataFrame(
    [],
    columns=['name', 'continent', 'area', 'population', 'gdp']
).astype(
    {
        'name': 'object',
        'continent': 'object',
        'area': 'Int64',
        'population': 'Int64',
        'gdp': 'Int64',
    }
)

Test = pd.DataFrame(
    [],
    columns=['name', 'population', 'area']
).astype(
    {
        'name': 'object',
        'population': 'Int64',
        'area': 'Int64',
    }
)
# Ok. Populating is just key=value, dictionary type:
World['name'] = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola']
World['continent'] = ['Asia', 'Europe', 'Africa', 'Europe', 'Africa']
World['area'] = [652230, 28748, 2381741, 468, 1246700]
World['population'] = [25500100, 2831741, 37100000, 78115, 20609294]
World['gdp'] = [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]

Test['name'] = ['Afghanistan', 'Algeria']
Test['population'] = [25500100, 37100000]
Test['area'] = [652230, 2381741]


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # world.query() or just key -> condition.
    # Extra better to use bitwise operators.
    world = world[
        (world['population'] >= 25000000) | (world['area'] >= 3000000)
    ].reset_index(drop=True)
    return world[['name', 'population', 'area']]


# Ok. We can't use just ASSERT to check Test == out.
# I need to use extra panda's lib.
# Resetting index to Test correctly. Actually I could just test 2 columns not whole DF.
# Fine for the first_time.
pandas.testing.assert_frame_equal(Test, big_countries(World))
