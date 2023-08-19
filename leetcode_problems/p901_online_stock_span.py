# Design an algorithm that collects daily price quotes for some stock
#   and returns the span of that stock's price for the current day.
# The span of the stock's price in one day is the maximum number of consecutive days
#   (starting from that day and going backward) for which the stock price was less than or equal
#   to the price of that day.
# For example, if the prices of the stock in the last four days is [7,2,1,2]
#   and the price of the stock today is 2, then the span of today is 4 because starting from today,
#   the price of the stock was less than or equal 2 for 4 consecutive days.
#   Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8,
#   then the span of today is 3 because starting from today,
#   the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:
#   - StockSpanner() Initializes the object of the class.
#   - int next(int price) Returns the span of the stock's price given that today's price is price.
# ----------------------
# 1 <= price <= 10 ** 5
# At most 10 ** 4 calls will be made to next.


class StockSpanner:
    # working_sol (98.81%, 80.01%) -> (307ms, 21.4mb)
    def __init__(self):
        self.list_stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        # By default any day span == 1.
        count: int = 1
        # We only care about -> ! maximum number of consecutive days !
        # Count everything lower and save this as previous sequence,
        # everything Higher will be continuation of this.
        # And everything lower will break sequence, and we can start a new One.
        while self.list_stack and self.list_stack[-1][0] <= price:
            count += self.list_stack.pop()[1]
        self.list_stack.append((price, count))
        return count


# Time complexity:
#       next: O(n) -> worst case deleting everything stored before => O(n).
#       n  - len of current list_stack^^|
# Auxiliary space:
#       O(m) -> object will store every new value we add, and if all of them lower than prev we store m => O(m).
#       m - all values added so far^^|
# ----------------------
# Stack with deleting everything lower and saving number of this lower values and new value?
# The most important part is -> ! maximum number of consecutive days !.
# So if we record consecutive days for some value, then anything higher will be a continuation of this.
# And anything lower is reset of sequence. We can just count this sequence and store with maximum value of it.
