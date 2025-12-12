# You are given an integer numberOfUsers representing the total number of users
#  and an array events of size n x 3.
# Each events[i] can be either of the following two types:
# 1. Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
#  - This event indicates that a set of users was mentioned in a message at timestampi.
#  - The mentions_stringi string can contain one of the following tokens:
#   - id<number>: where <number> is an integer in range [0,numberOfUsers - 1].
#     There can be multiple ids separated by a single whitespace
#      and may contain duplicates. This can mention even the offline users.
#   - ALL: mentions all users.
#   - HERE: mentions all online users.
# 2. Offline Event: ["OFFLINE", "timestampi", "idi"]
#  - This event indicates that the user idi had become offline at timestampi
#     for 60 time units. The user will automatically be online again
#     at time timestampi + 60.
# Return an array mentions where mentions[i] represents the number of mentions the user
#  with id i has across all MESSAGE events.
# All users are initially online, and if a user goes offline or comes back online,
#  their status change is processed before handling any message event 
#  that occurs at the same timestamp.
# Note that a user can be mentioned multiple times in a single message event,
#  and each mention should be counted separately.
# --- --- --- ---
# 1 <= numberOfUsers <= 100
# 1 <= events.length <= 100
# events[i].length == 3
# events[i][0] will be one of MESSAGE or OFFLINE.
# 1 <= int(events[i][1]) <= 10 ** 5
# The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
# 0 <= <number> <= numberOfUsers - 1
# It is guaranteed that the user id referenced in the OFFLINE
#  event is online at the time the event occurs.


def count_mentions(number_of_users: int, events: list[list[str]]) -> list[int]:
    # working_solution: (94.34%, 59.62%) -> (37ms, 18.02mb)  Time: O(n * log n + m * m)
    #                                                        Space: O(m)

    def comp(record) -> tuple[int, int]:
        # Equal timestamp, and we want to place `offline` first.
        # So, we could correctly ignore user `id`s after this.
        # 'A' > 'B' and numbers are going to be correct after.
        if record[1] == record[1]:
            if "O" == record[0][0]:
                return (int(record[1]), 0)

        return (int(record[1]), 1)
    
    events.sort(key=lambda x: comp(x))
    out: list[int] = [0 for _ in range(number_of_users)]
    ids: list[tuple[int, str]] = [(_, str(_)) for _ in range(number_of_users)]

    # { id: goes_online}
    offline_users: dict[str, int] = {}
    
    for event, timestamp, message in events:
        if 'O' == event[0]:
            offline_users[message] = int(timestamp) + 60
            continue
        if 'ALL' == message:
            for index, id in ids:
                    out[index] += 1
        elif 'HERE' == message:
            for index, id in ids:
                if id not in offline_users or int(timestamp) >= offline_users[id]:
                    out[index] += 1
        else:
            mentions: list[str] = message.split(' ')
            for mention in mentions:
                user_id: int = int(mention[2:])
                out[user_id] += 1
      
    return out


# Time complexity: O(n * log n + m * m)
# m - number_of_users
# Sorting `events` => O(n * log n).
# In the worst case, every event is the `HERE` and there's no `OFFLINE`.
# So, we're always traversing all users for each even => O(m * m + n * log n).
# --- --- --- ---
# Space complexity: O(m)


test: int = 2
test_events: list[list[str]] = [
    ["MESSAGE", "11", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]
]
test_out: list[int] = [2, 2]
assert test_out == count_mentions(test, test_events)

test = 2
test_events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
test_out = [2, 2]
assert test_out == count_mentions(test, test_events)

test = 2
test_events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
test_out = [0, 1]
assert test_out == count_mentions(test, test_events)

test = 2
test_events = [
    ["MESSAGE", "70", "HERE"], ["OFFLINE", "10", "0"], ["OFFLINE","71","0"]
]
test_out = [1, 1]
assert test_out == count_mentions(test, test_events)
