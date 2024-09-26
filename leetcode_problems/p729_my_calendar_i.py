# You are implementing a program to use as your calendar.
# We can add a new event if adding the event will not cause a double booking.
# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).
# The event can be represented as a pair of integers start and end that represents
#  a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
# Implement the MyCalendar class:
#  - MyCalendar() Initializes the calendar object.
#  - boolean book(int start, int end) Returns true if the event can be added to the calendar
#    successfully without causing a double booking.
#    Otherwise, return false and do not add the event to the calendar.
# ---------------------------
# 0 <= start < end <= 10 ** 9
# At most 1000 calls will be made to book.
from sortedcontainers import SortedList


class MyCalendar:
    # working_sol (67.72%, 10.74%) -> (178ms, 17.82mb)  time: O(n * log n) | space: O(n)
    def __init__(self):
        self.events_calendar: SortedList = SortedList([])

    def book(self, start: int, end: int) -> bool:
        position: int = self.events_calendar.bisect_right((start, end))
        if 0 == position:
            if self.events_calendar and not (end <= self.events_calendar[0][0]):
                return False
        if len(self.events_calendar) == position:
            if self.events_calendar and not (start >= self.events_calendar[-1][1]):
                return False
        if 0 < position < len(self.events_calendar):
            if (self.events_calendar and
                    (not (start >= self.events_calendar[position - 1][1])
                     or not (end <= self.events_calendar[position][0]))):
                return False
        self.events_calendar.add((start, end))
        return True


# Time complexity:
#   `book`: O(n * log n) <- n - number of the event insertion calls.
#           In the worst case, every call == insert == `self.events_calendar` == `n`.
#           Always searching insert position with `bisect_right` => O(log n).
#           Also inserting values with O(log n).
# Space complexity:
#   O(n) <- in the worst case, every call == event stored in `self.events_calendar`
