
# Roman to Integers
# Only for Valid Roman numbers. But tasks didn't mention validations
def romanToInt(s: str) -> int:
    symbols = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 500,
        "m": 1000,
    }
    romans = list(s.lower())
    for _ in romans:
        romans[romans.index(_)] = symbols[_]
    for x in range(len(romans) - 1):
        if romans[x + 1] > romans[x]:
            romans[x] *= -1
    return sum(romans)


test = romanToInt(s="vvv")
print(test)
