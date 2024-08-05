# Given a date string in the form Day Month Year, where:
#  - Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
#  - Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
#  - Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:
#  - YYYY denotes the 4 digit year.
#  - MM denotes the 2 digit month.
#  - DD denotes the 2 digit day.
# -------------------------
# The given dates are guaranteed to be valid, so no error handling is necessary.


def reformat_date(date: str) -> str:
    # working_sol (84.84%, 23.26%) -> (30ms, 16.51mb)  time: O(1) | space: O(1)
    day: str
    month: str
    year: str
    months: dict[str, int] = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
    }
    if date[1].isdigit():
        day = date[:2]
        month = date[5:8]
    else:
        day = '0' + date[:1]
        month = date[4: 7]
    year = date[-4:]
    out: str = f'{year}-{months[month]}-{day}'
    return out


# Time complexity: O(1)
# We're always taking the same slices and creating the same dictionary `months` => O(1).
# -------------------------
# Auxiliary space: O(1)


test: str = "20th Oct 2052"
test_out: str = "2052-10-20"
assert test_out == reformat_date(test)

test = "6th Jun 1933"
test_out = "1933-06-06"
assert test_out == reformat_date(test)

test = "26th May 1960"
test_out = "1960-05-26"
assert test_out == reformat_date(test)

test = "3rd Jun 1998"
test_out = "1998-06-03"
assert test_out == reformat_date(test)
