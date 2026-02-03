# You are asked to design an auction system that manages bids
#  from multiple users in real time.
# Each bid is associated with a userId, an itemId, and a bidAmount.
# Implement the AuctionSystem class:​​​​​​​
#  - AuctionSystem(): Initializes the AuctionSystem object.
#  - void addBid(int userId, int itemId, int bidAmount):
#     Adds a new bid for itemId by userId with bidAmount.
#     If the same userId already has a bid on itemId, replace it with the new bidAmount.
#  - void updateBid(int userId, int itemId, int newAmount):
#     Updates the existing bid of userId for itemId to newAmount.
#     It is guaranteed that this bid exists.
#  - void removeBid(int userId, int itemId):
#     Removes the bid of userId for itemId. It is guaranteed that this bid exists.
#  - int getHighestBidder(int itemId):
#     Returns the userId of the highest bidder for itemId.
#     If multiple users have the same highest bidAmount,
#     return the user with the highest userId. If no bids exist for the item, return -1.
# --- --- --- ---
# 1 <= userId, itemId <= 5 * 10 ** 4
# 1 <= bidAmount, newAmount <= 10 ** 9
# At most 5 * 10 ** 4 total calls to addBid, updateBid, removeBid, and getHighestBidder.
# The input is generated such that for updateBid and removeBid,
#  the bid from the given userId for the given itemId will be valid.
import heapq


class AuctionSystem:
    # working_solution: (22.96%, 66.16%) -> (299ms, 52.06mb)

    def __init__(self) -> None:
        # { item_id :  heapq[ (user_bid, user_id) ]  }
        self.bids_highest: dict[int, list[tuple[int, int]]] = {}
        # { item_id : { user_id: bid } }
        self.bids_item: dict[int, dict[int, int]] = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        item_record: dict = self.bids_item.get(itemId, {})
        if not item_record:
            self.bids_item[itemId] = {}
        self.bids_item[itemId][userId] = bidAmount
        if not self.bids_highest.get(itemId):
            self.bids_highest[itemId] = []
            heapq.heapify(self.bids_highest[itemId])
        heapq.heappush(
            self.bids_highest[itemId], (-1 * bidAmount, -1 * userId)
        )

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        # ! It is guaranteed that this bid exists. !
        self.bids_item[itemId][userId] = newAmount
        heapq.heappush(
            self.bids_highest[itemId], (-1 * newAmount, -1 * userId)
        )
        
    def removeBid(self, userId: int, itemId: int) -> None:
        # ! It is guaranteed that this bid exists. !
        self.bids_item[itemId].pop(userId)

    def getHighestBidder(self, itemId: int) -> int:
        item_record: dict[int, int] = self.bids_item.get(itemId, {})
        if not item_record:
            return -1
        highest_user: int = -1
        while self.bids_highest[itemId]:
            # We shouldn't `pop`, because we can get this recalled.
            highest_option: tuple[int, int] = self.bids_highest[itemId][0]
            cur_user: int = -1 * highest_option[1]
            last_bid: int | None = item_record.get(cur_user)
            # Old record, user already canceled.
            if last_bid is None:
                heapq.heappop(self.bids_highest[itemId])
                continue
            cur_bid: int = -1 * highest_option[0]
            # Olf record, user changed it's bid.
            if last_bid != cur_bid:
                heapq.heappop(self.bids_highest[itemId])
                continue
            # Current bid is correct with the highest record.
            highest_user = cur_user
            break
        
        return highest_user
