# A truck has two fuel tanks. You are given two integers,
#  mainTank representing the fuel present in the main tank in liters and additionalTank
#  representing the fuel present in the additional tank in liters.
# The truck has a mileage of 10 km per liter.
# Whenever 5 liters of fuel get used up in the main tank,
#  if the additional tank has at least 1 liters of fuel, 1 liters of fuel
#  will be transferred from the additional tank to the main tank.
# Return the maximum distance which can be traveled.
# Note: Injection from the additional tank is not continuous.
# It happens suddenly and immediately for every 5 liters consumed.
# --------------------
# 1 <= mainTank, additionalTank <= 100


def distance_traveled(mainTank: int, additionalTank: int) -> int:
    # working_sol (93.93%, 6.94%) -> (1ms, 17.86mb)  time: O(n) | space: O(1)
    if mainTank < 5:
        return mainTank * 10
        
    # Wasting all fuel in cycles, and every cycle == 5 fuel spend.
    # 5 fuel spend == +1 fuel.
    out: int = 0
    while (cycles := mainTank // 5) >= 1 and 0 < additionalTank:
        left_overs: int = mainTank % 5
        out += (mainTank - left_overs) * 10
        added_fuel: int = min(cycles, additionalTank)
        additionalTank -= added_fuel
        mainTank = left_overs + added_fuel
        cycles = 0

    return out + mainTank * 10


# Time complexity: O(n) <- n - input values `mainTank`, `additionalTank`.
# Always depleting `mainTank` => O(n)
# --------------------
# Auxiliary space: O(1)


test: int = 5
test_additional: int = 10
test_out: int = 60
assert test_out == distance_traveled(test, test_additional)

test = 1
test_additional = 2
test_out = 10
assert test_out == distance_traveled(test, test_additional)

test = 9
test_additional = 99
test_out = 110
assert test_out == distance_traveled(test, test_additional)
