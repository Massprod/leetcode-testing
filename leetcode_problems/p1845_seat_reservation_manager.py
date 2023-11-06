# Design a system that manages the reservation state of n seats that are numbered from 1 to n.
# Implement the SeatManager class:
#   SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n.
#    All seats are initially available.
#   int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
#   void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
# --------------------------
# 1 <= n <= 10 ** 5
# 1 <= seatNumber <= n
# For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
# For each call to unreserve, it is guaranteed that seatNumber will be reserved.
# At most 10 ** 5 calls in total will be made to reserve and unreserve.
import heapq


class SeatManager:
    # working_sol (67.56%, 44.64%) -> (440ms, 44mb)

    def __init__(self, n: int):
        self.empty_seats: list[int] = [seat for seat in range(1, n + 1)]
        heapq.heapify(self.empty_seats)

    def reserve(self) -> int:
        # ! For each call to reserve, it is guaranteed that there will be at least one unreserved seat. !
        # We don't care bout what seats are empty only lowest is matter.
        return heapq.heappop(self.empty_seats)

    def unreserve(self, seatNumber: int) -> None:
        # ! For each call to unreserve, it is guaranteed that seatNumber will be reserved. !
        # We won't have duplicates, and we don't care about anything, except returning it in the heap.
        heapq.heappush(self.empty_seats, seatNumber)


# Time complexity:
#       initiation: O(n) -> creating array with size of 'n' + heapify it => O(n).
#        n - input value 'n'.
#       reserve: O(log k) -> pop(), push() heapq operations are O(log k).
#        k - current number of value in heap.
#       unreserve: O(log k) -> pop(), push() heapq operations are O(log k).
# Auxiliary space:
#       classObject: O(n) -> we're always operating only with seats given on initiation => O(n).
