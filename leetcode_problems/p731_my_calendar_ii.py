# You are implementing a program to use as your calendar.
# We can add a new event if adding the event will not cause a triple booking.
# A triple booking happens when three events have some non-empty intersection
# (i.e., some moment is common to all the three events.).
# The event can be represented as a pair of integers start and end that represents a booking
#  on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
# Implement the MyCalendarTwo class:
#  - MyCalendarTwo() Initializes the calendar object.
#  - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully
#    without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
# ------------------------
# 0 <= start < end <= 10 ** 9
# At most 1000 calls will be made to book.
from sortedcontainers import SortedDict


class MyCalendarTwo:
    # working_sol (31.68%, 15.97%) -> (1280ms, 17.99mb)  time: O(n * log n) | space: O(n)
    def __init__(self, booking_limit: int = 2):
        self.good_bookings: SortedDict = SortedDict({})
        self.booking_limit: int = booking_limit

    def book(self, start: int, end: int) -> bool:
        # Some interval started from this position == +1
        self.good_bookings[start] = self.good_bookings.get(start, 0) + 1
        # Some interval ends on this position == -1
        self.good_bookings[end] = self.good_bookings.get(end, 0) - 1
        # Prefix sum of current intervals
        cur_bookings: int = 0
        for interval_booking in self.good_bookings.values():
            cur_bookings += interval_booking
            # There's more booking intervals than our limit.
            if self.booking_limit < cur_bookings:
                # Reset interval we added before.
                self.good_bookings[start] -= 1
                self.good_bookings[end] += 1
                # We don't need to delete it, but it's better than traversing an extra element.
                # And if it goes negative == problem, we need to maintain it as 0.
                if 0 == self.good_bookings[start]:
                    del self.good_bookings[start]
                return False
        return True


# Time complexity:
#   `self.book`: O(n * log n) <- n - current # of keys in `self.good_bookings`.
#       Insertion in `SortedDict` is logarithmic and we're doing it for all elements we provided.
# ------------------------
# Auxiliary space:
#   `self.good_bookings`: O(n) <- n - # of input values: start, end.
#       In the worst case, every interval is correct and all `start`, `end` will be stored in `self.good_bookings`.
