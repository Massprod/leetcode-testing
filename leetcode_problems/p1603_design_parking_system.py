# Design a parking system for a parking lot.
# The parking lot has three kinds of parking spaces:
#  big, medium, and small, with a fixed number of slots for each size.
# Implement the ParkingSystem class:
#  - ParkingSystem(int big, int medium, int small)
#    Initializes object of the ParkingSystem class.
#    The number of slots for each parking space are given as part of the constructor.
#  - bool addCar(int carType)
#    Checks whether there is a parking space of carType for the car that wants
#    to get into the parking lot. carType can be of three kinds:
#     big, medium, or small, which are represented by 1, 2, and 3 respectively.
#    A car can only park in a parking space of its carType.
#    If there is no space available, return false, else park the car in that size space and return true.
# ------------------------
# 0 <= big, medium, small <= 1000
# carType is 1, 2, or 3
# At most 1000 calls will be made to addCar


class ParkingSystem:
    # working_sol (99.43%, 33.45%) -> (95ms, 17.05mb)  time: O(1) | space: O(1)

    def __init__(self, big: int, medium: int, small: int):
        self.parking_spots: dict[int, int] = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        if self.parking_spots[carType]:
            self.parking_spots[carType] -= 1
            return True
        return False


# Time complexity:
#   __init__: O(1) <- always creating dictionary with default size, only values are set => O(1).
#   addCar: O(1) <- hashTable check => O(1).
# ------------------------
# Auxiliary space:
#   __init__: O(1) <- `parking_spots` - always of the same size == 3 => O(1).
#   addCar: O(1) <- nothing is changed and used => O(1).
